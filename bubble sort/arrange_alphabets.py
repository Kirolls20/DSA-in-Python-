# Arrange Alphabets using bubble sort in Decreasing order

def arrange_alphabets(s:str):
    lst= list(s)
    for i in range(len(lst),0,-1):
        for j in range(1,i):
            if lst[j-1] < lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]
    return lst


s = 'dswerc'
print(arrange_alphabets(s))