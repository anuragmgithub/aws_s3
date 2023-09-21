import boto3

# Specify the bucket name
bucket_name = 'dp-s3-cost-allocation-tag'

# Create an S3 client using the default credential provider chain
s3 = boto3.client('s3')

# List objects (files) in the specified bucket
try:
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if there are objects in the bucket
    if 'Contents' in response:
        print(f"Files in '{bucket_name}':")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f"No files found in '{bucket_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("==========================")
