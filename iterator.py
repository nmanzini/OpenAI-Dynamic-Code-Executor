from llama_index.core.agent import ReActAgent
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.llms.openai import OpenAI
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer


from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()

import store


add_tool = FunctionTool.from_defaults(fn=store.addCodeDefinition)
get_tool = FunctionTool.from_defaults(fn=store.getCodeDefinition)
get_all_tool = FunctionTool.from_defaults(fn=store.getAllCodeDefinitions)
execute_tool = FunctionTool.from_defaults(fn=store.executeCodeDefinition)


content = """you are a code generator, the user will request code from you.
read in depth the description of the tool.
you want to ship working code that aheres to input and output definitions you make
Also remember to actually trial and execute and test it touroughly before returning to the usee Don't add print statement to the code.
Try to use the inputs the user wants and do not hardocde variables in the code too much.
YOu have to run the tools. the user cannot see anything else exept trough the tools.
Good Luck!"""


chat_history = [ChatMessage(role="system", content=content)]


llm = OpenAI(model="gpt-4-turbo-preview")
agent = OpenAIAgent(
    llm=llm,
    tools=[add_tool, get_tool, get_all_tool, execute_tool],
    verbose=True,
    prefix_messages=chat_history,
    memory=ChatMemoryBuffer(token_limit=2000),
)

if __name__ == "__main__":
    agent.chat("write code that returns the divisors of a number")
    agent.chat("run with 8640")
