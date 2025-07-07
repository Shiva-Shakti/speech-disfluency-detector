import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavz

# CONFIG
FILENAME = "speech.wav"
DURATION = 5          # seconds
FS = 16000            # sampling rate
SILENCE_THRESH = 200  # below this RMS is considered “silence”
SILENCE_WINDOW = 0.2  # seconds


def record_audio():
    print("🎙 Speak now for 5 seconds...")
    rec = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, dtype='int16')
    sd.wait()
    wavz.write(FILENAME, FS, rec)
    print("✅ Audio saved.")


def detect_disfluency(audio_path=FILENAME):
    rate, audio = wavz.read(audio_path)
    audio = audio.flatten()
    window_size = int(SILENCE_WINDOW * rate)
    silent_windows = 0
    total_windows = len(audio) // window_size

    for i in range(total_windows):
        chunk = audio[i * window_size : (i + 1) * window_size]
        rms = np.sqrt(np.mean(chunk.astype(np.float32)**2))
        if rms < SILENCE_THRESH:
            silent_windows += 1

    silence_ratio = silent_windows / total_windows
    print(f"Silent windows / total = {silent_windows}/{total_windows} = {silence_ratio:.2f}")

    # Heuristics: if more than 30% windows are silent → disfluent
    return silence_ratio > 0.5


def main():
    record_audio()
    is_disfluent = detect_disfluency()
    print("\n🔍 Result:")
    if is_disfluent:
        print("❌ Likely DISFLUENT (many short pauses)")
    else:
        print("✅ Likely FLUENT (smooth speech)")


if __name__ == "__main__":
    main()