# Architecture

## Components

- Nginx → Web server
- Tomcat → Application server
- MySQL → Database
- RabbitMQ → Message broker
- Memcached → Caching

---

## Flow

Client → Nginx → Tomcat → Database / Cache / Queue

---

## Purpose

- Separate concerns across layers
- Improve scalability and performance