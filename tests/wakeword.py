import numpy as np
import pvporcupine
import pyaudio
import struct

def run():
    # porc = pvporcupine.create(keywords=["computer"])
    # porc = pvporcupine.create(keyword_paths=["../Hey-Fetch_en_mac_v2_1_0.ppn"])
    porc = pvporcupine.create(keyword_paths=["../Hey-Fetch_en_linux_v2_1_0.ppn"])
    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porc.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porc.frame_length)
    
    while True:
        pcm = audio_stream.read(porc.frame_length)
        pcm = struct.unpack_from("h" * porc.frame_length, pcm)
        
        keyword_index = porc.process(pcm)
        if keyword_index >= 0:
            print("Detected")
        
if __name__=="__main__":
    run()
