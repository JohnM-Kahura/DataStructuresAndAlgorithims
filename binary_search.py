arr=[1,2,3,4,5,6,7,8,9]
start=0
end=len(arr)-1
target=9

def binarySearch(arr,start,end,target):
    # write an exit statement here
    midIndex=start+end /2
    if target==arr[midIndex]: return True
    if arr[midIndex]>target: return binarySearch(arr,start,midIndex-1,target)
    else :return binarySearch(arr,midIndex+1,end,target)

print(binarySearch(arr,start,end,target))