#!/usr/bin/env bash

# Create certs dir if it does not exists
mkdir -p ./certs

# Generate publi - private key 
openssl req -newkey rsa:2048 -nodes -keyout ./certs/private.key -x509 -out ./certs/certificate.pem -subj '/CN=54.187.49.238' -addext "subjectAltName=IP:54.187.49.238"

openssl x509 -outform der -in ./certs/certificate.pem -out ./certificate.crt
