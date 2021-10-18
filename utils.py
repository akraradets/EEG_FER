import pickle
import mne

def load_dat(path):
    with open(path, 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1' # It could be that the .dat files are created in python2 which needs this fancy line to decode
        p = u.load()
        return p

def numpy_to_raw(data, sample_rate, ch_names, unit = 'u'):
    if(unit==''):
        multiplyer = 1
    elif(unit == 'u'):
        multiplyer = 1e-6
    else:
        raise ValueError(f"unit can only be ['u']")
    
    ch_types = ['eeg'] * len(ch_names)
    ten_twenty_montage = mne.channels.make_standard_montage('standard_1020')

    info = mne.create_info(ch_names=ch_names, ch_types=ch_types, sfreq=sample_rate,)# verbose=False)

    raw = mne.io.RawArray(data * multiplyer, info,)# verbose=False)
    raw.set_montage(ten_twenty_montage)
    return raw