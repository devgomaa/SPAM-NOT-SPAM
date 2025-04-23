import joblib 
import os 

model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
model = joblib.load(model_path)


def predict_spam (text): 
    predcion = model.predict([text])[0]
    return "spam" if predcion == 1 else "ham"