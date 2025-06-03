
import random

provinces_of_china = [
    "北京市", "天津市", "河北省", "山西省", "内蒙古自治区",
    "辽宁省", "吉林省", "黑龙江省",
    "上海市", "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省",
    "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省",
    "重庆市", "四川省", "贵州省", "云南省", "西藏自治区",
    "陕西省", "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区",
    "香港特别行政区", "澳门特别行政区", "台湾省"
]

# for province in provinces_of_china:
#     print(province)

# print(provinces_of_china[0])
# print(provinces_of_china[-3])

# provinces_of_china[0] = "北京儿市"
# print(provinces_of_china[0])

fruits = [
    "苹果", "香蕉", "橙子", "梨", "西瓜",
    "葡萄", "草莓", "桃子", "芒果", "菠萝",
    "荔枝", "龙眼", "猕猴桃", "柚子", "哈密瓜",
    "樱桃", "蓝莓", "石榴", "李子", "杨梅"
]

fruits.append("桑葚")
# print(fruits)

fruits.extend(["枇杷", "桑葚", "山楂", "无花果", "百香果",
            "木瓜", "椰子", "榴莲", "山竹", "红毛丹"])
# print(fruits)

names = [
    # 男性常见名
    "张伟", "王强", "李勇", "刘洋", "陈明", 
    "赵刚", "杨军", "周杰", "吴磊", "徐浩",
    
    # 女性常见名
    "李娜", "王芳", "张敏", "刘静", "陈丽",
    "杨雪", "周婷", "吴秀英", "徐燕", "孙小红"
]

# Option 1
print(names[random.randint(0,19)])

# Option 2
print(random.choice(names))

vegetables = [
    "土豆", "西红柿", "黄瓜", "胡萝卜", "白菜",
    "茄子", "青椒", "菠菜", "芹菜", "洋葱"
]

fruits = [
    "苹果", "香蕉", "橙子", "梨", "西瓜",
    "葡萄", "草莓", "桃子", "芒果", "菠萝"
]

dirty_dozen = [vegetables, fruits]
print(dirty_dozen)

