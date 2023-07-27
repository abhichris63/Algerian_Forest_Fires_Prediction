from flask import Flask,render_template,request
from flask_cors import cross_origin # Cross-Origin Resources Sharing
import pandas as pd
import numpy as np
import pickle
from Mongodb import MongodbConnection
from Logger import log

# Flask instance
app = Flask(__name__)

# Models
regression_model = pickle.load(open('models/regression.pkl','rb'))
classification_model = pickle.load(open('models/classification.pkl','rb'))
rand_forest_ss = pickle.load(open('models/rforest_standardisation.pkl','rb'))



# Home route for Web home page
@app.route('/')
# It is bases on HTTP headers. CORS enables secure 
# communication between browsers & servers from different resources.
@cross_origin()
def home():
    return render_template('home.html')



# Route for choosing single or bulk predictions
@app.route('/chooseinput',methods=['POST','GET'])
@cross_origin()
def chooseinput():
    try:
        choose = request.form['choose']
        log.info('Rendering prediction type page')
        if choose == 'Single_input':
            return render_template('singleprediction.html')
        else:
            return render_template('bulkprediction.html')
    except:
            log.error('Error while rendering prediction type page')
                


# Route for Single Prediction for Classification Model
@app.route('/c_prediction',methods=['POST','GET'])
def c_prediction():
    try:     
        all_values = [float(ele) for ele in request.form.values()]
        np_values = [np.array(all_values)]
        # Standardization model
        ss_transform = rand_forest_ss.transform(np_values)
        # classification model
        cls_pred = classification_model.predict(ss_transform)[0]
        log.info('inputs collected from webpage classification model prediction done.')
        # If Model predicts 0 it is safe, if it predicts 1 than it is danger
        if cls_pred == 0:
            comment  = 'Forest is Safe!'
        else:
            comment = 'Warning!!! Forest is in Danger!'
        return render_template('singleprediction.html', Predict_C = "{} --- Predicted {}".format(comment, cls_pred))
    except Exception as e:
         log.error('Something went wrong while predicting classification model',e)
         return render_template('singleprediction.html', Predict_C = 'Warning!!! Check the input')



# Route for Single Prediction for Regression Model
@app.route('/r_prediction',methods=['POST','GET'])
def r_prediction():
    try:
        all_values = [float(ele) for ele in request.form.values()]
        np_values = [np.array(all_values)]
        # Standardization model
        ss_transform = rand_forest_ss.transform(np_values)
        # Regression model
        reg_pred = regression_model.predict(ss_transform)
        log.info('inputs collected from webpage regression model prediction done.')
        # if regression model predicts greater than 15 forest is in danger.
        # if its predicts lesser than 15 than forest is Safe.
        if reg_pred > 15:
            comment = 'Warning!!!--High Hazard rating'
        else:
            comment = 'Forest is Safe ! --- Low Hazard rating'
        return render_template('singleprediction.html',Predict_R = "{} Fuel Moiture Code Index is {}".format(comment,reg_pred))
    except Exception as e:
         log.error("Something went wrong while predicting classification model",e)
         return render_template('singleprediction.html',Predict_R = 'Warning!!! check the input')



# Route for Bulk prediction data is retrieved from Mongodb and predicts. 
# Finally gives the best results for classification & regression.
@app.route('/bulk_prediction',methods=['POST','GET'])
def bulk_prediction():
        try:
            #MongoDB Connection
            databasename = request.form['database_name']
            col_name = request.form['collection_name']
            # Client connection
            client_config  = MongodbConnection(f'{databasename}',f'{col_name}','itsabhichrishere','test')
            log.info('Mongodb client is established successfully')
            # returns list of cursor 
            fetching_all_records = client_config.fetchrecords()
            log.info('Dataset is fetched from mongodb Successfully')
            # Converting list of cursor to DataFrame
            df = pd.DataFrame(fetching_all_records)
            log.info('Dataset from Mongodb, Is converted from list to DataFrame ')
            # Droping _id feature
            df.drop('_id',axis=1,inplace=True)
            # Does not required last 2 features because FWI is dependent feature for regression.
            # Classes is dependent feature for Classification.
            imp_features = df.iloc[:,:-2]
            # print(imp_features)
            # first row from the DataFrame
            first_row = client_config.bulk_results()
            result = pd.DataFrame(first_row)
            log.info('first row from DataFrame is returned Successfully')
            # Standardization model
            ss_transform = rand_forest_ss.transform(imp_features)
            # classification model
            c_pred = classification_model.predict(ss_transform)[0]
            # Regression model
            r_pred = regression_model.predict(ss_transform)[0]
            log.info('Bulk prediction Done for Regression & Classification...')
            return render_template('bulk_results.html',r_pred="{:.2f}".format(r_pred),c_pred=c_pred,results = result)
        except Exception as e:
             log.error('Error while fetching Bulk Results',e)
             


# It Allows You to Execute Code When the File Runs as a Script
# Turning on the debug mode will restart the server automatically after every change.
# app.run starts the app
if __name__ == '__main__':
    app.run(debug=True)