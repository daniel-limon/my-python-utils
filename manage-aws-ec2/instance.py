import boto3
from botocore.exceptions import ClientError

AWS_EC2 = boto3.client('ec2')


class Instance:

    def __init__(self, instance):
        self.launch_index = instance['AmiLaunchIndex']
        self.instance_id = instance['InstanceId']
        self.key_name = instance['KeyName']
        self.az = instance['Placement']['AvailabilityZone']
        self.public_dns = instance['PublicDnsName']
        self.state = instance['State']['Name']
        self.security_groups = instance['SecurityGroups']

    def start_instance(self):
        # dry run
        try:
            AWS_EC2.start_instances(InstanceIds=[self.instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, run start_instances without dry run
        try:
            response = AWS_EC2.start_instances(InstanceIds=[self.instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)

    def stop_instance(self):
        # dry run
        try:
            AWS_EC2.stop_instances(InstanceIds=[self.instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, call stop_instances without dry run
        try:
            response = AWS_EC2.stop_instances(InstanceIds=[self.instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)

    def reboot_instance(self):
        # dry run
        try:
            AWS_EC2.reboot_instances(InstanceIds=[self.instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                print("You don't have permission to reboot instances.")
                raise

        # dry run succeeded, calls reboot_instance without dry run
        try:
            response = AWS_EC2.reboot_instances(InstanceIds=[self.instance_id], DryRun=False)
            print('Success', response)
        except ClientError as e:
            print('Error', e)
