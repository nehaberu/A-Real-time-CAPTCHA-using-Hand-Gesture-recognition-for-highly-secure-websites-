# import os
# import MySQLdb
# from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
# from database import db_connect,admin_loginact,user_reg,user_loginact,admin_viewusers,lost_act,updateact,viewlost,admin_viewrevw,uviewact,uviewdeact,add_categoryact,add_productact,admin_viewproducts,admin_adelete,admin_cate,add_addacountdetailsact,add_moneyact
# from database import db_connect,user_viewaccuont,user_search,admin_search,admin_viewpurchaseproducts,admin_viewrecommedns,user_productsact,user_recommend,add_cartact,user_viewrecommend,user_viewcart,admin_pviewproducts
# from database import db_connect,purchase1,user_viewcatp,remove1,analyst_loginact,user_viewpurchase,viewstatus
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.secret_key = os.urandom(24)


# @app.route("/")
# def FUN_root():
#     return render_template("index.html")

# @app.route("/index.html")
# def index():
#     return render_template("index.html") 
#!/usr/bin/env python
import string    
import random # define the random module  
from IPython import display
from captcha.image import ImageCaptcha

def capt_str():
    S = 6  # number of characters in the string.    
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))  
    ran = str(ran)
    print("The randomly generated string is : " + ran) # print the random data 
    return(ran)

image_info = ImageCaptcha (width=250, height=100)

captcha_text = capt_str()
source = image_info.generate(captcha_text)
image_info.write(captcha_text, 'Captcha.png')

display.Image("./Captcha.png")

print("Type in the sequence displayed in the above image")
wrd = input()
c = 0
if (wrd == captcha_text):
    print ("Correct! Access granted")
else:
    print ("Wrong answer! Try again")
    wrd1 = input()
    if (wrd1 == captcha_text):
        print ("Correct! Access granted")
    else:
        print ("Wrong answer again! Access denied")