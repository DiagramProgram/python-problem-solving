n = int(input())

student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
#print(student_marks)
query_name = input()

tot = 0
for each in student_marks.get(query_name):
    tot += each
avg = tot/len(student_marks.get(query_name))

print("{:.2f}".format(avg)) #best way to round to whatever decimal places you need (in this case, 2)
