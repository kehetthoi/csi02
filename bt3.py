machang=[
    {
        "ID" : 111,
        "name": "Bu cao sao",
        "price": 300000,
    },

    {
        "ID" : 112,
        "name": "bup be ma am",
        "price": 120000,
    },

    {
        "ID" : 113,
        "name": "socola",
        "price": 50000,
    },

    {
        "ID" : 114,
        "name": "vot cl",
        "price": 1120000,
    }
]
p=int(input("nhap gia tien:"))
def timdo(item,price):
    mondo=[md for md in item if md["price"]==price ]
    if mondo:
        return mondo
    else:
        print("ko tim thay")
print(timdo(machang,p))