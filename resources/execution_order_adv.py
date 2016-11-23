    # python3
"""
    This execrcise demonstrates the order of execution as opposed
    to the definition of functions.
    The user should try to guess and write down the order of fruits
    before executing the code. 
"""
r = '         ===> '
print(r, "apple")
fruit = "banana"
print(r, fruit)

def main():
    print("main")
    fruit = "lemon"
    print(r, fruit)
    more_fruit("fig")
    other_fruit()
    basket_of_fruit()
    
print(r, fruit)

def special_fruit():
    print("special")
    print(r, "peach")
    print(r, fruit)

fruit = "cherry"

def more_fruit(apple):
    print("more")
    fruit = 'apple'
    print(r, "grape")
    print(r, apple)
    print(r, fruit)
    
def other_fruit(fruit='blackberry'):
    print("other")
    special_fruit()
    print(r, fruit)
    
def basket_of_fruit():
    print("basket")
    print(r, "pear")
    more_fruit(fruit)
    lemon = "plum"
    other_fruit(lemon)
    print(r, fruit)
    print(r, lemon)
    print(r, 'fruit')
    
print(r, "strawberry")
print(r, "grape")
main()
print(r, "mango")
          
    



    
