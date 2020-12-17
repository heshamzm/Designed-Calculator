from flask import Flask, render_template, url_for, request, redirect
import math

app = Flask(__name__)               



@app.route("/", methods=["GET", "POST"])
def calc():

    return render_template('calc.html')




# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == 'GET':
#         # render the add page
#         return render_template("add.html")
#     else:
#         # read the values from the form
#         n1 = int(request.form['n1'])   # read the value from the first number input
#         n2 = int(request.form['n2'])  # read the value from the second number input

#         return redirect(url_for("result", n1 = n1, n2 = n2, operation = 'add', answer = n1 + n2))




# @app.route("/subtract", methods=['GET', 'POST'])
# def subtract():
#     if request.method == 'GET':
#         # render the subtract method
#         return render_template("subtract.html")
#     else:
#         # read and cast the values from the form
#         n1 = int(request.form['n1'])
#         n2 = int(request.form['n2'])

#         answer = n1 - n2

#         # redirect the user to the result page
#         return redirect(url_for("result", n1 = n1, n2= n2, operation = 'subtract',answer=answer))



# @app.route("/multiply", methods=['GET', 'POST'])
# def multiply():
#     if request.method == 'GET':
#         # render the subtract method
#         return render_template("multiply.html")
#     else:
#         # read and cast the values from the form
#         n1 = int(request.form['n1'])
#         n2 = int(request.form['n2'])

#         # subtract the values
#         answer = n1 * n2

#         # redirect the user to the result page
#         return redirect(url_for("result", n1 = n1, n2= n2, operation = 'multiply', answer=answer))



# @app.route("/divide", methods=['GET', 'POST'])
# def divide():
#     if request.method == 'GET':
#         # render the subtract method
#         return render_template("divide.html")
#     else:
#         # read and cast the values from the form
#         n1 = int(request.form['n1'])
#         n2 = int(request.form['n2'])

#         # subtract the values
#         answer = n1 / n2

#         # redirect the user to the result page
#         return redirect(url_for("result", n1 = n1, n2= n2,  operation = 'divide', answer=answer))





# if __name__ == "__main__":       
#     app.run(debug=True)    
