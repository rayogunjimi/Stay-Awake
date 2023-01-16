import os

for i in range(10):
        os.system("osascript -e 'tell application \"System Events\"' -e 'key code 145' -e ' end tell'")
os.system("caffeinate -d")
