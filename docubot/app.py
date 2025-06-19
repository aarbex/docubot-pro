from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from index_docs import index_documents
from query_engine import query_rag

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'docs'

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta = None
    pergunta = None

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                index_documents()  # Atualiza o FAISS com novos documentos
                return redirect(url_for('index'))

        pergunta = request.form.get('pergunta')
        if pergunta:
            resposta = query_rag(pergunta)

    return render_template('index.html', resposta=resposta, pergunta=pergunta)

if __name__ == '__main__':
    os.makedirs('docs', exist_ok=True)
    app.run(debug=True)
