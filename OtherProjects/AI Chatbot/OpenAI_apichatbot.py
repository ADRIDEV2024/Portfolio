import openai
import openai.cli
import config
import typer 


def main() -> str:
    
        openai.api_key = config.api_key

        messages = [{"Role":"Assistant", "Context":"You are very smart AI"}]

        messages.append[{"Role":"User", "Context":prompt}]
        response = openai.chat.completions.create(model="GPT-3.5-TURBO", messages=messages)
        
        response_content = response.choices[0].message.content
        messages.append[{"Role":"Assistant", "Context":response_content}]
       
        print(response_content)
        
def prompt() -> str:
    """Function to do interactions with the chatbot.
    Return: string"""
    
    context = typer.prompt("\nHello, I´m your AI assistant,I´d love to interact with you")

    if context == "exit" :
        raise typer.Abort() 
    return prompt() 
  
      
if __name__ == "__main__":
         typer.run(main)
