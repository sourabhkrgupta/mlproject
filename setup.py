from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path: str) -> List[str]:
    with open(file_path, encoding='utf-8') as file:
        requirements = [
            line.strip() for line in file
            if line.strip() and not line.startswith('-e')
        ]
    return requirements




setup(
    name='mlproject',
    version='1.0.0',
    author='sourabh',
    author_email='sourabhkrgupta55@gmail.com',
    packages= find_packages(),
    install_requires=reqs
)