import sys
from multiprocessing.dummy import Pool as ThreadPool
from urllib.request import urlopen

# link to windows server ISO
# url = 'http://download.microsoft.com/download/6/2/A/62A76ABB-9990-4EFC-A4FE-C7D698DAEB96/9600.17050.WINBLUE_REFRESH.140317-1640_X64FRE_SERVER_EVAL_EN-US-IR3_SSS_X64FREE_EN-US_DV9.ISO'
# an image in .png
# url = 'https://www.guru99.com/images/Pythonnew/Python10.2.png'
num_threads = int(sys.argv[1]) # threads 
num_times = int(sys.argv[2]) # number of times
url = str(sys.argv[3]) # URL


def doneloadInChucksButDoNotSave(url=url):
    response = urlopen(url)
    CHUNK = 16 * 1024
    while True:
        chunk = response.read(CHUNK)
        if not chunk:
            break


listOfURLsToDownload = [url for i in range(num_threads)]

for i in range(num_times):
    pool = ThreadPool(num_threads)  # likely inefficient
    results = pool.map(doneloadInChucksButDoNotSave, listOfURLsToDownload)
    pool.close()
    pool.join()
    print('Itration done')

print("")
print("Done! Press any key to continue")
x = input()
