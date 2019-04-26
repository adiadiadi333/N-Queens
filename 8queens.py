def disconnected(l,t):
    for i,j in l:
        if i==t[0] or j==t[1] or abs(i-t[0])==abs(j-t[1]):
            return False
    return True

def find_new(l,n):
    r=len(l)+1
    for i in range(1,n+1):
        if disconnected(l,(r,i)):
            return (r,i)

def find_next(l,n):
    r=len(l)
    for i in range(1,n+1):
        if disconnected(l[:-1],(r,i)) and (r,i)>l[-1]:
            return (r,i)

def backtrack(l,n):
    if find_next(l,n):
        l[-1]=find_next(l,n)
    else:
        l.pop()
        backtrack(l,n)
        
def show(l,n):
    for i in range(n):
        for j in range(n):
            print(int(bool((i+1,j+1) in l)),end=" ")
        print()

if __name__=="__main__":
    l=[]
    s=[]
    n=int(input("enter n: "))
    while True:
        if find_new(l,n):
            l+=[find_new(l,n)]
        else:
            try:
                backtrack(l,n)
            except IndexError:
                break;
        if len(l)==n:
            #print(l)
            s.append(l.copy())
    i=1
    for soln in s:
        print("---------SOLN %d-----------"%i)
        i+=1
        show(soln,n)

