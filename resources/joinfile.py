# python3
"""
    Reconstruct the original big file from the small parts
"""

import itertools
import os.path

file_name = 'video_of_our_cat_new.mp4'
block_name = 'video_part_{}.dat'

def main():
    #with_exception()
    with_os_exists()
    
def with_exception():
    # handle FileNotFoundError to determine, when all files are finished
    with open(file_name, mode='wb') as fo:
        for blockno in itertools.count(start=1):
            bname = block_name.format(blockno)
            try:
                with open(bname, mode='rb') as fi:
                    block = fi.read()
            except FileNotFoundError:
                break
            fo.write(block)

def with_os_exists():
    # check existence of file, before trying to open it
    with open(file_name, mode='wb') as fo:
        
        for blockno in itertools.count(start=1):
            bname = block_name.format(blockno)
            if not os.path.exists(bname):
                break
            with open(bname, mode='rb') as fi:
                block = fi.read()
            fo.write(block)

main()
