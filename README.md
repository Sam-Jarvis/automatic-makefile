# Automatic-makefile

## Purpose:
Script that generates a makefile automatically. Intended for command line use, i.e. added to PATH. Built for linux, will not work on windows and untested on mac_OS.

## Usage:
Calling _mf_ from terminal will generate a makefile in the working directory. The program will search for _.c_ files in the working directory and create a makefile for the last modified _.c_ file. If no _.c_ files are found, the program will generate a makefile with _helloworld_ as the target, i.e. it will generate a generic makefile. The target, compiler, path or default comiler can be specified with command line arguments.

Command line arguments (all optional):
* -d --> specify default compiler (this is persistent)
* -c --> specify comiler for current makefile generation (this is temporary)
* -p --> specify path in which to search for _.c_ files
* -p --> specify compiler for current makefile generation
* -t --> specify target for current makefile generation

## Install:
Run the install script, _install.py_ with `python3 install.py`. This adds _mf.py_ to PATH so it can be called in terminal as _mf_.
Note: Do __not__ run _install.py_ as sudo.

Below is what the install script does. In case mf.py must be added to path manually, follow these steps:
1. Change _mf.py_ to an executable using `chmod +x`
2. Remove the _.py_ extension from _mf.py_ with `mv mf.py mf`
3. Create a foler somewhere (in _/home_ is recommended)
4. Move _mf_ from step 2 into the foler made in step 3 with `cp mf "path_to_folder"`
5. Add folder to path with `echo 'export PATH=$PATH":$HOME/your_folder"' >> .profile`. Note: make sure to change "your_folder" the the actual folder name. 
6. Run `source .profile` from terminal to refresh the _.profile_ file and make _mf_ usable. 
7. Try typing `mf` into terminal. If you get a "command not found" error, try restarting.
