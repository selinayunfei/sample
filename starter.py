"""
Title: 
Name:
Date:

Brief description of your program

"""

# Write your functions here
def method1(grades):
    g_sum = 0
    for val in grades:
        g_sum += val
    g_sum /= len(grades)
    return round(g_sum,1)

#def method2
#if the number of grades 10 or more points below median is 2 or less, remove those and calculate average
#otherwise, regular average
def method2(grades):
    grades.sort()
    median = grades[len(grades)//2]

    new_grades = []
    awful_course = []

    for val in grades:
        if val < median:
            if median-val >= 10:
                awful_course.append(val)

    if  0 < len(awful_course) <= 2:
        for x in grades:
            if x not in awful_course:
                new_grades.append(x)
    else:
        for x in grades:
            new_grades.append(x)

    g_sum = 0
    for i in new_grades:
        g_sum += i
    g_sum /= len(new_grades)

    return round(g_sum,1)
    

#def method 3
#compare the two grades of classes that have a sequel
#drop the first grade if improvement is shown
def method3(all_grades):

    new_grades = []
    improv_grade = []
    for a in range(2,10):
        improv_grade.append(all_grades[a])

     #if improvement shown, will take improved grades. if not, will take the average of the two. 
    for x in range(0,len(improv_grade)-1,2):
        if improv_grade[x] < 0:
            new_grades.append(improv_grade[x+1])
        elif improv_grade[x] > improv_grade[x+1]:
            new_grades.append((improv_grade[x]+improv_grade[x+1])//2)
        elif improv_grade[x] < improv_grade[x+1]:
            new_grades.append(improv_grade[x+1])
        else:
            new_grades.append(improv_grade[x])

    # appending the rest of the grades
    for i in range(0,2):
        if all_grades[i] > 0:
            new_grades.append(all_grades[i])
    for j in range(10,12):
        if all_grades[j] > 0:
            new_grades.append(all_grades[j])
    g_sum = 0
    for val in new_grades:
        g_sum += val
    g_sum /= len(new_grades)
    return round(g_sum,1)

#method4
#both method 2 and method 3 will be considered
#courses will be weighted; important classes considered more
def method4(all_grades, grades):
    average_m2 = method2(grades)
    average_m3 = method3(all_grades)

    weighted_grades = []
    wg_sum = 0
    for a in range(0,6):
        if all_grades[a] > 0:
            weighted_grades.append(all_grades[a])
    for val in weighted_grades:
        wg_sum += val
    w_average = round(wg_sum/len(weighted_grades),1)

    g_sum = 0
    for val in grades:
        g_sum += val
    average = round(g_sum/len(grades),1)

    if w_average-average >= 5:
        average_m4 = round((w_average+average)/2,1)
    else:
        average_m4 = average

    
    return round((average_m2+average_m3+average_m4)/3,1)

'''
all_grades = [-1, 88, 50, 90, 83, 87, 92, 78, 89, 91, 84, 84]
grades = [88,50, 90, 83, 87, 92, 78, 89, 91, 84, 84]
print(method4(all_grades,grades))
print(method3(all_grades))
print(method2(grades))
print(method1(grades))
'''


# Main body of your program


# opens the file grades.csv and stores it into variable grades_file 
grades_file = open("grades.csv", 'r')# r for read
studentID = 0

    #print(x)

accept = []
marks_method4 = []
marks_method3 = []
marks_method2 = []

for row in grades_file: 
    studentID += 1
    string_grades = row.strip().split(",")

    grades = [] # all grades provided by student
    all_grades = [] # all grades and classes, regardless of whether or not the student had taken them; this is used in method 3
    for s in string_grades:
        if len(s) > 0:
            all_grades.append(int(s))
            if int(s) > 0:
                grades.append(int(s))
    marks_method4.append(method4(all_grades,grades))
    marks_method3.append(method3(all_grades))
    marks_method2.append(method2(grades))

def close_to_200(method):
    possibilities = {}
    closest = 100

    for x in range(95,80,-1):
        num = 0
        for mark in method:
            if mark > x: 
                num += 1
        if 100 <= num <= 300:
            possibilities.update({x:num})
    
    for key in possibilities:  
        y = abs(200-int(possibilities[key]))  
        if y < abs(200-closest):
                closest = possibilities[key]
    print(f"Grade:{key}")
    print(f"Number of students:{closest}")

print("Method 4")
close_to_200(marks_method4)
print("")
print("Method 3")
close_to_200(marks_method3)
print("")
print("Method 2")
close_to_200(marks_method2)


#print(accept)
#print(len(accept))

        
'''
# list of student IDs for each method
accept1 = []
accept2 = []
accept3 = []
accept4 = []

# student ID corresponds to the row in the csv file 
studentID = 0

# the file is read as a list of strings
# each row in the file is read as a single string 
for row in grades_file: 
    studentID += 1
    string_grades = row.strip().split(",") # splits the row into its cells 
    
    # converts the row of grades from string to integer values 
    grades = []
    for s in string_grades:
        if len(s) > 0:
            grades.append(int(s))    
    
    
    # appends the student ID of those who pass the threshold 
    if method1(grades) > 100: # change 100 to the appropriate threshold 
        accept1.append(studentID)
    if method2(grades) > 100: # change 100 to the appropriate threshold 
        accept2.append(studentID)
    if method3(grades) > 100: # change 100 to the appropriate threshold 
        accept3.append(studentID)
    if method4(grades) > 100: # change 100 to the appropriate threshold 
        accept4.append(studentID)

print(accept1)
print(accept2)
print(accept3)
print(accept4)
'''
# close the grades file 
grades_file.close()   
    
    
    