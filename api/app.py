from flask import Flask, send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os
import random

app = Flask(__name__)

@app.route('/')
def get_watermarked_image():
    image_folder = 'img'  # Especifique o caminho para a pasta das imagens em seu computador
    image_files = os.listdir(image_folder)
    random_image = random.choice(image_files)

    image_path = os.path.join(image_folder, random_image)
    watermarked_image_path = add_watermark(image_path)

    return send_from_directory('.', watermarked_image_path)


def add_watermark(image_path):
    image = Image.open(image_path)
    width, height = image.size

    watermark_text = 'The Moon'  # Substitua pelo seu texto de marca d'água
    font = ImageFont.truetype('fontes/font.ttf', 50)  # Substitua pelo caminho da sua fonte e tamanho desejado

    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(watermark_text, font)

    # Gerar coordenadas X e Y aleatórias
    x = random.randint(0, width - text_width)
    y = random.randint(0, height - text_height)

    draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)  # Especifica a cor e transparência do texto

    watermarked_image_path = 'imge/marcada.png'  # Substitua pelo caminho para salvar a imagem marcada
    image.save(watermarked_image_path)

    return watermarked_image_path


if __name__ == '__main__':
    app.run()
