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

## Command line

```bash
❯ python src/pydownloader.py -h
usage: pydownloader.py [-h] [--url URL] [--file_name FILE_NAME] [--output_dir OUTPUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Download URL
  --file_name FILE_NAME
                        Downloaded file name
  --output_dir OUTPUT_DIR
                        Download directory

```

For example, we want to download the github repo [gitignore](https://github.com/github/gitignore) with `url = 'https://github.com/github/gitignore/archive/refs/heads/master.zip'` to the `download` folder with file name `gitignore-master.zip`:

```bash
❯ python src/pydownloader.py # run this line with all default settings

Downloading gitignore-master.zip...
Parts Number: 1
Downloading: gitignore-master.zip: 102656it [00:00, 191178.15it/s]
File MD5 Check: 9b178f9e5e12eb7c98262fa6d12b0962 # You can use the MD5 to verify the download.
```

If the file is already there, you will be asked to overwrite the file or not.

```bash
❯ python src/pydownloader.py # run this line with all default settings

Downloading gitignore-master.zip...
 ⛔️ download/gitignore-master.zip already exists, overwrite it?? (Y/N): y # y means overwrite it.
Downloading: gitignore-master.zip: 102656it [00:00, 154025.74it/s]
File MD5 Check: 9b178f9e5e12eb7c98262fa6d12b0962
```

Feel free to download other link, for example, let's download Google [TensorFlow Repo](https://github.com/tensorflow/tensorflow), we can do:

```bash
❯ python src/pydownloader.py --url https://github.com/tensorflow/tensorflow/archive/refs/heads/master.zip --file_name tensorflow-master.zip --output_dir download

Downloading tensorflow-master.zip...
Downloading: tensorflow-master.zip: 74670208it [00:20, 3610045.55it/s]
File MD5 Check: dcaba2148e899a87d8add27ec50fb960

```

Then we can find the zip files in our `download` folder.

```bash
❯ tree download
download
├── gitignore-master.zip
└── tensorflow-master.zip

0 directories, 2 files
```
