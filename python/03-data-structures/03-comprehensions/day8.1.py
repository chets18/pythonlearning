#list comprehension = A conside way to create lists in python compact and easier to read than tradional lpps
# [Expression for vlaue in iterable if condition]

grades = [85,42,79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >=60]

print(passing_grades)