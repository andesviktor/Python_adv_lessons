''' Факториал '''
# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print (factorial(-5))

''' Первоклассные функции '''

# def swap(a, b):
#     return b,a

# my_swap = swap
# print(my_swap(1,2))

# 2 в качестве аргументов

# def print_swap(func,a,b):
#     print(func(a,b))

# print_swap(swap, 1, 2)

# 3 возвращать функции

# def return_swap():
#     return swap

# print(return_swap()(1,2))

# 4 определенна где-угодно

# def test(a):

#     def test2(b):
#         print(b)
    
#     print('hello')
# test(5)

'''Каррирование'''

# def greet(greeting,name):
#     print(gretting + ', ' + name)
# greet ('Hello','German')

# def greet_curried(greeting):
#     def greet(name):
#         print(greeting + ', ' + name)
#     return greet

# hello_greet = greet_curried('Hello')
# hello_greet('Ivan')
# greet_curried('Welcome')('Boss')

# import requests
# def parse(headers):
#     def helper(param):
#         print(headers[param])
#     return helper

# google_pars = parse(requests.get("https://google.com").headers)
# google_pars('Date')
# google_pars('Expires')

# import requests, time

# def decor_web_headers_param(func):
#     def helper(*args,**kwargs):
#         start = time.time_ns()

#         func(*args,**kwargs)
#         print(f'Time = {time.time_ns() - start} ns', end='\n\n')
#     return helper

# @decor_web_headers_param
# def web_headers_param(site, param):
#     print (requests.get(site).headers[param])

# #web_headers_param = decor_web_headers_param(web_headers_param)

# web_headers_param('https://google.com','Date')

''' Lambda функции '''
# def add (a,b):
#     return a+b
# addLambda = lambda a,b: a+b

# print(add(1,2))
# print(addLambda(1,2))

# l = [i for i in range(1,21)]
# l = list(filter(lambda x: x%2 == 1,l) )
# l_str = list(map(str, l))
# print(l)
# print(l_str)

def add(*qwe):
    sum = 0
    for i in qwe:
        sum += i
    return sum

def add2(**qwe):
    print(type(qwe))
    sum=0
    print('sum =', end='')
    for k,v,in qwe.items():
        print(f'{k} +',end ='')
        sum +=v
    print()
    return sum

print(add2(a=1,b=2,c=5))

def add_all(*args,**kwargs):
    ret = 0
    for i in args:
        ret += i
    for i in kwargs.values():
        ret += i

    print(ret)

add_all(1,2,3,4,5,a=6,b=7,c=9)