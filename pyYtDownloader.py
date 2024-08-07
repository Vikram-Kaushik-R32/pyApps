from pytube import YouTube
import os

# Function to download YouTube video
def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object with the URL
        yt = YouTube(url)

        # Print video details
        print(f"Title: {yt.title}")
        print(f"Number of views: {yt.views}")
        print(f"Length of video: {yt.length} seconds")
        print(f"Description: {yt.description}")

        # Get the highest resolution stream available
        ys = yt.streams.get_highest_resolution()

        # Start downloading
        print("Downloading...")
        ys.download(save_path)
        print("Download completed!!")

    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=BK5rwsVizpQ'

# Path where the video will be saved
save_path = './downloaded_videos'

# Ensure save path directory exists
os.makedirs(save_path, exist_ok=True)

# Call the function to download the video
download_youtube_video(video_url, save_path)
