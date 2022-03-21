import argparse
from pathlib import Path

from readfile import readfile
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)

    p = parser.parse_args()
    # print(p.file_path, type(p.file_path), p.file_path.exists())
    input_file = open(p.file_path, 'r')
    input_data = readfile.parse_file(input_file)
    print(input_data)

    