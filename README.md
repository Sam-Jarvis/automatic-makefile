# Automatic-makefile

## Purpose:
Script that generates a makefile automatically. Intended for command line use, i.e. added to PATH. Built for linux, will not work on windows and untested on mac_OS.

## Usage:
Calling _mf_ from command line will generate a makefile in the specified path, specified target and specified compiler. If these values are not specified, path will default to _/home_, target will default to _helloworld_ and the compiler will default to _gcc_.

Command line arguments:
* -d --> specify default compiler (this is persistent)
* -p --> specify path
* -p --> specify compiler for current makefile genreation

## Install:
Run the install script as sudo. _install.py_ needs admin privileges because it adds _mf.py_ to PATH so it can be called from anywhere and referred to as _mf_.

Below is what the install script does. In case mf.py must be added to path manually, follow these steps:
1 Change _mf.py_ to an executable using chmod +x
2 Remove the _.py_ extension from _mf.py_ with _mv mf.py mf_
3 Create a foler somewhere (in _/home_ is recommended)
4 Move _mf_ from step 2 into the foler made in step 3
5 Add folder to path
6 If, when run, you get the "command not recognized" error, try restarting
