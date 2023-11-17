from flask import Flask
from flask import request
from flask import render_template
import random
import string
import subprocess

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio_equalizer')
def audio_editor():
    return render_template('audio_editor.html')

@app.route('/code', methods=['GET', 'POST'])
def code_editor():
    if request.method == 'POST':
        code = request.form['code']
        result = execute_code(code)
        return render_template('code_editor.html', code=code, result=result)
    return render_template('code_editor.html')

def execute_code(code):
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

# 2. Страница "Home"
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/code')
def code():
    return render_template('code_editor.html')

@app.route('/slider')
def slider():
    return render_template('slider.html')

# 3. Страница "About"
@app.route('/about')
def about():
    return render_template('about.html')

# 1. Бросок монетки
@app.route('/coinflip')
def coinflip():
    result = "Орёл" if random.choice([0, 1]) == 0 else "Решка"
    return render_template('result.html', result=result)

# 2. Генератор паролей
@app.route('/password')
def generate_password():
    password_length = 8  # Задайте желаемую длину пароля
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    return render_template('result.html', result=password)

# 3. Случайная картинка
@app.route('/random_image')
def random_image():
    # Здесь вы можете заменить список изображений на свой собственный
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    random_image = random.choice(images)
    return render_template('image.html', image=random_image)

@app.route('/random_text_letters')
def random_text_letters():
    texts = [
        "Дизайн!!!",
        "Купите мне хлеба...",
        "От Кирюши который устал :_)",
        "Возможно это не конец...",
        "Все что я сделал, не от меня! Я делаю не сам!",
        "Спасибо за внимание...",
        "ЭТО САМЫЙ РЕДКИЙ ТЕКСТ!!!",
        "чегото чат гпт напридумал там...",
        "привет!!!",
        "добавь меня в рублокс= l1f3rj",
        "2+2=4 дада",
        "пока",
    ]
    random_text = random.choice(texts)
    return render_template('random_text_letters.html', random_text=random_text)

@app.route('/random_text')
def random_text():
    # Здесь вы можете добавить свои собственные тексты или использовать библиотеку lorem ipsum
    texts = [
        "Дизайн!!!",
        "Купите мне хлеба...",
        "От Кирюши который устал :_)",
        "Возможно это не конец...",
        "Все что я сделал, не от меня! Я делаю не сам!",
        "Спасибо за внимание...",
        "ЭТО САМЫЙ РЕДКИЙ ТЕКСТ!!!",
        "чегото чат гпт напридумал там...",
        "привет!!!",
        "добавь меня в рублокс= l1f3rj",
        "2+2=4 дада",
        "пока",
    ]
    random_text = random.choice(texts)
    return render_template('random_text.html', random_text=random_text)

@app.route('/animations')
def animations():
    return render_template('animations.html')

@app.route('/text_animations')
def text_animations():
    return render_template('text_animations.html')

@app.route('/hover_animations')
def hover_animations():
    return render_template('hover_animations.html')

@app.route('/button_click_animations')
def button_click_animations():
    return render_template('button_click_animations.html')

@app.route('/interactive_objects')
def interactive_objects():
    return render_template('interactive_objects.html')

@app.route('/disco')
def disco():
    return render_template('disco.html')

if __name__ == '__main__':
    app.run(debug=True)
