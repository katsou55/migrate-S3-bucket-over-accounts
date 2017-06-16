### Migrate bucket between accounts

#EXAMPLE: python aws_bucket_migration.py migration-carlos-999 carlos-test-999 marionete

#STEPS
#1) Create migration bucket
#2) Migration
#3) Delete original bucket
#4) Create original bucket (on the account using the script)
#5) Move from migration bucket to new bucket
#6) Delete migration bucket

import sys
import subprocess

#print(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])
if(len(sys.argv) != 4):
    print("Incorrect number of args")
    sys.exit(1)
elif(sys.argv[1] is sys.argv[2]):
    print("First argument must be different from the second one")
    sys.exit(1)

m_bucket = sys.argv[1]
target_bucket = sys.argv[2]
profile_new_bucket = sys.argv[3]

command = """
aws s3 mb s3://{0} --profile {2} &&
aws s3 cp s3://{1}/ s3://{0}/ --recursive --profile {2} &&
aws s3 rb s3://{1} --force --profile {2} &&
aws s3 mb s3://{1} --profile {2} &&
aws s3 cp s3://{0}/ s3://{1}/ --recursive --profile {2}
""".format(m_bucket, target_bucket, profile_new_bucket)

rm_migration_bucket = """
aws s3 rb s3://{0} --force --profile {2}
""".format(m_bucket, target_bucket, profile_new_bucket)

subprocess.check_output(command, shell=True)
subprocess.check_output(rm_migration_bucket, shell=True)
