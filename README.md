# migrate-S3-bucket-over-accounts
##How to migrate a bucket (name and date inside it) over AWS accounts


Steps

1) Add the policy example to the bucket you want to migrate
2) Run the python script, as in the example below:

       python aws_bucket_migration.py migration-carlos-999 carlos-test-999 marionete
        
-first arg is the script itself
        
-second arg is the name of your migration bucket
                  
-third arg is the bucket you want to migrate
                  
-forth arg is your aws cli profile


Case some fails return error such as: "_An error occurred (AccessDenied) when calling the UploadPart operation: AccessDenied_"
It is related to this issue https://github.com/aws/aws-cli/issues/1674

To go around increase the multipart upload threshold.

$ aws configure set default.s3.multipart_threshold 64MB
$ aws configure set default.s3.multipart_chunksize 16MB
