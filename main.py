
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

join_names = name1.lower() + name2.lower()
count_t = join_names.count("t")
count_r = join_names.count("r")
count_u = join_names.count("u")
count_e = join_names.count("e")
sum_of_true = count_e + count_r + count_t + count_u

love_l = join_names.count("l")
love_o = join_names.count("o")
love_v = join_names.count("v")
love_e = join_names.count("e")
sum_of_love = love_e + love_l + love_v + love_o

love_score = str(sum_of_true) + str(sum_of_love)
change_to_int = int(love_score)
if change_to_int < 10 or change_to_int > 90:
  print(f"Your score is {change_to_int}, you go together like coke and mentos.")
elif change_to_int > 40 and change_to_int < 50:
  print(f"Your score is {change_to_int}, you are alright together.")
else:
  print(f"Your score is {change_to_int}")
