import os
import time

mp3_files = []
wav_files = []
mp4_files = []
mov_files = []
png_files = []
jpg_files = []

def invalid_input():
        clear_screen()
        print("\033[1mInvalid input. Please try again.\033[0m")
        input("\nPress Enter to return to main menu...")
        clear_screen()
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def byte_stream():
    clear_screen()
    print("="*59)
    print("\033[1;95m" + r"""
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
""" + "\033[0m")
    print("="*59)
    time.sleep(3)
    clear_screen()
    
def main_screen():
    print("="*59)
    print("\033[1mMedia Files:\033[0m")
    print("="*59)
    print("[1] Audio")
    print("[2] Video")
    print("[3] Image")
    print("[4] Exit\n")
    
def play_music_menu():
    while True:
        clear_screen()
        print("\033[1mPlay Music\033[0m")
        print("[1] Play MP3")
        print("[2] Play WAV")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            if not mp3_files:
                print("\033[1mNo MP3 files to play.\033[0m")
            else:
                clear_screen()
                print("\033[1mMP3 files\033[0m\n")
                for i, mp3 in enumerate(mp3_files):
                    print(f"[{i}] {mp3.file_name}.mp3\n")
                idx = int(input("Select file index to play: "))
                clear_screen()
                mode = input("Set the playback mode (loop/shuffle/none): ")
                mp3.setMode(mode)
                clear_screen()
                mp3_files[idx].play()
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_screen()
            if not wav_files:
                print("\033[1mNo WAV files to play.\033[0m")
            else:
                clear_screen()
                for i, wav in enumerate(wav_files):
                    print(f"[{i}] {wav.file_name}.mov\n")
                idx = int(input("Select file index to play: "))
                wav_files[idx].play()
            input("\nPress Enter to continue...")

        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()

def play_video_menu():
    while True:
        clear_screen()
        print("\033[1mPlay Video\033[0m")
        print("[1] Play MP4")
        print("[2] Play MOV")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            if not mp4_files:
                print("\033[1mNo MP4 files to play.\033[0m")
            else:
                clear_screen()
                print("\033[1mMP4 files\033[0m\n")
                for i, mp4 in enumerate(mp4_files):
                    print(f"[{i}] File name: {mp4.file_name}.mp4\n")
                idx = int(input("Select file index to play: "))
                clear_screen()
                speed = input("Enter the playback speed (Ex: 0.50, 1.0, 2.0): ")
                mp4.setSpeed(speed)
                clear_screen()
                mp4_files[idx].play()
            input("\nPress Enter to continue...")

        elif choice == "2":
            if not mov_files:
                print("\033[1mNo MOV files to play.\033[0m")
            else:
                clear_screen()
                print("\033[1mMOV files\033[0m\n")
                for i, mov in enumerate(mov_files):
                    print(f"[{i}] File name: {mov.file_name}.mov\n")
                idx = int(input("Select file index to play: "))
                clear_screen()
                mov_files[idx].play()
            input("\nPress Enter to continue...")

        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()
            
def view_image_menu():
    while True:
        clear_screen()
        print("\033[1mView Image\033[0m")
        print("[1] View PNG")
        print("[2] View JPG")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            if not png_files:
                print("\033[1mNo PNG files to view.\033[0m")
            else:
                clear_screen()
                print("\033[1mPNG files\033[0m\n")
                for i, png in enumerate(png_files):
                    print(f"[{i}] File name: {png.file_name}.png\n")
                idx = int(input("Select file index to view: "))
                clear_screen()
                png_files[idx].view()
            input("\nPress Enter to continue...")

        elif choice == "2":
            if not jpg_files:
                print("\033[1mNo JPG files to view.\033[0m")
            else:
                clear_screen()
                print("\033[1mJPG files\033[0m\n")
                for i, jpg in enumerate(jpg_files):
                    print(f"[{i}] File name: {jpg.file_name}.jpg\n")
                idx = int(input("Select file index to view: "))
                clear_screen()
                jpg_files[idx].view()
            input("\nPress Enter to continue...")

        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()

