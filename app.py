from flask import Flask, render_template
import pandas as pd
import os
app = Flask(__name__)

@app.route('/')
def home():
    
    my_dir = os.path.dirname(__file__)
    summary_filepath = os.path.join(my_dir, "summary.csv")
    # Read the CSV file
    
    data = pd.read_csv(summary_filepath)

    # Convert the dataframe into a dictionary for easier processing in the template
    data_dict = data.to_dict('records')

    # Render the template and pass the data
    return render_template('home.html', data=data_dict)

if __name__ == "__main__":
    app.run(debug=True)
