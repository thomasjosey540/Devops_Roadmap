# Kubernetes — Notes

Container orchestration: deploying, scaling, and operating containerized apps on a cluster.

## Cluster
- **Control plane** — API server, scheduler, controller manager, etcd.
- **Nodes** — run workloads via the kubelet and a container runtime.
- **Setup options** — Minikube (local), Kops, and managed EKS (provisioned with Terraform).

## Core objects
- **Pod** — smallest deployable unit; one or more containers.
- **ReplicaSet** — maintains a desired number of Pod replicas.
- **Deployment** — declarative updates and rollbacks over ReplicaSets.
- **Service** — stable endpoint for a set of Pods (ClusterIP / NodePort / LoadBalancer).
- **Ingress** — HTTP(S) routing into the cluster.
- **Namespace** — logical isolation within a cluster.

## Configuration
- **ConfigMap** — non-sensitive configuration.
- **Secret** — sensitive data, base64-encoded.
- **Volumes** — persistent or ephemeral storage for Pods.
- **Command & args / resources / probes** — container runtime control and health checks.

## Packaging & tooling
- **Helm** — package manager for Kubernetes; templated charts with values and releases.
- **kubectl** — primary CLI; **Lens** — GUI for cluster visibility.

## Useful commands
- `kubectl apply -f manifests/` — apply resources
- `kubectl get pods,svc,ingress` — list resources
- `kubectl describe pod <name>` / `kubectl logs <name>` — inspect
- `kubectl rollout status deployment/app` / `kubectl rollout undo` — deploy & rollback
- `kubectl scale deployment app --replicas=5` — scale
- `helm install app ./helm/app-chart` / `helm upgrade` — Helm release management

## Security note
Secret manifests in this repo use placeholder values; real secrets are supplied at deploy time and git-ignored.