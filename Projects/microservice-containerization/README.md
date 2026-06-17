# Microservice Containerization

End-to-end containerization of a multi-service application — building a custom Dockerfile per service and orchestrating them with Docker Compose.

## Architecture

A multi-tier app split into independently containerized services:

| Service | Image | Role |
|---------|-------|------|
| web | Nginx | Reverse proxy / front-end entry point |
| app | Tomcat (built from Maven) | Java application server |
| db | MySQL | Persistent data store |
| cache | Memcached | In-memory caching layer |
| mq | RabbitMQ | Message broker |

## What this covers

- Writing a dedicated **Dockerfile per service** (app, db, web)
- **Multi-stage build** for the application image (Maven build → slim runtime)
- Wiring all services together with **Docker Compose** (networks, volumes, dependencies)
- Building and running the full stack locally with one command
- Containerizing a complete **microservice project** end to end

## Run it

```bash
cp .env.example .env      # fill in values
docker compose up -d      # build & start all services
docker compose ps         # check status
docker compose down       # stop & remove
```

## Notes

No secrets or credentials are committed. Real values live in a git-ignored `.env`.