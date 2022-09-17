# CmdShiftSFTP

A slim(mable) Python-based SFTP image uploader designed for macOS versions which have Command+Shift+3-5 Screenshot and Screen record shortcuts

## To set up

Clone this repository, open main.py and change the connection, destination and parameters to your wish. Everything is commented to your ease. Then run

```sh
pip3 install -r requirements.txt
```

 and put the repository in a directory you deem safe. Press CMD+Shift+5 and click on options, then change the directory to the images directory in the cloned repository's new location.

## Background listening

Another thing you must do if you want to make this silent: Make an Automator **application** and add a "run shell script" block. In the block you might want to type:

```sh
cd ~/path/to/CmdShiftSFTP
python3 server.py # although you might want to change the python3 path if you have a homebrew installation of python3.
```

Here's why you need an application: Open System Preferences (Or System Settings in Ventura), go to Users and Groups and click on Login Items. Click on the plus and add your automator application. **Don't check "Hide", as it won't do anything regarding the cog at the menu bar**