#!/usr/bin/env bash

helm upgrade --install --values prometheus-opts.yml prometheus stable/prometheus
