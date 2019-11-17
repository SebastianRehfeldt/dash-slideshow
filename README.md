# Slideshow using Python Dash

This project implements a simple slideshow using Python Dash. The project provides the UI framework, including navigation, and a docker-compose setup for easy local setup.


## Screenshots

|                                      Agenda                                       |                          Slide with interactive Plot                          |
| :-------------------------------------------------------------------------------: | :---------------------------------------------------------------------------: |
| ![](https://github.com/SebastianRehfeldt/dash-slideshow/blob/master/docs/images/overview.png) | ![](https://github.com/SebastianRehfeldt/dash-slideshow/blob/master/docs/images/plot.png) |


## Add your own slides

1. Write a function in `src/slides` which creates the UI of your new slide
2. Add it within `src/slides/__init__.py` with your intended url for this slide
3. Eventually implement callbacks in `src/callbacks` for dynamic elements
4. Callbacks are added to the dash app in `src/callbacks/__init__.py`


## Setup using Docker

```bash
docker-compose build
docker-compose up -d

# Stop and remove container
docker-compose stop

# Restart container
docker-compose restart
```

You can change the title of the slideshow in `app.py` and once you are down developing, you can set debug to False and switch the command in the `docker-compose.yml`.


### Development in VS Code

I'd recommend to use VS Code as it allows to develop directly inside the Docker container.

1. Install the `Docker` and `Remote Development` extensions.
2. Start the docker image, open Docker tab in side-panel, right-click on the container and click attach VS Code
3. This opens the root folder in your container
4. Open your project folder and enable extensions if you need any (e.g. python for formatting or jupyter)

By default, the dash app is started using gunicorn and the code is reloaded on each code change. 
In case of errors, the image would shut down which is why the app creation is wrapped within a try/except block.
To check why the app fails, run `python app.py` from within the docker image.


### Code Checks

```bash
mypy .
flake8 .
pylint src
```
