# Tuono bash client
This is a very simple example client written in bash.  It does very little
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
#>  ./client.sh -h

Tuono example API script --

  Script to demonstrate basic interaction with the Tuono API

  You will need and be prompted for your username and password if they aren't in the environment.

    Usage: client.sh [ OPTIONS ]

      -l         [optional] Lists the Environments you have access to

  Examples:

    List environments:
        ./client.sh -l

```