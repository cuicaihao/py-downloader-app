# Step 1: install the package from PyPi by
# pip install pySpeedDownloader

# Step 2: run this scripts
# python test.py

from pySpeedDownloader import pydownloader

url = "https://github.com/tensorflow/tensorflow/archive/refs/heads/master.zip"
file_name = "tensorflow-master.zip"
output_dir = "download/tf"

file_md5 = pydownloader.run(url, file_name, output_dir)
print(file_md5)

url = "https://github.com/github/gitignore/archive/refs/heads/master.zip"
file_name = "gitignore-master.zip"

output_dir = "download/gitignore"

file_md5 = pydownloader.run(url, file_name, output_dir)
print(file_md5)
