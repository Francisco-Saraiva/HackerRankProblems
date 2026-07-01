# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split(' '))

all_marks = []
for _ in range(X):
    marks = list(map(float, input().split(' ')))
    all_marks.append(marks)

student_marks = list(zip(*all_marks))

for student in student_marks:
    print(round(sum(student) / len(student), 1))