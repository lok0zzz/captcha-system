# Importações das libs.
from captcha.image import ImageCaptcha
import random
import string
from flask import Flask, render_template
import json

# Gerar Simbolos Aleatórios
def gerar_simbolos_aleatorios(n):
    caracteres = list(string.ascii_letters.lower() + string.digits)
    random.shuffle(caracteres)
    
    captcha_text = []
    for _ in range(n):
        captcha_text.append(random.choice(caracteres))
        
    return "".join(captcha_text)

texto = gerar_simbolos_aleatorios(6)

image = ImageCaptcha(width=200, height=90)
data = image.generate(texto)
image.write(texto, f'static/{texto}.png')

jobj = {'texto': texto}

# Site

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', res=json.dumps(jobj))