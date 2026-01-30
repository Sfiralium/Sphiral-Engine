import streamlit as st

# --- НАСТРОЙКИ ---
st.set_page_config(page_title="Sfiralium Ecosystem", layout="wide", page_icon="💠")

# --- СТИЛЬ (Cyberpunk/Lab UI) ---
st.markdown("""
<style>
    /* Заголовки */
    .main-header {font-size: 3.5rem; color: #00CCFF; text-align: center; font-weight: bold; text-shadow: 0px 0px 15px rgba(0, 204, 255, 0.4);}
    .sub-header {font-size: 1.2rem; color: #aaaaaa; text-align: center; letter-spacing: 2px; margin-bottom: 3rem;}
    
    /* Текстовые блоки (Манифест) */
    .manifesto-box {
        background-color: #0e1117;
        border-left: 5px solid #00CCFF;
        padding: 20px;
        margin-bottom: 30px;
        border-radius: 5px;
    }
    .manifesto-title {color: #ffffff; font-size: 1.5rem; font-weight: bold;}
    .manifesto-text {color: #cfd8dc; font-size: 1.05rem; line-height: 1.6;}
    
    /* Карточки проектов */
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
    
    /* Футер и Лицензия */
    .legal-footer {text-align: center; color: #555; font-size: 0.8rem; margin-top: 50px; border-top: 1px solid #333; padding-top: 20px;}
</style>
""", unsafe_allow_html=True)

# --- 1. ШАПКА ---
st.markdown('<div class="main-header">💠 SFIRALIUM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">ECOSYSTEM CONTROL CENTER<br>Laboratory of Time-Genetics & S-Logic</div>', unsafe_allow_html=True)

# --- 2. МАНИФЕСТ (ОБЩИЙ ЗАМЫСЛ) ---
# Вернули блок "Зачем это надо"
st.markdown("""
<div class="manifesto-box">
    <div class="manifesto-title">🧬 Философия Проекта: Времягенетика</div>
    <div class="manifesto-text">
        <p>Современные вычисления линейны. Природа — нет. <br>
        Мы разрабатываем технологии, основанные на принципе <b>Зеркальной Антисимметрии Времени</b>. 
        Наши алгоритмы не просто обрабатывают данные — они устраняют энтропию (хаос) через геометрическое структурирование событий.</p>
        <p><b>Наша цель:</b> Создание вычислительных систем, работающих подобно живой материи — мгновенно, без задержек и обучения на гигабайтах данных.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🚀 Active Modules (Экосистема)")

# --- 3. СЕТКА ПРОЕКТОВ (2x2) ---

# === РЯД 1 ===
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card">
        <span class="tag">BIO-INFORMATICS</span>
        <h3>🧬 Protein Sfiral</h3>
        <p><b>Задача:</b> Фолдинг белков.<br>
        Вместо нейросетей мы используем геометрию. Модуль находит нативную структуру белка, минимизируя "сопротивление времени".</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ОТКРЫТЬ ЛАБОРАТОРИЮ", "https://protein-sfiral-tvflgztq3odxduv9ijeruw.streamlit.app/", use_container_width=True)

with c2:
    st.markdown("""
    <div class="card">
        <span class="tag">HARDWARE / PHYSICS</span>
        <h3>🛸 Sfiral Gyro</h3>
        <p><b>Задача:</b> Навигация без GPS.<br>
        Оптический гироскоп с фазовой антисимметрией (S-Gate). Устраняет дрейф нуля и подавляет вибрационный шум.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ТЕСТ ДРОНА", "https://sfiral-gyro-92q6d8vzqc6nkwwo84zgps.streamlit.app/", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True) 

# === РЯД 2 ===
c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="card">
        <span class="tag">INTELLIGENCE CORE</span>
        <h3>🧠 Dual Core System</h3>
        <p><b>LOGOS + FSIN</b><br>
        Гибридный интеллект. Лингвистическое ядро (работа со смыслами) + Нейросеть (FSIN) на PyTorch.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ DUAL CORE", "https://sphiral-engine-lmwfc57zgfna2umvbyqh6u.streamlit.app/", use_container_width=True)

with c4:
    st.markdown("""
    <div class="card">
        <span class="tag">KERNEL / RTOS</span>
        <h3>⏳ Time-OS</h3>
        <p><b>Операционная Система</b><br>
        Планировщик реального времени, управляемый энтропией (Event-Driven). Отсекает информационный шум на уровне ядра.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 ЗАПУСТИТЬ ЯДРО ВРЕМЕНИ", "https://sphiral-engine-hblqnts5xs2ptmfzbgqwmu.streamlit.app/", use_container_width=True)

# --- 4. ПОДВАЛ (ЛИЦЕНЗИРОВАНИЕ И ПАТЕНТЫ) ---
st.markdown("---")

with st.expander("⚖️ Правовая информация и Лицензирование (Legal Status)"):
    st.markdown("""
    #### 📜 Лицензия: CC BY-NC 4.0
    Весь исходный код и алгоритмы предоставляются на условиях лицензии **Creative Commons Attribution-NonCommercial 4.0 International**.
    * ✅ **Разрешено:** Использование в научных целях, обучение, личные некоммерческие проекты.
    * 🚫 **Запрещено:** Коммерческое использование S-Logic, интеграция в проприетарные продукты без соглашения.

    #### 🛡 Патентный портфель
    Технологии защищены приоритетными заявками (Patent Pending):
    1. **Способ вычисления:** Алгоритм нелинейной обработки событий.
    2. **S-Gate:** Метод фильтрации шума для роевых систем.
    3. **Сфиральный триггер:** Аппаратная логика срабатывания.
    4. **Сфиральный каскад:** Архитектура нейросети (FSIN).
    
    *© 2026 O.S. Basargin / Sfiralium Lab.*
    """)

st.markdown('<div class="legal-footer">Sfiralium Ecosystem v1.0 | Stable Build | Verified</div>', unsafe_allow_html=True)
