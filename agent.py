from llama_index.core.agent import ReActAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.llms.openai import OpenAI

from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()


def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

llm = OpenAI()
llm = Anthropic()
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)

response = agent.chat("What is 20+(2*4)? Calculate step by step ")

agent.chat_repl()
