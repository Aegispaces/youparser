import os
from pytube import YouTube

def download_video():
    url = input("Enter URL: ")

    try:
        yt = YouTube(url)

        title = yt.title

        if title:
            print("Downloading video:", title)

            output_directory = input("Enter Output Directory: ")

            os.makedirs(output_directory, exist_ok=True)
            
            output_file = os.path.join(output_directory, title + ".mp4")

            yt.streams.get_highest_resolution().download(output_directory)

            print("Download completed! Saved at:", output_file)
        else:
            print("Unable to fetch video title.")
    except Exception as e:
        print("Error:", str(e))
        
splash_screen = r"""
_____.___.           __________                                   
\__  |   | ____  __ _\______   \_____ _______  ______ ___________ 
 /   |   |/  _ \|  |  \     ___/\__  \\_  __ \/  ___// __ \_  __ \
 \____   (  <_> )  |  /    |     / __ \|  | \/\___ \\  ___/|  | \/
 / ______|\____/|____/|____|    (____  /__|  /____  >\___  >__|   
 \/                                  \/           \/     \/       
"""

print(splash_screen)
download_video()
