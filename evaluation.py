import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

def evaluation_pipeline(x_test_path, y_test_path, model_path):
    
    x_data = pd.read_csv(x_test_path)
    y_true = pd.read_csv(y_test_path)
    
    
    loaded_scaler = load('models/scaler/standard scaler.pkl')
    
    x_data_normalized = loaded_scaler.transform(x_data)
   
    loaded_model = load(model_path)
    
   
    y_pred = loaded_model.predict(x_data_normalized)
    
   
    accuracy = loaded_model.score(x_data_normalized, y_true)
    
    return y_pred, accuracy
