#doubles = [x * 2 for x in range(1, 16)]
#triples = [y * 3 for y in range(1, 16)]
#squares = [z * z for z in range(1, 16)]

#fruits = ["mango", "dragonfruit", "grape", "plum"]
#uppercase_words = [fruit.upper() for fruit in fruits]
#fruit_chars = [fruit[0] for fruit in fruits]

#numbers = [4, -5, 8, -1, 0, -4, 6]
#positive_numbers = [x for x in numbers if x >= 0]
#negative_numbers = [x for x in numbers if x < 0]
#even_numbers = [x for x in numbers if x % 2 == 0]
#odd_numbers = [x for x in numbers if x % 2 == 1]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 40]

print(passing_grades)