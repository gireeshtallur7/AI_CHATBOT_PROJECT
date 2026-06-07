from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from tool import web_search, web_scrape
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=ChatMistralAI(model="mistral-small-2603", temperature=0, max_tokens=3000) 

# 1st agent
def search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

# 2nd agent
def scrape_agent():
    return create_agent(
        model=llm,
        tools=[web_scrape]
    )

# write promt or LCEL pipeline
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can search the web and scrape web pages to gather information."),
    ("human", "What is the latest news on Cristiano Ronaldo winning ?")
])
