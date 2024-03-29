import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GuzikGUI",
    version="1.0.0",
    author="Alexandre Dumont",
    author_email="Alexandre.Dumont3@usherbrooke.ca",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2-3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy','matplotlib','SignalProcessing'],
    #packages=setuptools.find_packages(),
    packages=['GuzikGUI'],
    include_package_data=True,
    zip_safe=False
)
