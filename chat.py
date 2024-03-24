from llama_index.core.chat_engine import SimpleChatEngine
from dotenv import load_dotenv

load_dotenv()

chat_engine = SimpleChatEngine.from_defaults()

response = chat_engine.chat("how old was napoleon when he died?")

print(response)

response = chat_engine.chat("can you translate what you just said to italian?")


print(response)

from llama_index.llms.anthropic import Anthropic
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer

llm = Anthropic()

prefix_messages = [ChatMessage(role="system", content="You are a Julius Caesar expert.")]

mem = ChatMemoryBuffer(token_limit=1000)

chat_engine = SimpleChatEngine(llm=llm, memory=mem, prefix_messages=prefix_messages)

response = chat_engine.chat("whend did he die?")
print(response)


