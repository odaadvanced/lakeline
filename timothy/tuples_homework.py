universities = [
    ['California Institue of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachussets Institue of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

def enrollment_stats(uni_list):
    
    student_total = []
    tuition_total = []
    for school in uni_list:
        student_total.append(school[1])
        tuition_total.append(school[2])
    return student_total, tuition_total

def mean(uni_list):
    return sum(uni_list) / len(uni_list)

def median(uni_list):
    uni_list.sort()
    median_value = int(len(uni_list) / 2)
    return uni_list[median_value]

total = enrollment_stats(universities)

print(f"Total students: {sum(total[0])} \nTotal Tuition: {sum(total[1])} \nStudent Mean: {mean(total[0]):.1f}\nStudent Median: {median(total[0])}\nTuition Mean: {mean(total[1]):.1f}\nTuition Median: {median(total[1])}")