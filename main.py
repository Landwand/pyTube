from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
from time import time
# plots
import matplotlib.pyplot as plt


#  %matplotlib inline
# image operation
# import cv2 - python 2 only

#######


def select_stream():
    while True:
        select_stream = input("Choose the iTag Stream: ")
        confirm = input("Confirm the above stream ")
        if confirm == "y" or confirm == "Y":
            try:
                select_stream = int(select_stream)
                return select_stream
            except:
                print("Invalid - try again")


def download_it(itag):
    file_path = "./downloads/"
    filename = input('choose a file name: \n')
    print("Downloading ", itag)
    # stream = yt.streams.get_by_itag(itag)
    # stream.download()
    completed = yt.streams.get_by_itag(itag).download(output_path=file_path, filename_prefix=filename)
    return completed


######


yt = YouTube('https://www.youtube.com/watch?v=fUalcwgEYNU')
filtered = yt.streams.filter(file_extension="mp4", adaptive=True)
# audio & video separate, but HQ.
# filtered = yt.streams.filter(file_extension="mp4")
# filtered = yt.streams.filter(progressive=True) #audio & video, but lower Q

for i in filtered:
    print(i)

# stream = yt.streams.get_by_itag(select_stream)


itag = select_stream()
result = download_it(itag)
print(result, " Download Completed. ")

"""

    def _report_progress(title, curr, total, full_progbar):
        frac = curr / total
        filled_progbar = round(frac * full_progbar)
        print('\r', title + '#' * filled_progbar + '-' * (full_progbar - filled_progbar), '[{:>7.2%}]'.format(frac),
              end='')
              
"""


