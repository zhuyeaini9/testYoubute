from pytube import YouTube
from pytube import Playlist
import threading
import os.path
import socket

socket.setdefaulttimeout(30.0)


def downThread(video_link):
    while True:
        if down(video_link):
            break
        else:
            print('retry')


def down(video_link):
    try:
        y = YouTube(video_link)
        v = y.streams.filter(subtype='mp4', progressive=True, resolution='720p')
        if len(v) == 0:
            v = y.streams.get_highest_resolution()
        else:
            v = v.first()

        if os.path.isfile(save_path + v.default_filename) and os.stat(
                save_path + v.default_filename).st_size == v.filesize:
            return True

        v.download(output_path=save_path, skip_existing=False)
        print(v.default_filename)
        return True
    except:
        return False


url = "https://www.youtube.com/playlist?list=PLnHbptcieUBfQ-D4euoAK0MyN8D3AiGtH"
ytd = Playlist(url)
save_path = 'E:/code/testYoubute/youbute/' + ytd.title() + '/'
for video in ytd:
    t = threading.Thread(target=downThread, args=(video,))
    t.start()
