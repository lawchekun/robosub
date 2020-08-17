import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

print(setuptools.find_packages())

setuptools.setup(
    name="perception", 
    version="0.0.1",
    author="Underwater Robotics at Berkeley",
    description="Our Perception code for our autonomous submarine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    requires=['opencv']
)
