from setuptools import find_packages,setup
requirements = []
x = '-e .'
def get_requirements(file_path:str):
    '''this function will return list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if x in requirements:
            requirements.remove(x)
    return list(requirements)


setup(
name="demo project",
version='0.0.1',
author='Anirnudha sutar',
author_email='sutaraniudha604@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')


)