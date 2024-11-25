tambah = lambda a, b : a + b

kurang = lambda a, b : a - b

def operasi(func,a,b):
    return func(a,b)

print(operasi(kurang,5,10))