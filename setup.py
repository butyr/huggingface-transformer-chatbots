import pathlib
import setuptools
import pkg_resources


with open("README.md", "r") as fh:
    long_description = fh.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name="python-transformer-chatbots-butyr",
    version="0.1.1",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    author="Leonid Butyrev",
    author_email="L.Butyrev@gmx.de",
    description="A collection of transformer based chatbots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/butyr/python-transformer-chatbot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=install_requires,
)
