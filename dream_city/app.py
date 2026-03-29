from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Функция для загрузки данных из JSON файла
def load_city_data():
    """Загружает данные о городе из data.json"""
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        # Если файл не найден, возвращаем тестовые данные
        return {
            "city_name": "Город моей мечты",
            "description": "Здесь будет описание вашего идеального города",
            "population": 0,
            "area": 0,
            "founded": 2024,
            "attractions": [
                {"name": "Достопримечательность 1", "description": "Описание", "image": "pic1.jpg"},
                {"name": "Достопримечательность 2", "description": "Описание", "image": "pic2.jpg"},
                {"name": "Достопримечательность 3", "description": "Описание", "image": "pic3.jpg"}
            ],
            "features": ["Особенность 1", "Особенность 2"],
            "images": ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg"]
        }

# Функция для получения списка изображений из папки img
def get_images_from_folder():
    """Автоматически получает все изображения из папки static/img/"""
    img_folder = os.path.join('static', 'img')
    images = []
    if os.path.exists(img_folder):
        for file in os.listdir(img_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                images.append(file)
    return images

# ==================== СТРАНИЦА 1: ГЛАВНАЯ ====================
@app.route('/')
def index():
    """Главная страница города мечты"""
    city_data = load_city_data()
    return render_template('index1.html', city=city_data)

# ==================== СТРАНИЦА 2: ДОСТОПРИМЕЧАТЕЛЬНОСТИ ====================
@app.route('/attractions')
def attractions():
    """Страница с подробным описанием достопримечательностей"""
    city_data = load_city_data()
    return render_template('attractions.html', city=city_data)

# ==================== СТРАНИЦА 3: ГАЛЕРЕЯ ====================
@app.route('/gallery')
def gallery():
    """Страница с галереей изображений"""
    city_data = load_city_data()
    # Получаем все изображения из папки img
    all_images = get_images_from_folder()
    # Если в JSON есть список изображений, используем его, иначе все из папки
    images_to_show = city_data.get('images', all_images) if city_data.get('images') else all_images
    return render_template('gallery.html', city=city_data, images=images_to_show)

# API endpoint для получения данных в формате JSON (опционально)
@app.route('/api/city')
def api_city():
    """Возвращает данные о городе в JSON формате"""
    return jsonify(load_city_data())

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)