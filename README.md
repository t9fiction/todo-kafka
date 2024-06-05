# FastAPI Todo App

This repository contains a FastAPI Todo application with a Dockerized environment. The app allows users to manage their todo lists efficiently.

## Features

- Create, Read, Update, and Delete (CRUD) operations for todos.
- Dockerized environment for easy deployment.
- Utilizes Neon Database on the cloud for data storage.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory.
   ```bash
   cd fastapi-todo-app
   ```

3. Update the `DATABASE_URL` environment variable in the `compose.yml` file with your Neon Database connection string.

4. Run the Docker container using Docker Compose.
   ```bash
   docker-compose up -d
   ```

5. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Create a new todo: Send a POST request to `/todos` with JSON payload containing todo details.
- Get all todos: Send a GET request to `/todos`.
- Get a specific todo: Send a GET request to `/todos/{id}` with the todo ID.
- Update a todo: Send a PUT request to `/todos/{id}` with JSON payload containing updated todo details.
- Delete a todo: Send a DELETE request to `/todos/{id}` with the todo ID.

## Contributing

Contributions are welcome! Please feel free to fork this repository and submit pull requests to contribute new features, improvements, or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** Replace `<repository_url>` with the actual URL of your repository.
