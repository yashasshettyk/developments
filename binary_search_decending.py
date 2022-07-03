data = list(range(100,0,-1))
sear = 1
pos = -1

def search(array,num):
    l = 0
    u = len(array)-1
    while l<=u:
        mid = (l+u)//2
        if array[mid]==num:
            globals()['pos'] = mid
            return True
        else:
            if array[mid]<num:
                u = mid-1
            else:
                l = mid+1
    return False



if search(data,sear):
    print("Found at position {}".format(pos+1))
else:
    print("not found !")
