#!/usr/bin/env python3

from termcolor import colored
from os.path import expanduser
import argparse
import os
import datetime
import re

# PARSER
parser = argparse.ArgumentParser()

parser.add_argument('-p', dest='file_path', help='Folder path of .c file')
parser.add_argument('-d', dest='default_compiler', help='Sets the default compiler; '
                                                        'this is persistent')
parser.add_argument('-c', dest='compiler', help='Compiler to use')

args = parser.parse_args()

eg_variable = args.file_path

# FUNCTION DEFINITIONS
def write_makefile(compiler, target):
    with open('Makefile.txt', 'w') as makefile:
        makefile.write('CC = {}\n'.format(compiler))
        makefile.write('TARGET = {}\n'.format(target))
        makefile.write('NAME = {}\n\n'.format(target))
        makefile.write('.PHONY: clean\n\n')
        makefile.write('$(NAME): $(TARGET).c\n')
        makefile.write('\t$(CC) $(TARGET).c -o $(TARGET)\n\n')
        makefile.write('$(NAME).o: $(TARGET).c\n')
        makefile.write('\t$(CC) -c -o $(TARGET).o $(TARGET).c\n\n')
        makefile.write('clean:\n')
        makefile.write('\trm -f $(TARGET) $(TARGET).o')


def get_latest_file(list_of_files):
    list_length = len(list_of_files)
    a = list_of_files[0]
    i = 0
    while i < list_length:
        if get_date_from_file(list_of_files[i]) > get_date_from_file(a):
            a = list_of_files[i]
        i += 1
    return a


def get_date_from_file(file):
    timestamp = os.path.getmtime(file)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date


def search_directory(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(colored('[-]', 'red'), colored('incorrect path'))
        return

    regex = '^' + directory + '/{1}[A-Za-z0-9\s_.\-\(\):]*\.c$'
    files_in_dir = []
    for root, directories, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if re.search(regex, full_path):
                files_in_dir.append(full_path)
    if len(files_in_dir) < 1:
        print(colored('[-]', 'yellow'), colored('no C files found in working directory'))
        return -1
    return files_in_dir

# ^/home/samjarvis/git/automatic-makefile/{1}[A-Za-z0-9\s_.\-\(\):]*$
# ^(.*)(\.c)$


def get_target_name(path):
    sl = path.split('/')
    for fragment in sl:
        if re.search('^.*\.c$', fragment):
            f_name, ext = fragment.split('.')
            name = f_name
    return name


def save_default_compiler(default_compiler):
    hm_dir = get_home_dir()
    with open('{}/.default_compiler.txt'.format(hm_dir), 'w') as dc:
        default_compiler = default_compiler
        print(colored('[+]', 'green'), colored('default compiler set: {}'.format(default_compiler)))
        dc.write(default_compiler)


def read_default_compiler():
    hd = get_home_dir()
    default_compiler = 'gcc'
    try:
        with open('{}/.default_compiler.txt'.format(hd), 'r') as dc:
            default_compiler = dc.read()
            default_compiler = default_compiler
    except FileNotFoundError:
        print(colored('[-]', 'yellow'), colored('default compiler config not found'))
    return default_compiler


def get_home_dir():
    hm_dir = expanduser('~')
    return hm_dir


# OS
wrk_dir = os.getcwd()
hm_dir = get_home_dir()

compiler = read_default_compiler()

if wrk_dir == hm_dir:
    wrk_dir = os.path.expanduser("~/Desktop")

if args.file_path:
    wrk_dir = args.file_path

if args.default_compiler:
    compiler = args.default_compiler
    save_default_compiler(compiler)

if args.compiler:
    compiler = args.compiler

found_files = search_directory(wrk_dir)


def main():
    if found_files == -1:
        print(colored('[+]', 'green'), colored('generating generic makefile'))
        write_makefile(compiler, 'helloworld')
    elif found_files is None:
        print(colored('[*]', 'red'), colored('exiting.'))
        return
    else:
        if len(found_files) == 1:
            target_name = get_target_name(found_files[0])
            print(colored('[+]', 'green'), colored('generating makefile for: {}'.format(target_name)))
            write_makefile(compiler, target_name)
            print(colored('[*]', 'green'), colored('done.'))

        else:
            latest_file = get_latest_file(found_files)
            target_name = get_target_name(latest_file)

            print(colored('[+]', 'green'), colored('generating makefile for: {}'.format(target_name)))
            write_makefile(compiler, target_name)
            print(colored('[*]', 'green'), colored('done.'))


main()
