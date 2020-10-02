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

make_auth_call(){
  # Clear the previous result
  RESULT=""

  # Process params
  target="${1}"
  method="${2}"
  data="${3}"

  # Make the call
  if [[ "${data}" == "" ]];then
    RESULT=$(curl -S --silent --header "Content-Type: application/json" --header "Authorization: Bearer ${TOKEN}" \
           --request "${method}" "${API_BASE}/${target}")
  else
    RESULT=$(curl -S --silent --header "Content-Type: application/json" --header "Authorization: Bearer ${TOKEN}" \
           --request "${method}" --data "${data}" "${API_BASE}/${target}")
  fi

}

get_token(){
  # Clear the previous token, if present
  TOKEN=""

  # Process params
  username="${1}"
  password="${2}"

  # Create data string
  data=$(jq -n --arg user "${username}" --arg pass "${password}" '{username: $user, password: $pass}')

  # Make the call
  TOKEN=$(curl -S --silent --header "Content-Type: application/json" --request POST --data "${data}" \
          "${API_BASE}/auth/login" | jq -cr .object.token)
}

get_environments(){
  make_auth_call "environments" "GET"
  envs=$(echo "${RESULT}" | jq -cr .objects)
  RESULT="${envs}"
}