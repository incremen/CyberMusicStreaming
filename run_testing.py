from testing.more_testing import TestClass
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

CHUNK = 4096


def call_class_func(obj, method_name, *args, **kwargs):
    return getattr(obj, method_name)(*args, **kwargs)

def test_function():
    print("Test function ran!")

executor = ProcessPoolExecutor(max_workers=5)


class TestClass:
    def __init__(self):
        global executor
        future1 = executor.submit(test_function)
        future2 = executor.submit(call_class_func, self, 'class_test_func')
        
        print(future1.result())
        print(future2.result())
        
    def class_test_func(self):
        print("Class test function ran!")

if __name__ == "__main__":
    TestClass()

