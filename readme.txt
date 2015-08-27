python snake работающая на curses и просто на print
#TODO1: добавить рендер на pygame и sdl2
#TODO2: добавить тесты
#TODO3: отрефакторить
#TODO4: сделать хранение результатов игроков в файле или базе

Install
=======

install commands::

    mkdir snake
    cd snake
    git clone https://github.com/chaotism/python-snake.git

    sudo apt-get install $(cat requirements/packages.list)
    virtualenv .env --system-site-packages
    source .env/bin/activate
    pip install -r requirements/requirements.pip

USE
========
 сheck settings.local to you config. I am use pygame to render. Default curses
 run game.py
 for curses check world size and console size

Controls
=======
    W: up
    S: down
    A: left
    D: right
    Q: exit

    to change snake direction hold button
