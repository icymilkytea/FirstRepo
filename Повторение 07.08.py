data = ["5 12 3", "7 8 9", "15 2 1", "4 3 2"]

for d in data:
    sdata = [int(i) for i in d.split(" ")]
    filtered = filter(lambda x:  int(x)>10,sdata)
    print(list(filtered))

