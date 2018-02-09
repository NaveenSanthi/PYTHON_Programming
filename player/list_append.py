list=[1,2,4,5,7]
list2=[x+20 for x in list]
print (list2)

list3=[i*2 for i in range(0,29)]
print(list3)

list4=[x for x in list if x%2==0]
print (list4)

def fun(x):
    return x+30
print(fun(8))
