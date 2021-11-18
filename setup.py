from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='escpos-gen',
    version='0.0.1',
    description='Generator of printable binary files with helper methods based on ESC/POS protocol',
    py_modules=["escpos-gen"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fercorbar/escpos-gen',
    author='Fernando Córdova',
    author_email='fernando@cbin.mx',
    
)