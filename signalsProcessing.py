import winsound
import matplotlib.pyplot as plt
import numpy as np
import wavio
from scipy.io import wavfile

def write_wav_signal(y, file_name):
	length = len(y)
	wavio.write(file_name, y, length, sampwidth=1)
	print("Saved successfully")

def read_wav_signal(file_name):
	rate, data = wavfile.read(file_name)
	the_f_data = []
	length = len(data)
	for i in range(0, length):
		the_f_data.append(0.019961328125 * data[i] - 2.090138671875)
	the_f_data = np.array(the_f_data, dtype=float)
	print("readed successfully")

	return the_f_data

def play_sound(filename):
	winsound.PlaySound(filename, winsound.SND_FILENAME)
	print("sound on!")
