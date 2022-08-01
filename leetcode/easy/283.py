# my solution
arr=[0,1,0,3,12]

for i,a in enumerate(arr):
    if arr[i]==0:
        arr.remove(arr[i])
        arr.append(0)
print(arr)        
