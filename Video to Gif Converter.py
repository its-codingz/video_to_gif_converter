from moviepy.editor import VideoFileClip

videopath = input("Enter Video name with extension: ")

videoClip = VideoFileClip(videopath)

videoClip.write_gif("Output.gif")
