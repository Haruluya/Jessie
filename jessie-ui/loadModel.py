import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import librosa
from python_speech_features import mfcc
import pickle
import wave
import glob




def predict(filename,type):
    if type == "SixClas":
        pklName = "../resources.pkl"
        modelName = ".././SixClassModel.h5"
        with open(pklName, 'rb') as fr:
            [class2id, id2class, mfcc_mean, mfcc_std] = pickle.load(fr)

    else:
        pklName = "../jdresources.pkl"
        modelName = ".././JDClassModel.h5"
        with open(pklName, 'rb') as fr:
            [class2id, id2class, mfcc_mean, mfcc_std] = pickle.load(fr)
    print(class2id,id2class)
    mfcc_dim = 26
    model = load_model(modelName)
    path = filename


    sr = 16000
    min_length = 1 * sr
    slice_length = 3 * sr

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
    result = "预测结果为："+str(pred)+"("+str(prob)+")"

    return result




def load_and_trim(path, sr=16000,slice_length=3*16000):
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

#pcm格式转换为wav格式。
def pcm_to_wav(pcm_path, wav_path, channels=1, bits=16, sample_rate=16000):
    data = open(pcm_path, 'rb').read()
    fw = wave.open(wav_path, 'wb')
    fw.setnchannels(channels)
    fw.setsampwidth(bits // 8)
    fw.setframerate(sample_rate)
    fw.writeframes(data)
    fw.close()
    playsound("vedio.wav")




