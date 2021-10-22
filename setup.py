from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="rockman",
    version="0.0.1",
    description="A handy package for rocket simulation",
    author="shohei",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "rockman=rockman.eng:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ]
)
