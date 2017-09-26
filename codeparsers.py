def load_words_from_file(filename: "str") -> "set":
    with open(filename, 'r') as file:
        raw_text = file.read()
    return set(raw_text.strip().replace("'", "").replace(' ', '').split(','))


VALID_CODES_EXTENSIONS = ['.py', '.java']
PYTHON_INTERNAL_NAMES = load_words_from_file("python_built_ins")  # list of names to be treated as Python internal
JAVA_INTERNAL_NAMES = ""


class SourceCodeParser:
    def __init__(self, ext):
        self.ext = ext
        self.code_tree = None
        self.variables = []
        self.functions = []

    def analyse_source_code(self, code: "str") -> "dict":
        return {'variables': self.variables, 'functions': self.functions}


class PythonCodeParser(SourceCodeParser):
    def __init__(self):
        super(PythonCodeParser, self).__init__('.py')

    @staticmethod
    def double_underscore(name: "str") -> "bool":
        return name.startswith('__') and name.endswith('__')

    def analyse_source_code(self, source_code: "str") -> "dict":
        import ast
        self.code_tree = ast.parse(source_code)
        self.variables = {node.id.lower() for node in ast.walk(self.code_tree) if isinstance(node, ast.Name)}
        self.functions = {node.name.lower() for node in ast.walk(self.code_tree) if isinstance(node, ast.FunctionDef)}
        self.variables = {name for name in self.variables - self.functions - PYTHON_INTERNAL_NAMES
                          if (len(name) > 1) and not self.double_underscore(name)}
        self.functions = {name for name in self.functions - PYTHON_INTERNAL_NAMES
                          if (len(name) > 1) and not self.double_underscore(name)}

        return {'variables': self.variables, 'functions': self.functions}


class JavaCodeParser(SourceCodeParser):
    def __int__(self):
        super().__init__('.java')


VALID_PARSERS = [PythonCodeParser, JavaCodeParser]


def create_code_parser(ext="") -> "SourceCodeParser":
    parser = dict(zip(VALID_CODES_EXTENSIONS, VALID_PARSERS))[ext]
    return parser()
