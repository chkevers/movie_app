from logging import debug
from flask import Flask, render_template, redirect
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.io import curdoc
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)