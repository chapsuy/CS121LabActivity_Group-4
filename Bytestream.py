import os
import platform
from abc import ABC, abstractmethod

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class MediaFile(ABC):
    def __init__(self, file_name, file_size, file_format):
        self.file_name = file_name
        self.file_size = file_size
        self.file_format = file_format
        self.is_playing = False
        self.is_paused = False

    @abstractmethod
    def play(self):
        pass

    def pause(self):
        if self.is_playing and not self.is_paused:
            self.is_paused = True
            print(f"\n⏸️  {self.file_name} is currently paused.")
        elif self.is_paused:
            self.is_paused = False
            print(f"\n▶️ Resuming {self.file_name}...")

    def stop(self):
        self.is_playing = False
        self.is_paused = False
        print(f"\n⏹️  {self.file_name} is no longer playing.")

    def playback_controls(self):
        while self.is_playing:
            action = input("\n🎛️  Controls: [A] Keep playing | [B] Pause | [C] Stop: ").upper()

            if action == "B":
                self.pause()
                while self.is_paused:
                    action = input("\n⏸️  Paused: [A] Resume | [C] Stop: ").upper()
                    if action == "A":
                        self.pause()  # This will resume
                    elif action == "C":
                        self.stop()
                        return
            elif action == "C":
                self.stop()
                return
            elif action != "A":
                print("❌ Invalid input. Try again.")

            if not self.is_paused:
                # This will be overridden by child classes
                print(f"\n🎶 Now playing: {self.file_name}...")

class Audio(MediaFile):
    def __init__(self, file_name, file_size, file_format):
        super().__init__(file_name, file_size, file_format)
        self.volume = 50
        self.playback_mode = "normal"
        self.bit_depth = 16

    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        print(f"🔊 Volume set to {self.volume}%")
def set_playback_mode(self, mode):
        if mode.lower() in ["normal", "loop", "shuffle"]:
            self.playback_mode = mode.lower()
        else:
            print("⚠️ Invalid mode. Using 'normal'")

    def playback_controls(self):
        while self.is_playing:
            action = input("\n🎛️  Controls: [A] Keep playing | [B] Pause | [C] Stop: ").upper()

            if action == "B":
                self.pause()
                while self.is_paused:
                    action = input("\n⏸️  Paused: [A] Resume | [C] Stop: ").upper()
                    if action == "A":
                        self.pause()  # This will resume
                    elif action == "C":
                        self.stop()
                        return
            elif action == "C":
                self.stop()
                return
            elif action != "A":
                print("❌ Invalid input. Try again.")

            if not self.is_paused:
                print(f"\n🎶 Now playing: {self.file_name}...")

    def play(self):
        self.is_playing = True
        print(f"\n🎵 Now playing: {self.file_name}.{self.file_format}")
        print(f"📁 Size: {self.file_size}MB")
        print(f"🔊 Volume: {self.volume}%")
        print(f"🔁 Mode: {self.playback_mode.capitalize()}")
        if self.file_format in ["wav", "flac"]:
            print(f"🎚️  Bit Depth: {self.bit_depth}-bit")
        self.playback_controls()

class Video(MediaFile):
    def __init__(self, file_name, file_size, file_format):
        super().__init__(file_name, file_size, file_format)
        self.resolution = "1080p"
        self.playback_speed = 1.0
        self.has_subtitles = False
        self.frame_rate = 30

    def set_resolution(self, resolution):
        self.resolution = resolution
        print(f"🖥️  Resolution set to {self.resolution}")

    def set_playback_speed(self, speed):
        try:
            speed = float(speed)
            if speed > 0:
                self.playback_speed = speed
                print(f"⏩ Playback speed: {self.playback_speed}x")
            else:
                print("⚠️ Invalid speed. Using default (1.0x).")
        except ValueError:
            print("⚠️ Invalid input. Using default (1.0x).")

    def playback_controls(self):
        while self.is_playing:
            action = input("\n🎛️  Controls: [A] Keep playing | [B] Pause | [C] Stop: ").upper()
            if action == "B":
                self.pause()
                while self.is_paused:
                    action = input("\n⏸️  Paused: [A] Resume | [C] Stop: ").upper()
                    if action == "A":
                        self.pause()  # This will resume
                    elif action == "C":
                        self.stop()
                        return
            elif action == "C":
                self.stop()
                return
            elif action != "A":
                print("❌ Invalid input. Try again.")

            if not self.is_paused:
                print(f"\n🎬 Now showing: {self.file_name}...")

    def play(self):
        self.is_playing = True
        print(f"\n🎬 Now playing: {self.file_name}.{self.file_format}")
        print(f"📁 Size: {self.file_size}MB")
        print(f"🖥️  Resolution: {self.resolution}")
        print(f"⏩ Speed: {self.playback_speed}x")
        print(f"🎞️  Frame Rate: {self.frame_rate}fps")
        print(f"📜 Subtitles: {'✅ Yes' if self.has_subtitles else '❌ No'}")
        self.playback_controls()

