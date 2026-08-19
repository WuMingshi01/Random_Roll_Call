import tkinter
from random import randint as rint,choice as rcho,seed as rseed,shuffle
from time import time



#鼠标样式(非必要可省)
cursorList = ['arrow', 'xterm', 'watch', 'hand2', 'question_arrow', 'sb_h_double_arrow', 'sb_v_double_arrow', 'fleur',
              'crosshair', 'based_arrow_down', 'based_arrow_up', 'boat', 'bogosity', 'top_left_corner',
              'top_right_corner', 'bottom_left_corner', 'bottom_right_corner', 'top_side', 'bottom_side', 'top_tee',
              'bottom_tee', 'box_spiral', 'center_ptr', 'circle', 'clock', 'coffee_mug', 'cross', 'cross_reverse',
              'diamond_cross', 'dot', 'dotbox', 'double_arrow', 'top_left_arrow', 'draft_small', 'draft_large',
              'left_ptr', 'right_ptr', 'draped_box', 'exchange', 'gobbler', 'gumby', 'hand1', 'heart', 'icon',
              'iron_cross', 'left_side', 'right_side', 'left_tee', 'right_tee', 'leftbutton', 'middlebutton',
              'rightbutton', 'll_angle', 'lr_angle', 'man', 'mouse', 'pencil', 'pirate', 'plus', 'rtl_logo', 'sailboat',
              'sb_left_arrow', 'sb_right_arrow', 'sb_up_arrow', 'sb_down_arrow', 'shuttle', 'sizing', 'spider',
              'spraycan', 'star', 'target', 'tcross', 'trek', 'ul_angle', 'umbrella', 'ur_angle', 'X_cursor']
a=rcho(cursorList)

#人名单
#'孙学一',
#'王梓涵',
person=[
'刘恩溪',
'王金萱',
'张雨晨',
'程绘然',
'许芫苇',
'刘欣怡',
'姚弦月',
'张欣茹',
'吴昊宇',
'韩永乐',
'陈秀文',
'孙煜婷',
'王溪媛',
'李雨恒',
'马茗涵',
'张爱鑫',
'孙世博',
'秦梦佳',
'韩雨辰',
'张爱雨',
'孙雪晴',
'林紫旭',
'张洪帅',
'徐子瑄',
'金桐旭',
'王湘旭',
'任雨泽',
'杨雨贺',
'郭梦蕾',
'张延庆',
'张盛源',
'王馨晨',
'韩伟佳',
'欧建博',
'陈盈名',
'赵和娴',
'周志轩',
'王虹颖',
'何中远',
'高嘉骏',
'申宸羽',
'于俊轩',
'沈馨钰',
'李美琳',
'温雨涵',
'白璐豪',
'董文柏',
'尹如意',
'魏妍戎',
'孙瑞琳',
'张照奇',
'陈英杰',
'李明朗',
'杨明珠',
'马溪晨',
'王盛渠',
'刘梓涵',
'李建松',
'杨玉辉',
'杨傲翔',
'魏辰轩',
'秦佳忆',
'郑卓蕾',
'吴美萱',
'代帅',
'刘璐',
'郭啸',
]
rper=' '  #初始化rper
operson=list(person) #进行人名单初始值复制存储
rseed(time())  #使种子随机化成度与时间绑定
history=[]  #历史记录
num=0  #第几位

#定义抽人按钮命令
def dm():
    global a,person,operson,history,num,his,His
    #鼠标样式
    a=rcho(cursorList)
    #print(repr(a))
    button0.config(cursor=a)

    #核心抽人
    apn=len(person)-1
    if apn < 0:
        person0.config(text="!全班都抽了个遍了!\n在摁一次重置",font=('楷体',50))
        rseed(time()) #更新随机种子
        person=operson
        operson=list(person)
        return
    else:
        rper=rcho(person)
        #print(repr(rper))
        person0.config(text=rper,font=('楷体',100,'bold'))
        shuffle(person)#列表随机重排
        person.remove(rper)#移除本次随机到的人员
        #print(rper)
        
        num+=1
        b="第"+str(num)+"位："+rper
        #print(b)
        history.append(b)
        #print (history)
        if "His" in globals() and His.winfo_exists():  #关闭历史记录窗口
            His.destroy()
        

#定义更新按钮命令
def update():
    up=tkinter.Toplevel()
    up.title('更新路径')
    up.geometry('400x150')
    up.resizable(False, False)
    text0=tkinter.Label(
        up,
        text='更新去找孙世博啊\n搁这干哈？',
        font=("黑体", 20, "bold")).pack(expand=True)

#定义历史按钮命令
def History():
    global history,his,more,His
    His=tkinter.Toplevel()
    His.transient(r0)
    His.title("历史记录")
    His.geometry("200x500")
    his=tkinter.Text(His)
    his.config(state=tkinter.NORMAL)#开启写入
    for i in history:
        his.insert(tkinter.END, f" {i} \n")
    his.config(state=tkinter.DISABLED)#关闭写入
    his.pack(expand=True,fill='both',padx=10,pady=10)
    more.destroy()  #关闭选项窗口
    #print (history)
    



#定义选项按钮命令
def more():
    global more
    more = tkinter.Toplevel()
    more.title("更多")  
    more.geometry("400x300")  
    more.resizable(False, False) 
    #more.transient(r0)
    
    # 设置窗口内容
    more1 = tkinter.Label(
        more,
        text="开发者：204孙世博\n校验者：204孙世博\n\n版本号：1.6",
        font=("楷体", 20, "bold")
    )
    more1.pack()
    more2=tkinter.Button(
        more,
        text='检查更新',
        font=("楷体", 20, "bold"),
        command=update)
    more2.pack(expand=True)


    # 历史按钮
    close_btn = tkinter.Button(
        more,
        text="历史记录",
        font=("楷体", 16),
        command=History,
        padx=20,
        pady=5
    )
    close_btn.pack(side='bottom',pady=10)



    



#主窗口
r0 = tkinter.Tk()
r0.title("随机点名")
r0.geometry("800x500")
r0.resizable(True,True)
setting=tkinter.Button(r0,bitmap='gray12',relief='flat',command=more).pack(anchor='nw')
title=tkinter.Label(r0,text="二部(4)班随机点名微程序已就位\nAre you ready?",font=("楷体",30,"bold"),padx=50).pack(pady=(20,0))

person0=tkinter.Label(r0)
person0.pack(expand=True)
button0=tkinter.Button(r0,text="抽取幸运儿",font=("楷体",16,"bold"),command=dm,cursor=a,padx=40,pady=30)
button0.pack(expand=True,pady=(0,20))


r0.mainloop()











