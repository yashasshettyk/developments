# *********************************************************************************#
#**************************developed by yashas shetty******************************#
# *********************************************************************************#
print("TO CALCULATE <SGPA>")
grade = []
curr_sem = []
marks = []
credit_points = []
total_credit = 0
actual_credit = 0
backlog = 0
back_sem = 0
current_sem = int(input("enter the semester no. to be calculated (in digits) : "))
bl  = str(input("type yes if you have backlog :" ).lower())
p_cycle1 = [
         ["18MAT11",4],
         ["18PHY12",4],
         ["18ELE13",3],
         ["18CIV14",3],
         ["18EGDL15",3],
         ["18PHYL16",1],
         ["18ELEL17",1],
         ["18EGH18",1]
         ]
p_cycle2 = [
         ["18MAT21",4],
         ["18PHY22",4],
         ["18ELE23",3],
         ["18CIV24",3],
         ["18EGDL25",3],
         ["18PHYL26",1],
         ["18ELEL27",1],
         ["18EGH28",1]
         ]

c_cycle1 = [
         ["18MAT11",4],
         ["18CHE12",4],
         ["18CPS13",3],
         ["18ELN14",3],
         ["18MEL15",3],
         ["18CHEL16",1],
         ["18CPL17",1],
         ["18EGH18",1]
         ]
c_cycle2 = [
         ["18MAT21",4],
         ["18CHE22",4],
         ["18CPS23",3],
         ["18ELN24",3],
         ["18ME25",3],
         ["18CHEL26",1],
         ["18CPL27",1],
         ["18EGH28",1]
         ]

sem_3 = [
         ["18MAT31",3],
         ["18EC32",4],
         ["18EC33",3],
         ["18EC34",3],
         ["18EC35",3],
         ["18EC36",3],
         ["18ECL37",2],
         ["18ECL38",2],
         ["18-KVK-KAK/CPC -39/49",1]
         ]
sem_4 = [
         ["18MAT41",3],
         ["18EC42",4],
         ["18EC43",3],
         ["18EC44",3],
         ["18EC45",3],
         ["18EC46",3],
         ["18ECL47",2],
         ["18ECL48",2],
         ["18-KVK-KAK/CPC -39/49",1]
         ]
sem_5 = [
         ["18ES51",3],
         ["18EC52",4],
         ["18EC53",4],
         ["18EC54",3],
         ["18EC55",3],
         ["18EC56",3],
         ["18ECL57",2],
         ["18ECL58",2],
         ["18CIV59",1]
         ]

sem_6 = [
         ["18EC61",4],
         ["18EC62",4],
         ["18EC63",4],
         ["18XX64X",3],
         ["18XX65X",3],
         ["18ECL66",2],
         ["18ECL67",2],
         ["18ECMP68",2]
         ]
sem_1 = None
sem_2 = None
if current_sem == 1 or current_sem == 2:
    x = input("Enter the cycle < c or p > : ").lower()
    if current_sem == 1 and x=="c":
        sem_1 = c_cycle1
    else:
        sem_1 = p_cycle1
    if current_sem ==2 and x=="p":
        sem_2 = p_cycle2
    else:
        sem_2 = c_cycle2
sem = [0,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6]
def get_grade(n):
    if(n>=90):
        return 10
    elif(n<90 and n>=80):
        return 9
    elif(n<80 and n>=70):
        return 8
    elif(n<70 and n>=60):
        return 7
    elif(n<60 and n>=45):
        return 6
    elif(n<45 and n>=40):
        return 4
    else:
        return 0
if True:
    for i in range(len(sem[current_sem])):
        marks.append(int(input(f"Enter the marks for subject {sem[current_sem][i][0]} :")))
    # print(marks)   
    for j in marks:
        grade.append(get_grade(j))
    # print(grade)
    for k,l in enumerate(grade):
        if l!=0:
            actual_credit += sem[current_sem][k][1]  
        credit_points.append(l*sem[current_sem][k][1])
        total_credit += credit_points[k]
back_marks = []
back_grade = []
actual_back_credit = 0
back_credit_point = []
total_back_credit = 0
if bl=="yes":
    backlog = int(input("Enter the total number of backlog count : "))
    back_sem = int(input("Enter the sem of backlog : "))
    for i in range(len(sem[back_sem])):
        back_marks.append(int(input(f"fill only subject with backlog rest as 0 {sem[back_sem][i][0]} :")))
    print(back_marks)   
    for j in back_marks:
        back_grade.append(get_grade(j))
    # print(back_grade)
    for k,l in enumerate(back_grade):
        if l!=0:
            actual_back_credit += sem[back_sem][k][1]   
        back_credit_point.append(l*sem[back_sem][k][1])
        total_back_credit += back_credit_point[k]   
    # print(actual_back_credit)    
    # print(total_back_credit)
sgpa_marks = []
total_cgpa = 0
cgpa = input("do you wanna calculate CGPA [yes or no] : ")
if cgpa =="yes":
    data = int(input("Enter the no of sem's : "))
    for i in range(data):
        sgpa_marks.append(round(float(input("Enter the SGPA : ")), 2))
    for i in sgpa_marks:
        total_cgpa += i    
    print("Your total SGPA is :" , round((total_credit+total_back_credit)/(actual_back_credit + actual_credit) , 2))
    print("total CGPA is : ", round((total_cgpa/data),2)) 
else:
    print("Your total SGPA is :" , round((total_credit+total_back_credit)/(actual_back_credit + actual_credit) , 2))
    
    
    


    
         
    
    
    
