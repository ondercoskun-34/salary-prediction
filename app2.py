import streamlit as st
import pickle
st.title("SI ile maas tahmini yapan model :moneybag:")
model = pickle.load(open("salary.pkl", "rb"))
st.write("Model yüklendi.")
name = st.text_input("Adınızı girin:")
experience = st.number_input("Yıllık deneyiminizi girin:", 1,50)
test_score = st.number_input("Test puanınızı girin:", 1,10)
interview_score = st.number_input("Mülakat puanınızı girin:", 1,10)
if st.button("Tahmin et"):
    prediction = model.predict([[experience, test_score, interview_score]])
    
    st.write("Dear", name, "tahmin edilen maasiniz:", prediction)

# SI İle Maaş Tahmini Yapan Model :moneybag: