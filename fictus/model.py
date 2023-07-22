import pickle

news_classifier = pickle.load(open("fictus/models/news_classifier_model.model", "rb"))
fake_news_classifier = pickle.load(open("fictus/models/fake_news_classifier_model.model", "rb"))

def predict_news(message: str) -> str:
    if news_classifier.predict([message]) == [False]:
        return f"Menurut saya informasi HOAX\nTipe informasi {fake_news_classifier.predict(message)}"
    return "Menurut saya informasi BENAR."