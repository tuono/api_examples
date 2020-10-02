#!/usr/bin/env bash
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
API_BASE="https://portal.tuono.io/api/v1"
LIST_ENVS=false
RESULT=""
TOKEN=""

source tuono/tuono.sh

display_usage() {
    cat << EOF

Tuono example API script --

  Script to demonstrate basic interaction with the Tuono API

  You will need and be prompted for your username and password if they aren't in the environment.

    Usage: ${0##*/} [ OPTIONS ]

      -l         [optional] Lists the Environments you have access to

  Examples:

    List environments:
        ./client.sh -l

EOF
}

get_user_info(){
    # Get login creds, prompting the user if needed
    #
    # Returns: USERNAME, PASSWORD
    #
    if [[ -z "${PORTAL_USERNAME}" ]]; then
        read -rp "Portal username: " PORTAL_USERNAME
    fi

    if [[ -z "${PORTAL_PASSWORD}" ]]; then
        read -rsp "Portal password: " PORTAL_PASSWORD
    fi
}

get_options() {
    # Parse commandline options
    while getopts ':lh' option; do
        case "${option}" in
            l  ) LIST_ENVS=true ;;
            h  ) display_usage; exit ;;
            \? ) printf "\n\t%s\n\n" "Invalid option: -${OPTARG}" >&2; display_usage >&2; exit 1 ;;
            :  ) printf "\n\t%s\n\n" "Option -${OPTARG} requires an argument." >&2; display_usage >&2; exit 1 ;;
        esac
    done
    shift "$((OPTIND - 1))"

    if [[ "${LIST_ENVS}" == false ]]; then
        echo "You must specify at least one of list_envs (-l)."
        display_usage
        exit 1
    fi
}

main(){
  get_options "$@"
  get_user_info
  get_token "${PORTAL_USERNAME}" "${PORTAL_PASSWORD}"

  if [[ "${LIST_ENVS}" == true ]]; then
    get_environments
  fi

  echo "${RESULT}"
}

# Allow sourcing or execution of script
if [ "${0}" == "${BASH_SOURCE}" ]; then
    main "$@"
fi
