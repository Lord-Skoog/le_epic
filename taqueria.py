fode={
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total=[]
item = '_'
try:
    while len(item)>0:
        item = input("Item: ")
        item = item.lower()
        if item in fode:
            e = fode
            e[item]
            if item in e:
                total.append(e[item])
except EOFError:
    weezer = 0
    i = 0
    while i < len(total):
        total[i] = float(total[i])
        weezer = weezer+total[i]
        i +=1
    weezer = round(weezer, 2)
    weezer = float(weezer)
    print(f"${weezer:,.2f}")
