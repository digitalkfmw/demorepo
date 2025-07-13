import sys

# Read CLI arguments passed from Jenkins pipeline
adminUrl = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
appPath  = sys.argv[4]
appName  = sys.argv[5]
target   = sys.argv[6]   # Accept cluster name like 'DemoCluster'

# Connect to Admin Server
connect(username, password, adminUrl)

# Deploy WAR to the specified cluster
print('Deploying', appName, 'to target:', target)
deploy(appName=appName, path=appPath, targets=target, upload='true')

# Disconnect from Admin Server
disconnect()
exit()

