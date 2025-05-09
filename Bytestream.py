#Clearing Screen
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        
from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self,file_name,file_size, volume):
        self.file_name = file_name
        self.file_size = file_size
        self.volume = volume

#Methods
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass

#Subclass
class Mp3(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size, volume)
        self.mode = "none"

    def setMode(self,mode):
        if mode.lower() in ["loop","shuffle"]:
            self.mode = mode.lower()

        else:
            self.mode="none"

    def play(self):
        print(f"\033[1mNow playing\033[0m: {self.file_name}.mp3")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mMode is set\033[0m: {self.mode}")
        print(f"\033[1mVolume\033[0m: {volume}%")

    def pause(self):
        print(f"\n{self.file_name}.mp3 is currently paused.")
    def stop(self):
        print(f"{self.file_name}.mp3 is no longer playing.")

#Subclass
class Mp4(MediaFile):
    def __init__(self, file_name, file_size, resolutionmp4):
        super().__init__(file_name, file_size, volume)
        self.resolution = resolutionmp4
        self.playback_speed = 1.0
        
    def setSpeed(self, speed):
        if speed.replace('.', '', 1).isdigit():  
            speed = float(speed)
            if speed > 0:
                self.playback_speed = speed
            else:
                print("Invalid speed. Using default (1.0x).")
        else:
            print("Invalid input. Using default (1.0x).")

    def play(self):
        print(f"\033[1mNow playing\033[0m: {self.file_name}.mp4")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mResolution\033[0m: {self.resolution}p")
        print(f"\033[1mPlayback speed\033[0m: {self.playback_speed}x")
        print(f"\033[1mVolume\033[0m: {volume}%")
        
    def pause(self):
        print(f"\n{self.file_name}.mp4 is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mp4 is no longer playing.")

#Subclass
class Wav(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size, volume)
        self.bit_depth = 16

    def setBitDepth(self, depth):
        if depth in [16, 24, 32]:
            self.bit_depth = depth
        else:
            print("Unsupported bit depth. Using default 16-bit.")

    def play(self):
        print(f"\033[1mNow playing\033[0m: {self.file_name}.wav")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mBit Depth\033[0m: {self.bit_depth}-bit")
        print(f"\033[1mVolume\033[0m: {volume}%")

    def pause(self):
        print(f"\n{self.file_name}.wav is currently paused.")

    def stop(self):
        print(f"{self.file_name}.wav playback stopped.")

#Subclass
class Mov(MediaFile):
    def __init__(self, file_name, file_size, has_subtitles):
        super().__init__(file_name, file_size, volume)
        self.frame_rate = 30
        self.has_subtitles = has_subtitles
        
    def setframe_rate(self, frame_rate):
        valid_frame_rates = [24, 30, 48, 60, 72]
        if frame_rate in valid_frame_rates:
            self.frame_rate = frame_rate
        else:
            print(f"Invalid frame rate. Setting to default (30 fps).")

    def play(self):
        print(f"\033[1mNow playing\033[0m: {self.file_name}.mov")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mFrame Rate\033[0m: {self.frame_rate}fps")
        print(f"\033[1mSubtitles Included\033[0m: {'Yes' if self.has_subtitles else 'No'}")
        print(f"\033[1mVolume\033[0m: {volume}%")
        
    def pause(self):
        print(f"\n{self.file_name}.mov is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mov is no longer playing.")


#Main Program
while True:
    clear_screen()
    print("="*59)
    print(r"""
$$$$$$$\              $$\                                       
$$  __$$\             $$ |                                      
$$ |  $$ |$$\   $$\ $$$$$$\    $$$$$$\                          
$$$$$$$\ |$$ |  $$ |\_$$  _|  $$  __$$\                         
$$  __$$\ $$ |  $$ |  $$ |    $$$$$$$$ |                        
$$ |  $$ |$$ |  $$ |  $$ |$$\ $$   ____|                        
$$$$$$$  |\$$$$$$$ |  \$$$$  |\$$$$$$$\                         
\_______/  \____$$ |   \____/  \_______|                        
          $$\   $$ |                                            
          \$$$$$$  |                                            
           \______/                                             
 $$$$$$\    $$\                                                 
$$  __$$\   $$ |                                                
$$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\$$$$\  
\$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\  \____$$\ $$  _$$  _$$\ 
 \____$$\   $$ |    $$ |  \__|$$$$$$$$ | $$$$$$$ |$$ / $$ / $$ |
$$\   $$ |  $$ |$$\ $$ |      $$   ____|$$  __$$ |$$ | $$ | $$ |
\$$$$$$  |  \$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |$$ | $$ | $$ |
 \______/    \____/ \__|       \_______| \_______|\__| \__| \__|
""")
    print("="*59)
    print("\033[1mMedia Files:\033[0m")
    print("="*59)
    print(" [1] Mp3\n [2] Mp4\n [3] Wav\n [4] MOV\n [5] Exit\n")
    media_type=input("Select media type : ")
    clear_screen()

    if media_type == "1":
        name = input("Enter the audio file name: ")
        
        while True:
            try:
                size = float(input("Enter the file size (MB): "))
                if size <= 0:
                    raise ValueError("File size must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid file size.")
                
        mode = input("Set the playback mode (loop/shuffle/none): ")
        
        while True:
            try:
                volume = int(input("Enter volume (1-100): "))
                if volume < 1 or volume > 100:
                    raise ValueError("Volume must be between 1 and 100.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid volume.")
                
        clear_screen()
        audio = Mp3(name, size)
        audio.setMode(mode)
        audio.play()
        audio.pause()
        audio.stop()

    elif media_type == "2":
        name = input("Enter the video file name: ")
        
        while True:
            try:
                size = float(input("Enter the file size (MB): "))
                if size <= 0:
                    raise ValueError("File size must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid file size.")
                
        while True:
            try:
                resolution = int(input("Enter the resolution (Ex: 1080, 720): "))
                if size <= 0:
                    raise ValueError("File size must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid resolution.")
                
        speed = input("Enter the playback speed (Ex: 0.50, 1.0, 2.0): ")
        
        while True:
            try:
                volume = int(input("Enter volume (1-100): "))
                if volume < 1 or volume > 100:
                    raise ValueError("Volume must be between 1 and 100.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid volume.")
                
        clear_screen()
        video = Mp4(name, size, resolution)
        video.setSpeed(speed)
        video.play()
        video.pause()
        video.stop()

    elif media_type == "3":
        name = input("Enter the audio file name: ")
        
        while True:
            try:
                size = float(input("Enter the file size (MB): "))
                if size <= 0:
                    raise ValueError("File size must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid file size.")
                
        depth = input("Enter the bit depth (16/24/32): ")
        
        while True:
            try:
                volume = int(input("Enter volume (1-100): "))
                if volume < 1 or volume > 100:
                    raise ValueError("Volume must be between 1 and 100.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid volume.")
                
        clear_screen()
        audio = Wav(name, size)
        audio.setBitDepth(depth)
        audio.play()
        audio.pause()
        audio.stop()

    elif media_type == "4":
        name = input("Enter the video file name: ")
        
        while True:
            try:
                size = float(input("Enter the file size (MB): "))
                if size <= 0:
                    raise ValueError("File size must be greater than 0.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid file size.")
                
        frame_rate = input("Enter the frame rate (24, 30, 48, 60, 72): ")
        subtitle_input = input("Does the file have subtitles? (Yes/No): ")
        has_subtitles = subtitle_input.strip().lower() == "yes"
        
        while True:
            try:
                volume = int(input("Enter volume (1-100): "))
                if volume < 1 or volume > 100:
                    raise ValueError("Volume must be between 1 and 100.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid volume.")
        
        clear_screen()
        video = Mov(name, size, has_subtitles)
        video.setframe_rate(frame_rate)
        video.play()
        video.pause()
        video.stop()

    elif media_type == "5":
        print("Thank you from Group 6.")
        break

    else:
        print("Unsupported media type. Please select one of the given options.")

    input("\nPress enter to return to main menu.")
