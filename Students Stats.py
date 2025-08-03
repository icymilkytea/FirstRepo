data = {}
while True:
    user_input = input("Пользовательский ввод")
    if user_input.strip()=="":
        break
    name_part, scores_part = user_input.split(":")
    name = name_part.strip()
    scores = list(map(float, scores_part.strip().split(",")))

    data[name] = scores

for name, scores in data.items():
    avg_sc= round(sum(scores)/len(scores),2)
    print(f"{name}: средняя = {avg_sc} - Сдал") if avg_sc>=4 else print(f"{name}: средняя = {avg_sc} - Не сдал")