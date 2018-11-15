import pyaudio
import wave


def playaudio(filename):
	chuck = 1024 # split our audio file up into chucks
	wf = .wave.open(filename, 'rb')  # open the audio file as a 
	pa = pyaudio.pyAudio() # instantiate the pyAudio class

	stream = pa.open(format=pa.get_formal_from_width(wf.getsampwidth()),
	channel=wf.getnchannels(), 
	rate=wf.getframerate(), 
	output=True)

	data_stream = wf.readframes(chuck)

	while data_stream:
		stream.write(data_stream)
		data_stream = wf.readframes(chuck)

	stream.close()
	pa.terminate()

playaudio('./audio/alert1.wav')