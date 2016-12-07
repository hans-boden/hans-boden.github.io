# python3
"""
    Write a big file
    Generate test data for the split-join exercise
"""
file_name = 'video_of_our_cat.mp4'
target_size = 45987321 # size in bytes ~ 45 MB

def main():
    block = 100 * b'1234567890abcdefghijklmnopqrstuvwxyz'  # block of bytes
    block_size = len(block)
    block_count = target_size // block_size
    with open(file_name, mode="wb") as fo:
        for _ in range(block_count):
            fo.write(block)
        remaining_size = target_size - block_size * block_count
        fo.write(block[:remaining_size])
    # done

main()
