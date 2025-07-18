from tensorflow import keras
model=keras.models.load_model("brain_tumor_cnn_classifier.keras")
model.summary()