def select_sort(a):
    for j in range(0, len(a)):
        max=a[j]
        for i in range(j+1,len(a)):
            if(max > a[i]):
                a[j]= max
            else:
              temp = a[j]
              a[j]= a[i]
              a[i]=temp
              max=a[j]
        
    return a

b=[4, 3, 4 ,2, 7]
print(select_sort(b))

