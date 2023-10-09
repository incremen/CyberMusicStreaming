from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

CHUNK = 4096


def test_function():
    print("Test function ran!")


class TestClass:
    def __init__(self, songs_dir : str):
        self.executor = ProcessPoolExecutor(max_workers=5)
        
        self.executor.submit(test_function)
            
    def class_test_func(self):
        print("Class test function ran!")