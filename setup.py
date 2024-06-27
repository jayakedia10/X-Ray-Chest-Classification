from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requirements(file_path : str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

name="Xray",
version="0.0.1",
author="Jaya Kedia",
author_email="jayakedia10@gmail.com",
#install_requires=[], #either we can fill requirements here manually or we can write a logic that'll fetch from requirements_dev.txt
#logic based
install_requires= get_requirements("requirements_dev.txt"),
packages=find_packages()

)