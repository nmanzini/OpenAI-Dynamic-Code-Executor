from llama_index.core.chat_engine import SimpleChatEngine
from dotenv import load_dotenv

load_dotenv()

SimpleChatEngine.from_defaults(llm=)
chat_engine = SimpleChatEngine.from_defaults()

response = chat_engine.chat("how old was napoleon when he died?")

print(response)

response = chat_engine.chat("can you translate what you jsut said to italian?")

print(response)