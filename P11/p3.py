
def tambah(a,b):
    return a + b

def kurang(a,b):
    return a-b

def operasi(func,a,b):
    return func(a,b)

print(operasi(kurang,5,10))