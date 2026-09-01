# Elite Four

A small game I made for four of my friends.
Each of them has a dedicated mini-game, and the goal is to beat them all.

# Play the game

### Download an executable file

To play the game, you can download it in the [Releases](https://github.com/Hvrnbi/elite-four/releases) section.
- If you're using Windows, you can download the .exe file.
- If you're using linux, you can try the other executable, it was tested on Debian 13 with an amd64 architecture.
- If you're using something else, you can see the **run from the Python file** section or the **building** section.

### Run the game from the Python file

To run the game from the main.py file, you have to

- clone this repo with ```git clone https://github.com/Hvrnbi/elite-four```,
- go to the directory of the game with ```cd elite-four```,
- create a Python virtual environment with ```python3 -m venv .venv``` on Unix, ```python -m venv .venv``` on Windows,
- install the dependencies with ```.venv/bin/pip install -r requirements.txt``` on Unix, ```.venv\Scripts\pip install -r requirements.txt``` on Windows,
- and finally run the game with ```.venv/bin/python3 main.py``` or ```.venv\Scripts\python main.py```.

### Build the game from source

To build the game from source, do the steps above (without running the game) and run ```.venv/bin/pip install pyinstaller```.

You should now be able to run ```.venv/bin/pyinstaller main.py --add-data="images:images" --add-data="audio:audio" --hidden-import='PIL._tkinter_finder' --onefile```, and the game should be built !

# Demo

[Demo video](https://youtu.be/j4FESrdhjTo)

# Thanks

This game is dedicated to Mister C, Mister E, Miss N and Miss W 💜

The song from the Miss W"s game was performed by me and inspired by [the Scottish of Ruz Reor](https://youtu.be/_QP1e3a9Jhc)

All the pictures used for the Mister C's game are listed in [this file](PICTURES-CREDITS.md).

I used the website [flagcolorcodes](https://www.flagcolorcodes.com/search/france) for the color of the flags.

Thank you for your interest in this project made with ❤️ by a human for his friends.

## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G5J5206K5C)
[![liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/Harupi/donate)
