from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"

def grammar_correction(input_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=input_text,
        max_tokens=100
    )
    corrected_text = response.choices[0].text.strip()
    return corrected_text

@app.route('/')
def index():
    return render_template('index.html', corrected_text='')

@app.route('/corrected_text', methods=['POST'])
def corrected_text():
    user_text = request.form['user_text']
    corrected_text = grammar_correction(user_text)
    return render_template('index.html', corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True)