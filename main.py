# How to exit an if statement in Python

def my_function(num):
    if num > 0:
        print('num > 0')
        return
    if num < 0:
        print('num < 0')
        return

    print('num = 0')
    return


my_function(100) # 👉️ num > 0

print('-' * 50)

my_function(-30) # 👉️ num < 0

print('-' * 50)

my_function(0) # 👉️ num = 0