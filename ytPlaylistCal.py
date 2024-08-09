import googleapiclient.discovery
import googleapiclient.errors
import datetime

# Replace with your own API key
API_KEY = 'YOUR_API_KEY'


def get_playlist_videos(api_key, playlist_id):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    request = youtube.playlistItems().list(
        part='contentDetails',
        maxResults=50,
        playlistId=playlist_id
    )

    videos = []
    while request:
        response = request.execute()
        videos.extend(response['items'])
        request = youtube.playlistItems().list_next(request, response)

    return videos


def get_video_durations(api_key, video_ids):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(
        part='contentDetails',
        id=','.join(video_ids)
    )

    response = request.execute()
    durations = []
    for video in response['items']:
        duration = video['contentDetails']['duration']
        durations.append(duration)

    return durations


def parse_duration(duration):
    return datetime.timedelta(
        seconds=int(datetime.timedelta().total_seconds(datetime.datetime.strptime(duration, 'PT%HH%MM%SS').time())))


def calculate_total_duration(api_key, playlist_id):
    videos = get_playlist_videos(api_key, playlist_id)
    video_ids = [video['contentDetails']['videoId'] for video in videos]

    durations = []
    for i in range(0, len(video_ids), 50):  # YouTube API allows up to 50 videos in one request
        durations.extend(get_video_durations(api_key, video_ids[i:i + 50]))

    total_duration = datetime.timedelta()
    for duration in durations:
        total_duration += parse_duration(duration)

    return total_duration


if __name__ == '__main__':
    playlist_id = input('Enter YouTube Playlist ID: ')
    total_duration = calculate_total_duration(API_KEY, playlist_id)
    print(f'Total Duration of Playlist: {total_duration}')
