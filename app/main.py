from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
from transformers import BertTokenizer, BertModel
from lib.bert import calculate_similarity, BERT

app = Flask(__name__)
assets = Environment(app)

scss = Bundle('styles.scss', filters='scss', output='gen/main.css')
assets.register('scss_all', scss)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BERT()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentence_one = ''
    sentence_two = ''
    result = 0.0

    if request.method == 'POST':
        sentence_one = request.form.get('sentence-one')
        sentence_two = request.form.get('sentence-two')

        result = calculate_similarity(model, tokenizer, sentence_one, sentence_two, device='cpu')
    return render_template('index.html', sentence_one=sentence_one, sentence_two=sentence_two, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
