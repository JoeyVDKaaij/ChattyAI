from openai import OpenAI
import os

class OpenAI_Manager:
    client = None
    messages = []

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("Open_API_Key"))

        print("OpenAI Initialized.")

    def appendmessage(self, message):
        self.messages.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )
        self.messages.append({"role": completion.choices[0].message.role, "content": completion.choices[0].message.content})
        # Uncomment the line below to hear the response from the AI
        # print(completion.choices[0].message.content)
        return completion.choices[0].message.content