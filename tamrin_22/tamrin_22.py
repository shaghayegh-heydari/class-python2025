
def is_even(number):
    if number% 2 == 0:
        return True
    else:
        return False
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if is_even(num):
        print(f"{num}zoge ast")
    else:
        print(f"{num}fard ast")