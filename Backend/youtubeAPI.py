from apiclient.discovery import build

videoId = '5kmyOfvucp8'
YOUTUBE_API_KEY = 'Your_Youtube_Api_Key'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
videos_response = youtube.videos().list(
    part='snippet,statistics',
    id='{},'.format(videoId)
).execute()
# snippet
snippetInfo = videos_response["items"][0]["snippet"]
# statistics
statisticsInfo = videos_response["items"][0]["statistics"]
# 動画タイトル
title = snippetInfo['title']
# チャンネル名
channeltitle = snippetInfo['channelTitle']
# 再生回数
viewCount = statisticsInfo['viewCount']
# いいねの数
likeCount = statisticsInfo['likeCount']
print(channeltitle)
print(title)
print('再生回数：'+viewCount)
print('いいね数：'+likeCount)