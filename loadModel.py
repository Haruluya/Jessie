import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import librosa
from python_speech_features import mfcc
import pickle
import wave
import glob

with open('resources.pkl', 'rb') as fr:
    [class2id, id2class, mfcc_mean, mfcc_std] = pickle.load(fr)

model = load_model('./SixClassModel.h5')
paths = glob.glob('data/*/dev/*/*/*.pcm')
path = np.random.choice(paths, 1)[0]
label = path.split('\\')[1]
print(label, path)

mfcc_dim = 13
sr = 16000
min_length = 1 * sr
slice_length = 3 * sr



# def predict(filename):
#     with open('resources.pkl', 'rb') as fr:
#         [class2id, id2class, mfcc_mean, mfcc_std] = pickle.load(fr)
#
#     model = load_model('./SixClassModel.h5')
#     paths = glob.glob('data/*/dev/*/*/*.pcm')
#     path = filename
#     label = path.split('\\')[1]
#     print(label, path)
#
#     mfcc_dim = 13
#     sr = 16000
#     min_length = 1 * sr
#     slice_length = 3 * sr
#     audio, slices = load_and_trim(path)
#     X_data = [mfcc(s, sr, numcep=mfcc_dim) for s in slices]
#     X_data = [(x - mfcc_mean) / (mfcc_std + 1e-14) for x in X_data]
#     maxlen = np.max([x.shape[0] for x in X_data])
#     X_data = pad_sequences(X_data, maxlen, 'float32', padding='post', value=0.0)
#     print(X_data.shape)
#
#     prob = model.predict(X_data)
#     prob = np.mean(prob, axis=0)
#     pred = np.argmax(prob)
#     prob = prob[pred]
#     pred = id2class[pred]
#     result = "预测结果为："+pred+"(+"+label+")"+"("+prob+")"
#     return result


def load_and_trim(path, sr=16000):
    audio = np.memmap(path, dtype='h', mode='r')
    audio = audio[2000:-2000]
    audio = audio.astype(np.float32)
    energy = librosa.feature.rms(audio)
    frames = np.nonzero(energy >= np.max(energy) / 5)
    indices = librosa.core.frames_to_samples(frames)[1]
    audio = audio[indices[0]:indices[-1]] if indices.size else audio[0:0]

    slices = []
    for i in range(0, audio.shape[0], slice_length):
        s = audio[i: i + slice_length]
        slices.append(s)

    return audio, slices


audio, slices = load_and_trim(path)
X_data = [mfcc(s, sr, numcep=mfcc_dim) for s in slices]
X_data = [(x - mfcc_mean) / (mfcc_std + 1e-14) for x in X_data]
maxlen = np.max([x.shape[0] for x in X_data])
X_data = pad_sequences(X_data, maxlen, 'float32', padding='post', value=0.0)
print(X_data.shape)

prob = model.predict(X_data)
prob = np.mean(prob, axis=0)
pred = np.argmax(prob)
prob = prob[pred]
pred = id2class[pred]
print('True:', label)
print('Pred:', pred, 'Confidence:', prob)