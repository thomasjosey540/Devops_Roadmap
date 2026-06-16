# Docker — Containerization

Hands-on Docker projects from my DevOps learning journey: building images, multi-stage builds, volumes, and multi-container apps with Docker Compose.

## What this covers

| Area | Topics |
|------|--------|
| Fundamentals | Docker setup, core commands & concepts, container lifecycle |
| Images | Building images, Dockerfile instructions, multi-stage builds |
| Data | Volumes and persistent storage |
| Runtime | Logs, ENTRYPOINT vs CMD |
| Multi-container | Docker Compose for multi-service apps |

## Key concepts practiced

- **Images vs containers** — building, tagging, and running images
- **Dockerfile authoring** — layered builds, caching, ENTRYPOINT vs CMD
- **Multi-stage builds** — smaller, production-ready images by separating build and runtime
- **Volumes** — persisting data beyond the container lifecycle
- **Docker Compose** — defining and running multi-container applications
- **Logs & debugging** — inspecting running containers

## Notes

No secrets, credentials, or real registry tokens are committed. Image registry logins are handled via environment/CI variables that are git-ignored.