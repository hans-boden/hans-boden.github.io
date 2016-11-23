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
    other_fruit(fruit)
    
print(r, fruit)

def special_fruit():
    print("special")
    print(r, "peach")
    print(r, fruit)

fruit = "cherry"

def more_fruit(fruit):
    print("more")
    print(r, fruit)
    fruit = 'apple'
    print(r, "grape")
    print(r, fruit)
    
def other_fruit(fruit):
    print("other")
    special_fruit()
    print(r, fruit)
    
print(r, "strawberry")
main()
print(r, fruit)
          
    



    