def mp3_menu():
    while True:
        clear_screen()
        print("\033[1mMP3 Options:\033[0m")
        print("[1] Add MP3")
        print("[2] View MP3s")
        print("[3] Edit MP3")
        print("[4] Delete MP3")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("\033[1mAdd a new MP3 file\033[0m\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            mp3 = Mp3(name, size)
            mp3_files.append(mp3)
            clear_screen()
            print(f"\033[1m{mp3.file_name}.mp3 added successfully.\033[0m")
            input("\nPress Enter to continue...")
            clear_screen()
            
        elif choice == "2":
            clear_screen()
            if not mp3_files:
                print("\033[1mNo MP3 files.\033[0m")
            else:
                print("\033[1mMP3 Files\033[0m")
                for i, mp3 in enumerate(mp3_files):
                    print(f"\nFile name: {mp3.file_name}.mp3\nFile size: {mp3.file_size} MB")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not mp3_files:
                print("\033[1mNo MP3 files to edit.\033[1m")
            else:
                try:
                    print("\033[1mMP3 Files\033[0m\n")
                    for i, mp3 in enumerate(mp3_files):
                        print(f"[{i}] File name: {mp3.file_name}.mp3\n    File size: {mp3.file_size} MB\n")
                    idx = int(input("Select file index to edit: "))
                    selected = mp3_files[idx]
                    clear_screen()
                    print(f"Editing {mp3.file_name}.mp3: \n")
                    new_name = input("Enter new file name: ")
                    new_size = float(input("Enter new file size (MB): "))
                    setattr(selected, 'file_name', new_name)
                    setattr(selected, 'file_size', new_size)
                    clear_screen()
                    print(f"MP3 edited to {new_name}.mp3")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input()
                except ValueError:
                    invalid_input()
                
        elif choice == "4":
            try:
                clear_screen()
                if not mp3_files:
                    print("No MP3 files to delete.")
                else:
                    print("MP3 Files\n")
                    for i, mp3 in enumerate(mp3_files):
                        print(f"[{i}] File name: {mp3.file_name}.mp3\n    File size: {mp3.file_size} MB\n")
                    idx = int(input("Select file index to delete: "))
                    del mp3_files[idx]
                    clear_screen()
                    print(f"{mp3.file_name}.mp3 deleted successfully.")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
            except IndexError:
                invalid_input
            except ValueError:
                invalid_input()

        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()
        
def wav_menu():
    while True:
        clear_screen()
        print("\033[1mWAV Options:\033[0m")
        print("[1] Add WAV")
        print("[2] View WAVs")
        print("[3] Edit WAV")
        print("[4] Delete WAV")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("Add a new WAV file\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            depth = int(input("Enter bit depth (16/24/32): ") or 16)
            wav = Wav(name, size)
            wav.setBitDepth(depth)
            wav_files.append(wav)
            clear_screen()
            print(f"{wav.file_name}.wav added successfully.")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            if not wav_files:
                print("No WAV files.")
            else:
                print("WAV Files\n")
                for i, wav in enumerate(wav_files):
                    print(f"File name: {wav.file_name}.wav\nFile size: {wav.file_size} MB\nBit depth: {wav.bit_depth}\n")
                
            input("\nPress Enter to return to main menu...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not wav_files:
                print("No WAV files to edit.")
            else:
                try:
                    print("WAV Files\n")
                    for i, wav in enumerate(wav_files):
                        print(f"[{i}] File name: {wav.file_name}.wav\n    File size: {wav.file_size} MB\n    Bit depth: {wav.bit_depth}\n")
                    idx = int(input("Select file index to edit: "))
                    selected = wav_files[idx]
                    clear_screen()
                    print(f"Editing {wav.file_name}.wav:\n")
                    new_name = input("Enter new file name: ")
                    new_size = float(input("Enter new file size (MB): "))
                    depth = int(input("New bit depth (16/24/32): "))
                    setattr(selected, 'file_name', new_name)
                    setattr(selected, 'file_size', new_size)
                    setattr(selected, 'bit_depth', depth)
                    clear_screen()
                    print(f"WAV file edited to {new_name}.wav")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()
                    
        elif choice == "4":
            clear_screen()
            if not wav_files:
                print("No WAV files to delete.")
            else:
                try:
                    print("WAV Files\n")
                    for i, wav in enumerate(wav_files):
                        print(f"[{i}] File name: {wav.file_name}.wav\n    File size: {wav.file_size} MB\n    Bit depth: {wav.bit_depth}\n")
                    idx = int(input("Select file index to delete: "))
                    del wav_files[idx]
                    clear_screen()
                    print(f"{wav.file_name}.wav deleted successfully")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()

        elif choice == "0":
            clear_screen()
            break
        
        else:
            invalid_input()
        
def mp4_menu():
    while True:
        clear_screen()
        print("\033[1mMP4 Options:\033[0m")
        print("[1] Add MP4")
        print("[2] View MP4s")
        print("[3] Edit MP4")
        print("[4] Delete MP4")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("Add a new MP4 file\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            res = input("Enter resolution: ")
            mp4 = Mp4(name, size, res)
            mp4_files.append(mp4)
            clear_screen()
            print(f"{mp4.file_name}.mp4 added successfully.")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            if not mp4_files:
                print("No MP4 files.")
            else:
                print("MP4 Files\n")
                for i, mp4 in enumerate(mp4_files):
                    print(f"File name: {mp4.file_name}.mp4\nFile size: {mp4.file_size} MB\nResolution: {mp4.resolution}\n")
            input("\nPress Enter to return to main menu...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not mp4_files:
                print("No MP4 files to edit.")
            try:
                print("MP4 Files\n")
                for i, mp4 in enumerate(mp4_files):
                    print(f"[{i}] File name: {mp4.file_name}.mp4\n    File size: {mp4.file_size} MB\n    Resolution: {mp4.resolution}\n")
                idx = int(input("Select file index to edit: "))
                selected = mp4_files[idx]
                clear_screen()
                print(f"Editing {mp4.file_name}.mp4:\n")
                new_name = input("Enter new file name: ")
                new_size = float(input("Enter new file size (MB): "))
                mp4.resolution = int(input("Enter new resolution: "))
                setattr(selected, 'file_name', new_name)
                setattr(selected, 'file_size', new_size)
                setattr(selected, 'resolutionmp4', mp4.resolution)
                clear_screen()
                print(f"MP4 file edited to {new_name}.mp4")
                input("\nPress Enter to return to continue...")
                clear_screen()
            except IndexError:
                invalid_input
            except ValueError:
                invalid_input()

        elif choice == "4":
            clear_screen()
            if not mp4_files:
                print("No MP4 files to delete.")
            else:
                try:
                    print("MP4 Files\n")
                    for i, mp4 in enumerate(mp4_files):
                        print(f"[{i}] File name: {mp4.file_name}.mp4\n    File size: {mp4.file_size} MB\n    Resolution: {mp4.resolution}\n")
                    idx = int(input("Select file index to delete: "))
                    del mp4_files[idx]
                    clear_screen()
                    print(f"{mp4.file_name}.mp4 deleted successfully")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()
            
        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()

def mov_menu():
    while True:
        clear_screen()
        print("\033[1mMOV Options:\033[0m")
        print("[1] Add MOV")
        print("[2] View MOVs")
        print("[3] Edit MOV")
        print("[4] Delete MOV")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("Add a new MOV file\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            subtitles = input("Has subtitles? (yes/no): ").lower() == "yes"
            rate = int(input("Enter frame rate (24/30/60): ") or 30)
            mov = Mov(name, size, subtitles)
            mov.setframe_rate(rate)
            mov_files.append(mov)
            clear_screen()
            print(f"{mov.file_name}.mov added successfully.")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            if not mov_files:
                print("MOV Files\n")
            else:
                print("MOV Files\n")
                for i, mov in enumerate(mov_files):
                    print(f"File name: {mov.file_name}.mov\nFile size: {mov.file_size} MB\nSubtitles: {mov.has_subtitles}\nFramerate: {mov.frame_rate}\n")
            input("\nPress Enter to return to main menu...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not mov_files:
                print("No MOV files to edit.")
            else:
                try:
                    print("MOV Files\n")
                    for i, mov in enumerate(mov_files):
                        print(f"[{i}] File name: {mov.file_name}.mov\n    File size: {mov.file_size} MB\n    Subtitles: {mov.has_subtitles}\n    Framerate: {mov.frame_rate}\n")
                    idx = int(input("Select file index to edit: "))
                    selected = mov_files[idx]
                    clear_screen()
                    print(f"Editing {mov.file_name}.mov:\n")
                    new_name = input("Enter new file name: ")
                    new_size = float(input("Enter new file size (MB): "))
                    new_subtitles = input("Has subtitles? (yes/no): ").lower() == "yes"
                    new_rate = int(input("Enter new frame rate (24/30/60): ") or 30)
                    setattr(selected, 'file_name', new_name)
                    setattr(selected, 'file_size', new_size)
                    setattr(selected, 'has_subtitles', new_subtitles)
                    setattr(selected, 'frame_rate', new_rate)
                    clear_screen()
                    print(f"MOV file edited to {new_name}.mov")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()

        elif choice == "4":
            clear_screen()
            if not mov_files:
                print("No MOV files to delete.")
            else:
                try:
                    print("MOV Files\n")
                    for i, mov in enumerate(mov_files):
                        print(f"[{i}] File name: {mov.file_name}.mov\n    File size: {mov.file_size} MB\n    Subtitles: {mov.has_subtitles}\n    Framerate: {mov.frame_rate}\n")
                    idx = int(input("Select file index to delete: "))
                    del mov_files[idx]
                    clear_screen()
                    print(f"{mov.file_name}.mov deleted successfully")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()

        elif choice == "0":
            clear_screen()
            break
        else:
            invalid_input()

def png_menu():
    while True:
        clear_screen()
        print("\033[1mPNG Options:\033[0m")
        print("[1] Add PNG")
        print("[2] View PNGs")
        print("[3] edit PNGs")
        print("[4] Delete PNG")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("Add a new PNG file\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            png = Png(name, size)
            png_files.append(png)
            clear_screen()
            print(f"{png.file_name}.png added successfully.")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            if not png_files:
                print("No PNG files.")
            else:
               print("MP3 Files\n")
               for i, png in enumerate(png_files):
                print(f"File name: {png.file_name}.png\nFile size: {png.file_size} MB\n")
            input("\nPress Enter to return to main menu...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not png_files:
                print("No PNG files to edit.")
            else:
                try:
                    print("PNG Files\n")
                    for i, png in enumerate(png_files):
                        print(f"[{i}] File name: {png.file_name}.png\n    File size: {png.file_size} MB\n")
                    idx = int(input("Select file index to edit: "))
                    selected = png_files[idx]
                    clear_screen()
                    print(f"Editing {png.file_name}.png:\n")
                    new_name = input("Enter new file name: ")
                    new_size = float(input("Enter new file size (MB): "))
                    setattr(selected, 'file_name', new_name)
                    setattr(selected, 'file_size', new_size)
                    clear_screen()
                    print(f"PNG file edited to {new_name}.png")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()
                    
        elif choice == "4":
            clear_screen()
            if not png_files:
                print("No PNG files to delete.")
            else:
                try:
                    print("PNG Files\n")
                    for i, png in enumerate(png_files):
                        print(f"[{i}] File name: {png.file_name}.png\n    File size: {png.file_size} MB\n")
                    idx = int(input("Select file index to delete: "))
                    del png_files[idx]
                    clear_screen()
                    print(f"{png.file_name}.png deleted successfully")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()

        elif choice == "0":
            clear_screen()
            break
        
        else:
            invalid_input()

def jpg_menu():
    while True:
        clear_screen()
        print("\033[1mJPG Options:\033[0m")
        print("[1] Add JPG")
        print("[2] View JPGs")
        print("[3] Edit JPGs")
        print("[4] Delete JPG")
        print("[0] Back")
        choice = input("Select an option: ")

        if choice == "1":
            clear_screen()
            print("Add a new JPG file\n")
            name = input("Enter file name: ")
            size = float(input("Enter size (MB): ") or 0)
            jpg = Jpg(name, size)
            jpg_files.append(jpg)
            clear_screen()
            print(f"{jpg.file_name}.jpg added successfully.")
            input("\nPress Enter to return to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            if not jpg_files:
                print("No JPG files.")
            else:
                print("JPG Files\n")
                for i, jpg in enumerate(jpg_files):
                    print(f"File name: {jpg.file_name}.jpg\nFile size: {jpg.file_size} MB\n")
                
            input("Press Enter to return to main menu...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            if not jpg_files:
                print("No JPG files to edit.")
            else:
                try:
                    print("JPG Files\n")
                    for i, jpg in enumerate(jpg_files):
                        print(f"[{i}] File name: {jpg.file_name}.jpg\n    File size: {jpg.file_size} MB\n")
                    idx = int(input("Select file index to edit: "))
                    selected = jpg_files[idx]
                    clear_screen()
                    print(f"Editing {jpg.file_name}.jpg:\n")
                    new_name = input("Enter new file name: ")
                    new_size = float(input("Enter new file size (MB): "))
                    setattr(selected, 'file_name', new_name)
                    setattr(selected, 'file_size', new_size)
                    clear_screen()
                    print(f"JPG file edited to {new_name}.jpg")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()
                    
        elif choice == "4":
            clear_screen()
            if not jpg_files:
                print("No JPG files to delete.")
            else:
                try:
                    print("JPG Files\n")
                    for i, jpg in enumerate(jpg_files):
                        print(f"[{i}] File name: {jpg.file_name}.jpg\n    File size: {jpg.file_size} MB\n")
                    idx = int(input("Select file index to delete: "))
                    del wav_files[idx]
                    clear_screen()
                    print(f"{jpg.file_name}.jpg deleted successfully")
                    input("\nPress Enter to return to continue...")
                    clear_screen()
                except IndexError:
                    invalid_input
                except ValueError:
                    invalid_input()

        elif choice == "0":
            clear_screen()
            break
        
        else:
            invalid_input()
        
from abc import ABC, abstractmethod

# Parent class for all media files
class MediaFile(ABC):
    def __init__(self, file_name, file_size):
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

# Audio class inheriting from MediaFile
class Audio(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)

    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# MP3 class inheriting from Audio
class Mp3(Audio):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)
        self.mode = "none"

    def setMode(self, mode):
        if mode.lower() in ["loop", "shuffle"]:
            self.mode = mode.lower()
        else:
            self.mode = "none"

    def play(self):
        print(f"\033[1mNow playing\033[0m: {self.file_name}.mp3")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mMode is set\033[0m: {self.mode}")

    def pause(self):
        print(f"{self.file_name}.mp3 is currently paused.")
    
    def stop(self):
        print(f"{self.file_name}.mp3 is no longer playing.")

# WAV class inheriting from Audio
class Wav(Audio):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)
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

    def pause(self):
        print(f"{self.file_name}.wav is currently paused.")

    def stop(self):
        print(f"{self.file_name}.wav playback stopped.")

# Video class inheriting from MediaFile
class Video(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)

    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# MP4 class inheriting from Video
class Mp4(Video):
    def __init__(self, file_name, file_size, resolutionmp4):
        super().__init__(file_name, file_size)
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

    def pause(self):
        print(f"{self.file_name}.mp4 is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mp4 is no longer playing.")

# MOV class inheriting from Video
class Mov(Video):
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
        print(f"\033[1mNow playing\033[0m: {self.file_name}.mov")
        print(f"\033[1mFile Size\033[0m: {self.file_size}MB")
        print(f"\033[1mFrame Rate\033[0m: {self.frame_rate}fps")
        print(f"\033[1mSubtitles Included\033[0m: {'Yes' if self.has_subtitles else 'No'}")

    def pause(self):
        print(f"{self.file_name}.mov is currently paused.")

    def stop(self):
        print(f"{self.file_name}.mov is no longer playing.")

# Image class inheriting from MediaFile
class Image(MediaFile):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)

    @abstractmethod
    def view(self):
        pass
    
    def play(self):
        pass  # No functionality for play

    def pause(self):
        pass  # No functionality for pause

    def stop(self):
        pass  # No functionality for stop

# PNG class inheriting from Image
class Png(Image):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)

    def view(self):
        print(f"Displaying image: {self.file_name}.png")
        print(f"File size: {self.file_size}MB")

# JPEG class inheriting from Image
class Jpg(Image):
    def __init__(self, file_name, file_size):
        super().__init__(file_name, file_size)

    def view(self):
        print(f"Displaying image: {self.file_name}.jpeg")
        print(f"File size: {self.file_size}MB")

# Main Program
#byte_stream()
while True:
    main_screen()
    choice = input("Select media type: ")
    clear_screen()

    if choice == "1":
        print("\033[1mAudio Files:\033[0m")
        print("[1] MP3")
        print("[2] WAV")
        print("[3] Play music")
        print("[0] Back")
        sub_choice = input("Select audio format: ")

        if sub_choice == "1":
            mp3_menu()
        elif sub_choice == "2":
            wav_menu()            
        elif sub_choice == "3":
            play_music_menu()
        elif sub_choice == "0":
            clear_screen() 
            continue
        else:
            invalid_input()

    elif choice == "2":
        print("\033[1mVideo Files:\033[0m")
        print("[1] MP4")
        print("[2] MOV")
        print("[3] Play video")
        print("[0] Back")
        sub_choice = input("Select video format: ")

        if sub_choice == "1":
            mp4_menu()
        elif sub_choice == "2":
            mov_menu()
        elif sub_choice == "3":
            play_video_menu()
        elif sub_choice == "0":
            clear_screen()
            continue
        else:
            invalid_input()

    elif choice == "3":
        print("\033[1mImage Files:\033[0m")
        print("[1] PNG")
        print("[2] JPG")
        print("[3] View image")
        print("[0] Back")
        sub_choice = input("Select video format: ")
        
        if sub_choice == "1":
            png_menu()
        elif sub_choice == "2":
            jpg_menu()
        elif sub_choice == "3":
            view_image_menu()
        elif sub_choice == "0":
            clear_screen()
            continue
        else:
            invalid_input()

    elif choice == "4":
        print("Thank you for using the media player.")
        break

    else:
        print("Invalid input. Please try again.")
        input("\nPress Enter to return to main menu...")
        clear_screen()
