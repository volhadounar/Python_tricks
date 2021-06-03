#
# Implement the decorator function, which helps to count how many times
# the function has occurred.
# *NOTE:* NOT able to use global variables.

def counter(f):
    _func_calls = {}
    def inner(*args, **kwargs):
        if not f.__name__ in _func_calls:
            _func_calls[f.__name__] = 0
        _func_calls[f.__name__] += 1
        res = f(*args, **kwargs)
        return res, _func_calls[f.__name__]
    return inner

@counter
def sum(a, b):
    return a + b
@counter
def mult(a, b):
    return a * b

print(sum(1, 3))
print(sum(1, 3))
print(mult(1, 3))


### Task 2

# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.
#Example:

#```python
#>>> split_by_index(87178291199)
#(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
#```

def split_by_index(num):
    return tuple(int(digit) for digit in str(num))

def split_by_index2(num):
    return tuple([int(digit) for digit in str(num)])

def split_by_index3(num):
    return tuple(map(int, str(num)))

print(split_by_index3(3436435656456435643))

### Task 3

# Implement a function
# `get_pairs(lst: List) -> List[Tuple]` which returns a list of tuples containing pairs of elements.
#  Pairs should be formed as in the example. If there is only one element in the list return `None` instead.

def rotate(A, k):
    return A[k:]+A[0:k]


def get_pairs(lst: list):
    res = []
    times_to_rotate = len(lst)
    lst_rotated = lst
    for i in range(times_to_rotate):
        lst_rotated = rotate(lst_rotated, 1)
        res.extend(zip(lst, lst_rotated))
    return tuple(res)

print(get_pairs([1, 2, 3, 4]))



### Task 4

# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# 1) characters that appear in all strings

# 2) characters that appear in at least one string

# 3) characters that appear at least in two strings

# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

# ```python
# test_strings = ["hello", "world", "python", ]
#print(test_1_1(…
#>>> {'o'}
#print(test_1_2(…))
#>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
#print(test_1_3(…
#>>> {'h', 'l', 'o'}
#print(test_1_4(…
#>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
#```

def build_statistic(lst: list):
    ch_cnt = {}
    for word in lst:
        for ch in word.lower():
            if ch not in ch_cnt:
                ch_cnt[ch] = []
            if word not in ch_cnt[ch]:
                ch_cnt[ch].append(word)
    return ch_cnt


def find_most_popular_ch(lst: list):
    ch_cnt = build_statistic(lst)
    return {key for key, vals in ch_cnt.items() if len(vals) == len(lst)}

test_strings = ["hello", "world", "python", ]
print(find_most_popular_ch(test_strings))


def find_at_least_popular_ch(lst: list):
    ch_cnt = build_statistic(lst)
    return {key for key, vals in ch_cnt.items() if len(vals) >= 2}

print(find_at_least_popular_ch(test_strings))


def find_not_so_popular_ch(lst: list):
    ch_cnt = build_statistic(lst)
    return {key for key, vals in ch_cnt.items() if len(vals) >= 1}


print(find_not_so_popular_ch(test_strings))


def find_absent_ch(lst: list):
    all_ch = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
    ch_cnt = build_statistic(lst)
    existed = {key for key, vals in ch_cnt.items()}
    return all_ch - existed

print(find_absent_ch(test_strings))


### Task 5

# Implement a decorator `call_once` which runs a function or method once and caches the result.

# ```python
# @call_once
# def sum_of_numbers(a, b):
#    return a + b

#print(sum_of_numbers(13, 42))
#>>> 55
#sum_of_numbers(13, 42)
#sum_of_numbers(13, 42)
#sum_of_numbers(13, 42)
#```

def call_once(func):
    _cache = {}
    def inner(*args):
        res = _cache.get(args)
        if res is None:
            res = func(*args)
            _cache[args] = res
            return res
        return res
    return inner

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))


### Task 6

# Create decorator deprecated2 to take an optional argument — a function to call instead of the original function.
# Example:
#def deprecated2(...
#@deprecated2(new_foo_bar)
#def foo_bar(a, b):
#    return a + b
#foo_bar(1, 2)
#Result:
#foo_bar is deprecated. new_foo_bar will be called instead
#2

def deprecated(func):
    def wrapper(true_func):
        def inner(*args):
            print(f'{true_func.__name__} is deprecated. {func.__name__} will be called instead')
            return func(*args)
        return inner
    return wrapper

def mult(a, b):
    return a * b

@deprecated(mult)
def sum(a, b):
    return a + b


print(sum(3, 4))
# sum is deprecated. mult will be called instead
# 12



### Task 7

# Write a decorator which wraps functions to log function arguments and the return value on each call. 
# Provide support for both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both): 

#@logged 
#    def func(*args): 
#    return 3 + len(args) 

#func(4, 4, 4) 

#you called func(4, 4, 4) 
#it returned 6
#6

def logged(file):
    def logger(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(file, 'a') as f:
                print(args)
                
                params1 = [str(arg) for arg in args]
                params2 = [k+'='+str(v) for k, v in kwargs.items()]
                params= ', '.join(params1) + ', ' + ', '.join(params2)
                f.write(f'you called {func.__name__}({params})' + '\n')
                f.write(f'It returned {res}'  + '\n')
            return res
        return inner
    return logger

@logged('my_log.txt')
def func(*args, **kwargs): 
    return 3 + len(args) 

func(1, 2, 3, a=4)

