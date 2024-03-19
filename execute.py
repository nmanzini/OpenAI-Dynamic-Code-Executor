import textwrap


def execute_code(
    code: str, inputs: dict = None, outputs: dict = None
) -> dict:
    """
    code: str
        The code to execute
    inputs: dict
        The inputs to the code, to use it put your variable as a key in the dict and the value as the value
    outputs: dict
        To return outputs you have to put them in the outputs dict. The key is the name of the output and the value is the value of the output
    
    Execute the code based on the inputs and return the outputs. you need to run the code not only define the function. and remember to use the inputs and outputs dict to get the inputs and return the outputs.

    Example:
        execute_code(
            code="outputs['sum'] = a + b",
            inputs={"a": 3, "b": 4},
        )

    Example returns:
        {"sum": 7}
    """

    verbose=True

    inputs = inputs or {}
    try:
        code = textwrap.dedent(code)
        code = "outputs = {}\n" + code

        code_obj = compile(code, "<string>", "exec")
        local = dict(inputs)
        exec(code_obj, None, local)

        if verbose:
            print(f"execute_code code   : {code[:100]}")
            print(f"execute_code inputs : {inputs}")
            print(f"execute_code outputs: {local["outputs"]}")
        return local["outputs"]
    except Exception as e:
        return f"An Exception occurred: {e}"


if __name__ == "__main__":

    inputs = {"a": 3, "b": 4}
    code1 = """
        outputs['sum'] = a + b
        outputs['product'] = a * b
        """
    result = execute_code(code1, inputs)
    print("result", result)
    assert result == {"sum": 7, "product": 12}

    inputs["input_array"] = [5, 2, 8, 1, 9]
    code2 = """
        outputs["sorted_array"] = sorted(input_array)
        """
    result = execute_code(code2, inputs)
    print("result", result)
    assert result == {"sorted_array": [1, 2, 5, 8, 9]}
