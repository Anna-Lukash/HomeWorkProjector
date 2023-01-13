'''
Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.
Example:
@check_types
def add(a: int, b: int) -> int:
    return a + b
add(1, 2)
> 3
add(1, "2")
> TypeError: Argument b must be int, not str'''

#creating a decorator that checks type of variable.
def decorator(func):
    def wrapper(a,b):
        if type(a) != int:
            print(f'TypeError: Arguments a must be int, not {type(a)}.')
        elif type(b) != int:
            print(f'TypeError: Arguments b must be int, not {type(a)}.')
        else:
            print(func(a,b))
    return wrapper
                 
#using decorator on function
@decorator
def add(a: int, b: int) -> int:
    return a + b

add(2,'6')
