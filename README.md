# migrate-S3-bucket-over-accounts
##How to migrate a bucket (name and date inside it) over AWS accounts


Steps

1) Add the policy example to the bucket you want to migrate
2) Run the python script:
        EXAMPLE: python aws_bucket_migration.py migration-carlos-999 carlos-test-999 marionete
        Where the -first arg is the script itself
                  -second arg is the name of your migration bucket
                  -third arg is the bucket you want to migrate
                  -forth arg is your aws cli profile

