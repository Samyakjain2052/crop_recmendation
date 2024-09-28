import pandas as pd
import numpy as np
import pickle

model=pickle.load(open('C:/Users/Hp/PycharmProjects/crop_prediction_web/crop_pred.sav','rb'))
pred=([[83,57,19,25.730444,70.747393,6.877869,98.737713]])
ans=model.predict(pred).astype('int')
print(ans)