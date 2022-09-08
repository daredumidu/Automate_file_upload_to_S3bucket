import os
import glob
import subprocess

# list the files in the backup directory.
list_of_files = glob.glob("/opt/backup/Data-Backup-*.tar.gz")
# print (list_of_files)

# select the latest file from the file list.
latest_file = max(list_of_files, key=os.path.getctime)
# print (latest_file)

# upload the latest file to the S3 bucket. 
subprocess.check_output(['aws', 's3', 'cp', latest_file, 's3://data-backup', '--region', 'eu-west-1'])

# aws s3 cp latest_file s3://misp-backup --region eu-west-1
