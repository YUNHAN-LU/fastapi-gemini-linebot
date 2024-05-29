import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "zh": "哈囉！",
  "en": "Hello!"
}

AI_GUIDELINES = """"""
path = "resource/QAdata2.txt"
with open(path) as f:
    lines = f.readlines()
AI_GUIDELINES = ''.join(lines)


class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "model", 
                "parts": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(1)
        self.msg_list.append({"role": "user", "parts": new_msg})

    def generate_prompt(self):
        return self.msg_list