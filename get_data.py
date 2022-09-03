from googleapiclient.discovery import build
import config
import json

class Channel:
    def __init__(self):
        self.API_KEY = config.MY_API_TOKEN
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3'
        self.youtube = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.API_KEY
        )

    def get_channel(self, channel_name):
        search_response = self.youtube.search().list(
            q=channel_name,
            part='id,snippet',
            maxResults=50
        ).execute()

        channels = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#channel':
                channels.append('%s (%s)' % (search_result['snippet']['title'],
                                            search_result['id']['channelId']))

        # for channel in channels:
        #     print(channel)
        return channels
        
    def get_preserve_video(self, channel_id):
        '''
        Get the video that is preserved in the channel
        '''
        search_response = self.youtube.search().list(
            channelId=channel_id,
            part='snippet',
            order='date',
        ).execute()
        # print(json.dumps(search_response.get('items', []), indent=2))

        videos = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                if search_result['snippet']['liveBroadcastContent'] == 'upcoming':
                    videos.append('%s (%s) %s' % (search_result['snippet']['title'],
                                                search_result['id']['videoId'],
                                                search_result['snippet']['publishedAt']))
        
        # for video in videos:
        #     print(video)
        return videos