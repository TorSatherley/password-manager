import boto3
from pprint import pprint


# Connects to s3 client.
client = boto3.client("s3")

# Creates an S3 bucket.
bucket_name = "tor-warm-up-bucket"
client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "eu-west-2",
    },
)

# Loads two text files to the bucket.
books = """Assassins Apprentice
The Way of Kings
The Disposessed
"""

films = """Lord of the Rings
Harry Potter
The Matrix"""

client.put_object(Body=books, Bucket=bucket_name, Key="books.txt")
client.put_object(Body=films, Bucket=bucket_name, Key="films.txt")

items = client.list_objects_v2(
    Bucket=bucket_name,
)

# Prints a listing of the files, saving the filenames in a readable list.
items_in_bucket = [dic["Key"] for dic in items["Contents"]]
print(f" Files in S3 bucket {bucket_name}:\n{items_in_bucket}\n")

# Reads one of the files and prints it to the console.
response = client.get_object(Bucket=bucket_name, Key=items_in_bucket[0])
object_content = response["Body"].read().decode("utf-8")
print(f" Contents of {items_in_bucket[0]}:\n{object_content}")

# Deletes the files in the bucket.
client.delete_objects(
    Bucket=bucket_name,
    Delete={
        "Objects": [
            {"Key": "books.txt"},
            {"Key": "films.txt"},
        ],
        "Quiet": True,
    },
)

# Deletes the bucket.
client.delete_bucket(Bucket=bucket_name)

# Checks that the bucket is deleted by listing the available buckets (there should be none).
buckets = client.list_buckets()
print([bucket["Name"] for bucket in buckets["Buckets"]])

for bucket in buckets["Buckets"]:
    if bucket["Name"] == bucket_name:
        print(f"{bucket_name} has not been deleted!")
        break
else:
    print(f"{bucket_name} has been successfully deleted!")
