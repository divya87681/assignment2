import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('C:\Users\Rajendran\Desktop\stream\model.pkl', 'rb'))

def predict(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall,output):
    input_data = np.array([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall,output]]).astype(np.float64)
    prediction = model.predict_proba(input_data)

    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Prediction")
    html_temp = """
    <div style="background-color:#e2062c;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("age")
    sex = st.text_input("sex")
    cp = st.text_input("cp")
    trtbps = st.text_input("trtbps")
    chol = st.text_input("chol")
    fbs = st.text_input("fbs")
    restecg = st.text_input("restecg")
    thalachh = st.text_input("thalachh")
    exng = st.text_input("exng")
    oldpeak = st.text_input("oldpeak")
    slp = st.text_input("slp")
    caa = st.text_input("caa")
    thall = st.text_input("thall")
    output = st.text_input("output")
    
    safe_html = """
    <div style="background-color:#32cd32;padding:10px">
    <h2 style="color:white;text-align:center;">Your heart is good</h2>
    </div>
    """
    danger_html = """
    <div style="background-color:#DC3545;padding:10px">
    <h2 style="color:black;text-align:center;">Your heart is bad</h2>
    </div>
    """
    if st.button("Predict"):
        output = predict()
        if output > 0.5:
            st.markdown(safe_html, unsafe_allow_html=True)
        else:
            st.markdown(danger_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
