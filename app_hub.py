import streamlit as st
from PIL import Image

# --- НАСТРОЙКИ ---
st.set_page_config(page_title="Sfiralium Ecosystem", layout="wide", page_icon="🌀")

# CSS для красоты (Стиль Киберпанк)
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #00CCFF; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #aaaaaa; text-align: center; margin-bottom: 2rem;}
    .card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333;
        text-align: center;
        transition: transform 0.2s;
    }
    .card:hover {transform: scale(1.02); border-color: #00CCFF;}
    h3 {color: #ffffff;}
    p {color: #cccccc;}
</style>
""", unsafe_allow_html=True)

# --- ЗАГОЛОВОК ---
st.markdown('<div class="main-header">🌀 SFIRALIUM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Architecture of Time & Intelligence</div>', unsafe_allow_html=True)

st.markdown("---")

# --- ОПИСАНИЕ ФИЛОСОФИИ ---
c1, c2 = st.columns([2, 1])
with c1:
    st.info("💡 **Наша миссия:** Мы создаем технологии, основанные на принципе *Зеркальной Антисимметрии Времени*. Наши алгоритмы не просто вычисляют — они устраняют энтропию.")
    st.markdown("""
    * **S-Logic:** Логика, побеждающая хаос.
    * **FSIN:** Нейросети, работающие без обучения на гигабайтах данных.
    * **Time-Genetics:** Программирование материи через форму.
    """)

# --- КАРТОЧКИ ПРОЕКТОВ (ПОРТФОЛИО) ---
st.header("🚀 Active Modules (Модули)")

col1, col2, col3 = st.columns(3)

# 1. HARDWARE (GYRO)
with col1:
    st.markdown("""
    <div class="card">
        <h3>🛸 Sfiral Gyro</h3>
        <p><b>Hardware / Physics</b></p>
        <p>Оптический гироскоп с фазовой антисимметрией. Побеждает дрейф и шум.</p>
        <p><i>Status: Prototype Verified</i></p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ТЕСТ ДРОНА", "https://sfiral-gyro-92q6d8vzqc6nkwwo84zgps.streamlit.app/")

# 2. SOFTWARE (BIO)
with col2:
    st.markdown("""
    <div class="card">
        <h3>🧬 Protein Sfiral</h3>
        <p><b>Bio-Informatics</b></p>
        <p>Модуль фолдинга белков. Мгновенное предсказание 3D-структуры.</p>
        <p><i>Status: Working Beta</i></p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 СВЕРНУТЬ БЕЛОК", "https://protein-sfiral-tvflgztq3odxduv9ijeruw.streamlit.app/")

# 3. CORE (ENGINE)
with col3:
    st.markdown("""
    <div class="card">
        <h3>🧠 Sphiral Engine</h3>
        <p><b>OS / Kernel</b></p>
        <p>Операционная система реального времени на базе S-логики.</p>
        <p><i>Status: In Development</i></p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Вы находитесь здесь", disabled=True)

st.markdown("---")

# --- КОНТАКТЫ И ПАТЕНТЫ ---
st.subheader("📜 Patents & Research")
st.text("Все технологии защищены лицензией CC BY-NC 4.0 и патентными заявками класса G01C.")
st.caption("© 2026 O.S. Basargin / Sfiralium Lab.")