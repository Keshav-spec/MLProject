from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    ''' 
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name='MLProject',
    version='0.0.1',
    author='Keshav',
    author_email='ks7190782@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn','scikit-learn','catboost','xgboost','Flask']

)