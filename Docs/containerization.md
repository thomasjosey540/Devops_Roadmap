# Containerization — Notes

Containerizing a full multi-service application: one image per service, orchestrated with Docker Compose.

## Approach
- **One Dockerfile per service** — app, database, and web each get a dedicated, purpose-built image.
- **Multi-stage build for the app** — build with Maven in one stage, copy only the artifact into a slim runtime image.
- **Base images** — choosing minimal, official base images (alpine/slim variants) for smaller, safer images.
- **Docker Compose** — declaratively defines all services, their networks, volumes, and start-up dependencies.

## Service breakdown
- **web (Nginx)** — reverse proxy routing traffic to the app service.
- **app (Tomcat)** — runs the built Java application (WAR deployed as ROOT).
- **db (MySQL)** — schema initialized from a SQL file on first start; data persisted in a named volume.
- **cache (Memcached)** and **mq (RabbitMQ)** — supporting infrastructure services.

## Key takeaways
- Services communicate by **service name** over a shared bridge network (e.g. `app:8080`).
- **Named volumes** keep database data across restarts.
- `depends_on` controls **start-up order**.
- The whole stack builds and runs with a single `docker compose up`.

## Useful commands
- `docker compose up -d --build` — build images and start the stack
- `docker compose ps` — service status
- `docker compose logs -f app` — follow one service's logs
- `docker compose down -v` — stop and remove containers + volumes

## Security note
Database, broker, and app credentials are passed via a git-ignored `.env`; nothing sensitive is committed.