class Image(MediaFile):
    def __init__(self, file_name, file_size, file_format):
        super().__init__(file_name, file_size, file_format)
        self.brightness = 50
        self.contrast = 50
        self.zoom = 100

    def set_brightness(self, value):
            self.brightness = max(0, min(100, value))
        print(f"☀️ Brightness: {self.brightness}%")

    def set_contrast(self, value):
        self.contrast = max(0, min(100, value))
        print(f"🌈 Contrast: {self.contrast}%")

    def pause(self):
        print("🔄 Resetting image settings")
        self.brightness = 50
        self.contrast = 50
        self.zoom = 100
        print("☀️ Brightness reset to 50%")
        print("🌈 Contrast reset to 50%")
        print("🔍 Zoom reset to 100%")

    def stop(self):
        print("❌ Closing image viewer")
        self.is_playing = False
        self.is_paused = False

    def playback_controls(self):
        while self.is_playing:
            action = input("\n🎛️  Controls: [A] Keep viewing | [B] Reset settings | [C] Close: ").upper()

            if action == "B":
                self.pause()
                while self.is_paused:
                    action = input("\n⏸️  Paused: [A] Continue viewing | [C] Close: ").upper()
                    if action == "A":
                        self.pause()  #  resume
                    elif action == "C":
                        self.stop()
                        return
            elif action == "C":
                self.stop()
                return
            elif action != "A":
                print("❌ Invalid input. Try again.")

            if not self.is_paused:
                print(f"\n🖼️  Viewing: {self.file_name}...")

    def play(self):
        if self.is_playing:
            print("ℹ️ This image is already open")
            return

        self.is_playing = True
        print(f"\n🖼️  Image opened: {self.file_name}.{self.file_format}")
        print(f"📏 Size: {self.file_size}MB")
        print(f"☀️ Brightness: {self.brightness}%")
        print(f"🌈 Contrast: {self.contrast}%")
        print(f"🔍 Zoom: {self.zoom}%")
        #the image will be output
        print("\n" + "+-------------------+")
        print("|      IMAGE       |")
        print(f"|   {self.file_name:^15}  |")
        print("+-------------------+")

        self.playback_controls()

class TextDocument(MediaFile):
    def __init__(self, file_name, file_size, file_format):
        super().__init__(file_name, file_size, file_format)
        self.language = "English"
        self.page_count = 1
        self.font_size = 12
        self.is_editable = True

    def set_language(self, language):
        self.language = language
        print(f"🌐 Language set to {self.language}")

    def set_page_count(self, count):
        try:
            self.page_count = max(1, int(count))
            print(f"📄 Pages: {self.page_count}")
        except ValueError:
            print("⚠️ Invalid page count. Using default (1).")

    def set_font_size(self, size):
        if 8 <= size <= 72:
            self.font_size = size
            print(f"🔠 Font size: {self.font_size}pt")
        else:
            print("⚠️ Invalid font size. Using default (12pt).")

    def pause(self):
        print("🔄 Resetting document view")
        # mag rereset

    def stop(self):
        print("❌ Closing document")
        self.is_playing = False
        self.is_paused = False

    def playback_controls(self):
        while self.is_playing:
            action = input("\n🎛️  Controls: [A] Keep reading | [B] Reset view | [C] Close: ").upper()

            if action == "B":
                self.pause()
                while self.is_paused:
                    action = input("\n⏸️  Paused: [A] Continue reading | [C] Close: ").upper()
                    if action == "A":
                        self.pause()  # Mag resume
                    elif action == "C":
                        self.stop()
                        return
            elif action == "C":
                self.stop()
                return
            elif action != "A":
                print("❌ Invalid input. Try again.")

            if not self.is_paused:
                print(f"\n📖 Reading: {self.file_name}...")
     def play(self):
        if self.is_playing:
            print("ℹ️ This document is already open")
            return

        self.is_playing = True
             
        print(f"\n📄 Document opened: {self.file_name}.{self.file_format}")
        print(f"📏 Size: {self.file_size}MB")
        print(f"🌐 Language: {self.language}")
        print(f"📑 Pages: {self.page_count}")
        print(f"✍️  Editable: {'Yes' if self.is_editable else 'No'}")
        print("\n----- Document Content -----")
        print("This would show the actual document content...")
        print("---------------------------")
        self.playback_controls()
