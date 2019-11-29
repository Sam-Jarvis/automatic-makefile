# Automatic-makefile

## Purpose:
Script that generates a makefile automatically. Intended for command line use, i.e. added to PATH. Built for linux, will not work on windows and untested on mac_OS.

## Usage:
Calling _mf_ from command line will generate a makefile in the specified path, specified target and specified compiler. If these values are not specified, path will default to _/home_, target will default to _helloworld_ and the compiler will default to _gcc_.

Command line arguments:
* -d --> specify default compiler (this is persistent)
* -p --> specify path
* -p --> specify compiler for current makefile genreation
