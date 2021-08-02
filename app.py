from flask import Flask, request, session
from random import choice
from flask import Flask, request, Response
import os
import openai
app = Flask(__name__)

openai.api_key = os.getenv('Insert-key-here')
completion = openai.Completion()

start_sequence = """\nQoom:"""
restart_sequence = """\n\nYou:"""

session_prompt = """Welcome! I am QoomBot, Qoom's very own AI based chatbot. How may I help you?

You: What do you do?
Qoom: I am an AI tool to help you navigate the Qoom platform. 

You: How can I create a new project? 
Qoom: Go to your coding space and click New Project. Enter a project name and select Create. 

You: How can I learn to code?
Qoom: Go to qoom.io and navigate to the Tutorials page to learn how to code new projects. You can also go to your coding space and select the Qoom of the Week tab to join a workshop. 

You: Can I get involved with the Qoom organization? 
Qoom: Apply to Qoom's Creator Group sessions to start getting involved. 

You: Can you build me a website? 
Qoom: I'm afraid I'm not able to help you with that. 

You: What should I do first?
Qoom: You should start by creating an account. You can access tutorials, your coding space, and new opportunities. 

You:"""

stop = "\n"

def ask(question, chat_log=None):
 prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
 response = openai.Completion.create(
 engine="davinci",
 prompt=prompt_text,
 temperature=0.7,
 max_tokens=300,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0.1,
 stop=[stop],
 )
 story = response["choices"][0]["text"]
 return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
    return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"

def root_dir(): 
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename): 
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


app.config["SECRET_KEY"] = "insert-random-string-here"
@app.route("/qoombot/answer", methods=["POST"])
def qoom():
 incoming_msg = request.get_json()["question"]
 print(incoming_msg)
 chat_log = session.get("chat_log")
 answer = ask(incoming_msg, chat_log)
 return answer

@app.route("/", methods=['GET', 'POST'])
def home():
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route("/style.css", methods=['GET'])
def style():
    content = get_file('style.css')
    return Response(content, mimetype="text/css")

@app.route("/script.js", methods=['GET'])
def scriptjs():
    content = get_file('script.js')
    return Response(content, mimetype="text/js")

if __name__ == "__main__":
 app.run(debug=True)