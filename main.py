from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3.2:latest", request_timeout=30)

result = llm.complete("Hello World")

print(result)