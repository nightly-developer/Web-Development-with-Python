#!/bin/bash

# Read variables from .env file
while IFS= read -r line || [[ -n "$line" ]]; do
    export "$line"
done < .env

flask run
