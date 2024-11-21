from typing import Iterable

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print(f"m is {m:.3f} n is {n:.3f}")

def process_files(search_term, *file_paths):
    print(f"{search_term = }")
    print(f"{file_paths = }")
    
    for file_path in file_paths:
        print(file_path)

process_files('spam.txt', 'ham.txt', 'toast.txt')
# process_files(['spam.txt', 'ham.txt', 'toast.txt'])

def proc(file_paths: Iterable) -> None:
    for file_path in file_paths:
        print(file_path)

def greet(whom="world"):
    print(f"Hello, {whom}")

greet('Mom')
greet("JPMC")
greet()

def faux_grep(search_term, *file_paths, ignore_case=False):
    pass

faux_grep("wombat", "spam.txt", "ham.txt", ignore_case=True)

def config(**config_vars):
    print(f"{config_vars = }")
    
config(file_name="spam.txt", date="2023-04-19")

def _helper():
    pass

class Klown:
    pass
