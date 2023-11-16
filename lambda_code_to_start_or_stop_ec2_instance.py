import boto3
from datetime import datetime
import pytz

def main():
    # Get the current time in UTC

    # Define a mapping of regions to their time zones
    region_timezones = {
        'us-east-1': 'US/Eastern',   # Example for the US East (N. Virginia) region
        'ap-southeast-1': 'Asia/Singapore',  # Example for the Asia Pacific (Singapore) region
        # Add more regions as needed
    }

    # Iterate through each region
    for region, timezone in region_timezones.items():
        # Convert the current time to the region's time zone
        print(timezone)
        current_time_utc = datetime.utcnow()
        current_time_region = pytz.timezone(timezone)
        local_time = current_time_utc.replace(tzinfo=pytz.utc).astimezone(current_time_region)
        print(local_time.hour)

        # Specify the non-business hours for the region
        business_hours_start = 9  # 9 AM
        business_hours_end = 17  # 5 PM
        ec2 = boto3.client('ec2',region_name=region)

        # Get a list of all EC2 instances in the region
        instances = ec2.describe_instances()

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                # Check if the current time is outside business hours
                if local_time.hour < business_hours_start or local_time.hour >= business_hours_end:
                    # Stop the instance if it's running
                    try:
                        if instance['State']['Name'] == 'running':
                            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                            print(Instance[InstanceId])
                    except Exception as e:
                        print(e)
if __name__=="__main__": 
    main() 
