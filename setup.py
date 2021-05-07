import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plum",
    version="1.0.0",
    author="Andreas Backström",
    description="A simple build and management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mozzo1000/plum",
    project_urls={
        "Bug Tracker": "https://github.com/mozzo1000/plum/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=['plum'],
    entry_points={
        'console_scripts': ['plum=plum.main:main'],
    },
    python_requires=">=3.6",
)
