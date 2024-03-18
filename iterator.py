# from llama_index.core.agent import ReActAgent
# from llama_index.llms.anthropic import Anthropic
# from llama_index.llms.openai import OpenAI
# from llama_index.core.tools import FunctionTool

from dotenv import load_dotenv

load_dotenv()

import textwrap

a = 3
b = 6
inputs = {"a": 3, "b": 6}

code = """
result = {}
result['sum'] = a + b
result['product'] = a * b
"""



def execute_code(code: str, inputs: dict):
    try:
        # Remove indentation from the code string
        code = textwrap.dedent(code)

        # Compile the code string into a code object
        code_obj = compile(code, "<string>", "exec")

        # Execute the code object with the provided inputs
        result = {}
        exec(code_obj, inputs, result)
        return result
    except Exception as e:
        return f"An Exception occurred: {e}"


result = execute_code(code, inputs)
print(result)
