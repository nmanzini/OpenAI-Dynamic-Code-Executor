storage = {}

class CodeDefinition:
    def __init__(self, snippet, description, inputs, outputs):
        self.snippet = snippet
        self.description = description
        self.inputs = inputs
        self.outputs = outputs

    def getSnippet(self):
        return self.snippet

    def getInputs(self):
        return self.inputs

    def getOutputs(self):
        return self.outputs

    def getDescription(self):
        return self.description

    def __str__(self):
        return f"Code: {self.snippet}\n Description: {self.description}\nInputs: {self.inputs}\nOutputs: {self.outputs}"


def addCodeDefinition(
    name: str, snippet: str, description: str, inputs: dict, outputs: dict
) -> None:
    """
    Add a code snippet to the storage
    name: str
        The name of the code snippet
    snipper: str
        The code to execute
    description: str
        The description of the code snippet
    inputs: dict
        The inputs to the code snippet, key is the name value is the type
    outputs: dict
        The outputs of the code snippet, key is the name value is the type

    returns:
        None
    Example:
        addCodeDefinition(
            name="add",
            snippet="outputs['sum'] = a + b",
            description="Add two numbers",
            inputs={"a": "int", "b": "int"},
            outputs={"sum": "int"},
        )
    """
    existed = name in storage
    storage[name] = CodeDefinition(snippet, description, inputs, outputs)

    if existed:
        return f"Code snippet was updated, now can run with {executeCodeDefinition.__name__}"
    return f"Code snippet was added, now can run with {executeCodeDefinition.__name__}"


def getCodeDefinition(name: str) -> CodeDefinition:
    """
    Get the code snippet from the storage
    name: str
        The name of the code snippet

    returns:
        CodeDefinition

    example:
        getCodeDefinition("add")
    example returns:
        Code: outputs['sum'] = a + b
        Description: Add two numbers
        Inputs: {'a': 'int', 'b': 'int'}
        Outputs: {'sum': 'int'}
    """
    return storage[name]


def getAllCodeDefinitions() -> dict[str, CodeDefinition]:
    """
    Get all the code snippets from the storage

    returns:
        dict

    example:
        getAllCodeDefinitions()
    example returns:
        {
            "add": Code: outputs['sum'] = a + b
                    Description: Add two numbers
                    Inputs: {'a': 'int', 'b': 'int'}
                    Outputs: {'sum': 'int'}
        }
    """
    return storage


import execute


def executeCodeDefinition(name: str, inputs: dict) -> dict:
    """
    Execute the code snippet from the storage
    name: str
        The name of the code snippet
    inputs: dict
        The inputs to the code snippet

    returns:
        dict

    example:
        executeCodeDefinition("add", {"a": 3, "b": 4})
    example returns:
        {"sum": 7}
    """
    code = getCodeDefinition(name).getSnippet()
    return execute.execute_code(code, inputs)
