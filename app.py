import os
from flask import Flask, render_template
from pathlib import Path
app = Flask(__name__)
@app.route('/')
def home(): return render_template('index.html')
@app.route('/letter')
def letter(): return render_template('letter.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 7860)), debug=False)
