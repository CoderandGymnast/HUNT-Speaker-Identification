import numpy as np
from pyaudio import paInt16


# Signal processing
SAMPLE_RATE = 16000
PREEMPHASIS_ALPHA = 0.97
FRAME_LEN = 0.025
FRAME_STEP = 0.01
NUM_FFT = 512

# FILTER_RANGE = (300.,np.nextafter(3000,float('-inf')))  # frequency range to keep

# Recording options for realtime test
TEST_MODE = "online"
CHUNK = 1024
NUM_CHANNEL = 1
FORMAT = paInt16
ONLINE_RECORD_SEC = 1.5 
ONLINE_CONDITION = "Test"
ONLINE_SPEAKER = "Hung.VS"
AMBIENT_NAME="*ambient"


# Model
WEIGHTS_FILE = "data/model/weights.h5"
COST_METRIC = "cosine"  # euclidean or cosine
INPUT_SHAPE = (NUM_FFT,None,1)
MAX_SEC_ENROLL = 10
MAX_SEC_TEST = 4
BUCKET_STEP_SEC = 1
THRESHOLD=0.6


# Input/Output
ENROLL_WAV_DIR = "data/wav/enroll/"
ENROLL_LIST_FILE = "lst/batch_enroll_list.csv"
TEST_WAV_DIR = "data/wav/test_clean/"
TEST_LIST_FILE = "lst/batch_test_list.csv"

OFFLINE_RESULT_FILE = "res/results_online.csv"
OFFLINE_RESULT_WRITE_OPTION = 'w'  # 'a' or 'w'

ONLINE_WAV_FILE = "data/wav/test.wav"
ONLINE_RESULT_FILE = "res/results_online.csv"
ONLINE_RESULT_WRITE_OPTION = 'a'  # 'a' or 'w'



