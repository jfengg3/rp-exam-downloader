# RP Exam Downloader
Executable or script to download past years paper

## Description 
##### Inspired by [NUS Exams Downloader](https://github.com/nusmodifications/nus-exams-downloader)

RP Exam Downloader is a lightweight software designed to ease the process of downloading papers from the intranet.

Students can download past years paper with their **RP login** credentials and **module** code.

![Imgur](https://i.imgur.com/jiJPNB0.png)


## Usage

*Requires connection to RP's VPN.

#### Executable

```Simply run the executable (eg. downloader-gui.exe)```

#### Script

```$ python downloader-gui.py```

## Compile
##### Applicable for those who wants to make changes and compile manually

**Pre-requisites**
```
  1. Python 3.x.x (3.5/3.6 is recommended)
  2. requests_nltm (Use to authorize and access the intranet)
  3. urllib.request (An extension for url opening)
  4. BeautifulSoup (Web-parse, pull data out of HTML/XML)
  
    - External modules can be installed easily using pip (eg. pip install requests_nltm)
```

## Notes
My projects will always be open-sourced, feel free to contribute and give feedback on improving the software.
As of now, it supports only Windows. If anyone wants to compile it for Mac OS X, go ahead and leave me a message so I can upload it with the Windows version.

## Credits
- Pang Jing Jie
