from statistics import median

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Prinseton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40500],
    ["Yale", 11701, 40500]
]

def enrollment_stats():
    total_students = 0
    total_fees = 0
    for row in universities:
        total_students = total_students + row[1]
        total_fees = total_fees + row[2]
    return total_students, total_fees

def find_mean():
    student_mean = round(enrollment_stats()[0] / len(universities), 2)
    fee_mean = round(enrollment_stats()[1] / len(universities),2)
    return student_mean, fee_mean

def find_median():
    student_list = []
    fee_list = []
    for row in universities:
        student_list.append(row[1])
        fee_list.append(row[2])
    student_median = median(student_list)
    fee_median = median(fee_list)
    return student_median, fee_median

print(
    f"""*********************************************
    Total students: {enrollment_stats()[0]}
    Total tuition: ${enrollment_stats()[1]}
    
    
    Student mean: {find_mean()[0]}
    Student median: {find_median()[0]}
    
    
    Tuition mean: ${find_mean()[1]}"
    Tuition median: ${find_median()[1]}"
    *********************************************"""
)
