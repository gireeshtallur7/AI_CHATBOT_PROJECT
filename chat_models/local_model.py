from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFacePipeline.from_model_id(model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',task="text-generation",
                                  pipeline_kwargs=dict(max_new_tokens=520,do_sample=False,repetition_penalty=1.07))
model=ChatHuggingFace(llm=llm)
response=model.invoke("what is the purpose of BLDC fans?")
print(response.content)
