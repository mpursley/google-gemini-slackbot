from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import threading
import pathlib
import textwrap
import os
from dotenv import load_dotenv

import google.generativeai as genai
from threading import Thread

processed_ids = set()

# Load environment variables from .env file
load_dotenv()

# Define Google API Key and Set Gemini Pro Model
google_api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize a Web Client with the Slack bot token from the environment variables
slack_token = os.getenv('SLACK_BOT_TOKEN')
client = WebClient(token=slack_token)

# Get BOT_USER_ID from environment variables
BOT_USER_ID = os.getenv('BOT_USER_ID')
app = Flask(__name__)


def handle_event_async(data):
    thread = Thread(target=handle_event, args=(data,), daemon=True)
    thread.start()

def handle_event(data):
    event = data["event"]

    # --- Consolidated Bot Filtering ---
    # Ignore messages from any bot, including itself, to prevent loops.
    if "bot_id" in event or event.get("user") == BOT_USER_ID:
        return

    # --- Prevent Duplicate Processing from Slack Retries ---
    client_msg_id = event.get("client_msg_id")
    if client_msg_id and client_msg_id in processed_ids:
        return
    if client_msg_id:
        processed_ids.add(client_msg_id)

    channel_id = event["channel"]
    user_message = event.get("text", "")
    thread_ts = event.get("thread_ts") or event.get("ts")

    # If it's an app mention, remove the bot's user ID from the message text
    if f"<@{BOT_USER_ID}>" in user_message:
        user_message = user_message.replace(f"<@{BOT_USER_ID}>", "").strip()

    if not user_message:
        return

    try:
        conversation_history = []
        if thread_ts:
            # Fetch thread history
            result = client.conversations_replies(channel=channel_id, ts=thread_ts)
            messages = result.get("messages", [])

            # Construct conversation history for the model
            for msg in messages:
                # Skip the current message being processed, it's added at the end
                if msg.get("client_msg_id") == client_msg_id:
                    continue

                text = msg.get("text", "").replace(f"<@{BOT_USER_ID}>", "").strip()

                if msg.get("user") == BOT_USER_ID or "bot_id" in msg:
                    conversation_history.append(f"Bot: {text}")
                else:
                    conversation_history.append(f"User: {text}")

        # Add the current user message to form the complete prompt
        conversation_history.append(f"User: {user_message}")
        full_prompt = "\n".join(conversation_history)

        # Generate response from Gemini
        gemini = model.generate_content(full_prompt)
        textout = gemini.text.replace("**", "*")

        # Post the response back to the thread
        client.chat_postMessage(
            channel=channel_id,
            text=textout,
            thread_ts=thread_ts,
            mrkdwn=True
        )

    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
    except Exception as e:
        print(f"An error occurred: {e}")

@app.route('/gemini', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        gemini = model.generate_content("Hi")
        return gemini.text

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    if "event" in data:
        handle_event_async(data)

    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
