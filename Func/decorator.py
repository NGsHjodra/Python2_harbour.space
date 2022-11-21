import time
"""
def measure_call_time_decorator(func_to_call):
    #print("something")
    def result_func():
        t1 = time.time()
        func_to_call()
        t2 = time.time()
        print(f"Call time {t2-t1}")
    return result_func

@measure_call_time_decorator
def long_operation():
    x = 0
    for i in range(10000000):
        x+=2

long_operation()
"""
def measure_call_time_decorator(comment):
    def resulting_decorator(func_to_call):
        def result_func():
            print(comment)
            t1 = time.time()
            func_to_call()
            t2 = time.time()
            print(f"Call time {t2-t1}")
        return result_func
    return resulting_decorator

@measure_call_time_decorator("test")
def long_operation():
    x = 0
    for i in range(10000000):
        x+=2

long_operation()
long_operation()