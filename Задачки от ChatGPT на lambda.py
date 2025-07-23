"""1. Чётные квадраты
Напиши программу, которая:
получает список чисел от пользователя,
с помощью lambda и filter выбирает чётные числа,
затем с помощью map и lambda возводит их в квадрат."""

def square2(user_list):
    sort_list = list(filter(lambda i: i %2 == 0, user_list))
    print(sort_list)
    squared_list = list(map(lambda i: i**2, sort_list))
    return(squared_list)

text = list(map(int, input("Введите числа через пробел: ").split()))
print(square2(text))

"""2. Сортировка по длине
Есть список строк. Отсортируй его:
сначала по длине строки (используй sorted(..., key=lambda ...)),
потом по алфавиту (в рамках одинаковой длины)."""

list1 = ["список", "слов", "разной", "длины", "на", "сортировку","а", "б"]
sort_by_len = list(sorted(list1, key=lambda i: (len(i), i)))
print(sort_by_len)

"""3. Сумма с map
Пользователь вводит строку с числами через пробел.
Используя map и lambda, преобразуй её в список чисел и выведи их сумму."""

user_str = input("Введите числа через пробел: ").split()
sum_of_user_input = sum(map(lambda i: int(i), user_str))
print(sum_of_user_input)

"""4. Фильтр по первой букве
Пользователь вводит список слов.
С помощью filter и lambda оставь только те, которые начинаются на букву "а"."""
user_str =  list(input("Введите слова через пробел: ").split())
sort_by_letter = filter(lambda i: i[0].lower() == 'a', user_str)
print(sort_by_letter)

"""5 Преобразование в верхний регистр
Пользователь вводит список слов через пробел.
Используя map и lambda, преобразуй каждое слово в верхний регистр и выведи полученный список."""
user_str =  list(input("Введите слова через пробел: ").split())
sort_by_letter = list(map(lambda i: i.upper(), user_str))
print(sort_by_letter)

"""6. Подсчет длин слов
Пользователь вводит список слов через пробел.
Используя map и lambda, создай список с длинами каждого слова и выведи его."""
user_str =  list(input("Введите слова через пробел: ").split())
sort_by_letter = list(map(lambda i: len(i), user_str))
print(sort_by_letter)

user_str = input("Введите числа через пробел: ").split()
int_list = list(map(lambda i: int(i), user_str))
int_positive = list(filter(lambda i: i>0, int_list))
print(f"Положительные числа: {int_positive}")
min_val, max_val, avg = min(int_positive), max(int_positive), sum(int_positive)/len(int_positive)
print(f"Минимальное: {min_val}")
print(f"Максимальное: {max_val}")
print(f"Среднее: {avg}")
print("Отрицательные значения: ", list(filter(lambda i: i<0, int_list)))