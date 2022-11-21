from datetime import datetime

"""
Create a function that takes N (positive integer) as an argument and returns a function to 
calculate the sum of the first K integers in power N. E.g. for K=5, N = 2 result will be 55 (1 + 4 + 9 + 16 + 25).
Create a list of such functions for N from 1 to 5, ask the user for the K, and print corresponding sums.
"""

def SumofPower(N :int):
    def Power(K :int):
        return sum((i+1)**N for i in range(K))
    return Power

ListOfFunc = [SumofPower(i+1) for i in range(5)]

print("First task : ")
K = int(input("What is your K : "))

for i in range(len(ListOfFunc)):
    print(f"N = {i+1} : {ListOfFunc[i](K)}")





"""
Create a decorator, that for any function will log it's call with starting and 
finishing time and also function name (google how to do it). Demonstrate the behavior!

So, if function "print_hello" will be decorated with your decorator and called, output should be like this:
2022-11-21 10:50:72.321 Function 'print_hello' started.
Hello!
2022-11-21 10:50:72.875 Function 'print_hello' finished.
"""

def log_time_decorator(func_to_call):
    def result_func():
        print(f"{datetime.now()} Function '{func_to_call.__name__}' started.")
        func_to_call()
        print(f"{datetime.now()} Function '{func_to_call.__name__}' finished.")
    return result_func

@log_time_decorator
def hola():
    print("Hello!")

print("\nSecond task : ")
hola()