student_tuples = [
        ('john', 'A', 15, 1),
        ('jane', 'B', 12, 2),
        ('dave', 'B', 10, 2),
        ('david','C', 10, 10),
        ('kat','E', 10, 8),
        ('bob', 'F', 18, 7),
        ('alex', 'D', 10,6),
        ('www', 'E', 15, 2)
    ]
a = (sorted(student_tuples, key=lambda student: student[2], reverse=True))
print (a)

def fun(v):
    return (v[2],v[3])

b = (sorted(student_tuples, key=lambda student: student[2], reverse=True))
b.sort(key=fun)
print(b)