## SAFARICOM MPESA STATEMENT EXTRACTOR FOR PERSONAL ACCOUNTING USES
This repository is meant to be used as a simpler way to sort and extract daily transactions done on mpesa for easier accounting into a finance tracker of one's choice.
The idea is to prevent manual reading and recording of mpesa messages from one's phone, which is quite cumbersome and takes up alot of time. 

(Especially if sortingacross several days)

### PREREQUISITES
1. Have python3.8 or higher installed in your system
2. Request and download the MPESA statement document for the duration you want to analyse
3. Check your phone messages for the safaricom Mpesa-statement pdf password (this should be confidential)

### SETUP
Run
```console
pip install -r requirements.txt
```

Ensure your computer has java installed, tabula-py library requires it. 
For Ubuntu 20.04 and above, follow these instructions:

```console
sudo apt update
```

```console
sudo apt install default-jre
```

```console
sudo apt install default-jdk 
```

For windows 10 and above:
Follow instructions in the link provided: https://phoenixnap.com/kb/install-java-windows 


## RUN program
The file is run from main.py, and requires 2 inputs from you.
<input1> : Location of the mpesa pdf file. The code is currently set to pick a location relative to this repo directory, so pls copy the pdf into this repo for best results.
<input2> : PDF file password

For example:

```console
python main.py mpesa-statement.py 000111
```