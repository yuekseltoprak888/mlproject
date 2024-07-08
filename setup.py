from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return a list of requirments which are in the requirements.txt
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    description="A machine learning project",
    author="Yüksel Toprak",
    author_email="yuekseltoprak@findme.com",
    url="https://github.com/yuksel/mlproject",
    license="MIT",
    packages=find_packages(),  # Automatically find and include all packages in the directory
    install_requires=get_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'mlproject=mlproject.cli:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
)
