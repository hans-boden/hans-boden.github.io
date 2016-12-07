# python3
"""
    Split up a big file into small parts
"""

import itertools

file_name = 'video_of_our_cat.mp4'
block_name = 'video_part_{}.dat'

block_size = 10 * 1000 * 1000 # ~10MB

def main():
    with open(file_name, mode='rb') as fi:
        for blockno in itertools.count(start=1):
            block = fi.read(block_size)
            if not block:  # len(block) == 0:
                break
           
            with open(block_name.format(blockno), mode='wb') as fo:
                fo.write(block)
                  
    

main()
