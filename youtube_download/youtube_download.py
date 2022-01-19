# YouTube download script

# This script uses youtube-dl. Installed using:
# conda install -c conda-forge youtube-dl


# https://research.google.com/audioset/ontology/engine_1.html
# https://research.google.com/audioset/ontology/heavy_engine_low_frequency.html
# https://research.google.com/audioset//dataset/heavy_engine_low_frequency.html
# https://research.google.com/audioset//eval/heavy_engine_low_frequency.html

from __future__ import unicode_literals
import youtube_dl
import os, glob

                                                            # List of URLs to download
                                                            # Note: the _NN suffix on the URLs, below, is not part of the video URL
                                                            #   I guess this is something used by Google
urls = ['https://www.youtube.com/watch?v=-0J9HfwJ08c_30',
        'https://www.youtube.com/watch?v=-0JqTq_4jaE_40',
        'https://www.youtube.com/watch?v=-0pZsnG1MAI_30',
        'https://www.youtube.com/watch?v=--46xGNV1H0_30',
        'https://www.youtube.com/watch?v=--aVt0_KbIs_30',
        'https://www.youtube.com/watch?v=--Dxk606LRQ_30',
        'https://www.youtube.com/watch?v=--uhc3sHpTM_30',
        'https://www.youtube.com/watch?v=-1bchAh0bCk_30',
        'https://www.youtube.com/watch?v=-1guPbH2s3Y_27',
        'https://www.youtube.com/watch?v=-1PpGe_fk6U_30',
        'https://www.youtube.com/watch?v=-1rEwDd-5fU_17',
        'https://www.youtube.com/watch?v=-2BgMUP1sec_50',
        'https://www.youtube.com/watch?v=-2GC25ao1Og_30',
        'https://www.youtube.com/watch?v=-2ksTQGTlLA_30',
        'https://www.youtube.com/watch?v=-2McDjUrwKQ_2',
        'https://www.youtube.com/watch?v=-38FOBoZ3-E_0']

        # 'https://www.youtube.com/watch?v=--65x-naOz0_30',     # - OVERLOADED

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False,                                     # Delete videos, just keep .wav files
    'outtmpl': 'downloads/%(id)s.%(ext)s'                   # Store in downloads folder, with filename equal to YouTube ID
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)


