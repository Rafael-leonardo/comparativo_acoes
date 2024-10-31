from flask import Flask, render_template, request, redirect, url_for
from commands.commands import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    available_stock = get_stock_list()
    symbol1= request.form.get("symbol1")
    symbol2= request.form.get("symbol2")


    if symbol1 and symbol2:
        data1 = get_stock_data(symbol1)
        data2 = get_stock_data(symbol2)
    
        if data1 is not None and data2 is not None:
            plot_path = plot_comparison(data1, data2, symbol1, symbol2)
            return redirect(url_for('show_plot', plot_path=plot_path))
        else:
            return redirect(url_for('show_plot', plot_path=plot_path))
        
    return render_template('index.html', stock_data=available_stock)

@app.route("/plot")
def show_plot():
    plot_path = request.args.get('plot_path')
    return render_template('plot.html', plot_path=plot_path)

