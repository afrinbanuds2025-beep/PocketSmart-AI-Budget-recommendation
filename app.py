from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        income = float(request.form.get('income', 0))
        rent = float(request.form.get('rent', 0))
        food = float(request.form.get('food', 0))
        transport = float(request.form.get('transport', 0))
        savings = income - (rent + food + transport)
        
        if savings < 0:
            advice = "Selavu athigam! Budget-a kuraiyunga."
        elif savings < income * 0.2:
            advice = "Konjam save pannalam!"
        else:
            advice = "Super! Neenga nalla save panreenga!"

        result = {
            "income": income,
            "total_expense": rent + food + transport,
            "savings": savings,
            "advice": advice
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
