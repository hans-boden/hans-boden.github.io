# python3
"""
    sort a list of words alphabetically correct (for the portuguese language)
"""

infile = "./portuguese_words.txt"
outfile = "./sorted_word.txt"

portsort = ('AÀÁÂÃ', 'CÇ', 'EÈÉÊ', 'IÌÍÎ', 'OÒÓÔÕ', 'UÙÚÛ',
            'aàáâã', 'cç', 'eèéê', 'iìíî', 'oòóôõ', 'uùúû')


def main():
    trt = make_transtab()

    words = list(get_words(infile))

    # this is a list comprehension:
    word_tups = [(w.translate(trt).lower(), w) for w in words]
    """  the above statement is equivalent to:
    word_tups = []
    for w in words:
        wsort = w.translate(trt).lower()
        word_tups.append((wsort, w))
    """
    word_tups.sort()  # sort in-place
    
    with open(outfile, mode='w', encoding='utf-8') as fo:
        for _, word in word_tups:
            fo.write(word +'\n')  # add a new-line char after each word


def make_transtab():
    tr_dict = {}
    for chars in portsort:
        target = chars[0]
        for char in chars[1:]:
            tr_dict[char] = target
    tr_table = str.maketrans(tr_dict)
    return tr_table
        
def get_words(filename):
    with open(filename, mode='r', encoding="utf-8") as fi:
        for line in fi:
            line = line.strip()
            if line:
                yield line
main()
