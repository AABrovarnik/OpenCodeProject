from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Ключ для сессий (можно сменить)

# === НАСТРОЙКИ ===
# Смапленные настроения → эмодзи в начале поста
MOOD_EMOJI = {
    'нейтральное': '',
    'позитивное': '🔥',
    'восторженное': '⚡',
    'деловое': '💼',
    'интригующее': '💎',
}

MOOD_LABEL = {
    'нейтральное': 'Нейтральное',
    'позитивное': 'Позитивное',
    'восторженное': 'Восторженное',
    'деловое': 'Деловое',
    'интригующее': 'Интригующее',
}

# === ФУНКЦИЯ СБОРКИ ПОСТА ===
def build_post(title, description, benefit, summary, mood):
    """
    Собирает готовый пост из полей формы.
    Результат можно менять, редактируя f-строку ниже.
    """
    emoji = MOOD_EMOJI.get(mood, '')
    mood_text = MOOD_LABEL.get(mood, mood)

    # Если заголовок пустой — не добавляем его
    title_block = f"{emoji} {title}\n" if title.strip() else ""

    # Собираем пост по шаблону
    post = f"""{title_block}{description}

{'✅ Выгода: ' + benefit if benefit.strip() else ''}

{'📌 Саммари: ' + summary if summary.strip() else ''}

{'#новости #' + mood_text.lower() if mood_text else ''}"""

    # Чистим лишние пустые строки
    lines = [line for line in post.split('\n') if line.strip() != '']
    return '\n'.join(lines)


# === МАРШРУТЫ ===
@app.route('/', methods=['GET', 'POST'])
def index():
    # Инициализируем список постов в сессии
    if 'posts' not in session:
        session['posts'] = []

    generated_post = None

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        benefit = request.form.get('benefit', '').strip()
        summary = request.form.get('summary', '').strip()
        mood = request.form.get('mood', 'нейтральное')

        # Валидация: описание обязательно
        if not description:
            return render_template(
                'index.html',
                error='Поле «Описание новости» обязательно для заполнения.',
                moods=MOOD_LABEL,
                posts=session['posts'],
                title=title,
                benefit=benefit,
                summary=summary,
                mood=mood,
            )

        # Собираем пост
        generated_post = build_post(title, description, benefit, summary, mood)

        # Сохраняем в историю сессии
        now = datetime.now().strftime('%H:%M, %d.%m.%Y')
        post_entry = {
            'id': len(session['posts']) + 1,
            'text': generated_post,
            'time': now,
        }
        posts = session['posts']
        posts.append(post_entry)
        session['posts'] = posts

    return render_template(
        'index.html',
        generated_post=generated_post,
        moods=MOOD_LABEL,
        posts=session['posts'],
    )


if __name__ == '__main__':
    app.run(debug=True)
