Implementation of a genetic algorithm to solve a fixed-pipes version of FlapPyBird. Main script is "flappy.py". For some genetic algorithm related functionality, this relies on the external "ga_utils.py". Other files contain game data (sprites, sounds), installation related data (pipfiles used by pipenv).

The original FlapPyBird README is reported for installation information:


FlapPyBird
===============

A Flappy Bird Clone made using [python-pygame][pygame]

How-to (as tested on MacOS)
---------------------------

1. Install Python 3.x (recommended) 2.x from [here](https://www.python.org/download/releases/)

2. Install [pipenv]

2. Install PyGame 1.9.x from [here](http://www.pygame.org/download.shtml)

3. Clone the repository:

```bash
$ git clone https://github.com/sourabhv/FlapPyBird
```

or download as zip and extract.

4. In the root directory run

```bash
$ pipenv install
$ pipenv run python flappy.py
```

5. Use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

(For x64 windows, get exe [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame))

Notable forks
-------------

- [FlappyBird Fury Mode](https://github.com/Cc618/FlapPyBird)
- [FlappyBird Model Predictive Control](https://github.com/philzook58/FlapPyBird-MPC)

Made something awesome from FlapPyBird? Add it to the list :)


ScreenShot
----------

![Flappy Bird](screenshot1.png)

[pygame]: http://www.pygame.org
[pipenv]: https://pipenv.readthedocs.io/en/latest/
