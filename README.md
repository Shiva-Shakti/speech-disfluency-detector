# 🗣️ Speech Disfluency Detection
A Python tool that records your voice and detects disfluency (e.g., long pauses) using simple silence analysis.

## 📌 Features
- Records 5 seconds of live speech.
- Identifies silent segments using RMS threshold.
- Classifies speech as Fluent or Disfluent.
- Command-line based; real-time detection.

## 🧪 Sample Output
🎙 Speak now for 5 seconds...
✅ Audio saved.
Silent windows / total = 13/25 = 0.52

🔍 Result:
❌ Likely DISFLUENT (many short pauses)

## ⚙️ How It Works
- Divides the recorded audio into short 0.2-second chunks.
- Measures the RMS energy of each chunk.
- Flags low-energy chunks as silent.
- Calculates silence ratio = silent chunks / total chunks.
- Labels speech as "Disfluent" if silence ratio > 0.5.


## 🛠 Technologies Used
- Python
- NumPy
- SciPy
- SoundDevice

## 🚀 Installation
Install the dependencies:

```bash
pip install numpy scipy sounddevice



#### ✅ 7. **How to Run**
```markdown
## ▶️ Running the Project

```bash
python model.py
