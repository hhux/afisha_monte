#!/bin/bash

AUTH=$(curl --location 'http://185.188.181.170:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username":
        "Monteluck"
    ,
    "password":
        "Zuba3478*"

}')

token=$(echo "$AUTH" | jq '.access')

token=$(eval echo $biba)
curl --location 'http://185.188.181.170:8000/check_posts' \
--header "Authorization: Bearer $token" \

current_date_time=$(date)
echo "Started date and time: $current_date_time"
