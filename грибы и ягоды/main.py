import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class MushroomBerryApp:
    def __init__(self, window):
        self.window = window
        self.window.title("🍄 Справочник грибов и ягод 🍓")
        self.window.geometry("1200x750")
        self.window.minsize(900, 600)
        self.window.configure(bg="#1a1a2e")
        
        # Цветовая схема (современная, темная тема с акцентами)
        self.colors = {
            'bg_dark': '#1a1a2e',
            'bg_medium': '#16213e',
            'bg_light': '#0f3460',
            'accent_green': '#2ecc71',
            'accent_red': '#e74c3c',
            'accent_yellow': '#f1c40f',
            'text_light': '#ecf0f1',
            'text_dark': '#2c3e50',
            'card_bg': '#ffffff',
            'success': '#27ae60',
            'danger': '#c0392b'
        }
        
        # Данные о грибах и ягодах
        self.mushrooms_data = {
            "Белый гриб": {
                "desc": "Съедобный гриб первой категории. Имеет массивную коричневую шляпку и толстую светлую ножку. Ценится за превосходный вкус и аромат. Растет в лиственных и смешанных лесах.",
                "edible": True,
                "category": "Гриб",
                "season": "Июнь-Сентябрь"
            },
            "Мухомор": {
                "desc": "ЯДОВИТЫЙ гриб! Ярко-красная шляпка с характерными белыми хлопьями. Содержит токсичные вещества, вызывающие тяжелое отравление и галлюцинации. Категорически запрещен к употреблению!",
                "edible": False,
                "category": "Гриб",
                "season": "Июль-Октябрь"
            },
            "Подосиновик": {
                "desc": "Съедобный гриб с характерной оранжево-красной шляпкой. Мякоть на срезе синеет. Обладает нежным вкусом и плотной текстурой. Растет преимущественно под осинами.",
                "edible": True,
                "category": "Гриб",
                "season": "Июнь-Сентябрь"
            },
            "Ложный опенок": {
                "desc": "ЯДОВИТЫЙ двойник съедобного опенка. Отличается отсутствием кольца на ножке и более яркой серно-желтой окраской. Вызывает серьезное желудочно-кишечное отравление!",
                "edible": False,
                "category": "Гриб",
                "season": "Август-Октябрь"
            },
            "Земляника": {
                "desc": "Съедобная лесная ягода. Мелкие ароматные плоды ярко-красного цвета с множеством семян на поверхности. Богата витамином C и антиоксидантами. Растет на солнечных полянах.",
                "edible": True,
                "category": "Ягода",
                "season": "Июнь-Июль"
            },
            "Волчья ягода": {
                "desc": "СМЕРТЕЛЬНО ЯДОВИТАЯ ягода! Ярко-красные блестящие плоды, собранные в кисти. Все части растения содержат опасные токсины. Даже несколько ягод могут вызвать летальный исход!",
                "edible": False,
                "category": "Ягода",
                "season": "Июль-Август"
            },
            "Малина": {
                "desc": "Съедобная ягода, известная своими целебными свойствами. Сладкие ароматные плоды используются в народной медицине как жаропонижающее средство. Растет на лесных опушках и вырубках.",
                "edible": True,
                "category": "Ягода",
                "season": "Июль-Август"
            },
            "Черника": {
                "desc": "Съедобная ягода иссиня-черного цвета с восковым налетом. Улучшает зрение и богата антиоксидантами. Растет в хвойных лесах, часто образует обширные заросли.",
                "edible": True,
                "category": "Ягода",
                "season": "Июль-Август"
            },
            "Бледная поганка": {
                "desc": "СМЕРТЕЛЬНО ЯДОВИТЫЙ гриб! Самый опасный гриб в мире. Содержит аматоксины, разрушающие печень. Смертельная доза - всего 30 граммов. Не имеет противоядия!",
                "edible": False,
                "category": "Гриб",
                "season": "Июль-Октябрь"
            },
            "Лисичка": {
                "desc": "Съедобный гриб характерного желтого цвета с волнистым краем шляпки. Никогда не бывает червивым. Обладает приятным фруктовым ароматом и нежной мякотью.",
                "edible": True,
                "category": "Гриб",
                "season": "Июнь-Сентябрь"
            },
            "Клюква": {
                "desc": "Съедобная болотная ягода. Кислые красные плоды богаты витамином C и бензойной кислотой, что обеспечивает длительное хранение. Собирают поздней осенью.",
                "edible": True,
                "category": "Ягода",
                "season": "Сентябрь-Ноябрь"
            },
            "Вороний глаз": {
                "desc": "ЯДОВИТАЯ ягода! Одиночная синевато-черная ягода на верхушке стебля с четырьмя листьями. Все части растения токсичны. Вызывает нарушение сердечного ритма!",
                "edible": False,
                "category": "Ягода",
                "season": "Июль-Август"
            }
        }
        
        # Создаем красивые изображения-заглушки
        self.create_placeholder_images()
        
        # Избранное
        self.favorites = []
        
        # Создаем интерфейс
        self.setup_ui()
        
        # Привязываем события
        self.window.bind('<Configure>', self.on_window_resize)
        
    def create_placeholder_images(self):
        """Создает стильные изображения-заглушки для каждого вида"""
        for name, data in self.mushrooms_data.items():
            # Создаем изображение 300x300
            img = Image.new('RGB', (300, 300), color='#f8f9fa')
            draw = ImageDraw.Draw(img)
            
            # Рисуем рамку
            draw.rectangle([5, 5, 295, 295], outline='#dee2e6', width=2)
            
            # Определяем эмодзи в зависимости от типа и съедобности
            if data['category'] == 'Гриб':
                emoji = '🍄' if data['edible'] else '☠️🍄'
                color = '#2ecc71' if data['edible'] else '#e74c3c'
            else:
                emoji = '🍓' if data['edible'] else '☠️🍓'
                color = '#2ecc71' if data['edible'] else '#e74c3c'
            
            # Рисуем круг
            draw.ellipse([75, 75, 225, 225], fill=color, outline='#2c3e50', width=3)
            
            # Добавляем текст с эмодзи (используем простой текст, так как не все шрифты поддерживают эмодзи)
            try:
                font = ImageFont.truetype("arial.ttf", 60)
            except:
                font = ImageFont.load_default()
            
            # Рисуем текст
            text_bbox = draw.textbbox((0, 0), emoji, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (300 - text_width) // 2
            text_y = (300 - text_height) // 2
            draw.text((text_x, text_y), emoji, fill='white', font=font)
            
            # Добавляем название
            try:
                small_font = ImageFont.truetype("arial.ttf", 16)
            except:
                small_font = ImageFont.load_default()
            
            name_text = name[:15] + '...' if len(name) > 15 else name
            text_bbox = draw.textbbox((0, 0), name_text, font=small_font)
            text_width = text_bbox[2] - text_bbox[0]
            text_x = (300 - text_width) // 2
            draw.text((text_x, 260), name_text, fill='#2c3e50', font=small_font)
            
            data['image'] = ImageTk.PhotoImage(img)
    
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        
        # Главный контейнер с градиентным фоном
        self.main_container = tk.Frame(self.window, bg=self.colors['bg_dark'])
        self.main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Левая панель
        self.setup_left_panel()
        
        # Правая панель
        self.setup_right_panel()
        
        # Настройка весов для адаптивности
        self.main_container.grid_columnconfigure(0, weight=3)  # Левая панель
        self.main_container.grid_columnconfigure(1, weight=7)  # Правая панель
        self.main_container.grid_rowconfigure(0, weight=1)
    
    def setup_left_panel(self):
        """Настройка левой панели с поиском и избранным"""
        
        # Контейнер левой панели
        left_panel = tk.Frame(self.main_container, bg=self.colors['bg_medium'])
        left_panel.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        left_panel.grid_propagate(False)
        
        # Заголовок
        title_frame = tk.Frame(left_panel, bg=self.colors['bg_light'], height=60)
        title_frame.pack(fill='x', pady=(0, 15))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text='🔍 Поиск', 
                               font=('Segoe UI', 16, 'bold'),
                               bg=self.colors['bg_light'], fg=self.colors['text_light'])
        title_label.pack(expand=True)
        
        # Поисковая строка
        search_frame = tk.Frame(left_panel, bg=self.colors['bg_medium'])
        search_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.update_list)
        
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                                font=('Segoe UI', 12),
                                bg=self.colors['card_bg'],
                                fg=self.colors['text_dark'],
                                relief='flat',
                                highlightthickness=1,
                                highlightcolor=self.colors['accent_green'],
                                highlightbackground=self.colors['bg_light'])
        search_entry.pack(fill='x', ipady=8)
        
        # Список растений
        list_container = tk.Frame(left_panel, bg=self.colors['bg_medium'])
        list_container.pack(fill='both', expand=True, padx=15)
        
        # Canvas с прокруткой для списка
        self.list_canvas = tk.Canvas(list_container, bg=self.colors['bg_medium'],
                                     highlightthickness=0)
        list_scrollbar = tk.Scrollbar(list_container, orient='vertical',
                                      command=self.list_canvas.yview)
        self.list_frame = tk.Frame(self.list_canvas, bg=self.colors['bg_medium'])
        
        self.list_frame.bind('<Configure>', 
                            lambda e: self.list_canvas.configure(scrollregion=self.list_canvas.bbox('all')))
        
        self.list_canvas.create_window((0, 0), window=self.list_frame, anchor='nw')
        self.list_canvas.configure(yscrollcommand=list_scrollbar.set)
        
        self.list_canvas.pack(side='left', fill='both', expand=True)
        list_scrollbar.pack(side='right', fill='y')
        
        # Разделитель
        separator = tk.Frame(left_panel, bg=self.colors['bg_light'], height=2)
        separator.pack(fill='x', padx=15, pady=10)
        
        # Заголовок избранного
        fav_title_frame = tk.Frame(left_panel, bg=self.colors['bg_medium'])
        fav_title_frame.pack(fill='x', padx=15)
        
        fav_icon = tk.Label(fav_title_frame, text='⭐', 
                           font=('Segoe UI', 14),
                           bg=self.colors['bg_medium'], fg=self.colors['accent_yellow'])
        fav_icon.pack(side='left')
        
        fav_label = tk.Label(fav_title_frame, text='Избранное',
                            font=('Segoe UI', 12, 'bold'),
                            bg=self.colors['bg_medium'], fg=self.colors['text_light'])
        fav_label.pack(side='left', padx=5)
        
        # Список избранного
        fav_container = tk.Frame(left_panel, bg=self.colors['bg_medium'])
        fav_container.pack(fill='both', expand=True, padx=15, pady=(5, 10))
        
        self.fav_canvas = tk.Canvas(fav_container, bg=self.colors['bg_medium'],
                                    highlightthickness=0)
        fav_scrollbar = tk.Scrollbar(fav_container, orient='vertical',
                                     command=self.fav_canvas.yview)
        self.fav_frame = tk.Frame(self.fav_canvas, bg=self.colors['bg_medium'])
        
        self.fav_frame.bind('<Configure>',
                           lambda e: self.fav_canvas.configure(scrollregion=self.fav_canvas.bbox('all')))
        
        self.fav_canvas.create_window((0, 0), window=self.fav_frame, anchor='nw')
        self.fav_canvas.configure(yscrollcommand=fav_scrollbar.set)
        
        self.fav_canvas.pack(side='left', fill='both', expand=True)
        fav_scrollbar.pack(side='right', fill='y')
        
        # Кнопка теста
        test_button_frame = tk.Frame(left_panel, bg=self.colors['bg_medium'])
        test_button_frame.pack(side='bottom', fill='x', padx=15, pady=15)
        
        self.test_button = tk.Button(test_button_frame,
                                     text='📝 ПРОЙТИ ТЕСТ',
                                     font=('Segoe UI', 13, 'bold'),
                                     bg=self.colors['accent_yellow'],
                                     fg=self.colors['bg_dark'],
                                     relief='flat',
                                     cursor='hand2',
                                     command=self.open_test_window)
        self.test_button.pack(fill='x', ipady=12)
        
        # Привязываем события ховера
        self.test_button.bind('<Enter>', lambda e: self.test_button.configure(bg='#f39c12'))
        self.test_button.bind('<Leave>', lambda e: self.test_button.configure(bg=self.colors['accent_yellow']))
    
    def setup_right_panel(self):
        """Настройка правой панели с информацией о растении"""
        
        # Контейнер правой панели
        right_panel = tk.Frame(self.main_container, bg=self.colors['card_bg'])
        right_panel.grid(row=0, column=1, sticky='nsew')
        right_panel.grid_propagate(False)
        
        # Внутренний контейнер с отступами
        inner_panel = tk.Frame(right_panel, bg=self.colors['card_bg'])
        inner_panel.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Контейнер для изображения
        image_frame = tk.Frame(inner_panel, bg=self.colors['card_bg'])
        image_frame.pack(pady=(0, 20))
        
        self.image_label = tk.Label(image_frame, bg=self.colors['card_bg'])
        self.image_label.pack()
        
        # Название растения
        self.name_label = tk.Label(inner_panel, text='',
                                   font=('Segoe UI', 24, 'bold'),
                                   bg=self.colors['card_bg'], fg=self.colors['text_dark'])
        self.name_label.pack()
        
        # Категория и сезон
        info_frame = tk.Frame(inner_panel, bg=self.colors['card_bg'])
        info_frame.pack(pady=10)
        
        self.category_label = tk.Label(info_frame, text='',
                                       font=('Segoe UI', 12),
                                       bg=self.colors['card_bg'], fg='#7f8c8d')
        self.category_label.pack(side='left', padx=5)
        
        self.season_label = tk.Label(info_frame, text='',
                                     font=('Segoe UI', 12),
                                     bg=self.colors['card_bg'], fg='#7f8c8d')
        self.season_label.pack(side='left', padx=5)
        
        # Статус съедобности
        self.status_frame = tk.Frame(inner_panel)
        self.status_frame.pack(pady=10)
        
        self.status_label = tk.Label(self.status_frame, text='',
                                     font=('Segoe UI', 14, 'bold'),
                                     padx=20, pady=8)
        self.status_label.pack()
        
        # Описание
        desc_frame = tk.Frame(inner_panel, bg='#f8f9fa', relief='flat')
        desc_frame.pack(fill='both', expand=True, pady=(10, 0))
        
        self.desc_text = tk.Text(desc_frame,
                                 font=('Segoe UI', 12),
                                 bg='#f8f9fa',
                                 fg=self.colors['text_dark'],
                                 wrap='word',
                                 relief='flat',
                                 padx=15,
                                 pady=15,
                                 height=8,
                                 borderwidth=1,
                                 highlightthickness=1,
                                 highlightcolor='#dee2e6',
                                 highlightbackground='#dee2e6')
        self.desc_text.pack(fill='both', expand=True)
        self.desc_text.config(state='disabled')
    
    def update_list(self, *args):
        """Обновление списка растений с учетом поиска"""
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        search_term = self.search_var.get().lower()
        
        for name in self.mushrooms_data.keys():
            if search_term in name.lower():
                self.create_list_item(name)
    
    def create_list_item(self, name):
        """Создание элемента списка"""
        data = self.mushrooms_data[name]
        is_fav = name in self.favorites
        
        # Контейнер элемента
        item_frame = tk.Frame(self.list_frame, bg=self.colors['bg_medium'])
        item_frame.pack(fill='x', pady=2)
        
        # Фон при наведении
        def on_enter(e):
            item_frame.configure(bg=self.colors['bg_light'])
            name_label.configure(bg=self.colors['bg_light'])
            star_btn.configure(bg=self.colors['bg_light'])
        
        def on_leave(e):
            item_frame.configure(bg=self.colors['bg_medium'])
            name_label.configure(bg=self.colors['bg_medium'])
            star_btn.configure(bg=self.colors['bg_medium'])
        
        # Звездочка избранного
        star_char = '★' if is_fav else '☆'
        star_color = self.colors['accent_yellow'] if is_fav else '#95a5a6'
        
        star_btn = tk.Label(item_frame, text=star_char,
                           font=('Segoe UI', 14),
                           bg=self.colors['bg_medium'],
                           fg=star_color,
                           cursor='hand2')
        star_btn.pack(side='left', padx=(5, 10))
        star_btn.bind('<Button-1>', lambda e, n=name: self.toggle_favorite(n))
        
        # Иконка категории
        icon = '🍄' if data['category'] == 'Гриб' else '🍓'
        icon_label = tk.Label(item_frame, text=icon,
                             font=('Segoe UI', 12),
                             bg=self.colors['bg_medium'])
        icon_label.pack(side='left', padx=(0, 5))
        
        # Название
        name_label = tk.Label(item_frame, text=name,
                             font=('Segoe UI', 11),
                             bg=self.colors['bg_medium'],
                             fg=self.colors['text_light'],
                             anchor='w',
                             cursor='hand2')
        name_label.pack(side='left', fill='x', expand=True)
        
        # Привязка событий
        for widget in [item_frame, name_label, icon_label]:
            widget.bind('<Enter>', on_enter)
            widget.bind('<Leave>', on_leave)
            widget.bind('<Button-1>', lambda e, n=name: self.show_info(n))
    
    def update_favorites_display(self):
        """Обновление отображения избранного"""
        for widget in self.fav_frame.winfo_children():
            widget.destroy()
        
        if not self.favorites:
            empty_label = tk.Label(self.fav_frame,
                                  text='Нет избранных растений\nНажмите ☆ чтобы добавить',
                                  font=('Segoe UI', 10),
                                  bg=self.colors['bg_medium'],
                                  fg='#95a5a6',
                                  justify='center')
            empty_label.pack(pady=20)
            return
        
        for name in self.favorites:
            data = self.mushrooms_data[name]
            
            item_frame = tk.Frame(self.fav_frame, bg=self.colors['bg_medium'])
            item_frame.pack(fill='x', pady=1)
            
            # Звездочка
            star_label = tk.Label(item_frame, text='★',
                                 font=('Segoe UI', 12),
                                 bg=self.colors['bg_medium'],
                                 fg=self.colors['accent_yellow'])
            star_label.pack(side='left', padx=(5, 8))
            
            # Иконка
            icon = '🍄' if data['category'] == 'Гриб' else '🍓'
            icon_label = tk.Label(item_frame, text=icon,
                                 font=('Segoe UI', 10),
                                 bg=self.colors['bg_medium'])
            icon_label.pack(side='left')
            
            # Название
            name_label = tk.Label(item_frame, text=name,
                                 font=('Segoe UI', 10),
                                 bg=self.colors['bg_medium'],
                                 fg=self.colors['text_light'],
                                 anchor='w',
                                 cursor='hand2')
            name_label.pack(side='left', fill='x', expand=True, padx=5)
            
            # Кнопка удаления
            del_btn = tk.Label(item_frame, text='✕',
                              font=('Segoe UI', 10),
                              bg=self.colors['bg_medium'],
                              fg='#95a5a6',
                              cursor='hand2')
            del_btn.pack(side='right', padx=5)
            del_btn.bind('<Button-1>', lambda e, n=name: self.toggle_favorite(n))
            
            # Привязка клика по названию
            name_label.bind('<Button-1>', lambda e, n=name: self.show_info(n))
            icon_label.bind('<Button-1>', lambda e, n=name: self.show_info(n))
    
    def toggle_favorite(self, name):
        """Переключение избранного"""
        if name in self.favorites:
            self.favorites.remove(name)
        else:
            self.favorites.append(name)
        
        self.update_list()
        self.update_favorites_display()
    
    def show_info(self, name):
        """Отображение информации о растении"""
        data = self.mushrooms_data[name]
        
        # Изображение
        self.image_label.configure(image=data['image'])
        
        # Название
        self.name_label.configure(text=name)
        
        # Категория и сезон
        self.category_label.configure(text=f"{data['category']} •")
        self.season_label.configure(text=data['season'])
        
        # Статус
        if data['edible']:
            self.status_label.configure(text='✓ СЪЕДОБНО',
                                       bg=self.colors['success'],
                                       fg='white')
            self.status_frame.configure(bg=self.colors['success'])
        else:
            self.status_label.configure(text='⚠ ЯДОВИТО!',
                                       bg=self.colors['danger'],
                                       fg='white')
            self.status_frame.configure(bg=self.colors['danger'])
        
        # Описание
        self.desc_text.config(state='normal')
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(1.0, data['desc'])
        self.desc_text.config(state='disabled')
    
    def on_window_resize(self, event):
        """Обработка изменения размера окна"""
        # Адаптация размеров шрифтов и элементов при необходимости
        pass
    
    def open_test_window(self):
        """Открытие окна тестирования"""
        test_window = tk.Toplevel(self.window)
        test_window.title("Тест на знание грибов и ягод")
        test_window.geometry("600x500")
        test_window.minsize(500, 400)
        test_window.configure(bg=self.colors['bg_dark'])
        
        # Центрирование окна
        test_window.transient(self.window)
        test_window.grab_set()
        
        # Данные теста
        self.current_question = 0
        self.correct_answers = 0
        
        self.questions = [
            {
                "question": "Какой из этих грибов ядовитый?",
                "answers": ["Белый гриб", "Подосиновик", "Мухомор", "Лисичка"],
                "correct": "Мухомор"
            },
            {
                "question": "Какая ягода смертельно ядовита?",
                "answers": ["Земляника", "Волчья ягода", "Малина", "Черника"],
                "correct": "Волчья ягода"
            },
            {
                "question": "Какой гриб считается самым опасным в мире?",
                "answers": ["Мухомор", "Ложный опенок", "Бледная поганка", "Сатанинский гриб"],
                "correct": "Бледная поганка"
            },
            {
                "question": "Какая ягода улучшает зрение?",
                "answers": ["Малина", "Земляника", "Черника", "Клюква"],
                "correct": "Черника"
            },
            {
                "question": "Какой гриб никогда не бывает червивым?",
                "answers": ["Белый гриб", "Подосиновик", "Лисичка", "Подберезовик"],
                "correct": "Лисичка"
            }
        ]
        
        # Заголовок
        title_label = tk.Label(test_window,
                              text='📋 ТЕСТ НА ЗНАНИЕ ГРИБОВ И ЯГОД',
                              font=('Segoe UI', 16, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg=self.colors['accent_yellow'])
        title_label.pack(pady=20)
        
        # Прогресс
        self.progress_label = tk.Label(test_window,
                                       text=f'Вопрос {self.current_question + 1} из {len(self.questions)}',
                                       font=('Segoe UI', 11),
                                       bg=self.colors['bg_dark'],
                                       fg='#95a5a6')
        self.progress_label.pack()
        
        # Фрейм вопроса
        question_frame = tk.Frame(test_window, bg=self.colors['bg_medium'])
        question_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        self.question_label = tk.Label(question_frame,
                                       text='',
                                       font=('Segoe UI', 14),
                                       bg=self.colors['bg_medium'],
                                       fg=self.colors['text_light'],
                                       wraplength=500,
                                       justify='center')
        self.question_label.pack(pady=20)
        
        # Фрейм ответов
        self.answers_frame = tk.Frame(question_frame, bg=self.colors['bg_medium'])
        self.answers_frame.pack(fill='both', expand=True, pady=10)
        
        self.answer_var = tk.StringVar()
        
        # Кнопка проверки
        self.check_button = tk.Button(test_window,
                                      text='ПРОВЕРИТЬ',
                                      font=('Segoe UI', 12, 'bold'),
                                      bg=self.colors['accent_green'],
                                      fg='white',
                                      relief='flat',
                                      cursor='hand2',
                                      command=self.check_answer)
        self.check_button.pack(pady=20, ipadx=30, ipady=10)
        
        # Запускаем первый вопрос
        self.update_question()
    
    def update_question(self):
        """Обновление вопроса в тесте"""
        if self.current_question >= len(self.questions):
            self.show_test_results()
            return
        
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data['question'])
        self.progress_label.config(text=f'Вопрос {self.current_question + 1} из {len(self.questions)}')
        
        # Очищаем старые ответы
        for widget in self.answers_frame.winfo_children():
            widget.destroy()
        
        # Создаем новые радио-кнопки
        for answer in question_data['answers']:
            rb = tk.Radiobutton(self.answers_frame,
                               text=answer,
                               variable=self.answer_var,
                               value=answer,
                               font=('Segoe UI', 12),
                               bg=self.colors['bg_medium'],
                               fg=self.colors['text_light'],
                               selectcolor=self.colors['bg_light'],
                               activebackground=self.colors['bg_medium'],
                               activeforeground=self.colors['text_light'],
                               cursor='hand2')
            rb.pack(anchor='w', pady=5)
    
    def check_answer(self):
        """Проверка ответа"""
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning('Внимание', 'Пожалуйста, выберите ответ')
            return
        
        question_data = self.questions[self.current_question]
        
        if selected == question_data['correct']:
            self.correct_answers += 1
            messagebox.showinfo('Правильно!', '✅ Отличный ответ!')
        else:
            messagebox.showerror('Ошибка',
                               f'❌ Неправильно!\nПравильный ответ: {question_data["correct"]}')
        
        self.current_question += 1
        self.answer_var.set('')
        self.update_question()
    
    def show_test_results(self):
        """Показ результатов теста"""
        # Очищаем окно
        for widget in self.check_button.master.winfo_children():
            widget.destroy()
        
        test_window = self.check_button.master
        test_window.configure(bg=self.colors['bg_dark'])
        
        # Результаты
        result_frame = tk.Frame(test_window, bg=self.colors['bg_dark'])
        result_frame.pack(fill='both', expand=True)
        
        total = len(self.questions)
        percentage = (self.correct_answers / total) * 100
        
        # Заголовок
        title = tk.Label(result_frame,
                        text='🏆 РЕЗУЛЬТАТЫ ТЕСТА',
                        font=('Segoe UI', 20, 'bold'),
                        bg=self.colors['bg_dark'],
                        fg=self.colors['accent_yellow'])
        title.pack(pady=30)
        
        # Счет
        score_text = f'{self.correct_answers} из {total} правильных ответов'
        score_label = tk.Label(result_frame,
                              text=score_text,
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg='white')
        score_label.pack(pady=10)
        
        # Процент
        percent_label = tk.Label(result_frame,
                                text=f'{percentage:.1f}%',
                                font=('Segoe UI', 18),
                                bg=self.colors['bg_dark'],
                                fg='#95a5a6')
        percent_label.pack()
        
        # Оценка
        if percentage == 100:
            message = '🌟 Превосходно! Вы настоящий эксперт!'
            color = self.colors['success']
        elif percentage >= 80:
            message = '👍 Очень хорошо! Отличные знания!'
            color = self.colors['accent_green']
        elif percentage >= 60:
            message = '👌 Хороший результат! Продолжайте изучать!'
            color = self.colors['accent_yellow']
        else:
            message = '📚 Нужно больше практики! Изучайте справочник!'
            color = self.colors['danger']
        
        message_label = tk.Label(result_frame,
                                text=message,
                                font=('Segoe UI', 14, 'bold'),
                                bg=self.colors['bg_dark'],
                                fg=color,
                                wraplength=400,
                                justify='center')
        message_label.pack(pady=30)
        
        # Кнопка закрытия
        close_btn = tk.Button(result_frame,
                             text='ЗАКРЫТЬ',
                             font=('Segoe UI', 12, 'bold'),
                             bg=self.colors['accent_yellow'],
                             fg=self.colors['bg_dark'],
                             relief='flat',
                             cursor='hand2',
                             command=test_window.destroy)
        close_btn.pack(ipadx=30, ipady=10)

# Запуск приложения
if __name__ == '__main__':
    window = tk.Tk()
    app = MushroomBerryApp(window)
    
    # Показываем первый элемент при запуске
    first_item = list(app.mushrooms_data.keys())[0]
    app.show_info(first_item)
    
    # Обновляем списки
    app.update_list()
    app.update_favorites_display()
    
    window.mainloop()