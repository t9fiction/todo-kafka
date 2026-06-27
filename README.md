# Todo Kafka

A FastAPI Todo API that publishes creation events to Apache Kafka, with a Kafka UI for monitoring. Runs entirely in Docker.

## Architecture

```
┌──────────┐    POST /todos    ┌──────────┐    produce    ┌────────┐
│  Client  │ ────────────────> │  FastAPI  │ ───────────> │ Kafka  │
└──────────┘                   │   Todo    │              │ Broker │
                               │   API     │              └────────┘
                               │           │              ┌────────┐
                               │           │              │Kafka UI│
                               └──────────┘              │:8080   │
                                   │                      └────────┘
                                   ▼
                              ┌──────────┐
                              │  Neon DB  │
                              │(Postgres) │
                              └──────────┘
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| `api` | 8000 | FastAPI Todo CRUD + Kafka producer |
| `broker` | 9092 | Apache Kafka 3.7.0 (KRaft mode) |
| `kafka-ui` | 8080 | Kafka cluster management UI |

## Quick start

```bash
# 1. Set your Neon DB connection string
export DATABASE_URL="postgresql://user:pass@your-neon-host/todo-docker?sslmode=require"

# 2. Start everything
docker compose up -d

# 3. API is live at http://localhost:8000
#    Kafka UI at http://localhost:8080
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/todos` | List all todos |
| `GET` | `/todos/{id}` | Get a todo |
| `POST` | `/todos` | Create a todo (produces Kafka event) |
| `PUT` | `/todos/{id}` | Update a todo |
| `DELETE` | `/todos/{id}` | Delete a todo |

### POST /todos

```json
{
  "name": "Learn Kafka",
  "content": "Integrate Kafka with FastAPI"
}
```

Creates the todo in Neon DB and publishes a message to the `todos` Kafka topic. The consumer logs received messages to stdout.

## Environment variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | Neon PostgreSQL connection string |
| `TEST_DATABASE_URL` | Test database connection string |
| `BOOTSTRAP_SERVER` | Kafka broker address (default: `broker:19092`) |
| `KAFKA_ORDER_TOPIC` | Topic name (default: `order`) |

## Tech stack

- **FastAPI** — API framework
- **SQLModel** — ORM (SQLAlchemy + Pydantic)
- **aiokafka** — Async Kafka producer/consumer
- **Apache Kafka 3.7** — Event streaming (KRaft mode, no Zookeeper)
- **Neon** — Serverless PostgreSQL
- **Docker Compose** — Orchestration
