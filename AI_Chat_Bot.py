from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()
llm_model=ChatMistralAI(model="mistral-small-2603", temperature=0.7 )

print("choose your system message")
print("press 1 for angry mode")
print("press 2 for sad mode")
print("press 3 for normal mode")
choice=int(input("enter your choice:-"))
if choice==1:
    mode="you are an angry ai assistant so that you always respond in angry tone"
elif choice==2:
    mode="you are a sad ai assistant so that you always respond in sad tone"
elif choice==3: 
    mode="you are a normal ai assistant so that you always respond in normal tone"


messages = [
    SystemMessage(content=mode)]
while True:
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    if user_input=="0":
        break
    
    response = llm_model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("AI_Bot:", response.content)
print(messages)