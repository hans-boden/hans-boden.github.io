# python3
"""
    Fizzbuzz - a small exercise to get used to the keyboard
    print the numbers from 1 to 50, but
    replace all numbers that are a multiple of:
         3  with the word 'fizz'
         5  with the word 'buzz'
        15  with the word 'fizzbuzz'
"""

def main():
    for num in range(1, 51):
        if not num % 15:
            print('fizzbuzz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0:
            print('fizz')
        else:
            print(num)

# use of the if..else construct often allows to avoid indented blocks
# Shorter, less indented code is usually better to read and faster

def short():
    for num in range(1, 51):
        txt = ''
        if num % 3 == 0:
            txt += 'fizz'
        if num % 5 == 0:
            txt += 'buzz'
        print(txt if txt else num)

def shorter():
    for num in range(1, 51):
        txt = '' if num % 3 else 'fizz'
        txt = txt if num % 5 else txt+'buzz'
        print(txt if txt else num)

def enough():
    for num in range(1, 51):
        txt = ('' if num % 3 else 'fizz') + ('' if num % 5 else 'buzz')
        print(txt if txt else num)
        
#main()
#short()
#shorter()
enough()
