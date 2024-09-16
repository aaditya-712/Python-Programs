eng = int(input("Enter marks in english: "))
mar = int(input("Enter marks in Marathi: "))
hindi = int(input("Enter marks in Hindi: "))
maths = int(input("Enter marks in Maths: "))
sci = int(input("Enter marks in Science: "))

totalMarks = eng + mar + hindi + maths + sci
percent = (100 * totalMarks) / 500
print(f"Marks Obtained: {totalMarks} out of 500")
print(f"Percent: {percent}")

if percent > 90:
    print("Grade: O")

elif percent > 80 and percent < 90:
    print("Grade: A")

elif percent > 70 and percent < 80:
    print("Grade: B")

else :
    print("Grade: Fail")
