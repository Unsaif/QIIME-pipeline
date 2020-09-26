import pandas as pd
from requests import get
import re
import urllib.request
import sys
import os
import glob
import urllib
import time

####
#fetches single-end FASTQ files for each individual
#creates manifest file for qiime

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def download_fastq_automation_func(mysql, method):

    if method == 1 or method == 2:
        table = pd.read_csv(mysql, sep='\t', header = 0)
    if method == 3:
        table = pd.read_csv(mysql, header = 0)

    rows = []
    for accession in table["accession"]:
    
        url = 'https://www.ebi.ac.uk/ena/data/warehouse/filereport?accession=' + str(accession) + '&result=read_run&fields=fastq_ftp'
        response = get(url)
        result = re.search('\n(.*)\n', response.text)
        link = result.group(1)
        link = link.split("\t", 1)[1]
        rows.append([str(accession), os.getcwd() + '/' + str(accession) + '.fastq.gz'])
        remaining_download_tries = 15
    
        while remaining_download_tries > 0:

            try: 
                print("Downloading " + str(accession) + ".fastq.gz")
                print("HTTP request sent, awaiting response...")
                urllib.request.urlretrieve('ftp://' + link, os.getcwd() + '/' + str(accession) + '.fastq.gz', reporthook)
                print('\n')
            except:
                print('\n')
                print("Error downloading on trial no: " + str(16 - remaining_download_tries), "\n")
                remaining_download_tries = remaining_download_tries - 1  
                if remaining_download_tries == 0:
                    print("")
                    print("Please check connection status and try again")
                    sys.exit(1) 
                continue
            else:                
                break
                    
    manifest = pd.DataFrame(rows, columns=["sample-id", "absolute-filepath"]) 
    manifest.to_csv('manifest.tsv', sep="\t", index = False, header = True) 

    print("Download complete\n")
####

if __name__ == '__main__':
    path_txt = glob.glob("*.txt")
    path_csv = glob.glob("*.csv")
    path_tsv = glob.glob("*.tsv")

    if path_txt != []:
        path = path_txt
        op = 1
    if path_tsv != []:
        path = path_tsv
        op = 2
    if path_csv != []:
        path = path_csv  
        op = 3

    print("")
    print("Downloading files...", "\n")

    download_fastq_automation_func(path[0], op)
