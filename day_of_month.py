# developed by yashas shetty #
days = [
        ["Sunday",None,1],
        ["Monday",None,2],
        ["Tuesday",None,3],
        ["Wednesday",None,4],
        ["Thursady",None,5],
        ["Friday",None,6],
        ["Saturday",None,7]
        ]
refactored = []
total_days = int(input("Enter the total number days in month :"))
first_day = None
print("Enter the respective number to select the first day of the month and day to be searched for : ")
for i in range(len(days)):
    print(f"Enter {days[i][2]} for {days[i][0]}  ")
first_day = int(input("Enter first day : "))
search_day = int(input("Enter the day to be searched : "))

store1 = first_day
store2 = search_day
for i in range(len(days)):
    if days[i][2] == first_day:
        first_day = days[i][0]
    if days[i][2] == search_day:
        search_day = days[i][0]
        
        
print(f"First day of the month is : {first_day}")
print(f"day to be searched is: {search_day}")

refactored += days[store1-1 : ]
refactored += days[0:store1-1]
track = 0
for i in range(len(days)):
    refactored[i][1] = track
    # refactored[i].pop()
    track+=1
print(refactored)
for day in range(len(refactored)):
    if refactored[day][0] == search_day:
        search_day = day
        
    
print(search_day)

if total_days <=28:
    for i in range(len(refactored)):
        refactored [i][2] = 4
print(refactored)
store = 0
mem = 0
if total_days>28:
    for i in range(len(refactored)):
        refactored[i][2] = 4
    print(refactored)

    if search_day+28 <= total_days:
        for i in range(len(refactored)):
            if refactored[i][1] == search_day:
                refactored[i][2]+=1
                mem = i
                
print(f"total number of days that {refactored[mem][0]} in a month is{refactored[mem][2]} ")
    


   
        
    
    
    