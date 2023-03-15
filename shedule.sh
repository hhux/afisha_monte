#!/bin/bash

AUTH=$(curl --location 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username":
        "admin"
    ,
    "password":
        "admin"

}')

biba=$(echo "$AUTH" | jq '.access')



biba=$(eval echo $biba)
curl --location 'http://127.0.0.1:8000/check_posts' \
--header "Authorization: Bearer $biba" \
