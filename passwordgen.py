#passgen - generates a random password

import argparse
import random
import sys

#define constant values here
#CAUTION: MINLEN must be equal to or greater than the sum of all
#   minimum characters. Change with caution.
MINLEN  = 8  #minimum password length
MAXLEN  = 32 #maximum password length
LC_MIN  = 2  #minimum of lower case characters
UC_MIN  = 2  #minimum of upper case characters
NUM_MIN = 2  #minimum of digits
SC_MIN  = 2  #minimum of special characters
INVALID_LENGTH = 1 #error code for invalid input
SUCCESS = 0  #program executed successfully
UC_ARRAY = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
    'R','S','T','U','V','W','X','Y','Z']
LC_ARRAY = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
    'r','s','t','u','v','w','x','y','z']
DG_ARRAY = ['0','1','2','3','4','5','6','7','8','9']
SC_ARRAY = ['~','!','@','#','$','%','^','&','*','(',')','{','}','<','>','?']

###########
def randomize_password(args):
    lc = LC_MIN
    uc = UC_MIN
    dg = NUM_MIN
    sc = SC_MIN

    i = MINLEN

    #adjusts parameters based on if special chars are excluded
    if args.excludespecialchars:
        lastNum = 3
        passLength = args.length + 2
    else:
        lastNum = 4
        passLength = args.length

    #randomly determines how many chars to get from each char category
    while i < passLength:
        pickQueue = random.randint(1,lastNum)
        if pickQueue == 1:
            lc += 1
        elif pickQueue == 2:
            uc += 1
        elif pickQueue == 3:
            dg += 1
        else:
            sc += 1
        i += 1

    lcList = random.choices(LC_ARRAY, k = lc)
    ucList = random.choices(UC_ARRAY, k = uc)
    dgList = random.choices(DG_ARRAY, k = dg)

    masterList = lcList + ucList + dgList

    #appends special chars only if they are to be included
    if not(args.excludespecialchars):
        scList = random.choices(SC_ARRAY, k = sc)
        masterList += scList

    random.shuffle(masterList)
    return ''.join(masterList)

###########
def get_arguments():
    parser = argparse.ArgumentParser(description='random password generator')
    parser.add_argument("-l", "--length", type=int, default=MINLEN,
            help=f"password length - default and min are {MINLEN}, max is {MAXLEN}")
    parser.add_argument("-x", "--excludespecialchars", action="store_true",
            help="exclude special characters")
    return parser.parse_args()

###########
def generate_password():
    #gets command line arguments
    args = get_arguments()

    #validates length of password
    if args.length < MINLEN or args.length > MAXLEN:
        print(f"Invalid Input: Length must be between {MINLEN} and {MAXLEN}")
        sys.exit(INVALID_LENGTH) #returns error code

    #print randomized password
    print(randomize_password(args))

############
### MAIN ###
############

generate_password()
