from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

NEWS = [
    {
        "id": 1,
        "source": "OpenCode",
        "badge": "🔥 HOT",
        "badge_color": "#ff6b6b",
        "title": "OpenCode v1.16.0: managed workspaces и skill discovery",
        "text": "Релиз с управляемыми клонами репозиториев, OpenAI через Bedrock, файловыми скиллами, `run --replay` и десятками фиксов. 172K ★ на GitHub.",
        "url": "https://github.com/anomalyco/opencode/releases/tag/v1.16.0",
        "date": "5 июня 2026"
    },
    {
        "id": 2,
        "source": "Claude Code",
        "badge": "🤖 AI",
        "badge_color": "#00cec9",
        "title": "Dynamic Workflows — Claude сам пишет оркестрацию",
        "text": "Dynamic workflows GA: Claude Code создаёт harness на лету, распараллеливая subagent'ов. Fallback-модели, `/plugin list`, version guardrails.",
        "url": "https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code",
        "date": "4 июня 2026"
    },
    {
        "id": 3,
        "source": "Cursor",
        "badge": "🎨 Design",
        "badge_color": "#e17055",
        "title": "Cursor 3.7: Design Mode с визуальными промптами",
        "text": "Кликай, обводи, говори голосом — Cursor понимает изменения в UI. Canvas-артефакты, Context Explorer, JSONL-стора для SDK, Auto-review.",
        "url": "https://cursor.com/changelog",
        "date": "5 июня 2026"
    },
    {
        "id": 4,
        "source": "Codex CLI",
        "badge": "🧠 GPT-5",
        "badge_color": "#0984e3",
        "title": "Hermes Plugin: SQLite-память для Codex CLI",
        "text": "Плагин Hermes добавляет FTS5-память — Codex помнит правила и решения между сессиями. Контекст не теряется, промпты короче.",
        "url": "https://habr.com/ru/articles/1045262/",
        "date": "7 июня 2026"
    },
    {
        "id": 5,
        "source": "Anthropic",
        "badge": "⚡ Mythos",
        "badge_color": "#a29bfe",
        "title": "Anthropic готовит Claude Fable 5 — коммерческий Mythos",
        "text": "Публичная адаптация закрытой архитектуры Glasswing. Коммерческая версия мощнейшей модели для массового рынка.",
        "url": "https://vc.ru/ai/2970962-anthropic-predstavlyaet-kommercheskuyu-versiyu-mythos-i-fable-5",
        "date": "9 июня 2026"
    },
    {
        "id": 6,
        "source": "Cursor",
        "badge": "💼 Business",
        "badge_color": "#fdcb6e",
        "title": "Teams: Premium-места и раздельные лимиты",
        "text": "Standard $40 → Premium $120. В 5x больше включённого использования. Админ-панель с контролем расходов в Slack/email.",
        "url": "https://cursor.com/blog",
        "date": "1 июня 2026"
    },
    {
        "id": 7,
        "source": "Microsoft",
        "badge": "🔒 Security",
        "badge_color": "#e74c3c",
        "title": "GitHub: десятки репозиториев закрыты из-за ИИ-вредоноса",
        "text": "Вредоносное ПО для кражи данных через ИИ-агентов. Атаки на AWS, Azure, менеджеры паролей и инструменты разработчиков.",
        "url": "https://vc.ru/ai/2970454-microsoft-zakryla-repozitorii-na-github-iz-za-vredonosnogo-po",
        "date": "9 июня 2026"
    },
    {
        "id": 8,
        "source": "China AI",
        "badge": "🇨🇳 $295B",
        "badge_color": "#e17055",
        "title": "Китай инвестирует $295 млрд в ИИ-инфраструктуру",
        "text": "China Mobile и China Telecom управляют инфраструктурой на местных чипах. Крупнейшая государственная ИИ-программа.",
        "url": "https://vc.ru/ai/2970786-kitay-investitsii-infrastruktura-ii",
        "date": "9 июня 2026"
    },
    {
        "id": 9,
        "source": "Yandex",
        "badge": "🎧 Wearable",
        "badge_color": "#00b894",
        "title": "Яндекс Дропс — наушники с Алисой AI",
        "text": "Первое носимое ИИ-устройство Яндекса. Голосовая активация, запись идей, споттер в 200 КБ. Статья о разработке на Habr.",
        "url": "https://habr.com/ru/companies/yandex/articles/1042706/",
        "date": "9 июня 2026"
    },
    {
        "id": 10,
        "source": "Moonshot AI",
        "badge": "🌙 Kimi",
        "badge_color": "#6c5ce7",
        "title": "Kimi Code и Kimi Work — ИИ-агент для локальных файлов",
        "text": "Китайская Moonshot обновила IDE-агента Kimi Code и выпустила Kimi Work — аналог Claude Cowork для работы с файлами.",
        "url": "https://vc.ru/ai/2970849-kimi-code-i-kimi-work-ot-moonshot-dlya-rabotyi-s-lokalnyimi-faylami",
        "date": "9 июня 2026"
    }
]


@app.route("/")
def index():
    return render_template("index.html", news=NEWS, year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
