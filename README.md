# Eyesight
## Control your objects just by looking around 

![Flask|Python](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![raspberry](https://camo.githubusercontent.com/17b6032a55bb14ed30116823fa500b769a8f4a2f114cebe916284b681f3602ba/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d52617370626572727925323050692d4335314134413f7374796c653d666c61742d737175617265266c6f676f3d5261737062657272792d5069)

[![Build Status](https://camo.githubusercontent.com/4e084bac046962268fcf7a8aaf3d4ac422d3327564f9685c9d1b57aa56b142e9/68747470733a2f2f7472617669732d63692e6f72672f6477796c2f657374612e7376673f6272616e63683d6d6173746572)](#)

Eyesight is a solution to control your connected devices by looking at IP cameras or USB webcam situated in your house .

- Look on the left facing a camera to switch On or Off your device 
- Look on the right to do the same thing on another device
- You can set two devices per camera 

## Flask Application Structure 
```
.
|──────app/
|────eyesight/
| | |────static/
| | | |─────css/
| | | | |─────calendar.css
| | | | |─────index.css
| | | | |─────profil.css
| | | | |─────sidebars.css
| | | |─────img/
| | | | |─────boisleve.jpg
| | | | |─────eye-fill.svg
| | | | |─────jridi.jpg
| | | | |─────pilliet.jpg
| | | | ─────bonnePhoto.png
| | |────templates/
| | | |──────calendar.html
| | | |──────contact.html
| | | |──────dashboard.html
| | | |──────index.html
| | | |──────profil.html
| | | |──────register.html
| | |────views.py
| |────bonnePhoto.png
| |────cam.sh
| |────init_db.py
| |────choix.txt
| |────config.txt
| |────coordonnees_rect.py
| |────data.txt
| |────data3.txt
| |────etat.txt
| |────frame.py
| |────haarcascade_eye.xml
| |────haarcascade_frontalface_default.xml
| |────image.py
| |────objet_1.txt
| |────objet_2.txt
| |────objet_3.txt
| |────objet_4.txt
| |────objet_5.txt
| |────objet_6.txt
| |────On_off.py
| |────on_off.txt
| |────ouverture.py
| |────position_yeux.txt
| |────run.py
| |────symbole.py
```


Flask is an open-source micro framework for web development in Python. It is classified as microframework because it is very lightweight. Flask aims to keep a simple but extensible core. It does not include an authentication system, no database abstraction layer, or form validation tool. However, many extensions make it easy to add functionality. It is distributed under the BSD license.

> In 2018, Flask was voted "Most Popular Web Framework" by the Python Developers Survey6.
> In January 2020, it had more than 49,000 stars on GitHub,
> more than any other Python web development framework.


## Tech

To make Eyesight work, we used a number of open source projects and tools to make it work properly:

- [HTML] - Markup language designed to represent web pages.
- [PyCharm] - PyCharm is an integrated development environment used to program in Python.
- [Bootstrap] - Great UI boilerplate for modern web apps
- [Shell] - Interpreter that executes your Python programs, other Python code fragments, or simple commands.
- [Raspberry Pi 4] - The Raspberry Pi is a credit card-sized, ARM-based, single-board nanocomputer.


And of course Eyesight itself is open source with a [public  repository](https://github.com/PierreBoisleve/Eyesight) 
on GitHub.

## Installation

Eyesight requires [Python](https://www.python.org/) v3.9.2+ to run.
and [Flask](https://flask.palletsprojects.com/en/2.0.x/) v1.1.2+ to run.

But also different packages such as
- [Matlab] - Matlab is a scripting language emulated by a development environment of the same name; it is used for numerical calculation purposes.
- [NumPy] - NumPy is a library for Python programming language, intended to manipulate matrices or multidimensional arrays as well as mathematical functions operating on these arrays.

Install the dependencies and devDependencies and start the server.

```sh
cd Downloads
./flask.sh
```

For production environments without using flask.sh...

```sh
export FLASK_APP = run.py
export FLASK_ENV = dvp
export DB_USERNAME = /*your db username*/
export DB_PASSWORD = /*your db password*/
flask run
```

## Server

Eyesight is a Raspberry Server based application it is very easy to install and deploy on your computer.

By default, the Docker will expose port 5000 of the Rapsberry, so you can't access the application from your computer.
So to access the application you must be connected to the same Network as your Raspberry. Then type the following command lines via the Raspberry terminal you can access via a secured SSH connection.

```sh
$ flask run --host=0.0.0.0
```

> Note: launching the application via the SSH connexion `$ sh flask.sh` is required for making it work on your computer.

Otherwise, the application is accessible by navigating to your server address in
your preferred browser on the Raspberry.

```sh
127.0.0.1:5000
```

## License

MIT

**Free Application, Hell Yeah!**