while True:
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
    print("\n📁 Media Files:\n")
    print(" [1]. Audio 🎵")
    print(" [2]. Video 🎬")
    print(" [3]. Image 📷")
    print(" [4]. Text Document 📝")
    print(" [5]. Exit\n")

    media_type = input("👉 Select media type or 5 to exit: ")
    clear_screen()
#AUDIO
    if media_type == "1":
        print("🎵 AUDIO PLAYER 🎵")
        print("-----------------")
        name = input("📝 Enter audio file name: ")
        size = input("💾 Enter file size (MB): ")
        format_choice = input("🎚️   Format (mp3/wav/flac): ") or "mp3"
        audio = Audio(name, size, format_choice)

        volume = input("🔊 Volume (0-100): ") or "50"
        audio.set_volume(int(volume))

        mode = input("🔁 Mode (normal/loop/shuffle): ") or "normal"
        audio.set_playback_mode(mode)

        if format_choice in ["wav", "flac"]:
            depth = input("🎚️   Bit depth (16/24/32): ") or "16"
            audio.bit_depth = int(depth)
        clear_screen()
        audio.play()
#VIDEO
    elif media_type == "2":
        print("🎬 VIDEO PLAYER 🎬")
        print("-----------------")
        name = input("📝 Enter video file name: ")
        size = input("💾 Enter file size (MB): ")
        format_choice = input("🎞️   Format (mp4/mov/avi): ") or "mp4"
        video = Video(name, size, format_choice)
        resolution = input("🖥️   Resolution (e.g., 1080p): ") or "1080p"
        video.set_resolution(resolution)

        speed = input("⏩ Speed (e.g., 1.0): ") or "1.0"
        video.set_playback_speed(float(speed))

        frame_rate = input("🎞️   Frame rate (24/30/60): ") or "30"
        video.frame_rate = int(frame_rate)

        subtitles = input("📜 Subtitles? (y/n): ").lower() == "y"
        video.has_subtitles = subtitles

        clear_screen()
        video.play()
#IMAGE
    elif media_type == "3":
        print("📷 IMAGE VIEWER 📷")
        print("-----------------")
        name = input("📝 Enter image file name: ")
        size = input("💾 Enter file size (MB): ")
        format_choice = input("🖼️   Format (jpg/png/gif): ") or "jpg"
        image = Image(name, size, format_choice)

        brightness = input("☀️ Brightness (0-100): ") or "50"
        image.set_brightness(int(brightness))

        contrast = input("🌈 Contrast (0-100): ") or "50"
        image.set_contrast(int(contrast))

        clear_screen()
        image.play()


#DOCUMENT
    elif media_type == "4":
        print("📝 TEXT VIEWER 📝")
        print("----------------")
        name = input("📝 Enter document name: ")
        size = input("💾 Enter file size (MB): ")
        format_choice = input("📄 Format (txt/pdf/docx): ") or "txt"
        doc = TextDocument(name, size, format_choice)
        language = input("🌐 Language: ") or "English"
        doc.set_language(language)

        pages = input("📄 Page count: ") or "1"
        doc.set_page_count(int(pages))
        font_size = input("🔠 Font size (8-72): ") or "12"
        doc.set_font_size(int(font_size))

        editable = input("✏️ Editable? (y/n): ").lower() == "y"
        doc.is_editable = editable

        clear_screen()
        doc.play()

    elif media_type == "5":
        print("\n👋 Thank you from Group 6!")
        break

    else:
        print("❌ Unsupported media type. Please select 1-5.")

    input("\n👆 Press enter to return to main menu...")
            
            
