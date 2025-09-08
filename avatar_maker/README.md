# Avatar maker

Self explanatory title.

Check the conversation that gives me the path: [ai conversation](AI_Chat.md).

## Usage

The Docker environment offers two ways to interact with the application:

1. Command line
2. Web app.

### Interacting with the command line

Enters in the container and execute python commands executing `cli.py`.

To check options from command line, run (inside the container) `python3 --help`

### Interacting with web app.

To use the web interface, there are some additional steps, though:

1. Enter in the `avatar_maker_app` container (from `docker-compose.yml` receipt) and start server running:

```
flask run --host=0.0.0.0
```

2. Enter in the `avatar_maker_web` container (from `docker-compose.yml` receipt as well) and start the development react server with the following command:

```
npm run start
```

The api can be accessed in the following address: `http://0.0.0.0:3001`

The web interface can be acessed by the following address: `http://0.0.0.0:5001`
