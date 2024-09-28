import streamlit as st
import numpy as np
import pickle

model=pickle.load(open('C:/Users/Hp/PycharmProjects/crop_prediction_web/crop_pred.sav','rb'))


def predict(input_data):

    input_data_as_array=np.asarray(input_data)
    input_data_reshape=input_data_as_array.reshape(1,-1)


    ans = model.predict(input_data_reshape).astype('int')
    if ans[0]==1 :return 'rice'
    elif ans[0]==2 :return 'maize'
    elif ans[0]==3 :return 'chickpea'
    elif ans[0]==4 :return 'kidneybeans'
    elif ans[0]==5 :return 'pigeonpeas'
    elif ans[0]==6 :return 'mothbeans'
    elif ans[0]==7 :return 'mungbean'
    elif ans[0]==8 :return 'blackgram'
    elif ans[0]==9 :return 'lentil'
    elif ans[0]==10 :return 'pomegranate'
    elif ans[0]==11 :return 'banana'
    elif ans[0]==12 :return 'mango'
    elif ans[0]==13 :return 'grapes'
    elif ans[0]==14 :return 'watermelon'
    elif ans[0]==15 :return 'muskmelon'
    elif ans[0]==17 :return 'apple'
    elif ans[0]==18 :return 'orange'
    elif ans[0]==19 :return 'papaya'
    elif ans[0]==20 :return 'coconut'
    elif ans[0]==21 :return 'cotton'
    elif ans[0]==22 :return 'jute'
    elif ans[0]==23 :return 'coffee'




def main():
    st.title('Crop Prediction')

    N=st.text_input('Nitrogen')
    P = st.text_input('phos')
    K = st.text_input('K')
    temperature = st.text_input('Temperature')
    humidity = st.text_input('humidity')
    ph=st.text_input('ph Value')
    rainfall = st.text_input('rainfall')

    data=''
    if st.button('Best crop'):
        data=predict([N,P,K,temperature,humidity,ph,rainfall])


    st.success(data)






