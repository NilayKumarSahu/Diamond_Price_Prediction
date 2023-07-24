from setuptools import find_packages,setup #for creating packages and finding packages in project
from typing import List #for getting packages in list

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]: #accepting file path in str and returning as list
    requirements=[]
    with open(file_path)as file_obj: #opening file to read
        requirements = file_obj.readlines() #reading line by line
        requirements=[req.replace("\n","")for req in requirements] # removing \n

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # removing -e .


    return requirements



setup(
    name='Regressor Project',
    version='0.0.1',
    author='Nilay',
    author_email='nilaykr27@gmail.com',
    install_requires=get_requirements('requirements.txt'), # giving requirements.txt file
    packages=find_packages()


)
