import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url_or_id):
    if "youtube.com" in url_or_id:
        if "v=" in url_or_id:
            return url_or_id.split("v=")[1].split("&")[0]
    if "youtu.be" in url_or_id:
        return url_or_id.split("/")[-1].split("?")[0]
    return url_or_id

if len(sys.argv) < 2:
    print("Usage: python3 get_youtube_transcript.py <video_url_or_id>")
    sys.exit(1)

video_id = get_video_id(sys.argv[1])

try:
    ytt = YouTubeTranscriptApi()
    transcript = ytt.fetch(video_id)
    for entry in transcript:
        print(entry.text)
except Exception as e:
    print(f"Error fetching transcript: {e}")
