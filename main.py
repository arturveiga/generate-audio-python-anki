import gtts
import re
import os
from playsound import playsound


def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)


def remove_old_files():
    audio_directory = 'audios'
    for filename in os.listdir(audio_directory):
        if filename.endswith('.mp3'):
            os.remove(os.path.join(audio_directory, filename))


def generate_mp3():
    with open('frases.txt', 'r') as file:
        for line in file:
            filename = 'audios/' + sanitize_filename(line.strip().replace('.', '')) + ".mp3"
            frase = gtts.gTTS(line, lang='en-us')
            frase.save(filename)
            # playsound(filename)


if __name__ == '__main__':
    remove_old_files()
    generate_mp3()


