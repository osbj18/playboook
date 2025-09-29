import os
import requests
api_key = os.getenv("MIMO_OPENAI_API_KEY")
url = "https://ai.mimo.org/v1/openai/message"
headers = {
  "api-key": api_key
}

def send_message(user_message, thread_id):
  body = {
    "message": user_message
  }
  if thread_id:
    body["threadId"] = thread_id
  response = requests.post(url, headers=headers, json=body)
  return response.json()


thread_id = None
print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new thread for you.\n")

threads = []
while True:
  user_message = input("You: ")
  if user_message == "exit".lower():
    break
  elif user_message == "new".lower():
    current_thread_id = None
    print("You are now starting a new thread!")
    continue
  response_data = send_message(user_message, thread_id)
  latest_message = response_data.get("response")
  current_thread_id = response_data.get("threadId")
  print(f"GPT: {latest_message}")
  if current_thread_id not in threads:
    threads.append(current_thread_id)
  



