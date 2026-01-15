import streamlit as st
import time
from sphiral_core import SphiralLogos, VOCAB

# --- НАСТРОЙКА КРАСОТЫ (CSS) ---
st.set_page_config(page_title="Sfiral Engine", page_icon="🌀", layout="centered")

# Темная тема с красными акцентами (под "Нана Бонана" / Баннер)
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        color: #ffffff;
        background-color: #262730;
    }
    h1 {
        color: #ff4b4b; /* Красный как на логотипе */
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
    }
    .energy-high { color: #00ff00; font-weight: bold; }
    .energy-low { color: #ffaa00; font-weight: bold; }
    .birth-anim { 
        font-size: 24px; 
        color: #ff4b4b; 
        text-align: center; 
        animation: pulse 2s infinite; 
    }
</style>
""", unsafe_allow_html=True)

# --- ИНИЦИАЛИЗАЦИЯ МОЗГА ---
if 'logos' not in st.session_state:
    st.session_state.logos = SphiralLogos()
if 'history' not in st.session_state:
    st.session_state.history = []

# --- ЗАГОЛОВОК ---
st.title("🌀 SFIRAL ENGINE")
st.caption("Topological AI Core v1.1 | Anti-Symmetry Logic")

# --- БОКОВАЯ ПАНЕЛЬ (СЛОВАРЬ) ---
with st.sidebar:
    st.header("📚 База Знаний")
    st.write("Доступные понятия:")
    for word in VOCAB.keys():
        st.code(word)
    st.info("💡 Совет: Попробуйте ввести 'ХАОС И ПОРЯДОК'")

# --- ЧАТ ---
st.divider()

# Вывод истории диалога
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- ВВОД ПОЛЬЗОВАТЕЛЯ ---
prompt = st.chat_input("Введите пару понятий (например: ЖИЗНЬ И СМЕРТЬ)...")

if prompt:
    # 1. Показываем ввод пользователя
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 2. Думаем (Визуализация процесса)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Перехватываем print() из ядра, чтобы вывести красиво
        # (Для простоты мы эмулируем логику здесь, вызывая методы ядра)
        
        # АНАЛИЗ
        words = prompt.upper().replace(",", " ").replace(" И ", " ").split()
        message_placeholder.markdown(f"🔍 *Сканирую сфиральное поле...* `{words}`")
        time.sleep(0.8)
        
        # ЗАПУСК РЕАКТОРА
        # Чтобы не переписывать логику вывода, мы просто используем ядро и формируем ответ для UI
        bot = st.session_state.logos
        
        # (Упрощенная логика для UI - дублирует sphiral_core, но с красивым выводом)
        active = []
        for w in words:
            if w in VOCAB:
                v = VOCAB[w]
                active.append(bot.memory[0] if False else None) # Заглушка
                # В реальном app.py лучше импортировать класс Bingle, но мы сделаем проще:
        
        # ХАК: Мы перенаправляем стандартный вывод в переменную, чтобы показать его в UI
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            bot.think(prompt)
        output = f.getvalue()
        
        # Парсим вывод для красоты
        lines = output.split('\n')
        clean_output = ""
        born_concept = None
        
        for line in lines:
            if "Interaction" in line:
                clean_output += f"⚡ **СТОЛКНОВЕНИЕ:** {line.split(':')[1]}\n\n"
            elif "Energy" in line:
                clean_output += f"🔋 **ЭНЕРГИЯ:** `{line.split('|')[0].strip()}`\n\n"
            elif "BIRTH" in line:
                clean_output += f"🌟 **РОЖДЕНИЕ НОВОГО!**\n\n"
            elif "LOGOS:" in line:
                text = line.split('LOGOS:')[1].strip()
                clean_output += f"### 🤖 {text}\n\n"
                if "born" in text or "Рождено" in text:
                    born_concept = text
            elif "ALLIANCE" in line:
                 clean_output += f"🤝 **АЛЬЯНС (Усиление)**\n\n"
        
        if not clean_output:
            clean_output = "⚠️ *Нет реакции. Попробуйте слова из словаря.*"

        message_placeholder.markdown(clean_output)
        st.session_state.history.append({"role": "assistant", "content": clean_output})
        
        if born_concept:
            st.balloons() # Праздник рождения смысла!
