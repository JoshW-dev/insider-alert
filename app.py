from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Read the CSV file
    filename="summary.csv"
    data = pd.read_csv('/home/JoshWDev/insider-alert/csv/'+filename)

    # Convert the dataframe into a dictionary for easier processing in the template
    data_dict = data.to_dict('records')

    # Render the template and pass the data
    return render_template('home.html', data=data_dict)

if __name__ == "__main__":
    app.run(debug=True)
