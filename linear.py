pos=-1

def linear(list,n):

    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    
    return False


list=[1,2,3,4,5,6,7]
n= 7

if linear(list,n):
    print("search found", pos+1)
else:
    print("not found")

