# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020 Tuono, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
import argparse
import os
import pprint

from getpass import getpass
from tuono import Tuono


def parse_args():
    parser = argparse.ArgumentParser(
        description="Tuono API example",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--apply_environment",
        "-ae",
        action="store",
        help="Run apply on the given environment id",
    )
    parser.add_argument(
        "--destroy_environment",
        "-de",
        action="store",
        help="Run destroy on the given environment id",
    )
    parser.add_argument(
        "--environment",
        "-e",
        action="store",
        choices=["local", "prod", "stage"],
        default="local",
        help="Where you are running this script against - local, prod, stage",
    )
    parser.add_argument(
        "--job_status",
        "-js",
        action="store",
        help="Get the status of the specified job_id."
    )
    parser.add_argument(
        "--list_environments",
        "-le",
        default=False,
        action="store_true",
        help="List environments in the account",
    )
    parser.add_argument(
        "--list_roles",
        "-lr",
        default=False,
        action="store_true",
        help="List your roles",
    )
    parser.add_argument(
        "--list_secrets",
        "-ls",
        default=False,
        action="store_true",
        help="List secrets available to you",
    )
    parser.add_argument(
        "--password",
        "-p",
        action="store",
        default=os.environ.get("PORTAL_PASSWORD"),
        help="The password to login the portal with - its better to set the PORTAL_PASSWORD env variable",
    )
    parser.add_argument(
        "--preview_environment",
        "-pe",
        action="store",
        help="Run preview on the given environment id",
    )
    parser.add_argument(
        "--token",
        action="store",
        help="The JWT token to use in API calls to the portal.",
    )
    parser.add_argument(
        "--username",
        "-u",
        action="store",
        default=os.environ.get("PORTAL_USERNAME"),
        help="The username to login the portal with",
    )
    args = parser.parse_args()

    if args.token is None and args.username is None:
        args.username = input("Portal username: ")

    if args.token is None and args.password is None:
        args.password = getpass("Portal password: ")
    return args


def main(args):
    if args.token:
        tno = Tuono(token=args.token)
    else:
        tno = Tuono(username=args.username, password=args.password)

    if args.list_environments:
        pprint.pprint(tno.get_environments())
    elif args.list_roles:
        pprint.pprint(tno.get_roles())
    elif args.list_secrets:
        pprint.pprint(tno.get_secrets())
    elif args.preview_environment:
        pprint.pprint(tno.preview_environment(args.preview_environment))
    elif args.job_status:
        pprint.pprint(tno.get_job_status(args.job_status))
    elif args.apply_environment:
        pprint.pprint(tno.apply_environment(args.apply_environment))
    elif args.destroy_environment:
        pprint.pprint(tno.destroy_environment(args.destroy_environment))
    else:
        print("No valid action provided.")


if __name__ == "__main__":
    args = parse_args()
    main(args)
