from llama_index.core.agent import ReActAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.llms.openai import OpenAI
from llama_index.core.base.llms.types import ChatMessage


from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()

import execute


execute_tool = FunctionTool.from_defaults(fn=execute.execute_code)


llm = OpenAI()
llm = Anthropic()
chat_history = [
    ChatMessage(
        role="system",
        content="you are a code generator, the user will request code from you. you want to ship working code so you can trial and test it before showing it tot he user Don't add print statement to the code. try to use the inputs the user wants and do not hardocde variables in the code too much. Good Luck!",
    )
]

agent = ReActAgent.from_tools(
    [execute_tool], llm=llm, verbose=True, chat_history=chat_history
)

if __name__ == "__main__":

    agent.chat(
        "write code that returns the divisors of a number"
    )
    # agent.chat_repl()
