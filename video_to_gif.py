from moviepy import VideoFileClip
clip = VideoFileClip("my_video.mp4")
clip.write_gif("my_video.gif")