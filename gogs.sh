#!/usr/bin/env bash

kubectl create \
    --dry-run \
    --output=yaml \
    configmap ini-secret-inject-script \
    --from-file=scripts/ini-inject-secrets.py |
kubectl apply -f -

kubectl create \
    --dry-run \
    --output=yaml \
    configmap gogs-main-config \
    --from-file=config/gogs/app.ini |
kubectl apply -f -

kubectl apply -f gogs-secrets.yml
kubectl apply -f gogs.yml
kubectl apply -f gogs-ingress.yml