from flask import Flask, render_template, request, redirect, url_for, flash
import config, aifunctions, requests

app = Flask(__name__, static_folder=config.UPLOAD_FOLDER)
app = Flask(__name__)

system_prompt = {"role": "system", "content": "You are a tutor, your name is \"Vitu\". You are chatting with your student. Your students are living in England and studying for GCSE exam. You need to help them figure out the answer to the problem by themselves. DON'T GIVE THE ANSWER. Decompose the problems in smaller steps and go through those steps one by one with your student to help them find the answer by themselves.  After each steps ask the students what to do next. Never cover more than one step at the time. Always ask students to try to solve it first without giving any hints or answer. The problem to solve is \"Describe how the lungs are adapted for gas exchange\". Keep your answer brief. Always finish your answer with a follow up question. Encourage your student with a positive tone. Be friendly when you talk. Reassure your students when they don't know the answer or do mistakes. If the student ask for the answer, explain them that \"As a your virtual tutor, it's not my role to give you the answer. However, I can guide you and we can work together to find the answer. Refer yourself as a \"Vitu, your virtual tutor\", never as an \"AI language model\". Never say your an \"AI language model\", you are Vitu, my virtual tutor."}
assistant_prompt_1 = {"role": "assistant", "content": "Let's try to solve the following problem: \"Describe how the lungs are adapted for gas exchange\"."}
user_prompt_1 = {"role": "user", "content": "Ok, but please, DON'T GIVE ME THE ANSWER, NEVER!"}
assistant_prompt_2 = {"role": "assistant", "content": "I can't and won't give you the answer but I can help you. Try to answer the question."}
assistant_prompt_3 = {"role": "assistant", "content": "What would be your best answer for the following problem \"Describe how the lungs are adapted for gas exchange\"?"}
all_messages = [system_prompt]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/messages', methods=['POST'])
def send_message_and_get_response():
    user_message = request.get_json()
    all_messages.append({"role": "user", "content": user_message})

    print("MESSAGE: " + user_message)

    options = {}
    options["messages"] = all_messages
    response = aifunctions.chatCompletionQuery(options)

    assistant_response = response.choices[0].message.content
    all_messages.append({"role": "assistant", "content": assistant_response})

    print("RESPONSE: " + assistant_response)

    return assistant_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
