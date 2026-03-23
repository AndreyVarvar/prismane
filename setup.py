from setuptools import setup, find_packages

setup(
    name="prismane",
    version="0.1.0",
    author="AndreyVarvar",
    description="A pygame engine used to accelerate the development of pygame programs.",
    packages=find_packages(),
    install_requires=[
        "pygame-ce>=2.5.6"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13',
)
