from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import logging

application = Flask(__name__)
CORS(application)  # This will enable CORS for all routes

app = application

# Configuring logging
logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

@app.route('/')
@cross_origin()
def home_page():
    """
    Home page route.
    Renders the main template (index.html).
    """
    logging.info("STEP 1: Accessing the homepage.")
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict_datapoint():
    """
    Route to predict gemstone price based on provided parameters.
    Handles both GET (rendering form) and POST (handling form submission and prediction) methods.
    """
    if request.method == 'GET':
        logging.info("STEP 1: Accessing the prediction form via GET request.")
        return render_template('index.html')
    else:
        logging.info("STEP 1: Received POST request for prediction.")
        
        logging.info("STEP 2: Extracting data from form submission.")
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        logging.info("STEP 3: Converting data to DataFrame format.")
        pred_df = data.get_data_as_dataframe()
        
        logging.info("STEP 4: Initializing prediction pipeline.")
        predict_pipeline = PredictPipeline()

        logging.info("STEP 5: Making price prediction using the model.")
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0], 2)

        logging.info(f"STEP 6: Returning predicted price: {results}")
        return render_template('index.html', results=results, pred_df=pred_df)

@app.route('/predictAPI', methods=['POST'])
@cross_origin()
def predict_api():
    """
    API route to predict gemstone price based on JSON data.
    Expects a POST request with JSON data.
    """
    logging.info("API STEP 1: Received POST request for prediction via API.")
    
    logging.info("API STEP 2: Extracting data from JSON payload.")
    data = CustomData(
        carat=float(request.json['carat']),
        depth=float(request.json['depth']),
        table=float(request.json['table']),
        x=float(request.json['x']),
        y=float(request.json['y']),
        z=float(request.json['z']),
        cut=request.json['cut'],
        color=request.json['color'],
        clarity=request.json['clarity']
    )

    logging.info("API STEP 3: Converting data to DataFrame format.")
    pred_df = data.get_data_as_dataframe()

    logging.info("API STEP 4: Initializing prediction pipeline.")
    predict_pipeline = PredictPipeline()

    logging.info("API STEP 5: Making price prediction using the model.")
    pred = predict_pipeline.predict(pred_df)

    dct = {'price': round(pred[0], 2)}

    logging.info(f"API STEP 6: Returning predicted price: {dct['price']}")
    return jsonify(dct)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
