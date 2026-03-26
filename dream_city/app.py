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
                {"name": "Достопримечательность 1", "description": "Описание"},
                {"name": "Достопримечательность 2", "description": "Описание"}
            ],
            "features": ["Особенность 1", "Особенность 2"]
        }

# Главная страница
@app.route('/')
def index():
    """Главная страница города мечты"""
    city_data = load_city_data()
    # 🔧 ЧТО ИЗМЕНИТЬ: 
    # - Можете добавить больше переменных для передачи в шаблон
    # - Можете создать несколько маршрутов для разных страниц
    return render_template('index1.html', city=city_data)

# API endpoint для получения данных в формате JSON (опционально)
@app.route('/api/city')
def api_city():
    """Возвращает данные о городе в JSON формате"""
    return jsonify(load_city_data())

# Дополнительный маршрут для страницы с достопримечательностями
@app.route('/attractions')
def attractions():
    """Страница с подробным описанием достопримечательностей"""
    city_data = load_city_data()
    # 🔧 ЧТО ИЗМЕНИТЬ:
    # - Создайте отдельный шаблон attractions.html
    # - Добавьте больше деталей о каждой достопримечательности
    return render_template('attractions.html', city=city_data)

# Дополнительный маршрут для галереи
@app.route('/gallery')
def gallery():
    """Страница с галереей изображений"""
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)