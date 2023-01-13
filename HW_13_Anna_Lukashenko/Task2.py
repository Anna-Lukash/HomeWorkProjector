'''Write a decorator that will calculate the execution time of a function.
Example:
    @calculate_execution_time
    def add(a: int, b: int) -> int:
        return a + b
add(1, 2)
    > 3
    > Execution time: 0.0005 seconds'''
#importing time module   
import time 
#creating decorator that will calculate time of function execution
def calculate_execution_time(func):
    def wrapper(a,b):
        start = time.time()
        res = func(a,b)
        end = time.time()
        execut = end - start
        print(res)
        print(f"Execution time: {execut} seconds")
    
    return wrapper

@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b

add(167872463567865678656787656745678,98978754234567890987654323456)