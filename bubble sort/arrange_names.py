# Write a Program to accept five names from user and arrange them using bubble sort 

def arrange_names(user_inp):
    lst= []
    for i in range(user_inp):
        name= input(f' name {i+1} ?')
        lst.append(name)
    
    for i in range(len(lst),0,-1):
        for j in range(1,i):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]

    return lst

user_inp= int(input('How many names?'))
print(arrange_names(user_inp))