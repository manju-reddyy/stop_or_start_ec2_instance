# stop_or_start_ec2_instance
First step is to create the Lamda function using the python file
Second step is to attach the IAM role to the Lambda function so that the Lambda function has access to all the EC2 instances in the accounts, follow the steps in the Lambda_role.docx to create the IAM role.
Finally follow the steps in the Cloud_Watch_role.docx to configure a cloud watch rule to trigger the lambda to stop the instances every day after business hours. 
