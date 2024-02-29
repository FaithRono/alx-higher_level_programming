#!/bin/bash
# Bash script that send a DELETE request to the URL passed as the firstargument
curl -sX DELETE "$1"
