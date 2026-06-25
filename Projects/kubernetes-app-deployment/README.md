# Kubernetes App Deployment — VProfile Multi-Tier Application

Deployment of the **VProfile** multi-tier Java web application onto a **Kubernetes cluster provisioned with Kops on AWS**. All services run as Deployments with Services for discovery, persistent storage for the database, secrets for credentials, init containers for start-up ordering, and an Ingress for external access.

## Architecture

| Component | Image | Role | Service name |
|-----------|-------|------|--------------|
| App | vprocontainers/vprofileapp (Tomcat) | Java application tier | vproapp-service |
| Database | vprocontainers/vprofiledb (MySQL) | Persistent data store | vprodb |
| Cache | memcached | In-memory caching | vprocache01 |
| Message broker | rabbitmq | Async messaging | vpromq01 |
| Ingress | nginx ingress | External HTTP routing | — |

## Key concepts demonstrated

- **Multi-tier deployment** — five coordinated components on one cluster
- **Persistent storage** — `PersistentVolumeClaim` (3Gi) for MySQL data
- **Secrets** — DB and RabbitMQ credentials injected via a Kubernetes Secret
- **Init containers** — the app waits for DB, cache, and MQ DNS to resolve before starting (ordered start-up)
- **Service discovery** — components reach each other by Service name over ClusterIP
- **Ingress** — external access routed to the app service by hostname
- **Cluster provisioning** — Kubernetes cluster stood up with Kops on AWS

## Deploy

```bash
kubectl apply -f secret.yaml
kubectl apply -f dbpvc.yaml
kubectl apply -f .
kubectl get pods,svc,ingress
```

## Notes

The Secret in this repo uses a **placeholder** value. Real credentials are supplied at deploy time and never committed.