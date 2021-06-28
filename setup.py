import setuptools
from pathlib import Path
# with open("ReadMe.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="pySpeedDownloader",
    version="0.1.2",
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
    install_requires=[
        'tqdm>=4.40.0',
        'requests>=2.9.1',
        'multitasking>=0.0.8',
        'retry>=0.9.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
