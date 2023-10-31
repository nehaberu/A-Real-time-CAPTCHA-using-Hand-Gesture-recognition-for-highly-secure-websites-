import os
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
import string    
import random # define the random module  
from IPython import display
from captcha.image import ImageCaptcha
import cv2
import mediapipe as mp

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def capt_str():
    S = 6  # number of characters in the string.    
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))  
    ran = str(ran)
    print("The randomly generated string is : " + ran) # print the random data 
    image_info = ImageCaptcha (width=250, height=100)
    source = image_info.generate(ran)
    image_info.write(ran, 'static/Captcha.png')

    display.Image("./Captcha.png")
    return render_template("index.html", ran=ran) 



@app.route("/adminlogact", methods=['GET', 'POST'])
def adminlogact():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        password = request.form['password']
        print(password)
        itext = request.form['itext'] 
        print(itext)

        otext = request.form['otext'] 
        print(itext)

       

        if ((username== 'admin') and (password== 'admin') and (otext== itext)):


            gestures_db = {'index':['index'], 'peace':['index','middle'], 'three':['index','middle','ring'], 'four':['index','middle','ring','little'], 'five':['thumb','index','middle','ring','little'], 'closed-fist':[]}

            res = img, img_fingers = random.choice(list(gestures_db.items()))
            print("....................")
            print(res)
            
            print("The question is : " + str(res))

            resi = res[0]

            q1 = res[1]
            print("qqqqq1")
            print(q1)

            q1 = len(q1)
            print(q1)

        
            print("***************")

            print(res)
            # import cv2
            
            # abc = display.Image("./"+img+".png")
            # image_info = ImageCaptcha (width=250, height=100)
            # source = image_info.generate(res)
            # image_info.write(res, './abc.png')

            
            return render_template("welcome.html", m1="sucess",resi=resi,q1 = q1)
        else:
            return render_template("index.html", m2="Login Failed")

@app.route("/uactivate")
def uactivate():

    q1 = request.args.get('q1')
    cap = cv2.VideoCapture(0)
    mp_Hands = mp.solutions.hands
    hands = mp_Hands.Hands()
    mpDraw = mp.solutions.drawing_utils

    cv2.startWindowThread()

    finger_Coord = [(8,6), (12, 10), (16, 14), (20, 18)]
    thumb_Coord = (4,2)
    question = ['index', 'middle']
    print ("fingers open in question:", question)
    x =[]

    while True:
        success, image = cap.read()
        print("pppppppppp")
        print(image)
        RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(RGB_image)
        multiLandMarks = results.multi_hand_landmarks
        stri = ""

        if multiLandMarks:
            handList = []
            for handLms in multiLandMarks:
                mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
                for idx, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    handList.append((cx, cy))
                for point in handList:
                    cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
            
                    upCount = 0
                for coordinate in finger_Coord:
                    if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                        upCount += 1
                if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                    upCount += 1
                    stri = stri+ "thumb "
            
                i = 0
                for coordinate in finger_Coord:
                    if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                        if (i == 0):
                            stri = stri+"index "
                        elif (i == 1):
                            stri = stri+"middle "
                        elif (i == 2):
                            stri = stri+"ring "
                        elif (i == 3):
                            stri = stri+"little "
                    i = i+1
            
                if len(stri) == 0:
                    stri = stri + "closed-fist"
                
                cv2.putText(image, str(upCount), (10,100), cv2.FONT_HERSHEY_PLAIN, 4, (0,255,0), 4)
                cv2.putText(image, stri, (50,95), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
                cv2.putText(image, "<<press 'q' button to capture screen>>", (75,50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255), 2)
                x = stri.split()

        cv2.imshow("Counting number of fingers", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('frame.jpg',image)
            x = len(x)
            print ("fingers open in screencapture:",x)
            cv2.destroyAllWindows()
            break
    
    if (str(x) == str(q1)):
        print("CORRECT ANSWER!")
        return render_template("welcome1.html", m1="sucess")
    else:
        print("WRONG ANSWER! TRY AGAIN.")
        return render_template("index.html", m1="sucess")
    cap.release()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)








    # print("Type in the sequence displayed in the above image")
    # wrd = input()
    # c = 0
    # if (wrd == captcha_text):
    #     print ("Correct! Access granted")
    # else:
    #     print ("Wrong answer! Try again")
    #     wrd1 = input()
    #     if (wrd1 == captcha_text):
    #         print ("Correct! Access granted")
    #     else:
    #         print ("Wrong answer again! Access denied")
#!/usr/bin/env python






