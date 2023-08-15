from setuptools import find_packages, setup  # Importing required functions for package setup
from typing import List  # Importing List from the typing module for type hinting

HYPHEN_E_DOT = '-e .'  # A constant representing a string to possibly remove from requirements

def get_requirements(file_path:str)->List[str]:
    '''
    Retrieves a list of requirements from the specified file path.

    This function reads the requirements from the given file, typically 
    "requirements.txt", and returns them as a list of strings, removing
    any newline characters and specific unwanted strings.

    :param file_path: A string representing the path to the requirements file.
    :return: A list of strings representing the requirements.
    '''
    requirements = []  # Initializing blank requirements list

    # Opening the file in read mode
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Reading all the lines from the file
        requirements = [req.replace("\n", "") for req in requirements]  # Removing newline characters from each requirement
        
        # Remove the hyphen_e_dot string if present in requirements
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements  # Returning the list of requirements

# Setting up the package information
setup(
    name='gemstonepricepredictionproject',  # Package name
    version='0.0.1',  # Package version
    author='Ashish Roy',  # Author's name
    author_email='ashishgithubprojects@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=get_requirements('requirements.txt')  # Getting the requirements from the specified file
)
