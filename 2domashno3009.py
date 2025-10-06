grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good = []
pass_list = []
fail = []

for grade in grades:
    if grade >= 90:
        excellent.append(grade)
    elif 70 <= grade <= 89:
        good.append(grade)
    elif 50 <= grade <= 69:
        pass_list.append(grade)
    else:
        fail.append(grade)

print("Excellent:", excellent)
print("Good:", good)
print("Pass:", pass_list)
print("Fail:", fail)
