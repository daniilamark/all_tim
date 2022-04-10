# pip install pytube
import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=xuaBtJpHN7k')

fn = yt.title
print(fn)

video_author = yt.author
print(video_author)

video_id = yt.video_id
print(video_id)


