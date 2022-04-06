from encoder import *
from decoder import *
from readChars import *
from signalsProcessing import *


characters = read_chars()
list_chars = list(characters.values())
y = encode('Welcome', characters)
write_wav_signal(y, "test.wav")
r = read_wav_signal("test.wav")
play_sound('test.wav')

n = np.arange(len(r))
string, decoded_frequencies = decode_fft(r, list_chars, fs=8000)
print(decoded_frequencies)
print(string)
print(decode_BPF(r, list_chars, fs=8000))
