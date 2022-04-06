from scipy.signal import butter, lfilter
from numpy.fft import fft
from signalsProcessing import *
decoded_frequencies = ''


def decode_fft(the_f_data, list_chars, fs=8000):

	global decoded_frequencies
	sample_length = len(the_f_data)

	T = 0.04
	N = int(fs * T)
	print (N)
	step = N

	startOfSignal = 0
	endOfSignal = N
	decoded_sting = ''
	for c in range(0, int(sample_length / step)):

		z = the_f_data[startOfSignal:endOfSignal]
		yf = fft(z)
		startOfSignal += step
		endOfSignal += step

		index = int(fs / step)
		freq = []
		# for i in range(4, int(len(yf))):
		# 	if int(abs(yf[i])) > 1:
		# 		freq.append(i * index)
		# typeOfChar = freq[0]
		# low = freq[1]
		# middle = freq[2]
		# high = freq[3]

		for i in range(4, int(len(yf))):
			if int(abs(yf[i])) > 1:
				freq.append(i * index)
		if (freq[2] == 1000) and (freq[1] == 800):
			typeOfChar = freq[0]
			low = freq[2]
			middle = freq[1]
			high = freq[3]

		elif (freq[2] == 1600) and (freq[3] == 2000):
			typeOfChar = freq[0]
			low = freq[1]
			middle = freq[3]
			high = freq[2]
		else:
			typeOfChar = freq[0]
			low = freq[1]
			middle = freq[2]
			high = freq[3]
		# if(middle < high):
		# 	temp = middle
		# 	middle = high
		# 	high = temp

		# print("low {}, middle {}, high {}".format(low, middle, high))

		decoded_frequencies = decoded_frequencies + "typeOfChar {},low {}, middle {}, high {}".format(typeOfChar , low, middle, high)
		# print("low {}, middle {}, high {}".format(low, middle, high))
		# print(decoded_frequencies)
		for i in range(0, len(list_chars)):
			if (list_chars[i]['typeOfChar'] == typeOfChar) & (list_chars[i]['low'] == low) & (list_chars[i]['middle'] == middle) & (
				 list_chars[i]['high'] == high):
				# print(list_chars[i]['char'])
				decoded_frequencies = decoded_frequencies + " => '{}'\n".format(list_chars[i]['char'])
				decoded_sting += list_chars[i]['char']
		print(decoded_frequencies)

	return decoded_sting , decoded_frequencies




def butter_bandpass(lowcut, highcut, fs, order=5):
	nyq = 0.5 * fs
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
	b, a = butter_bandpass(lowcut, highcut, fs, order=order)
	y = lfilter(b, a, data)
	return y


def BPF(the_f_data, center, startOfSignal, endOfSignal):
	lowcut = center - 50
	highcut = center + 50
	fs = 8000.0
	for order in [3, 6, 9]:
		b, a = butter_bandpass(lowcut, highcut, fs, order=order)
	x = the_f_data[startOfSignal:endOfSignal]
	y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
	return y


def check_freq(the_f_data, center, startOfSignal, endOfSignal):
	y = BPF(the_f_data, center, startOfSignal, endOfSignal)
	z = np.array(y)
	yf = fft(z)
	# my_plot_2(yf)

	for k in range(0, int(len(yf) / 2)):
		if int(abs(yf[k])) > 100:
			if k * 25 > center - 10 & k * 25 < center + 10:
				return True
	return False


def decode_BPF(the_f_data, list_chars, fs=8000):
	global decoded_frequencies

	sample_length = len(the_f_data)
	T = 0.04
	N = int(fs * T)
	step = N
	startOfSignal = 0
	endOfSignal = N
	decoded_sting = ''
	typeOfChar_frequencies = [100, 200]
	low_frequencies = [400, 600, 1000]
	middle_frequencies = [800, 1200, 2000]
	high_frequencies = [1600, 2400, 4000]

	for c in range(0, int(sample_length / step)):

		# z = the_f_data[startOfSignal:endOfSignal]
		# yf = fft(z)
		for f in typeOfChar_frequencies:
			if check_freq(the_f_data, f, startOfSignal, endOfSignal):
				typeOfChar = f

		for f in low_frequencies:
			if check_freq(the_f_data, f, startOfSignal, endOfSignal):
				low = f

		for f in middle_frequencies:
			if check_freq(the_f_data, f, startOfSignal, endOfSignal):
				middle = f

		for f in high_frequencies:
			if check_freq(the_f_data, f, startOfSignal, endOfSignal):
				high = f

		decoded_frequencies = decoded_frequencies + "typeOfChar {} ,low {}, middle {}, high {}".format(typeOfChar,low, middle,high)
		#(decoded_frequencies)

		for i in range(0, len(list_chars)):
			if (list_chars[i]['typeOfChar'] == typeOfChar) & (list_chars[i]['low'] == low) & (list_chars[i]['middle'] == middle) & (
				 list_chars[i]['high'] == high):
				# print(list_chars[i]['char'])
				decoded_frequencies = decoded_frequencies + " => '{}'\n".format(list_chars[i]['char'])
				decoded_sting += list_chars[i]['char']

		startOfSignal += step
		endOfSignal += step

	return decoded_sting, decoded_frequencies
