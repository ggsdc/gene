import setuptools

with open("README.rst") as fh:
    long_description = fh.read()

required = []
with open("requirements.txt", "r") as fh:
    required.append(fh.read().splitlines())

setuptools.setup(
    name="gene",
    version="0.0.0a1",
    author="Guillermo González-Santander",
    author_email="g.gsantanderdelacruz@gmail.com",
    description="Library and framework to work with genetic algorithms",
    long_description=long_description,
    url="https://github.com/ggsdc/gene",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=required,
)
