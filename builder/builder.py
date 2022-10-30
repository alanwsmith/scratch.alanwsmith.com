#!/usr/bin/env python3

import glob
import os

def get_file_list(source_dir = ''):
    if len(source_dir) == 0:
        source_dir = f"{os.path.dirname(os.path.realpath(__file__))}"
    if source_dir[0] != '/':
        source_dir = f"{os.path.dirname(os.path.realpath(__file__))}/{source_dir}"
    file_list = [
        file for file in glob.glob(f"{source_dir}/*")
        if os.path.isfile(file)
    ]
    print(source_dir)
    return file_list

files = get_file_list()

print(files)

