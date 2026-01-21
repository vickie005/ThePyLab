score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
# if 90 <= score <= 100:  # Alternative syntax
# if score >= 90:  # Since score cannot be more than 100
    print("Grade: A")

elif score >= 80 and score < 90:
# elif 80 <= score < 90:  
# elif score >= 80:  # Since score is less than 90 here
    print("Grade: B")

elif score >= 70 and score < 80:
    print("Grade: C")

elif score >= 60 and score < 70:
    print("Grade: D")

else:
    print("Grade: F")
    