def average(Marks):
    assert len(Marks) != 0, "List is empty."
    return sum(Marks)/len(Marks)

Marks = [2,4,7,9,3,5,8]
print("average marks of a student", average(Marks))

Marks = []
print("average marks of a student", average(Marks))


def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
