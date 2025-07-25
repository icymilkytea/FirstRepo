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