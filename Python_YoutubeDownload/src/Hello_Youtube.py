from pytube import YouTube
from pytube import Playlist
import pytube.exceptions

url_list = []
order = 1
with open('video.txt') as file:
 for line in file:
  url_list.append(line.rstrip())


for video_url in url_list:
 # Normal Download
 try:
  print(order , YouTube(video_url).streams.filter(res='720p').first().title) # Download Video
  YouTube(video_url).streams.filter(res='720p').first().download()
 # Exception
 except pytube.exceptions.ExtractError:  # skip ExtractError videos
  print(order , ' ExtractError')
 except pytube.exceptions.HTMLParseError:  # skip HTML Parse Error
  print(order, ' HTMLParseError')
 except pytube.exceptions.LiveStreamError:  # skip LiveStreamError videos
  print(order , ' LiveStreamError')
 except pytube.exceptions.MembersOnly:  # skip MembersOnly videos
  print(order , ' MembersOnly')
 except pytube.exceptions.RecordingUnavailable:  # skip RecordingUnavailable videos
  print(order , ' RecordingUnavailable')
 except pytube.exceptions.RegexMatchError:  # skip RegexMatchError videos
  print(order , ' RegexMatchError')
 except pytube.exceptions.VideoPrivate:  # skip private videos
  print(order , ' VideoPrivate')
 except pytube.exceptions.VideoRegionBlocked:  # skip VideoRegionBlocked videos
  print(order , ' VideoRegionBlocked')
 except pytube.exceptions.VideoUnavailable:  # skip VideoUnavailable videos
  print(order , ' VideoUnavailable')
 order = order + 1

