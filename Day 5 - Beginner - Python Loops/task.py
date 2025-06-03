fruits = [
    "苹果", "香蕉", "橙子", "梨", "西瓜",
    "葡萄", "草莓", "桃子", "芒果", "菠萝"
]

# for fruit in fruits:
#     print(fruit)

students_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
total_exam_score = sum(students_scores)
print(total_exam_score)

highest_score = 0
for score in students_scores:
    # sum += score
    if score > highest_score:
        highest_score = score
print(highest_score)

for number in range(1,10): # 从1到10，但不包括10
    print(number)

for number in range(1,11,3):
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)
