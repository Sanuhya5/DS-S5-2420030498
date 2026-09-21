# finding the square root

def find_square_root(n):
    return math.sqrt(n)
num_to_square=input()
square=find_square_root(int(num_to_square))
print(f"The square root of {num_to_square} is {square}")


#finding the number if it is even or odd using function

def check_even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

num_to_check=input()
result=check_even_odd(int(num_to_check))
print(f"The number {num_to_check} is {result}")