import traceback
from PIL import Image, ImageDraw, ImageFont
import os,sys,time,ctypes,random,json
from datetime import date
import os
# import tkinter
# import tkinter.messagebox #弹窗库
try:
    # os.getpid()
    whnd = ctypes.windll.kernel32.GetConsoleWindow()

    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    
    try:
        f = open('./config.json',encoding='utf-8')
        t = json.load(f)
    except Exception as e:
        t = {'name':'中考',"y":"2022",'m':"6",'d':"17"}
        #t = {'name':'中考',"y":"2022",'m':"3",'d':"25"}
    # t['pid'] = os.getpid() 
    
    def zh(s):
        return ImageFont.truetype(p+"/zh.ttf", int(s//bl))
    def en(s):
        return ImageFont.truetype(p+"/en.ttf", int(s//bl))
    while True:
    	
        start = date(year=int(time.strftime("%Y",time.localtime())) ,month=int(time.strftime("%m",time.localtime())),day=int(time.strftime("%d",time.localtime())))
        end = date(year=int(t['y']),month=int(t['m']),day=int(t['d']))
        cc=str((end-start).days)
        p= './file'
        #p= os.path.split(os.path.realpath(__file__))[0] + 'file'        
        im = Image.open(p+"/img/"+str(random.randint(1,25))+".jpg").convert('RGBA')
        im = im.resize((2440, 1440), Image.ANTIALIAS)
        txt=Image.new('RGBA', im.size, (255,255,255,0))
        bl=2505/im.size[1]
        #print('start')
        d=ImageDraw.Draw(txt)       

        t1=zh(200)
        word="今天"+"  "+time.strftime("%Y-%m-%d", time.localtime()) 
        w,h=t1.getsize(word)
        d.text((int((im.size[0]-w)//2), int(100//bl)), word, font=t1, fill=(255,255,255,255))

        t1=zh(200)
        word="距离"+t['name']+"还有" 
        w,h=t1.getsize(word)
        d.text((int((im.size[0]-w)//2), int(450//bl)), word, font=t1, fill=(255,255,255,255))

        t1=en(1000)
        word=cc
        w,h=t1.getsize(word)
        if int(cc) >= 100:
            d.text((int((im.size[0]*0.95-w)//2), int(700//bl)), word, font=t1, fill=(204,255,102,255))
        elif int(cc) >= 50:
            d.text((int((im.size[0]*0.95-w)//2), int(700//bl)), word, font=t1, fill=(255,255,102,255))
        elif int(cc) >=5:
            d.text((int((im.size[0]*0.95-w)//2), int(700//bl)), word, font=t1, fill=(255,102,102,255))
        else:
            d.text((int((im.size[0]*0.95-w)//2), int(700//bl)), word, font=t1, fill=(255,0,51,255))
        # d.text((int((im.size[0]*0.95-w)//2), int(700//bl)), word, font=t1, fill=(255,255,255,255))

        t1=zh(200)
        word="天"
        d.text((int((im.size[0]*0.95+w)//2), int(1400//bl)), word, font=t1, fill=(255,255,255,255))

        t1=zh(200)
        word=t['name']
        w,h=t1.getsize(word)
        d.text((int((im.size[0]*0.75-w)//2), int(1900//bl)), word, font=t1, fill=(255,255,255,255))

        t1=en(200)
        word=t['y']+'-'+t['m']+'-'+t['d']
        #print(word)#2022-6-18
        d.text((int((im.size[0]*0.75+w)//2), int(1900//bl)), word, font=t1, fill=(255,255,255,255))

        #合并两个图片
        out=Image.alpha_composite(im, txt).convert('RGB')
        p2=p+"/output/tr.jpg"
        out.save(p2)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(p2), 3)
        #print(p+"/output/tr.jpg")
        time.sleep(6)
        

except Exception as e:
    with open('./error.log', 'w') as file_object:
        file_object.write(str(traceback.print_exc())+str(e))
    # tkinter.messagebox.showerror('错误','当前程序出现错误，请查看说明')
