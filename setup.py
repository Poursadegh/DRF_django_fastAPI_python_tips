from setuptools import setup

setup(
    name='my_bandit_plugin',
    version='0.1.0',
    description='A custom Bandit plugin to check for dangerous functions',
    packages=['my_bandit_plugin'],
    entry_points={
        'bandit': [
            'dangerous_function_check = my_plugin:create_check',
        ],
    },
)
