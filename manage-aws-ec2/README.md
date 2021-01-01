MANAGE EC2 INSTANCES

NOTE: This may incur charges to your AWS account. Additionally, there are plenty of tutorials on the web that can guide you through the process of getting AWS set up.

What it does: This program simply creates a console menu, displaying your EC2 instances, their state and public IPv4 DNS name. It gives you the option to start, stop or reboot the servers.

Why: Have the ability to start, stop and reboot servers without having to log into the AWS console.

Prerequisites:
- AWS user account with programmatic access
- Key pair associated with the AWS user account
- AWS CLI installed and configured on local machine
  -- Works if output is configured as 'json'
  -- Must use key pair associated with AWS user account

ToDo:
- Give user the option to update security groups in order to secure access to the instances.
- Write test script.

