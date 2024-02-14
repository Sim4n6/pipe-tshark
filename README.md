# Docker Compose Project

This project consists of two simple Flask web apps and an Nginx load balancer, all running in separate Docker containers.

## Project Structure

- `app1/`: Contains the Dockerfile and Python file for the first Flask web app.
- `app2/`: Contains the Dockerfile and Python file for the second Flask web app.
- `nginx.conf`: Contains the configuration file for the Nginx load balancer.
- `docker-compose.yml`: Defines the services that make up the app.

## How to Run

1. Build the Docker images:

```bash
docker-compose build
```

2. Run the Docker containers:

```bash
docker-compose up
```

You should now be able to access the Flask web apps via the Nginx load balancer at `http://localhost`.

## How to Stop

To stop the Docker containers, use the following command:

```bash
docker-compose down
```
```

Please replace `http://localhost` with the actual URL if you have configured it differently in your Nginx configuration.