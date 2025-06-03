import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("石头剪刀布，你出哪个？输入0是石头，输入1是布，输入2是剪刀："))
computer_choice = random.randint(0,2)
print(f"电脑的选择：{computer_choice}")

# if user_choice == 0:
#     print(rock)
#     if computer_choice == 0:
#         print("电脑的选择：\n")
#         print(rock)
#         print("平局！")
#     elif computer_choice == 1:
#         print("电脑的选择：\n")
#         print(paper)
#         print("你输了！")
#     elif computer_choice == 2:
#         print("电脑的选择：\n")
#         print(scissors)
#         print("你赢了！")
# elif user_choice == 1:
#     print(paper)
#     if computer_choice == 0:
#         print("电脑的选择：\n")
#         print(rock)
#         print("你赢了！")
#     elif computer_choice == 1:
#         print("电脑的选择：\n")
#         print(paper)
#         print("平局！")
#     elif computer_choice == 2:
#         print("电脑的选择：\n")
#         print(scissors)
#         print("你输了")
# else:
#     print(scissors)
#     if computer_choice == 0:
#         print("电脑的选择：\n")
#         print(rock)
#         print("你输了！")
#     elif computer_choice == 1:
#         print("电脑的选择：\n")
#         print(paper)
#         print("你赢了！")
#     elif computer_choice == 2:
#         print("电脑的选择：\n")
#         print(scissors)
#         print("平局")


if user_choice >= 3 or user_choice < 0 :
    print("无效，你输了。")
elif user_choice == 0 & computer_choice == 2:
    print("你赢了！")
elif computer_choice == 0 & user_choice == 2:
    print("你输了！")
elif computer_choice > user_choice:
    print("你输了！")
elif user_choice > computer_choice:
    print("你赢了")
elif computer_choice == user_choice:
    print("平局")
