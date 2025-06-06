def enrollment_stats(list_of_universities):
    total_students = []
    total_tuition = []
    for university in list_of_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])
    return total_students, total_tuition
def mean(values):
    """Return the mean value in the list 'values'"""
    return sum(values) / len(values)
def median(values):
    """Return the median value of the list 'values'"""
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        
        left_center_index = (len(values) -1) // 2
        right_center_index = (len(values) +1) // 2
        return mean([values[left_center_index], values[right_center_values]])
universities = [
    ["California Institut of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]
totals = enrollment_stats(universities)
print("\n")
print("*****" * 6)
print(f"Total students: {sum(totals[0]):,}")
print(f"Total tuition: $ {sum(totals[1]):,}")
print(f"\nStudent mean: {mean(totals[0]):,.2f}")
print(f"Student median: {median(totals[0]):,}")
print(f"\nTuition mean: $ {mean(totals[1]):,.2f}")
print(f"Tuition median: {median(totals[1]):,}")
print("*****" * 6)
print("\n")