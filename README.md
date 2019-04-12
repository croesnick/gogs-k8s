# gogs-k8s

That's my Gogs Kubernetes setup playground. :-)
Its main purpose is for me to have a real application running in Kubernetes whose setup is extensible enough to keep me learning.

In its purest form, the setup just starts a Gogs server.
Later iterations may include proper handling of secrets (be it via k8s secrets, or Hashicorp Vault integration), monitoring with Prometheus using auto-discovery of services, proper ingress controller setup (Traefik), certificate chains, log shipping and management, ... You got the point. :-)

