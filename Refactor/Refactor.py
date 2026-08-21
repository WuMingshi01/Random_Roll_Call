
from random import choice
import json
import os    #和sys一起，获取文件位置，变相获取random_person.py所在目录
import sys   
import tkinter as tk    #引入tkinter模块，目的是为了使用文件对话框选择文件
from tkinter import filedialog


# 获取程序所在目录（兼容 .py 和 .exe）
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)  # exe 所在目录
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # .py 所在目录

#list_path = os.path.join(base_dir, 'person_list.txt')  #拼接目录，确保指向同目录下的person_list.txt 
json_path = os.path.join(base_dir, 'person_list.json')  #拼接目录，确保指向同目录下的person_list.json


class Random_person:
    def __init__(self,person_list: list):
        self.persons=person_list


    def random(self):
        return choice(self.persons)





if os.path.exists(json_path)== False:   #如果json文件不存在，则创建json文件，并让用户选择人名列表文件
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口


    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    with open(json_path,'w',encoding='utf-8') as j:
        json.dump({},j,ensure_ascii=False,indent=4)   #如果json文件不存在，则创建空json文件
    with open(json_path,'r',encoding='utf-8') as j:
        lastdir = json.load(j).get("lastdir", "C:/")             # 获取上次选择的目录，默认为 C:/
        persons_file_path = filedialog.askopenfilename(title="选择人名列表文件",initialdir=lastdir,filetypes=[("文本文件(Text Files)", "*.txt")])

    

else :
    with open(json_path,'r',encoding='utf-8') as j:
        person=json.load(j)   #读取json文件，生成人名表
# with open(list_path,'r',encoding='utf-8') as p:
#     person=[line.strip() for line in p if line.strip()]    #按照每行为一个人名，生成人名表

# with open(json_path,'w',encoding='utf-8') as j:
#     json.dump(person,j,ensure_ascii=False,indent=4)   #将人名表写入json文件，方便后续使用



a=Random_person(person)

print(a.random())

