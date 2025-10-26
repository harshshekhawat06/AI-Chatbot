from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from openai import AzureOpenAI
 
load_dotenv()
app = Flask(__name__)
 
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
 
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
 
    conversation_history.append({"role": "user", "content": user_message})
 
    response = client.chat.completions.create(
        model=deployment_name,
        messages=conversation_history,
        max_tokens=200
    )

    bot_reply = response.choices[0].message.content
    token_usage = response.usage.total_tokens   
 
    conversation_history.append({"role": "assistant", "content": bot_reply})

    return jsonify({"reply": bot_reply, "tokens_used": token_usage})

if __name__ == "__main__":
    app.run(debug=True)
