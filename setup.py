from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author="Sarika Kamble",
    author_email='sarikamble@yahoo.com',
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"
    ],
    packages=find_packages()  # Fixed the typo here
)
