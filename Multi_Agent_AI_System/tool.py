from langchain.tools import tool
from tavily import TavilyClient
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os   
load_dotenv()
from rich import print
tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for the recent and  relevant information on topic this will returns URLs,return titles."""
    response = tavily.search(query=query,max_results=7) 
    return response

    out_puts=[]
    for r in response['results']:
        out_puts.append(f"Title: {r['title']}\nURL: {r['url']}\nsnippet:{r['content'][:200]}\n")
        return "\n **********\n".join(out_puts)

# print(web_search.invoke("What is the latest news on ronaldo winning ? "))

@tool
def web_scrape(url: str) -> str:
    """Scrape the content of a web page given its URL."""
    try:
        response = requests.get(url, timeout=10,headers={"User-Agent": "Mozilla/5.0"})  # Set a timeout for the request
        # response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(["script", "style", "footer" ,"nav"]):
            script.decompose()  # Remove script and style elements
        return soup.get_text(separator=" ",strip=True)[:3000]  # Get the text content of the page
    except Exception as e:
        return f"An error occurred while trying to scrape the web page or URL: {str(e)}"
print(web_scrape.invoke("https://en.wikipedia.org/wiki/Cristiano_Ronaldo"))