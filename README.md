# Slideshow using Python Dash

This project implements a simple slideshow using Python Dash. The project provides the UI framework, including navigation, and a docker-compose setup for easy local setup.

**SHOW SOME IMAGES HERE**


## Add your own slides


## Setup using Docker

```bash
docker-compose build
docker-compose up -d

# Stop and remove container
docker-compose stop

# Restart container
docker-compose restart
```

### Development in VS Code

I'd recommend to use VS Code as it allows to develop directly inside the Docker container.

1. Install the `Docker` and `Remote Development` extensions.
2. Once, the container is up, open the Docker tab in the side-panel, right-click on the container you want to mount and attach VS Code
3. This opens the root folder in your container
4. Open your project folder and enable extensions if you need any (e.g. python for formatting or jupyter)

### Code Checks