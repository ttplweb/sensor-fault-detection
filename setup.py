from setuptools import find_packages,setup
from typing import List


REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List['str']:
    """
    This function returns list of requirements
    """
    requirement_list:List['str'] = []
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement.replace("/n","") for requirement in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name="sensor",
    version="1.0",
    author="subhajit",
    author_email="subhajitbera16.93@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    )