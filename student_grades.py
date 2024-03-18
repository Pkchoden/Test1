num_students= int(input('Enter number of students:'))

i=1 # i- current student
while i<= num_students:
    total_grade = 0
    num_subject = int(input(f'Enter number of subject:'))
    for j in range (1, num_subject+1):# +1 is to include the last number too and j is current subject
        grade = float(input(f'Enter subject {j} grade for student {i}:'))
        total_grade += grade
    avg_grade = total_grade / num_subject
    print(f"avg grade for student {i}: {avg_grade:.2f}") # .2f is to convert the given value in two decimal points
    i += 1