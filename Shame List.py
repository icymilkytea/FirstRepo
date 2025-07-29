#user_input=input("Пользовательский ввод, аргументов и кваргументов:").split(",")
user_input="1 2 3 4 5 2 4, filter_even=True, square=True, unique=True".split(",")
def analyze(user_input):
    numbers_str = user_input[0]  # "1 2 3 4 5 2 4"
    numbers = list(map(int, numbers_str.split()))
    flags = user_input[1:]
    kwargs = {}
    for flag in flags:
        key, value = flag.strip().split("=")
        kwargs[key] = value == "True"
    def decorator(func):
        def wrapper():
            print("Функция началась")
            result = numbers

            if kwargs.get("filter_even", False):
                result = list(filter(lambda i: i % 2 == 0, result))

            if kwargs.get("square", False):
                result = list(map(lambda i: i ** 2, result))

            if kwargs.get("unique", False):
                result = list(set(result))

            func(result)
        return wrapper
    return decorator

@analyze(user_input)
def process_numbers(result):
    print(result)

process_numbers()

user_input=input("Пользовательский ввод: ").split(",")

def word_processor(user_input):
    fruits_str=user_input[0]
    fruits=list(fruits_str.split())
    flags=user_input[1:]
    kwargs ={}
    for flag in flags:
        key,value = flag.strip().split("=")
        kwargs[key] = value == "True"
    def decorator(func):
        def wrapper():
            result = fruits
            if kwargs.get("upper"):
                result = list(map(lambda x: x.upper(), result))
            if kwargs.get("unique"):
                result=list(set(result))
            if kwargs.get("reverse"):
                result=result[::-1]
            func(result)
        return wrapper
    return decorator

@word_processor(user_input)
def l(result):
    print(result)

l()