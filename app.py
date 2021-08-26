from logging import debug
from flask import Flask, render_template, redirect, request
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.io import curdoc
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
import pandas as pd

app = Flask(__name__)

pd_bok = pd.read_csv("C:\\Users\\kevec\\PycharmProjects\\SourceData\\IMDb movies\\IMDb movies.csv", low_memory=False)
pd_bok.fillna(0)
pd_test = pd_bok[pd_bok['imdb_title_id'] == 'tt0346647']
print(pd_test.head())
# pd_bok.dtypes

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/graph', methods=['GET', 'POST'])
def result_search():

    id = request.form['movie']
    pd_prot = pd_bok[pd_bok['imdb_title_id'] == id]

    source = ColumnDataSource()
    
    fig = figure(plot_height=600, plot_width=720, tooltips=[("Title", "@title"), ("Released", "@released")])
    fig.circle(x="x", y="y", source=source, size=8, color="color", line_color=None)
    fig.xaxis.axis_label = "Reviews from Users"
    fig.yaxis.axis_label = "Reviews from Critics"
    
    source.data = dict(
    x = list(pd_prot['reviews_from_users']),
    y = list(pd_prot['reviews_from_critics']),
    color = ["#FF9900" for i in list(pd_prot['title'])],
    title = list(pd_prot['title']),
    released = list(pd_prot['year']),
    imdbvotes = list(pd_prot['votes']),
    genre = list(pd_prot['genre'])
    )

    output_file("graph.html")
    script, div = components(fig)
    return  render_template('graph.html',
                            plot_script=script,
                            plot_div=div,
                            js_resources=INLINE.render_js(),
                            css_resources=INLINE.render_css(),
                            ).encode(encoding='UTF-8')



@app.route('/choice', methods=['GET','POST'])
def movie_input():
        
        if request.method == 'POST':
            return redirect('/graph')
        else:
            return render_template('form.html')
    

    
if __name__ == "__main__":
    app.run(debug=True)






