# Kubernetes — Orchestration

Deploying and operating a multi-service application on Kubernetes — core objects, configuration, networking, Helm packaging, and an EKS cluster provisioned with Terraform.

## What this covers

| Area | Topics |
|------|--------|
| Cluster setup | Minikube, Kops, kubeconfig, EKS via Terraform |
| Workloads | Pods, ReplicaSets, Deployments, namespaces |
| Networking | Services (ClusterIP/NodePort/LoadBalancer), Ingress |
| Configuration | ConfigMaps, Secrets, Volumes, command & args |
| Operations | Logging levels, kubectl CLI, Lens |
| Packaging | Helm charts (templating, values, releases) |

## Key concepts practiced

- **Declarative workloads** — Deployments managing ReplicaSets and Pods
- **Service discovery & networking** — exposing Pods via Services and Ingress
- **Configuration & secrets** — decoupling config from images with ConfigMaps and Secrets
- **Persistent storage** — Volumes for stateful workloads
- **Packaging** — templating and releasing apps with Helm
- **Provisioning** — standing up an EKS cluster with Terraform (Infrastructure as Code)

## Run it (local)

```bash
kubectl apply -f manifests/
kubectl get pods,svc,ingress
kubectl rollout status deployment/app
```

## Notes

No real secrets are committed. Secret manifests use placeholder values; real secrets are supplied at deploy time and git-ignored.