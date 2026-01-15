import streamlit as st
import time
# Пробуем импортировать. Если файл называется по-другому, поправьте импорт здесь.
try:
    from sphiral_core import SphiralLogos, VOCAB
except ImportError:
    st.error("Ошибка: Файл sphiral_core.py не найден! Убедитесь, что он лежит рядом с app.py")
    st.stop()

# --- НАСТРОЙКА КРАСОТЫ (CSS) ---
st.set_page_config(page_title="Sfiral Engine", page_icon="🌀", layout="centered")

# Темная тема с красными акцентами (под "Нана Бонана")
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

# --- БОКОВАЯ ПАНЕЛЬ ---
with st.sidebar:
    st.header("📚 База Знаний")
    if VOCAB:
        st.write("Доступные понятия:")
        for word in list(VOCAB.keys())[:10]: # Покажем первые 10
            st.code(word)
    st.info("💡 Совет: Попробуйте 'ХАОС И ПОРЯДОК'")

# --- ЧАТ ---
st.divider()

# Вывод истории
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- ВВОД ПОЛЬЗОВАТЕЛЯ ---
prompt = st.chat_input("Введите пару понятий (например: ЖИЗНЬ И СМЕРТЬ)...")

if prompt:
    # 1. Показываем ввод
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 2. Думаем (Визуализация)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # ХАК: Перехватываем вывод print() из ядра, чтобы показать его в вебе
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            st.session_state.logos.think(prompt)
        output = f.getvalue()
        
        # Очистка вывода для красоты
        clean_output = ""
        for line in output.split('\n'):
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
                    st.balloons()
            elif "ALLIANCE" in line:
                 clean_output += f"🤝 **АЛЬЯНС (Усиление)**\n\n"

        if not clean_output:
            clean_output = "⚠️ *Нет реакции. Используйте слова из словаря.*"

        message_placeholder.markdown(clean_output)
        st.session_state.history.append({"role": "assistant", "content": clean_output})
