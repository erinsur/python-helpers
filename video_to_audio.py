from moviepy import VideoFileClip


def extract_audio(video_path, audio_path="output.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path

audio_path = extract_audio("vid.MP4")
