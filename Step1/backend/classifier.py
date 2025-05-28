import fasttext

MODEL_PATH = 'model.bin'

class PhishClassifier:
    def __init__(self):
        try:
            self.model = fasttext.load_model(MODEL_PATH)
        except:
            self.model = None

    def predict(self, text: str) -> float:
        if not self.model:
            keywords = ['login', 'password', 'verify', 'bank', 'card']
            score = 0.1 + 0.2 * sum(1 for k in keywords if k in text.lower())
            return min(score, 1.0)
        labels, probs = self.model.predict(text)
        return probs[0]
