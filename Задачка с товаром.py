#tovar =input("Введите наименование товара и цену через пробел").split(",")
tovar="Хлеб 30, Молоко 70, Сыр 150, Вода 25".split(",")
tovar_d = {}
print("Каталог товаров: \n")
for pair in tovar:
    name, price = pair.split()
    tovar_d[name] = int(price)
    print(f"{name} - {int(price)}")

print("\nДорогие товары (больше 50 руб.):")
count=0
avg=0
for key, value in tovar_d.items():
    if value > 50:
     print(f"- {key.upper()}")
     avg = avg+int(value)
     count +=1

avg = avg/count
print(f"\nСредняя цена дорогих товаров: {avg} руб.")