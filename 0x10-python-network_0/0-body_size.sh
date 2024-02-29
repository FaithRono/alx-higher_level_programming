#!/bin/bash
# Send a request to the URL and save the output in a temporary file
curl -s "${1}" | wc -c
