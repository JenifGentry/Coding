def merge(alist):
    if len(alist)>1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        merge(left )
        merge(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if int(left[i]) < int(right[j]):
                alist[k]=left[i]
                i=i+1
            else:
                alist[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1
List = []
n = int(input('Enter Number of Elements in the list: '))
for i in range(0, n):
    x = int(input('Enter the Element %d :' %(i+1)))
    List.append(x)
print('Before sorting :', List)
merge(List)
print('After sorting:', List) 



