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
  
Example, download the tensorflow git repo (about 76 MB)

```python
from pySpeedDownloader import pydownloader

url= "https://github.com/tensorflow/tensorflow/archive/refs/heads/master.zip"
file_name="tensorflow-master.zip" 
output_dir="download"
file_md5 = pydownloader.run(url, file_name, output_dir, check=True)

``` 
Bash command window output
```bash
>>> from pySpeedDownloader import pydownloader
>>> url= "https://github.com/tensorflow/tensorflow/archive/refs/heads/master.zip"
>>> file_name="tensorflow-master.zip" 
>>> output_dir="download"
>>> file_md5 = pydownloader.run(url, file_name, output_dir, check=True)
Downloading tensorflow-master.zip...
 ⛔️ download/tensorflow-master.zip already exists, overwrite it?? (Y/N): Y
Downloading: tensorflow-master.zip: 76027904it [00:21, 3604606.75it/s]                                                                         
```