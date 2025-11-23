PredictX — Next Word Prediction (Markov Chain Model)

PredictX is a Python-based Next-Word Prediction system built using 1st, 2nd, and 3rd order Markov Chains.
Given a text dataset, the model learns word transitions and predicts the most likely next word based on user input.

📌 What This Project Does

Builds Markov Chain models from your text files

Supports 1st, 2nd, and 3rd order prediction

Saves trained models as JSON

Loads models to predict the next word typed by the user

Includes sample scripts for training and testing

Works on any custom dataset (not only Gutenberg/NLTK)

🧠 How It Works

A Markov Chain learns transitions like:

Word_A → Word_B (count: X)


The model uses these transition counts to compute probabilities and generate the most likely next word.

1st Order Example:
{
  "word_A": {"word_B": 3, "word_C": 1}
}

2nd Order Example:
{
  "word_A word_B": {"word_C": 2, "word_D": 1}
}


Higher order = more context = better predictions.

📁 Project Structure
PredictX/
├── chain.py
├── train1storder.py
├── train2ndorder.py
├── train3rdorder.py
├── user.py
├── retest.py
├── *.json (saved models)
└── pics/

🚀 Usage
🔹 Train Model
python train1storder.py
python train2ndorder.py
python train3rdorder.py

🔹 Predict Next Word
python user.py


Type something → press Enter → get prediction.

Press q to exit.

📝 Notes

Works with any .txt training file

NLTK Gutenberg corpora supported but optional

Trained models are saved automatically as .json

🧪 Testing
python retest.py


Loads an existing JSON model and checks transitions.

🖼 Examples

1st order prediction:

2nd order prediction:

3rd order prediction:

📜 License

MIT License

lic
