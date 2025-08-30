from setuptools import setup, find_packages

setup(
    name="topsis-ridhamgarg",  # Must be unique on PyPI
    version="0.1.0",
    author="Ridham Garg",
    author_email="your_email@example.com",
    description="A Python package to implement TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis-ridhamgarg",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
