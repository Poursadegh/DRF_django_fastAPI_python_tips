# 1-pip install bandit


from bandit.core.checks import Issue
from bandit.core.test_set import TestSet
from bandit.core import manager


class DangerousFunctionCheck:
    def __init__(self):
        self.dangerous_functions = ['eval', 'exec']
        # other types of attach detection

        # self.dangerous_functions = ['eval', 'exec', 'os.system', 'subprocess.call', 'pickle.load']

    def run(self, tree, filename):
        for node in tree.body:
            if hasattr(node, 'func') and node.func.id in self.dangerous_functions:
                yield Issue(
                    severity='High',
                    confidence='High',
                    text=f'Use of dangerous function: {node.func.id}',
                    filename=filename,
                    lineno=node.lineno,
                    issue_type='DANGEROUS_FUNC'
                )


def create_check():
    return DangerousFunctionCheck()


import re


# if there is a hard coded password?
def run(self, tree, filename):
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and re.search(r'password', target.id, re.I):
                    yield Issue(
                        severity='High',
                        confidence='High',
                        text='Hardcoded password found',
                        filename=filename,
                        lineno=node.lineno,
                        issue_type='HARDCODED_PASSWORD'
                    )



#ووردیهای کاربر درست اعتبار سنجی میشن ؟
def run(self, tree, filename):
    # Check for functions that accept user input without validation
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            # Logic to check for input validation
            # If no validation, yield an issue


#not using https
            def run(self, tree, filename):
                # Check for HTTP usage
                if 'http://' in code:
                    yield Issue(
                        severity='High',
                        confidence='High',
                        text='Use of HTTP instead of HTTPS',
                        filename=filename,
                        lineno=line_number,
                        issue_type='HTTP_USED'
                    )