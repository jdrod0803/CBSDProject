from CBSD_Project_Flask import app, forms
from flask import request, render_template

@app.route('/', methods=['GET','POST']) #The function below this is executed every time we visit this url pattern
def search():
    searchForm = forms.AQIParameters(request.form)
    if request.method=="POST":
        parameter_chosen = request.form["aqiparameter"]
        parameter_requested = forms.aqi_parameter()[parameter_chosen]

        print(parameter_chosen)
        print(parameter_requested)
        parameter_unit = ""
        if parameter_chosen == "temperatureC":
            parameter_unit = "celsius"
        elif parameter_chosen == "pressure":
            parameter_unit = "inHg"
        elif parameter_chosen == "humidity":
            parameter_unit == "%"
        '''
        If the user makes a post request, please save the selected value by the user into a variable
        Also, call the function aqi_parameter (from forms.py) with all the results
        Then, render template parameter_result.html only with the parameter requested by the user
        Which means that you should assign the correct value for the variable parameter_requested below
        '''

        return render_template('parameter_result.html', result=parameter_requested, chosen = parameter_chosen,unit = parameter_unit)
    return render_template('parameter_search.html', form=searchForm)