import json

from setuptools import find_packages, setup

INFO = json.load(open("package.json"))
INFO["long_description"] = open("README.md").read()

setup(
    url=INFO["url"],
    name=INFO["name"],
    author=INFO["author"],
    license=INFO["license"],
    version=INFO["version"],
    keywords=INFO["keywords"],
    include_package_data=True,
    author_email=INFO["email"],
    description=INFO["description"],
    long_description=INFO["long_description"],
    packages=find_packages(exclude=["env", "tests"]),
    install_requires=[],
    project_urls={"Source Code": "https://github.com/alexpdev/torrentfileQt"},
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": "visualsort = visualsort:main"
    },
    classifiers=[],
)
