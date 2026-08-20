
from random import choice


import os
import sys

# 获取程序所在目录（兼容 .py 和 .exe）
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)  # exe 所在目录
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # .py 所在目录
list_path = os.path.join(base_dir, 'person_list.txt')  #拼接目录，确保指向同目录下的person_list.txt


class Random_person:
    def __init__(self,person_list: list):
        self.persons=person_list


    def random(self):
        return choice(self.persons)


with open(list_path,'r',encoding='utf-8') as p:
    person=[line.strip() for line in p if line.strip()]    #按照每行为一个数据，生成列表

#person=['a','B','1','@']


a=Random_person(person)

print(a.random())

