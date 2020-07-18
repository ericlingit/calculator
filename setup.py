import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculator",
    version="0.0.1",
    author="ericlingit",
    author_email="ericlingit@users.noreply.github.com",
    description="An example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericlingit/calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
