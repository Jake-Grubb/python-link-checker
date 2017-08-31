# Python Link Checker
## Description
This program is a python script, used in conjunction with the W3C link-checker. It takes input in the form of a line-seperated list of URL's. It will then scan the relevant webpage of each URL for broken hyperlinks, and will log any instances of 404 errors into the output file.

## Requirements:
|Name | Link |
| ------------ | ------------|
| `Python 2.7.13`| https://www.python.org/downloads/release/python-2713/|
| `W3C link-checker`| https://github.com/w3c/link-checker|

**NOTE**: The program may work on other versions of Python 2, but these have not been fully tested and may have issues. Python 3 is **NOT** currently supported.

### Python Libraries
**This program uses Python 2**, and assumes it is installed with your operating system. It does not require any additional libraries to be installed.


## Running the program:
Begin by loading the `\data-files\links.txt`. Afterwards, make sure your terminal is in the `\program-files\` directory, and then type the terminal command `python link-checker.py`. The program does take some time, but the terminal will display your progress as the program runs. After completion, your results will be found in the file`\data-files\output.txt`

## GNU GENERAL PUBLIC LICENSE
