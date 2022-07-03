start,end,srch = [int(input("Enter the value for start & end range and search value [press enter after each input]: ")) for x in range(3) ]
mylis = list(range(start,end))
pos = -1
# print(mylis)
def search(array,num):
    l = 0
    u  =len(array)
    
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
    print("Found at position :{}".format(pos))
else:
    print("Not found !")
