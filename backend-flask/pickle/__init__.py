import pickle

soh_model = pickle.load(open('backend-flask/pickle/soh_rf_est.pkl', 'rb'))
temp_model =  pickle.load(open('backend-flask/pickle/temp_model.pkl', 'rb'))
soc_model = pickle.load(open('backend-flask/pickle/soc_model.pkl', 'rb'))