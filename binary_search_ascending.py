start = 1
end = 101
srch  = 100
mylis = list(range(start,end))
pos = -1
# print(mylis)
def search(array,num):
    l = 0
    u  =len(array)-1
    
    global pos
    while l<=u:
        mid = (l+u)//2
        # print(mid)
        if array[mid]==num:
            pos = mid
            return True
        else:
            if array[mid]<num:
                l = mid+1
            else:
                u = mid-1
    return False

if search(mylis,srch):
    print("Found at position :{}".format(pos+1))
else:
    print("Not found !")
