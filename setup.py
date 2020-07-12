import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hourglass",
    version="0.0.1",
    author="Raimi bin Karim",
    author_email="raimi.bkarim@gmail.com",
    description="Hourglass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remykarem/hourglass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
