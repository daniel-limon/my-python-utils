# ec2-manage.py
#
# created by: Daniel Rios
#
# What does it do? Uses a Python script to manage AWS ec2 instances.
# This way, you can start and stop instances without logging into
# the web console.
#
# Prerequisites: AWS account. AWS user account with programmatic access,
#   appropriate permissions, access keys, configured aws cli tool(?)
#
# Credits:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html
#
#Todo 1: Provide option to update applicable security groups to permit either all IPs, or just my IP.
#Todo 2: Provide option to update ansible playbook with new IPs or dns names.
#Todo 3: Write test script.

import boto3
from instance import Instance
from prettytable import PrettyTable


def server_menu(inst):
    # this dictionary 'maps' instance states to menu options
    server_options = {
        "stopped": ["on"],
        "running": ["stop", "reboot"],
        "pending": [],
        "stopping": []
    }

    # uses pretty table to generate console table
    pt = PrettyTable()
    pt.field_names = ["No.", "Option(s)"]
    index_list = []

    # generates one row for each menu option
    for option in server_options[inst.state]:
        pt.add_row([
            server_options[inst.state].index(option),
            option
        ])
        index_list.append(server_options[inst.state].index(option))

    # pretty prints server menu table to the console
    print(pt.get_string())

    # loops until valid input is entered. exits upon valid entry
    #   and returns to main menu.
    while True:
        i = input("\nEnter action No., M for main menu: ")
        if i.upper() == 'M':
            break
        elif i.isdigit():
            i = int(i)
            if i in index_list:
                if server_options[inst.state][i] == "on":
                    inst.start_instance()
                elif server_options[inst.state][i] == "stop":
                    inst.stop_instance()
                elif server_options[inst.state][i] == "reboot":
                    inst.reboot_instance()
                else:
                    print("Something went very wrong")
                break
            else:
                print("Invalid input")
        else:
            print("Invalid input")


def main_menu():
    ec2 = boto3.client('ec2')

    # refresh_menu is used to loop back through the AWS query in order to refresh the
    #   status of the EC2 instances
    refresh_menu = True

    # initially loops through once and will re-iterate if there is a need to refresh
    #   the main menu
    while refresh_menu:
        # query AWS and generate main menu
        response = ec2.describe_instances()

        # extracts error code, exits program if there is an error, else continues
        response_code = response['ResponseMetadata']['HTTPStatusCode']
        if response_code != 200:
            print(f"There was an error with the request, response code: {response_code}")
            refresh_menu = False
        else:
            # list objects will be of data type Instance, one for each ec2 instance
            ec2_list = []

            # iterate through Reservations then Instances to access each instance's info
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    ec2_list.append(Instance(instance))

            # use pretty table to generate the text table
            pt = PrettyTable()
            pt.field_names = ["No.", "Name", "State", "DNS"]

            # this list will serve as an index for menu options
            index_list = []

            # adds a row to the pretty print table for each ec2 instance
            for inst in ec2_list:
                pt.add_row([
                    ec2_list.index(inst),
                    inst.key_name,
                    inst.state,
                    inst.public_dns
                ])
                index_list.append(ec2_list.index(inst))

            # print pretty table to console
            print(pt.get_string())

            # keeps looping until valid entry is entered, will exit loop to
            #   refresh main menu, can also quit program from here
            while True:
                i = input("\nEnter instance No., R to refresh, Q to quit: ")

                # if R, then refresh, exits this nested while loop
                if i.upper() == 'R':
                    break

                # if Q, then Quit, exits both while loops and quits program
                elif i.upper() == 'Q':
                    refresh_menu = False
                    break

                # checks if digit, re-loops through nested while loop if not digit
                #   or if digit is not a valid choice. if valid choice, it proceeds
                #   to server_menu then exits inner nested while loop in order to
                #   refresh main menu
                elif i.isdigit():
                    i = int(i)
                    if i in index_list:
                        server_menu(ec2_list[i])
                        break
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")


if __name__ == "__main__":
    main_menu()
