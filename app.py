#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Created on   :2021/06/03 00:46:04
@author      :Caihao (Chris) Cui
@file        :app.py
@content     :xxx xxx xxx
@version     :0.1.0 in DevOpt
@License :   (C)Copyright 2021 MIT
'''

# here put the import lib

from src.pySpeedDownloader.pydownloader import run

import os
import json
from gooey import Gooey, GooeyParser
import logging

logging.basicConfig(
    level=logging.INFO,
    # filename='output.log',
    filemode='w',
    datefmt='%Y/%m/%d %H:%M:%S',
    format='%(asctime)s-%(levelname)s - %(message)s')
# format='%(levelname)s-%(message)s')

logger = logging.getLogger(__name__)

W, H = (480, 540)


@Gooey(
    program_name="Py-Downloader APP",
    default_size=(W, H),
    advanced=True,
    required_cols=1,
    optional_cols=2,
    progress_regex=r"(\d+)%",
    tabbed_groups=True,
    # dump_build_config=True,   # Dump the JSON Gooey uses to configure itself
    # load_build_config=None,    # Loads a JSON Gooey-generated configuration
    # navigation="Tabbed",
    menu=[
        {
            "name":
            "File",
            "items": [
                {
                    "type": "AboutDialog",
                    "menuTitle": "About",
                    "name": "Py-Downloader APP",
                    "description": "Py-Downloader APP",
                    "version": "0.5.0",
                    "copyright": "2021",
                    "developer": "Chris.Cui"
                },
                {
                    "type":
                    "MessageDialog",
                    "menuTitle":
                    "Information",
                    "caption":
                    "Py-Downloader APP",
                    "message":
                    "This repo is built by Chris Cui.",
                },
            ],
        },
        {
            "name":
            "Help",
            "items": [{
                "type":
                "Link",
                "menuTitle":
                "Documentation",
                "url":
                "https://github.com/cuicaihao/py-downloader-app"
            }],
        },
    ],
)
def parse_args():
    """
    Use GooeyParser to build up the arguments we will use in our script
    Save the arguments in a default json file so that we can retrieve them
    every time we run the script.
    """
    # stored_args = {}
    # get the script name without the extension & use it to build up
    # the json filename
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.json".format(script_name)
    # Read in the prior arguments as a dictionary
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = json.load(data_file)
        # return stored_args

    settings_msg = "Py-Downloader APP"
    parser = GooeyParser(description=settings_msg)

    parser.add_argument('--version', '-v', action='version',
                        version='%(prog)s 0.5.0')

    parser.add_argument('url', type=str,  action="store", default="https://github.com/github/gitignore/archive/refs/heads/master.zip",
                        help="Download URL")
    parser.add_argument('file_name', type=str, action="store", default="gitignore-master.zip",
                        help="Name of the download file.")
    parser.add_argument(
        'output_dir', type=str,  action="store", default="./download", help="Download directory", widget="DirChooser",)

    args = parser.parse_args()
    # Store the values of the arguments so we have them next time we run
    with open(args_file, "w") as data_file:
        # Using vars(args) returns the data as a dictionary
        json.dump(vars(args), data_file)
    return args


if __name__ == "__main__":
    conf = parse_args()
    # Output Input Configurations
    for arg in vars(conf):
        logging.info("{}:{}".format(arg, getattr(conf, arg)))
    file_md5 = run(conf.url, conf.file_name, conf.output_dir, check=False)
    logging.info(f"{conf.file_name} MD5: {file_md5}")
    print("\r" * 3)
