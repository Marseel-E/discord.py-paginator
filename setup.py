import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="discord.py-paginator",
    version="1.5.0",
    author="Marseel Eeso",
    author_email="marseeleeso@gmail.com",
    description="A button & interactions pagination template for discord bots coded in discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marseel-E/discord.py-paginator",
    project_urls={
        "Bug Tracker": "https://github.com/Marseel-E/discord.py-paginator/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
