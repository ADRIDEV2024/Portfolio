import openai
import openai.cli
import config


openai.api_key = config.api_key

while True:
    

     messages = [{"Role":"System", "Context":"You are very smart AI"}]
     context = input("Hello, I´m your AI assistant,I´d love to interact with you")

     if context == "exit" :
         break

     messages.append[{"Role":"User", "Context":context}]
     response = openai.chat.completions.create(model="GPT-3.5-TURBO", messages=messages)
     
     