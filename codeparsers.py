import ast


def load_internal_names(filename: "str") -> "set":
    with open(filename, 'r') as file:
        raw_text = file.read()
    return set(raw_text.strip().replace("'", "").replace(' ', '').split(','))


VALID_CODES_EXTENSIONS = ['.py', '.java', '.cpp']
PYTHON_INTERNAL_NAMES = load_internal_names("python_built_ins")
CPP_INTERNAL_NAMES = ""
JAVA_INTERNAL_NAMES = ""


class SourceCodeParser:
    def __init__(self, ext):
        self.ext = ext
        self.code_tree = None
        self.variables = []
        self.functions = []

    def analyse_source_code(self, code: "str"):
        pass


class PythonCodeParser(SourceCodeParser):
    def __init__(self):
        super(PythonCodeParser, self).__init__('.py')

    @staticmethod
    def double_underscore(name: "str") -> "bool":
        return name.startswith('__') and name.endswith('__')

    def analyse_source_code(self, source_code: "str") -> "dict":
        self.code_tree = ast.parse(source_code)
        self.variables = {node.id for node in ast.walk(self.code_tree) if isinstance(node, ast.Name)}
        self.functions = {node.name for node in ast.walk(self.code_tree) if isinstance(node, ast.FunctionDef)}
        self.variables = {name for name in self.variables - self.functions - PYTHON_INTERNAL_NAMES
                          if not self.double_underscore(name)}
        self.functions = {name for name in self.functions - PYTHON_INTERNAL_NAMES if not self.double_underscore(name)}

        return {'variables': self.variables, 'functions': self.functions}


class JavaCodeParser(SourceCodeParser):
    def __int__(self):
        super().__init__('.java')


class CppCodeParser(SourceCodeParser):
    def __int__(self):
        super().__init__('.cpp')


VALID_PARSERS = [PythonCodeParser, JavaCodeParser, CppCodeParser]


def create_code_parser(ext=" ", verb=True, noun=False, func=True, vrbl=False) -> "SourceCodeParser":
    parser = dict(zip(VALID_CODES_EXTENSIONS, VALID_PARSERS))[ext]
    return parser()
