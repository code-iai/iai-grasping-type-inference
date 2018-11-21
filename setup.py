import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grasping_type_inference",
    version="1.0.0",
    author="Sebastian Koralewski",
    author_email="seba@cs.uni-bremen.de",
    description="Utilizes a Markov Logic Network to infer the most probable grasping type for a defined object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/code-iai/iai-grasping-type-inference",
    packages=setuptools.find_packages(exclude=("test",)),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)