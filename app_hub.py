import streamlit as st

# --- НАСТРОЙКИ ---
st.set_page_config(page_title="Sfiralium Ecosystem", layout="wide", page_icon="💠")

# --- СТИЛЬ (Cyberpunk UI) ---
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #00CCFF; text-align: center; font-weight: bold; text-shadow: 0px 0px 10px #00CCFF;}
    .sub-header {font-size: 1.2rem; color: #aaaaaa; text-align: center; margin-bottom: 2rem;}
    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #30363d;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s, border-color 0.2s;
    }
    .card:hover {
        transform: translateY(-5px); 
        border-color: #00CCFF;
        box-shadow: 0 0 15px rgba(0, 204, 255, 0.2);
    }
    h3 {color: #ffffff; margin-bottom: 5px;}
    .tag {color: #00CCFF; font-size: 0.9rem; font-weight: bold; letter-spacing: 1px; margin-bottom: 15px; display: block;}
    p {color: #8b949e; font-size: 0.95rem; line-height: 1.5;}
</style>
""", unsafe_allow_html=True)

# --- ЗАГОЛОВОК ---
st.markdown('<div class="main-header">💠 SFIRALIUM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">ECOSYSTEM CONTROL CENTER<br>Architecture of Time & Intelligence</div>', unsafe_allow_html=True)

st.markdown("---")

# --- СЕТКА ПРОЕКТОВ (2 ряда по 2 колонки) ---

# === РЯД 1: ФУНДАМЕНТАЛЬНАЯ НАУКА ===
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card">
        <span class="tag">BIO-INFORMATICS</span>
        <h3>🧬 Protein Sfiral</h3>
        <p>Модуль сворачивания белков. Геометрический поиск нативной структуры без обучения на Big Data.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ЛАБОРАТОРИЮ", "https://protein-sfiral-tvflgztq3odxduv9ijeruw.streamlit.app/", use_container_width=True)

with c2:
    st.markdown("""
    <div class="card">
        <span class="tag">HARDWARE / PHYSICS</span>
        <h3>🛸 Sfiral Gyro</h3>
        <p>Оптический гироскоп с фазовой антисимметрией (S-Gate). Абсолютная навигация без дрейфа нуля.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ТЕСТ ДРОНА", "https://sfiral-gyro-92q6d8vzqc6nkwwo84zgps.streamlit.app/", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True) # Отступ

# === РЯД 2: ВЫЧИСЛИТЕЛЬНОЕ ЯДРО ===
c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="card">
        <span class="tag">INTELLIGENCE CORE</span>
        <h3>🧠 Dual Core System</h3>
        <p><b>LOGOS + FSIN</b>. Гибридный движок: Лингвистическая S-Логика (смыслы) + Нейросеть (PyTorch).</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ДВИЖОК", "https://sphiral-engine-lmwfc57zgfna2umvbyqh6u.streamlit.app/", use_container_width=True)

with c4:
    st.markdown("""
    <div class="card">
        <span class="tag">KERNEL / RTOS</span>
        <h3>⏳ Time-OS</h3>
        <p>Операционная система реального времени. Планировщик событий на основе энтропии (Event-Driven).</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ЯДРО ВРЕМЕНИ", "https://sphiral-engine-hblqnts5xs2ptmfzbgqwmu.streamlit.app/", use_container_width=True)

st.markdown("---")
st.caption("© 2026 Sfiralium Lab. All Systems Operational. | License: CC BY-NC 4.0")
