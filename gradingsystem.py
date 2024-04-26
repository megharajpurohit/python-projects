more_entries = True

while more_entries:
    while True:
        student_name = input('Enter Name Of Student: ')
        if student_name.isnumeric():
            print('Please enter only alphabetic characters.')
        else:
            break

    while True:
        try:
            num_subjects = int(input('Enter number of subjects student has: '))
            if num_subjects < 1:
                raise ValueError('Please enter a valid value.')
            elif num_subjects > 15:
                raise ValueError('Too many subjects. Please enter subjects ranging from 1 to 15 only.')
            else:
                break
        except ValueError as e:
            print(e)

    marks_list = []
    for i in range(num_subjects):
        while True:
            try:
                print("Enter marks of subject ", i+1, ': ', end=' ')
                marks = float(input())
                if marks < 1 or marks > 100:
                    raise ValueError('Please enter marks from 1 to 100 only.')
                else:
                    marks_list.append(marks)
                    break
            except ValueError as e:
                print(e)

    total_marks = sum(marks_list)
    average = total_marks / num_subjects

    print('')
    print('------------------------------')
    print('Student Name:', student_name)
    print('Student Average Score:', average)
    print('Student Subjects Wise Score:')
    for i, marks in enumerate(marks_list):
        print('Score in Subject', i + 1, 'is =', marks)

    if average < 40:
        print('Student Result: Fail')
    elif 40 <= average <= 50:
        print('Student Grade: C')
    elif 51 <= average <= 60:
        print('Student Grade: B')
    elif 61 <= average <= 70:
        print('Student Grade: B+')
    elif 71 <= average <= 80:
        print('Student Grade: A')
    elif 81 <= average <= 90:
        print('Student Grade: A+')
    elif 91 <= average <= 100:
        print('Student Grade: O')

    while True:
        try:
            more_entries_input = int(input('For more entries press 1. To quit, press any other number: '))
            if more_entries_input != 1:
                more_entries = False
            break
        except ValueError as e:
            print('Please enter a valid input.')

print('Thank you for using the program.')