# This function is written to get list of EC2 instances as Dictionary Object in Python
import boto3
ec2 = boto3.client('ec2',region_name="us-east-1")

ec2_dict=ec2.describe_instances()
print("ec2_dict type is",type(ec2_dict))
print("ec2_dict is",ec2_dict)
