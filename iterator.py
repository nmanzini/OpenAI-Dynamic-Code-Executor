# from llama_index.core.agent import ReActAgent
# from llama_index.llms.anthropic import Anthropic
# from llama_index.llms.openai import OpenAI
# from llama_index.core.tools import FunctionTool

from dotenv import load_dotenv

load_dotenv()

import textwrap


def execute_code(code: str, inputs: dict = {}, outputs: dict = None):
    outputs = outputs or {}
    inputs = inputs or {}
    try:
        # Remove indentation from the code string
        code = textwrap.dedent(code)

        # Compile the code string into a code object
        code_obj = compile(code, "<string>", "exec")

        # Execute the code object with the provided inputs and outputs
        exec(code_obj, inputs, outputs)
        return outputs
    except Exception as e:
        return f"An Exception occurred: {e}"


if __name__ == "__main__":

    inputs = {"a": 3, "b": 4}
    code1 = """
        result = {}
        result['sum'] = a + b
        result['product'] = a * b
        """
    result = execute_code(code1, inputs)
    print(result)
    assert result == {"result": {"sum": 7, "product": 12}}

    inputs["input_array"] = [5, 2, 8, 1, 9]
    code2 = """
        sorted_array = sorted(input_array)
        """
    result = execute_code(code2, inputs)
    assert result == {"sorted_array": [1, 2, 5, 8, 9]}
    print(result)
