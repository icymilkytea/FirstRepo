#Генерим список из четных
def even_numbers(i):
    for j in range(0, i + 1):
        if j % 2 == 0:
            yield j

even = even_numbers(6)
for i in even:
    print(i)

#Отсчет от обратного
def countdown(n):
    for j in range(n, -1, -1):
        yield j

even = countdown(6)

for i in even:
    print(i)

#Напиши генераторную функцию even_squares(n),
# которая генерирует квадраты только чётных чисел от 1 до n включительно.

def even_squares(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            i = i **2
            yield(i)

ev_sq = even_squares(6)

for i in ev_sq:
    print(i)

#Напиши генераторную функцию even_squares(n),
# которая генерирует квадраты только чётных чисел от 1 до n включительно.

def vowel_filter(n):
    vowels="аеёиоуыэюяaeiou"
    for i in n:
        if i.lower() in vowels:
            yield i

vowels = vowel_filter("ПрИвЕт, Hello!")

for i in vowels:
    print (i)