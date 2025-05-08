#MediaFile Program
#Audio: MP3, WAV, FLAC, AAC.
#Video: MP4, AVI, MKV, MOV.




from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self,file_name,file_size):
        self.file_name = file_name
        self.file_size = file_size



    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Mp3(MediaFile):
    def __init__(self,file_name,file_size):
        super().__init__(file_name,file_size)
        self.mode="none"

    def setMode(self,mode):
        if mode.lower() in ["loop","shuffle"]:
            self.mode=mode.lower()

        else:
            self.mode="none"

    def play(self):
        print(f"Now playing: {self.file_name}.mp3")
        print(f"File Size:{self.file_size}MB")
        print(f"Mode is set to: {self.mode}")

    def pause(self):
        print(f"{self.file_name}.mp3 is currently paused.")
    def stop(self):
        print(f"{self.file_name}.mp3 is no longer playing.")


#Dito Maglagay ng subclass
class Mp4(MediaFile):
    def __init__(self, file_name, file_size, resolutionmp4):
        super().__init__(file_name, file_size)
        self.resolution = resolution
        self.playback_speed = 1.0
        
    def setSpeed(self, speed):
        if speed.replace('.', '', 1).isdigit():  # checks if it's a number, including decimal
            speed = float(speed)
            if speed > 0:
                self.playback_speed = speed
            else:
                print("Invalid speed. Using default (1.0x).")
        else:
            print("Invalid input. Using default (1.0x).")

    def play(self):
        print(f"Now playing: {self.file_name}.mp4")
        print(f"File Size: {self.file_size}MB")
        print(f"Resolution: {self.resolution}")
        print(f"Playback speed: {self.playback_speed}x")
        

    def pause(self):
        print(f"{self.file_name}.mp4 is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mp4 is no longer playing.")

#Dito Maglagay ng subclass
class Wav(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)
        self.bit_depth = 16

    def setBitDepth(self, depth):
        if depth in [16, 24, 32]:
            self.bit_depth = depth
        else:
            print("Unsupported bit depth. Using default 16-bit.")

    def play(self):
        print(f"Now playing: {self.file_name}.wav")
        print(f"File Size: {self.file_size}MB")
        print(f"Bit Depth: {self.bit_depth}-bit")

    def pause(self):
        print(f"{self.file_name}.wav is currently paused.")

    def stop(self):
        print(f"{self.file_name}.wav playback stopped.")


#Dito maglagay ng subclass
class Mov(MediaFile):
    def __init__(self, file_name, file_size, has_subtitles):
        super().__init__(file_name, file_size)
        self.frame_rate = 30
        self.has_subtitles = has_subtitles
        
    def setframe_rate(self, frame_rate):
        valid_frame_rates = [24, 30, 48, 60, 72]
        if frame_rate in valid_frame_rates:
            self.frame_rate = frame_rate
        else:
            print(f"Invalid frame rate. Setting to default (30 fps).")

    def play(self):
        print(f"Now playing: {self.file_name}.mov")
        print(f"File Size: {self.file_size}MB")
        print(f"Frame Rate: {self.frame_rate}fps")
        print(f"Subtitles Included: {'Yes' if self.has_subtitles else 'No'}")
        

    def pause(self):
        print(f"{self.file_name}.mov is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mov is no longer playing.")


#Main Program

print("="*59)
print("*"*59)
print()
print()
print(" [1]. MP3\n [2]. MP4\n [3]. WAV\n [4]. MOV\n")
print()


media_type=input("Select media type : ")
if media_type=="mp3":
    name=input("Enter the audio file name: ")
    size=input("Enter the file size (MB): ")
    mode=input("Set the playback mode (loop/shuffle/none): ")
    
#objects
    print()
    audio=Mp3(name,size)
    audio.setMode(mode)
    audio.play()
    audio.pause()
    audio.stop()
    
elif media_type=="mp4":
    name= input("Enter the video file name: ")
    size= input("Enter the file size (MB): ")
    resolution= input("Enter the resolution (Ex: 1080p, 720p): ")
    speed = input("Enter the playback speed (Ex: 0.50, 1.0, 2.0): ")

    print()
    video = Mp4(name, size, resolution)
    video.setSpeed(speed)
    video.play()
    video.pause()
    video.stop()
    
elif media_type=="wav":
    name = input("Enter the audio file name: ")
    size = input("Enter the file size (MB): ")
    depth = int(input("Enter the bit depth (16/24/32): "))
    
#objects
    print()
    audio = Wav(name, size)
    audio.setBitDepth(depth)
    audio.play()
    audio.pause()
    audio.stop()

elif media_type=="mov":
    name = input("Enter the video file name: ")
    size = input("Enter the file size (MB): ")
    frame_rate = input("Enter the frame rate (24, 30, 48, 60, 72): ")
    subtitle_input = input("Does the file have subtitles? (Yes/ No): ")
    has_subtitles = subtitle_input.strip().lower() == "yes"

#objects
    print()
    video = Mov(name, size, has_subtitles)
    video.setframe_rate(frame_rate)
    video.play()
    video.pause()
    video.stop()
    
#maglagay lang ng elif dito for your objects

else:
    print(f"Unsupported media type. Please select on the given options.")
