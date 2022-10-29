# Local and remote debugging demo

## Playing locally

1. Ensure you are in the `main` branch.
2. Run `py game.py` from the command line and play the game to check that it works fine.
3. Go to Visual Studio Code and load the `game.py` file into it.
4. Add some breakpoints, watchers, etc.
5. Start a debug session with the "python file" and play the game from the integrated terminal.

## Remote debugging

1. Change to branch `debugRemote`.
2. You will need to create the virtual environment for the remote game to work:
    * From the command line, type `py -m venv .venv` to create a new empty virtual environment.
    * Activate the virtual environment running `.venv\scripts\activate`.
    * Install the required library: `pip install -r requirements.txt`.
3. You can now start the game by typing `py game.py`. The debugger will wait for client connections.
4Go to Visual Studio Code and add some breakpoints, watchers, etc.
5. Start a new debugging session of type "remote attach". Enter "localhost" for the host and "2633" for the port.
6. The program should start and you will be able to trace it from VSCode in remote mode.

