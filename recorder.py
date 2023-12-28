import soundfile as sf


def record(data, samplerate, file_name):
    file_name = f'{file_name}.wav'
    sf.write(file_name, data, samplerate)


def file_to_play(file_name):
    data, samplerate = sf.read(f'voices/{file_name}.wav')
    return data, samplerate
