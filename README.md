# gogs-k8s

That's my Gogs Kubernetes setup playground. :-)
Its main purpose is for me to have a real application running in Kubernetes whose setup is extensible enough to keep me learning.

In its purest form, the setup just starts a Gogs server.
Later iterations may include proper handling of secrets (be it via k8s secrets, or Hashicorp Vault integration), monitoring with Prometheus using auto-discovery of services, proper ingress controller setup (Traefik), certificate chains, log shipping and management, ... You got the point. :-)

# Prerequisites

This sample setup assumes that all requests to `.k8s` TLD are resolved locally to `localhost`.
One solution would be to add a respective entry to you `/etc/hosts` file, another (for macOS) would be to use [`dnsmasq`](https://www.stevenrombauts.be/2018/01/use-dnsmasq-instead-of-etc-hosts/).

In addition to the name resolution setup, ensure you have [`helm`](https://helm.sh) installed

# Setup

- Initialize helm: `./helm-init.sh`
- Set up nginx as ingress controller: `./nginx.sh`
- Set up prometheus: `./prometheus.sh`
- Set up gogs: `./gogs.sh`

After a short while (check `kubectl get po -w`), [Gogs](http://gogs.k8s), [Prometheus](http://prometheus.k8s), and [Alertmanager](http://alertmanager.prometheus.k8s) should be up and accessible.
