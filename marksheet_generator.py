hindi_marks = int(input("enter hindi marks"))
english_marks = int(input("enter english marks"))
maths_marks = int(input("enter maths marks"))
science_marks = int(input("enter science marks"))
social_marks = int(input("enter social marks"))


total_marks = hindi_marks+english_marks+maths_marks+science_marks+social_marks

print(total_marks)


percentage = total_marks / 5
print(percentage)

if percentage>=90 and percentage <= 100:
    print("grade A+")
elif percentage>=80:
    print("grade A")
elif percentage>70:
    print("grade B")

else:
    print("fail")
