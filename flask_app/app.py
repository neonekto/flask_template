from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Настройка папки для загрузки файлов
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    # Сохранение файла
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Здесь можно добавить логику обработки файла
    age, gender = process_file(file_path)

    return render_template('result.html', age=age, gender=gender)

def process_file(file_path):
    # Здесь добавьте свою логику для обработки файла
    # Например, вы можете использовать библиотеку для анализа данных
    # Это заглушка, замените на вашу логику
    return 25, 'Мужчина'  # Пример результата

if __name__ == '__main__':
    app.run(debug=True)
