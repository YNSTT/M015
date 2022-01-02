#! /usr/bin/python3

banner = r'''
#########################################################################
#                                                                       #
#                                                                       #
#########################################################################
'''

import requests
import os

na = 'https://sky4k.ga/BERNAMA_SKY4K/assets/playlist.m3u8'
def grab(line):
    try:
        _id = line.split('/')[4]
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}').json()['qualities']['auto'][0]['url']
        m3u = s.get(response).text
        m3u = m3u.strip().split('\n')[-1]
    except:
        m3u = na
    print(m3u)

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
s = requests.Session()
with open('../dailymotion_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
