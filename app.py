from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    savings = 0
    if request.method == 'POST':
        try:
            income = float(request.form.get('income', 0) or 0)
            rent = float(request.form.get('rent', 0) or 0)
            food = float(request.form.get('food', 0) or 0)
            transport = float(request.form.get('transport', 0) or 0)
            
            total_expense = rent + food + transport
            savings = income - total_expense
            
            if savings < 0:
                result = f"Warning! Over budget by Rs.{abs(savings)}. Reduce expenses!"
            elif savings < (income * 0.2):
                result = f"Savings: Rs.{savings}. Try to save at least 20% of income."
            else:
                result = f"Great! You saved Rs.{savings}. Keep it up!"
        except Exception as e:
            result = f"Please enter valid numbers only!"
    
    return render_template('index.html', result=result, savings=savings)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
