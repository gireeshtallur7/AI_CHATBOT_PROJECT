from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
 
# from langchain_openai import init_chat_model #from this line of code we can use  
#any chat model 

# model=init_chat_model("gpt-3.5-turbo") #we can use any model by changing the name of the model here
# response=model.invoke("What is cricket?") #we can ask any question to the model and it will give us the answer
# print(response)

# from langchain_openai import openai
# model= openai(model="gpt-5")
# response=model.invoke("What is cricket?")   
# print(response.content)


from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file
from langchain.chat_models import init_chat_model
model=init_chat_model("groq:openai/gpt-oss-120b") 
response = model.invoke("give one paragraph of  definition of machine learning")
print(response.content) # Initialize the ChatGroq model

from langchain_groq import ChatGroq
model=ChatGroq(model='openai/gpt-oss-120b')
response=model.invoke("give one paragraph of  definition of ronaldo")
print(response.content)   # Initialize the ChatGroq model

from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2506",temperature=0.7,max_tokens=70 )
response = model.invoke("write 2 short joke about programmers")
print(response.content) 