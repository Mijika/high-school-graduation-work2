#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import pyaudio
import wave
import sys
import os


class SoundController:
    def __init__(self):
        pass
    
    def soundPlay(self):
        pass
    
    def randomSound(self):
        pass


class SoundFileLoder:
    def __init__(self):
        pass

    def soundLode(self, file_name):
        if self.file_name_ck(file_name) is False:
            raise "올바른 file name 입력하시오"
        
        wf = wave.open(os.path.join("./sound_file", file_name), 'rb')

        sound_file = os.path.join("./sound_file", file_name)
        return sound_file

    def file_name_ck(self, file_name):
        if file_name.split(".")[1] != "wav":
            return False

        return True

if __name__ == "__main__":
    
    sound_file_loder = SoundFileLoder()
    print(sound_file_loder.file_name_ck("test.wav"))
    print(os.path.exists(os.path.join("./sound_file", "test.wav")))
    # print(sound_file_loder.soundLode("test.wav"))