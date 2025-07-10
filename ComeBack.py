#student grade checker
# use tuple to store Name and Roll NO.
# use list to store multiple student detail
# use three subject and accept the grade
# print all the student with their grade
#     Note: >=80%=1st divistion
#     >=60%&<80%=2nd division

def grade_check():
    ## Firstly take the input as name from user.
    name = input('Please Enter your Name: ')
    rollNumber = input('Please Enter your Roll Number: ')

    student_detail = (name, rollNumber)
    subjects = ['Math', 'Science', 'English', 'Nepali', 'Social']

    d = {}
    for subject in subjects:
        marks = int(input(f'Enter Your Marks in {subject} :'))
        d[subject] = marks
    
    value = sum(d.values())
    totalpercentage = value / len(subjects)

    print(f'This is the total percentage : {totalpercentage}')

    print(f'This is the value of dictionary {d}')

    if totalpercentage > 80:
        print('1st Division')
    else:

        
        print('2nd Division')
    

grade_check()