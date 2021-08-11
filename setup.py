from setuptools import setup

setup(
    name='very-basic-auth',
    version='0.0.1',
    description='Very Basic auth for jupiter hub',
    packages=["very_basic_auth"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    py_modules=["very_basic_auth"],
    long_description_content_type="text/markdown",
    url="https://github.com/joe-gasewicz/basic-auth",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
    install_requires=[
        "jupyterhub",
    ]
)