from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc

cmdclass = {'build_sphinx': BuildDoc}

with open("README.md", 'r') as f:
    long_description = f.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()
name = 'Telegram-Planner-Bot'
version = '1.0.0'
setup(
    name=name,
    version=version,
    install_requires=required,
    author=['Starovoytov Fedor', 'Emil Mamedov', 'Daniil Nikolaev'],
    url="https://github.com/aladdin120/Telegram-Planner-Bot",
    packages=find_packages(),
    long_description=long_description,
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs')
        }},
)
