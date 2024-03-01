from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

scss = Bundle('styles.scss', filters='scss', output='gen/main.css')
assets.register('scss_all', scss)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
