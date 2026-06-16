# Docker — Notes

Containerization with Docker: packaging applications and their dependencies into portable images.

## Core ideas
- **Image** — an immutable, layered template for a container.
- **Container** — a running instance of an image.
- **Dockerfile** — instructions to build an image.
- **Registry** — stores and distributes images (Docker Hub, AWS ECR, GitLab Registry).

## Key concepts
- **Layers & caching** — each Dockerfile instruction is a cached layer; order matters for build speed.
- **Multi-stage builds** — separate build and runtime stages to produce smaller, secure images.
- **ENTRYPOINT vs CMD** — ENTRYPOINT sets the fixed executable; CMD sets default arguments that can be overridden.
- **Volumes** — persist data outside the container lifecycle.
- **Networks** — let containers communicate (bridge networks in Compose).
- **Docker Compose** — declaratively define and run multi-container applications.

## Useful commands
- `docker build -t myapp .` — build an image
- `docker run -d -p 8080:8080 myapp` — run a container
- `docker ps` / `docker logs <id>` — list / inspect containers
- `docker exec -it <id> sh` — shell into a running container
- `docker compose up -d` / `docker compose down` — start / stop a multi-container app
- `docker image prune` — clean up unused images

## Security note
No registry credentials or secrets are committed. Logins use environment/CI variables that are git-ignored.