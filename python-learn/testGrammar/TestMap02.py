"""
遍历字典的方法：
    1：for key,value in Map.items():
    这样可以一次获取到key和value
    2：for key in Map.keys():
    这样可以获取key
    3：for value in Map.values():
    可以获取value
    遍历得到的结果是无序的，和存储的顺序没有关系
"""

favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

for key in favorite_languages.keys():
    print(key.title())