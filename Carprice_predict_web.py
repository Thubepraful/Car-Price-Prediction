

from flask import *
import pickle

app=Flask(__name__)

def make_pred(inps):
    model = pickle.load(open('price_pred.pkl','rb'))
    res=model.predict([inps])[0]
    return res

@app.route("/")
def home_fun():
    return render_template("main_form.html")

@app.route("/carprices",methods=["POST"])
def check_fun():
    make_in=int(request.form["make"])
    fuel_in=int(request.form["fuel"])
    body_in=int(request.form["body"])
    wheel_in=int(request.form["wheel"])
    engine_in=int(request.form["engine"])
    enginetype_in=int(request.form["engtype"])
    symbol_in=int(request.form["symbol"])
    normalized_in=int(request.form["normalized"])
    width_in=int(request.form["width"])
    height_in=int(request.form["height"])
    enginesize_in=int(request.form["engsize"])
    horsepower_in=int(request.form["hp"])
    citympg_in=int(request.form["citympg"])
    highwaympg_in=int(request.form["highwaympg"])

    ip_params=[make_in,fuel_in,body_in,wheel_in,engine_in,enginetype_in,symbol_in,normalized_in,width_in,
    height_in,enginesize_in,horsepower_in,citympg_in,highwaympg_in]

    result=make_pred(ip_params)
    return render_template("display_res.html",res=result)

if __name__=="__main__":
    app.run(debug=True)

