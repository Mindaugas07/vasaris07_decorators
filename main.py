from typing import Callable


# def give_something(text: str) -> str:
#     return text


# def another_function(fn: Callable[[str], str], name: str) -> str:
#     return fn(name)


# a = another_function(give_something, name="Mindaugas")

# print(a)


# def print_dot_a():
#     print("asdfl")

#     def return_dot_b():
#         print("lk;vcjx")

#     def return_dot_c():
#         print("wwwwwwwwwww")

#     return_dot_c()
#     return_dot_b()


# print_dot_a()


# def takes_numb(numb: int):

#     def single_digit():
#         return "Its a single digit"

#     def multi_digit():
#         return "Its multidigit"

#     if numb <= 9:
#         return single_digit
#     return multi_digit


# number_1 = takes_numb(11)
# print(number_1())
# # print(takes_numb(8)())


# def my_decorator(fn: Callable):

#     def wrapper():
#         print("Say somethibg")
#         fn()
#         print("say something else")

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello")


# # me_say = my_decorator(say_hello)
# say_hello()


# @my_decorator
# def give_two_numbers():
#     print("2", "78")


# give_two_numbers()


# def my_decorator(fn: Callable):

#     def wrapper():
#         print("Say somethibg")
#         result = fn()
#         print("say something else")
#         return result

#     return wrapper


# @my_decorator
# def give_two_numbers():
#     return 2


# val = give_two_numbers()

# print(val)


# Create a simple function that generates random word and returns a lentgh of that word.
# Create a decorator function that would inform if the word is short (< 6 characters) or long (>=6 chars).
# from random import randint

# letters = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]


# def gen_word(fn: Callable):

#     def wrapper():
#         word = ""
#         length = randint(1, 20)
#         for _ in length:
#             letter_index = randint(1, 26)
#             word.append(letters[letter_index])
#         length = fn()
#         return length

#     return wrapper


# @gen_word
# def word_len():
#     if gen_word() >= 6:
#         return "long"
#     return "short"


# val = gen_word()

# print(val())


# import random
# from typing import Callable, List


# WORDS = [
#     "Create",
#     "simple",
#     "function",
#     "that",
#     "generates",
#     "random",
#     "word",
#     "returns",
#     "lentgh",
#     "that",
#     "word",
# ]


# def info_about_word(fn: Callable):

#     def wrapper() -> str:
#         word_lenght = fn()
#         if word_lenght < 6:
#             print("It is short word")
#         else:
#             print("It is long word")
#         return word_lenght

#     return wrapper


# @info_about_word
# def random_word() -> int:
#     return len(random.choice(WORDS))


# word_info = random_word()

# print(word_info)

# Write a Python decorator @time_it that measures the time taken by a function to execute and prints it.

# from timeit import Timer


# def time_it(fn: Callable):

#     def wrapper():
#         t = Timer()
#         start = t.timeit()
#         result = fn()
#         end = t.timeit()
#         print(end - start)
#         return result

#     return wrapper


# @time_it
# def adding_two_numbers():
#     return 2 + 2


# time = adding_two_numbers()
# time


# Write two decorators that would make the function output in uppercase (first) and should reverse the output string (second).
# Apply both decorators to a function that returns "hello world".


# def to_upercase(fn: Callable[[None], str]):

#     def wrapper():
#         result = fn()

#         return result.upper()

#     return wrapper


# def to_reverse(fn: Callable[[None], str]):

#     def wrapper():
#         result = fn()

#         return result[::-1]

#     return wrapper


# @to_reverse
# @to_upercase
# def returns_hello_world() -> str:
#     return "hello world"


# word = returns_hello_world()

# print(word)


# Create a decorator that logs (prints and to the file) the function name, time and results every time the function is called.
# import datetime
# import logging

# logging.basicConfig(level=logging.DEBUG, filename="data.log", filemode="w")


# def log_func_info(fn: Callable):

#     def wrapper():
#         current_time = datetime.datetime.now()
#         print(f"Current time is: ", current_time)
#         logging.info(f"Current time is: {current_time}")
#         result = fn()
#         print(f"You called function: ", fn.__name__)
#         logging.info(f"You called function: {fn.__name__}")
#         logging.info(f"The result of the function is: {result}")
#         return f"The result of the function is: {result}"

#     return wrapper


# @log_func_info
# def adding_two_numbers():
#     return 2 + 2


# time = adding_two_numbers()
# print(time)

# import logging
# from typing import Callable


# logging.basicConfig(
#     level=logging.INFO,
#     filename="logger.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# def logger(fn: Callable) -> str:

#     def wrapper():
#         my_func = fn()
#         logging.info(f"Function {fn.__name__!r}")
#         print(f"Function {fn.__name__!r}")
#         return my_func

#     return wrapper


# @logger
# def count_smth():
#     return 50 * 50


# print(count_smth())

# import time
# from typing import Callable


# def measure_time(fn: Callable):

#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         start_time = time.time()
#         procers = fn(*args, **kwargs)
#         end_time = time.time()
#         duration = end_time - start_time
#         print(f"Function {fn.__name__} took {duration:.6f} seconds to execute.")
#         return procers

#     return wrapper


# @measure_time
# def example_function(nr: int):
#     for i in range(nr):
#         i = i**2
#     return "Done"

# @measure_time
# def next_funtion(a: int, b: int, c: int):
#     return a + b + c


# example_function(nr=100000)

# print(example_function(nr=100000))

# result = next_funtion(10, 15, c=20)
# print(result)

# Write a decorator that should check if all arguments passed to the method are positive.
# If not, it should raise a ValueError. A function should calculate square of numbers.


# def if_positive_numbers(fn: Callable):

#     def wrapper(*args, **kwargs):
#         is_negative = False
#         for arg in args:
#             if arg < 0:
#                 is_negative = True

#         if not is_negative:
#             my_func = fn(*args, **kwargs)
#             return my_func
#         else:
#             raise ValueError("Please use positive numbers!")

#     return wrapper


# @if_positive_numbers
# def square_of_numbers(nr_one: int, nr_two: int) -> int:
#     return nr_one**2, nr_two**2


# print(square_of_numbers(1, 3))
# print(square_of_numbers(1, -9))


# Write a decorator that catches any exceptions thrown by the function and prints an error message instead of letting the program crash.

# from typing import Callable


# def error_hunter(fn: Callable):

#     def wrapper(*args, **kwargs):
#         try:
#             result = fn(*args, **kwargs)
#             return result
#         except Exception as err:
#             print(f"Error: {err}")

#     return wrapper


# @error_hunter
# def divide_by_zero(number: int):
#     return number / 0


# print(divide_by_zero(4))

# Write a decorato that retries a function if it raises an exception. The function should be retried 3 times before finally raising the exception.

# def error_hunter(fn: Callable):

#     def wrapper(*args, **kwargs):
#         counter = 0
#         for _ in range(3):
#             try:
#                 result = fn(*args, **kwargs)
#                 return result
#             except Exception:
#                 pass
#             counter += 1
#             print(counter)
#         return fn(*args, **kwargs)

#     return wrapper


# @error_hunter
# def divide_by_zero(number: int):
#     return number / 0


# print(divide_by_zero(4))
