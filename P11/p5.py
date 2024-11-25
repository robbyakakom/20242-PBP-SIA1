def tambah(a, b):
    j = a + b
    return( tambah(j,b) if j < 100 else j)
    if j < 100 :
        return(tambah(j,b))
    else:
        return j

print(tambah(0,3))
