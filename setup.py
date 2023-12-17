from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e .' #this is used so that it can trigger setup.py file and simulatnously it can run install requirements and build the ml package using setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements= file_obj.read()
        requirements = [requirement.strip() for requirement in requirements.split("\n")]
        #or requirements  = [req.replace("\n", "") for req in requirements]
        
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    
    return requirements


#Meta data information 
setup(
name = 'ML_project',
version = '0.0.1',
author = 'Aishwarya',
author_email = 'aish.bhanage0412@gmail.com',
packages= find_packages(),
install_requires= get_requirements("requirements.txt"),
)