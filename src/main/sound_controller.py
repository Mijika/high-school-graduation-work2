#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pyaudio
import wave
import sys
import os


class SoundController:
    def __init__(self):
        self.chunk = 1024

    def soundPlay(self, sound_file, sound_file_info):
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(sound_file_info[0]),
                channels=sound_file_info[1],
                rate=sound_file_info[2],
                output=True)

        for chunk in sound_file:
            stream.write(chunk)

        stream.stop_stream()
        stream.close()

        p.terminate()


    def randomSound(self):
        pass


class SoundFileLoder:
    def __init__(self):
        self.chunk = 1024

    def soundLode(self, file_name):
        if self.file_name_ck(file_name) is False:
            raise "올바른 file name 입력하시오"

        wf = wave.open(os.path.join("./sound_file", file_name), 'rb')

        sound_file =  []
        chunk = wf.readframes(self.chunk)
        sound_file.append(chunk)

        while len(chunk) > 0:
            sound_file.append(chunk)
            chunk = wf.readframes(self.chunk)

        wf.close()

        return sound_file

    def get_sound_file_info(self, file_name):
        if self.file_name_ck(file_name) is False:
            raise "올바른 file name 입력하시오"

        wf = wave.open(os.path.join("./sound_file", file_name), 'rb')

        sampwidth = wf.getsampwidth()
        channels = wf.getnchannels()
        framerate = wf.getframerate()

        wf.close()

        return [sampwidth, channels, framerate]


    def file_name_ck(self, file_name):
        if file_name.split(".")[1] != "wav":
            return False

        return True


if __name__ == "__main__":

    sound_file_loder = SoundFileLoder()
    sound_controller = SoundController()

    sound_file = sound_file_loder.soundLode("test.wav")
    sound_file_info = sound_file_loder.get_sound_file_info("test.wav")

    sound_controller.soundPlay(sound_file, sound_file_info)

    # print(sound_file_loder.file_name_ck("test.wav"))
    # print(sound_file_loder.soundLode("test.wav"))

