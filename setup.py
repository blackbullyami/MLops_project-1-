from setuptools import find_packages,setup
from typing import List
x='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if x in requirements:
        requirements.remove(x)
    return requirements

setup(
    name="Ml_project",
    version="1.0.0.1",
    author="Mayank Rawat",
    author_email='mayank.rawat9921@gmail.com',
    packages=find_packages(),
    install=get_requirements('requirements.txt')

)

        