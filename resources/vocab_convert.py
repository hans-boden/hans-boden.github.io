# python3
"""
    Process some text from a portuguese - english dictionary
    get a list of portuguese word
    the original text was copied from a sequence of web pages
"""

def main():
    infile = 'portuguese_vocab.txt' 
    outfile = 'portuguese_words.txt' 

    words = set()  # add the word into a set, to avoid duplicates

    lines = line_reader(infile)
    for word in first_words(lines, minsize=5):
        if word[0] == '(':
            continue
        words.add(word.lower())

    with open(outfile, mode='w', encoding='utf-8') as fo:
        for ndx, word in enumerate(sorted(words)):
            # print to the console n words per line
            # to show the use of enumerate and the print function
            print(word, end=' ')
            if not (1+ndx)%8:
                print()
                
            fo.write(word+'\n')
    return

def first_words(lines, minsize=6 ):
    # only check the first two words of each line
    # return one word per line, if there is a word >= minsize
    for line in lines:
        tup = line.split()
        if not tup:
            continue
        if len(tup[0]) >= minsize:
            yield tup[0]
            continue
        if len(tup) > 1 and len(tup[1]) > minsize:
            yield tup[1]

def line_reader(infile):
    # return non-empty stripped lines from a file
    with open(infile, encoding='utf-8') as fi:
        for line in fi:
            line = line.strip()
            if line == '':
                continue
            yield line

if __name__ == '__main__':
    main()
