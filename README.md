# What is Fraudtect ?

[![Version](https://img.shields.io/badge/fraudtect-v1-brightgreen)]()
[![Version](https://img.shields.io/badge/leetname-jihyoppa-red)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/supportedOS-linux%20%7C%20Windows-important)]()

Fraudtect is a Open-source Python tool designed to detect scam websites by scanning their SSL certificates. It detects scam websites by 
establishes an SSL/TLS connection to the website and retrieves the certificate. 
It then examines the certificate details, such as the issuer, subject, valid from, and valid until dates. And compares the SSL certificate of the website being checked 
with the SSL certificate of a legitimate website provided by the user.


# Screenshot
<img src="https://raw.githubusercontent.com/jihyoppa/fraudtect/main/sample.png" width="100%"></img> 



## Getting Started
1. ```git clone https://github.com/jihyoppa/fraudtect.git```
2. ```cd fraudtect```
3. ```python run.py ```


##  :heavy_exclamation_mark: Requirements

- must install required modules
- colorama 
- prompt_toolkit
- tqdm
- time
- socket
- ssl

## How to install modules
 ```pip install (modules you want to install)```
