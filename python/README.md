# Tuono python client
This is a very simple example client written in python.  It does very little
error checking or handling and is meant to demonstrate how to connect to
the Tuono API as simply and clearly as possible.  You will want to write your
own code with much better error handling.

You will need an account with Tuono in order to use this utility. You can
use your Tuono username and password to login, or you can pass in a JWT you already
have (maybe from an active browser session).

The username and password can be gotten from the environment variables PORTAL_USERNAME
and PORTAL_PASSWORD, respectively.  Alternatively, the script will prompt you
for your username and password if they are not otherwise provided.  It is
recommended that you do not use the command option --password so that your
password is not stored in your command history in plain text.

# To run the example code
```ignorelang
#> python3 client.py --help
usage: client.py [-h] [--apply_environment APPLY_ENVIRONMENT]
                 [--destroy_environment DESTROY_ENVIRONMENT]
                 [--environment {local,prod,stage}] [--job_status JOB_STATUS]
                 [--list_environments] [--list_roles] [--list_secrets]
                 [--password PASSWORD]
                 [--preview_environment PREVIEW_ENVIRONMENT] [--token TOKEN]
                 [--username USERNAME]

Tuono API example

optional arguments:
  -h, --help            show this help message and exit
  --apply_environment APPLY_ENVIRONMENT, -ae APPLY_ENVIRONMENT
                        Run apply on the given environment id
  --destroy_environment DESTROY_ENVIRONMENT, -de DESTROY_ENVIRONMENT
                        Run destroy on the given environment id
  --environment {local,prod,stage}, -e {local,prod,stage}
                        Where you are running this script against - local,
                        prod, stage
  --job_status JOB_STATUS, -js JOB_STATUS
                        Get the status of the specified job_id.
  --list_environments, -le
                        List environments in the account
  --list_roles, -lr     List your roles
  --list_secrets, -ls   List secrets available to you
  --password PASSWORD, -p PASSWORD
                        The password to login the portal with - its better to
                        set the PORTAL_PASSWORD env variable
  --preview_environment PREVIEW_ENVIRONMENT, -pe PREVIEW_ENVIRONMENT
                        Run preview on the given environment id
  --token TOKEN         The JWT token to use in API calls to the portal.
  --username USERNAME, -u USERNAME
                        The username to login the portal with
```
