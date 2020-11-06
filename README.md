# RevShellGen

One line reverse shell code for Linux based OS written in python

```
usage: shellgen.py [-h] [-i IPADDR] [-p PORT] [-t TARGET] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -i IPADDR, --ipaddr IPADDR
                        IP address
  -p PORT, --port PORT  Port number
  -t TARGET, --target TARGET
                        Type of script for Reverse shell
  -l, --list            List of scripts
```

## Installation

```
git clone https://github.com/arslanblcn/RevShellGen.git
cd RevShellGen
pip3 install -r requirements.txt
```

## Usage

```
Example usage: 
python3 shellgen.py -i 10.0.0.2 -p 1337 -t bash 
python3 shellgen.py -l 
```
