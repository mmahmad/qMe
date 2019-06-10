# QMe

IN DEVELOPMENT

## Development server

Each module of the application, front-end, back-end, and database, has been Docker-containerized for easy development and development.

The project uses:
- Angular, for the front-end
- Flask, for the APIs
- Postgres as the DBMS

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 7.3.7.

1) Install <a href="https://www.docker.com/products/docker-desktop">Docker Desktop</a>
2) Clone the repo
3) Run `chmod +x start.sh && chmod +x stop.sh`
4) Run `./init.sh`
5) Navigate to `localhost:4201` for the front-end
6) Navigate to `localhost:5000` for the back-end

To access Postgres from host: `host='localhost'` and `port=32000`
To access Postgres from container: `host='postgres'` and `port=5432`

The front-end app will automatically reload if you change any of the source files.
