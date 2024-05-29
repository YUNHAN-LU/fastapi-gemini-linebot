from api.prompt import Prompt
import os
import google.generativeai as genai


genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

class Gemini:
    def __init__(self):
        self.prompt = Prompt()
        self.model = genai.GenerativeModel('gemini-pro')


    def get_response(self):
        tmp = self.prompt.generate_prompt()
        response = self.model.generate_content(tmp)
        #print(tmp)
        try:
            return response.text
        except:
            print(response)

    def add_msg(self, text):
        self.prompt.add_msg(text)

#gemini = Gemini()

# while(1):
#     mes = input()
 
    
#     chatgpt.add_msg(f"HUMAN:{mes}?\n")
#     reply_msg = chatgpt.get_response().replace("AI:", "", 1)
#     chatgpt.add_msg(f"AI:{reply_msg}\n")
#     print("say:" + reply_msg)
