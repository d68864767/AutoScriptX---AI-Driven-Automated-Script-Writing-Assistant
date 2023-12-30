```python
# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding

# Initialize tokenizer
tokenizer = Tokenizer()

def analyze_style_and_tone(script):
    """
    Analyze the style and tone of the script.
    """
    # Tokenize the script
    sequences = tokenizer.texts_to_sequences([script])

    # Load the pre-trained style and tone analysis model
    model = load_model('style_tone_model.h5')

    # Predict the style and tone of the script
    prediction = model.predict(sequences)

    return prediction

def load_model(model_path):
    """
    Load a pre-trained model.
    """
    # Load the model
    model = tf.keras.models.load_model(model_path)

    return model

def create_model():
    """
    Create a new style and tone analysis model.
    """
    # Define the model
    model = Sequential()
    model.add(Embedding(10000, 32))
    model.add(LSTM(32))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

    return model
```
