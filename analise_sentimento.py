from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score




class SentimentoAnalyzer:

    
    def __init__(self):
        self.vectorizer = CountVectorizer()  # transformar os textos em vetores de contagem
        self.clf = MultinomialNB()           # variante de classificadores Naive Bayes
        self.is_trained = False              # verifica se o modelo foi treinado



    def train(self, textos, labels):
        X = self.vectorizer.fit_transform(textos)
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
        
        self.clf.fit(X_train, y_train)
        self.is_trained = True

        y_pred = self.clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Acurácia: {accuracy * 100:.2f}%")
        

    def predict_sentiment(self, text):
        if not self.is_trained:
            raise Exception("O modelo ainda não foi treinado.")
        
        text_vectorized = self.vectorizer.transform([text])
        prediction = self.clf.predict(text_vectorized)
        
        if prediction[0] == 1:
            return "Positivo"
        else:
            return "Negativo"




