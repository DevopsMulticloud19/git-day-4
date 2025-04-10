import boto3
import linux
ec2 = boto3.client('ec2', region_name='us-east-1')  
response = ec2.run_instances(
    ImageId='ami-0aef1234567890', 
    InstanceType='t2.micro',          
    KeyName='your-key-pair-name',    
    MinCount=1,
    MaxCount=1
   
