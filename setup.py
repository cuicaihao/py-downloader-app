import setuptools
from pathlib import Path
# with open("ReadMe.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="pySpeedDownloader",
    version="0.0.3",
    author="Chris Cui",
    author_email="",
    description="A powerful python based downloader module.",
    long_description=Path("ProjectDescription.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/cuicaihao/py-downloader-app",
    package_dir={"": "src"},
    project_urls={
    },
    packages=setuptools.find_packages(
        where="src", exclude=['test', 'target', 'build', 'main']),
    python_requires=">=3.7",

)
