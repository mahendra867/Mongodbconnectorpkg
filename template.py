import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", # here the package name is mongodb_connect , actually we have mongodb code for conecting to mongodb database and iam going to write the code in such a way that so with single go iam can able to connect the mongodb database and thats going to my package which iam going to create over here in the below file mongo_crud.py
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/test_unit.py", # here in this file iam going to write all my test cases of unit testing and unit means individual component so we are testing the individual component, and in this unit.py iam going to write the unit testing code 
   "tests/integration/__init__.py",
   "tests/integration/test_int.py",# here inside this int.py file iam going to write all the testcases of integrating testing, and in this int.py iam going to write the integrating testing code 
   "init_setup.sh", # this init_setup.sh is shell script basically iam going to write the linux commands whatever iam running in the terminal individually so i will mention the linux commands in unified way inside this shellscript and then i can run this init_setup.sh file on top of the terminal , so instead of writing individual linux commands on top of the terminal , i will give all the linux commands inside this init_setup.sh file , by just 1 command we can execute this init_setup.sh file so which ever the linux commands we mention inside this init_setup.sh file those  all linux commands get executed   
   "requirements.txt",  # it is used for production enivronment , so iam going to mention the libraries which are used for production environment
   "requirements_dev.txt", # it used for local environemnt or developing environment , because in devloping environment testing is required, lets say iam developing a code or project or product so for that i need to test the product, and from the user side the testing is not required , so whatever the libraies and whatever testing we are going to use in requirements_dev.txt just used for development environment, so finally iam going to keep all the libraries which are required to developing the product of developing environment 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file