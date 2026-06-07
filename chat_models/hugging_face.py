from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

llm_model=HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
model=ChatHuggingFace(llm=llm_model)
response=model.invoke("what is the purpose of BLDC fans?")
print(response.content) 