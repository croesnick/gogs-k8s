#!/usr/bin/env bash

kubectl apply -f nginx-tcp.yml
helm install stable/nginx-ingress --name gogs-nginx --values nginx-opts.yml
