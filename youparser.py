import os
from pytube import YouTube

def download_video():
    url = input("Enter URL: ")

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the video title
        title = yt.title

        if title:
            print("Downloading video:", title)

            # Prompt the user to enter the output directory
            output_directory = input("Enter Output Directory: ")

            # Create the output directory if it doesn't exist
            os.makedirs(output_directory, exist_ok=True)

            # Set the output path for the downloaded video
            output_file = os.path.join(output_directory, title + ".mp4")

            # Download the video
            yt.streams.get_highest_resolution().download(output_directory)

            print("Download completed! Saved at:", output_file)
        else:
            print("Unable to fetch video title.")
    except Exception as e:
        print("Error:", str(e))

# ASCII splash screen
splash_screen = r"""
_____.___.           __________                                   
\__  |   | ____  __ _\______   \_____ _______  ______ ___________ 
 /   |   |/  _ \|  |  \     ___/\__  \\_  __ \/  ___// __ \_  __ \
 \____   (  <_> )  |  /    |     / __ \|  | \/\___ \\  ___/|  | \/
 / ______|\____/|____/|____|    (____  /__|  /____  >\___  >__|   
 \/                                  \/           \/     \/       
"""

print(splash_screen)

# Call the download_video function
download_video()