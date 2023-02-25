import json
import os
from flask import Flask
from flask import request
from flask import make_response
from service.Case_hello import hello_function

# Flask
app = Flask(__name__)
@app.route('/', methods=['POST'])

def MainFunction():

    #รับข้อความจาก Dailog flow
    messageFromUser = request.get_json(silent=True, force=True)

    #สร้างคำตอบ
    answerFromBot = generating_answer(messageFromUser)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answerFromBot)
    r.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป
    return r

def generating_answer(message):

    #Print intent ที่รับมาจาก Dailogflow
    print('raw message ===> \n',json.dumps(message, indent=4 ,ensure_ascii=False))

    #เก็บค่า ชื่อของ intent group ที่รับมาจาก Dailogflow
    intent_group_question_str = message["queryResult"]["intent"]["displayName"] 
    print(intent_group_question_str)

    #ลูปตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'Case_sleepy':
        answer_from_bot = {"fulfillmentText": "ง่วงเหมือนกัน"}
    elif intent_group_question_str == 'Case_Hello':
        answer_from_bot = hello_function()
    else: 
        answer_from_bot = {"fulfillmentText": "พูดไรนิ"}

    #สร้างการแสดงของ dict 
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot

#กำหนด port ให้ flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)