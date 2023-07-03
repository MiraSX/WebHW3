from pathlib import Path
from threading import Thread
from shutil import copyfile, rmtree
import argparse
import logging
from time import time



"""
--source [-s]
--output [-o] default folder = dist
"""

parser = argparse.ArgumentParser(description='Sorting folders')
parser.add_argument('-s', '--source', help='Source folder', required=True)
parser.add_argument('-o', '--output', help='Output folder', default='dist')

args = vars(parser.parse_args())

source = Path(args.get('source'))
output = Path(args.get('output'))

folders = []

def grabs_folders(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folders(el)

def copy_files(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_folder = output / ext
            try:
                new_folder.mkdir(parents=True, exist_ok=True)
                copyfile(el, new_folder / el.name)
            except OSError as err:
                logging.error(err)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    print(source, output)
    folders.append(source)
    grabs_folders(source)
    copy_files(source)

    threads = []
    for folder in folders:
        th = Thread(target=copy_files, args=(folder,))
        th.start()
        threads.append(th)

    cur_time = time()
    [el.join() for el in threads]

    print(f'Time: {time() - cur_time}sec')
    delete = input('Done, delete source folder? [y/n]')
    if delete == 'y':
        rmtree(source)
    
  


