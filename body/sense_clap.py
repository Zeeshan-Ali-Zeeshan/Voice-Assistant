import pyaudio
import struct
import math

# Constants
SHORT_NORMALIZE = (1.0 / 32768.0)
INITIAL_TAP_THRESHOLD = 0.12
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_RATE_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)
OVERSENSITIVE = 15.0 / INPUT_BLOCK_TIME
UNDERSENSITIVE = 70.0 / INPUT_BLOCK_TIME
MAX_TAP_BLOCKS = int(0.15 / INPUT_BLOCK_TIME)
REQUIRED_CLAPS = 2

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS + 1
        self.quietcount = 0
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_devices(self):
        device_index = None
        for i in range(self.pa.get_device_count()):
            devinfo = self.pa.get_device_info_by_index(i)
            if devinfo["maxInputChannels"] > 0:
                if "mic" in devinfo["name"].lower() or "input" in devinfo["name"].lower():
                    device_index = i
                    return device_index
        return None

    def open_mic_stream(self):
        device_index = self.find_input_devices()

        stream = self.pa.open(format=FORMAT,
                              channels=CHANNELS,
                              rate=RATE,
                              input=True,
                              input_device_index=device_index,
                              frames_per_buffer=INPUT_RATE_PER_BLOCK)
        return stream

    @staticmethod
    def get_rms(block):
        count = len(block) // 2
        format = "%dh" % count
        shorts = struct.unpack(format, block)
        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        return math.sqrt(sum_squares / count)

    def listen(self):
        try:
            block = self.stream.read(INPUT_RATE_PER_BLOCK, exception_on_overflow=False)
        except IOError as e:
            self.errorcount += 1
            print("(%d) Error Recording: %s" % (self.errorcount, e))
            self.noisycount = 5
            return False

        amplitude = self.get_rms(block)

        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                self.tap_threshold *= 1.1
            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return True
        else:
            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return True
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                self.tap_threshold *= 0.9

        return False

# Main function
def clap_detect():
    print("Listening for claps...")
    tt = TapTester()
    clap_count = 0

    try:
        while True:
            if tt.listen():
                clap_count += 1
                print(f"Clap #{clap_count}")
                if clap_count >= REQUIRED_CLAPS:
                    print("👏 Clap Detected!")
                    break
    finally:
        tt.stop()

# Run it
if __name__ == "__main__":
    clap_detect()
