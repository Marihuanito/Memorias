#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from gtts import gTTS
import os
tts = gTTS('Ahí ta has semao')
tts.save('saludo.mp3')
os.system('mpg123 -q saludo.mp3')
