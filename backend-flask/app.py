from flask import Flask, request, render_template
import numpy as np 
import pandas as pd
from .pickle import soh_model, temp_model, soc_model
from .static import plot_json, plot_json_1, plot_json_2

app = Flask(__name__)

@app.route('/')
def home():
       
        return render_template('master_2_new.html')

@app.route('/soh', methods= ['POST', 'GET'])
def soh():
        file = request.files['file']
        df=pd.read_excel(file)
        # df= pd.read_csv(file)
        
        test_soh =df[['time', 'voltage_measured', 'current_measured', 'temperature_measured' ]]
        soh_pred = soh_model.predict(test_soh)
        df['soh_pred'] = soh_pred
        # print(soh_pred)

        test_temp =df[['voltage_measured', 'current_measured' ]]
        temp_pred = temp_model.predict(test_temp)
        df['temp_pred'] =temp_pred
        # print(temp_pred)

        test_soc = df[['voltage_measured', 'current_measured', 'temperature_measured' ]]
        soc_pred = soc_model.predict(test_soc)
        df['soc_pred'] = soc_pred
        # print(soc_pred)

        x = soc_pred
        p1 = 606.2
        p2 = -2235
        p3 = 3330
        p4 = -2569
        p5 = 1092
        p6 = -251
        p7 = 28.64
        p8 = 2.645
        #Curve Fitting Equation OCV
        y = p1*(x**7) + p2*(x**6) + p3*(x**5)+ p4*(x**4) + p5*(x**3) + p6*(x**2) +p7*x + p8
        ocv_pred = y
        df['ocv_pred'] = ocv_pred
        # print(ocv_pred)
        df['index'] = np.arange(1, len(df)+1)
        soc_text = df[['soh_pred','temp_pred','ocv_pred','soc_pred']].describe()
        df.to_excel('output_df.xlsx')
        df.to_csv('output.csv')
        # print(df.columns)
        

        op_xls=pd.read_excel('output_df.xlsx')
        return render_template('op_1.html',  plot_json=plot_json, plot_json_1= plot_json_1, plot_json_2= plot_json_2, soc_text=soc_text)
   
if __name__ == "__main__":
        app.run(debug = True)
        