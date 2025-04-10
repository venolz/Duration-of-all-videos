import os
import moviepy.editor as mp

def get_total_video_duration(folder_path):
    total_duration = 0 

    # recursively traversing all files and folders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # checking if the file is a video
            if file.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".flv")):
                try:
                    # we upload the video and get its duration
                    video = mp.VideoFileClip(file_path)
                    total_duration += video.duration  # adding the duration
                    video.close()
                except Exception as e:
                    print(f"File processing error {file_path}: {e}")

    # returning the total duration
    return total_duration

if __name__ == "__main__":

    folder_path = input("Enter the path to the video folder: ")
    
    if not os.path.isdir(folder_path):
        print("The specified path is not a folder!")
    else:
        total_duration = get_total_video_duration(folder_path)

        # converting the duration to hours, minutes, and seconds
        hours = int(total_duration // 3600)
        minutes = int((total_duration % 3600) // 60)
        seconds = int(total_duration % 60)

        print(f"Total video duration: {hours} h {minutes} min {seconds} sec")