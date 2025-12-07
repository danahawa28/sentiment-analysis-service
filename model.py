import pickle

def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

def predict_text(model, text):
    return model.predict([text])[0]
