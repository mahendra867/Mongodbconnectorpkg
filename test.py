from setuptools import setup, find_packages # from setuptool module iam going to import setup method or fucntion which we have defined inside this setuptool module and also find_package , and this setup methode we can get this code in setup.p
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]: # i have defined 1 function named as  get_requirement and which that fucntion is collecting all the requirements_dev.txt file content in the form of list 
    requirements = [] # here i have initilized the empty list
    with open(file_path) as f: # and iam going to open the file which is requirements_dev.txt
        requirements=f.readlines() # iam going to read the requirements_dev.txt
        requirements=[req.replace("\n","")for req in requirements] # and after reading the requirements_dev.txt file content in sequence iam going to save in requirements and which is line of code is list comprehension

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # and here we are going to remove the -e  from the list which has requirements varaible 
    return requirements # and finally we are going to return the requirements varaible which contains the requirements_dev.txt file content

print(get_requirement("./requirements.txt"))