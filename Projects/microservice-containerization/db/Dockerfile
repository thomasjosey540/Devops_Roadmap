# DB image: MySQL with schema initialized at first start.
FROM mysql:8.0

# Database name is provided via environment at runtime.
# Any .sql files placed here run automatically on first container start.
COPY db_backup.sql /docker-entrypoint-initdb.d/db_backup.sql

EXPOSE 3306