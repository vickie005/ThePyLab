# Quiz Game
score = 0

print("Q1: Is Antartica a cold place or hot? : ")
ans1 = input().strip().lower()
if ans1 == 'cold':
  score += 1
else:
  print("Incorrect!")
  
print("Q2: What is the capital of Kenya? : ")
ans2 = input().strip().lower()
if ans2 == 'nairobi':
  score += 1
else:
  print("Incorrect!")

print("Q3: Who is the king of the jungle? : ")
ans3 = input().strip().lower()
if ans3 == 'lion':
  score += 1
else:
  print("Incorrect!")
  
print("Q4: Which is faster, a sneeze or a blink? : ")
ans4 = input().strip().lower()
if ans4 == 'sneeze':
  score += 1
else:
  print("Incorrect!")
  
print("Q5: Which is the shortest complete sentence in English? : ")
ans5 = input().strip().lower()
if ans5 == 'i am':
  score += 1
else:
  print("Incorrect!")
  
print("Q6: The kiswahili word for spinach is? : ")
ans6 = input().strip().lower()
if ans6 == 'mchicha':
  score += 1
else:
  print("Incorrect!")
  
print("Q7: How many legs does a lobster have? : ")
ans7 = input().strip().lower()
if ans7 == '10':
  score += 1
else:
  print("Incorrect!")
  
print("Q8: Adults have less bones than children. True or False? : ")
ans8 = input().strip().lower()
if ans8 == 'true':
  score += 1
else:
  print("Incorrect!")  
  
print(f"Your total score is {score}/8")