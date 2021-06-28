# Python Downloader Demo

Build a powerful python based downloader app.

## Requirements

- python>=3.6
- requests
- tqdm
- retry
- hashlib
- multitasking
- signal
- gooey (GUI only / check the Github repo)
  
Example, create a `test.py` file with the following code to download the tensorflow git repo (about 76 MB) and the gitignore git repo (about 100KB)

The `run` function will return the md5 of the downloaded file for checking purposes.


```python
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

``` 

Bash command window output will be like:

```bash
❯ python test.py
Downloading tensorflow-master.zip...
Downloading: tensorflow-master.zip: 76029696it [00:21, 3457111.70it/s]                                                                   
dd8bfb4bab14f81742574bbe19aae8a6
Downloading gitignore-master.zip...
Downloading: gitignore-master.zip: 103808it [00:02, 35557.32it/s]                                                                        
8c0224157f4748eead1423530f52f401  
```

If you re-run the code again, it will ask you if you want to overwrite the existing files.
```bash
❯ python test.py
Downloading tensorflow-master.zip...
 ⛔️ download/tf/tensorflow-master.zip already exists, overwrite it?? (Y/N): N
dd8bfb4bab14f81742574bbe19aae8a6
Downloading gitignore-master.zip...
 ⛔️ download/gitignore/gitignore-master.zip already exists, overwrite it?? (Y/N): N
8c0224157f4748eead1423530f52f401
```