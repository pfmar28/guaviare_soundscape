# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:57:18 2022

@author: pfmar
"""

from maad import sound
from maad.rois import find_rois_cwt
from maad.util import plot_spectrogram


s, fs = sound.load(r'E:\WWF/Prueba_Grab/Grabaciones_E/3324/SM_20140901_053000.wav')
Sxx, tn, fn, ext = sound.spectrogram(s, fs, nperseg=1024, noverlap=512)
plot_spectrogram(Sxx, extent=ext, db_range=60, gain=20, figsize=(4,10))

df_not = find_rois_cwt(s, fs, flims=(4500,8000), tlen=0.2, th=0, display=True, figsize=(10,6))
print(df_not)

df_not.to_csv(r'C:\Users\pfmar\Downloads/notas1.csv') 
