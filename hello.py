marks = [23,34,76,89]
mixed = [3.14, "Hello", False,43]
marks.append(63)
mixed.append(54)
marks.extend(mixed)
print(marks)
print(mixed)
print(marks[3])