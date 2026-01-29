import streamlit as st
import pandas as pd
import numpy as np
import time

# --- НАСТРОЙКИ (Имя вкладки браузера) ---
st.set_page_config(page_title="Ядро Time-OS", layout="wide", page_icon="⏳")

# --- ЗАГОЛОВОК (Внутри приложения) ---
st.title("⏳ Time-OS: Ядро Событий")
st.caption("Демонстрация нелинейного S-планировщика (S-Scheduling)")

# --- 1. ТЕОРИЯ ---
with st.expander("ℹ️ Архитектурная справка"):
    st.markdown("""
    * **Ядро (Kernel):** S-Logic RTOS v0.1
    * **Планировщик:** Основан на энтропии (Нелинейное время)
    * **Статус:** Режим симуляции
    """)

# --- 2. ГЕНЕРАТОР ЗАДАЧ ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Входящий Поток")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Кнопка генерации случайных задач
    if st.button("⚡ Впрыск Энтропии (Хаос)", type="primary"):
        new_tasks = [
            {"PID": np.random.randint(100, 999), 
             "Тип": np.random.choice(["Шум_Сенсора", "КРИТИЧЕСКИЙ_S-GATE", "Био_Фолдинг", "Пинг_Системы"]), 
             "Вес (Энтропия)": np.random.randint(1, 100)} 
            for _ in range(5)
        ]
        st.session_state.tasks.extend(new_tasks)

    if st.session_state.tasks:
        st.dataframe(pd.DataFrame(st.session_state.tasks), hide_index=True, use_container_width=True)
    else:
        st.info("Буфер пуст. Ожидание сигналов...")

# --- 3. ЯДРО (KERNEL) ---
with col2:
    st.subheader("⚙️ Обработка Ядра")
    
    mode = st.radio("Логика Планировщика:", ["Линейная (Тактовое время)", "Сфиральная (Событийное время)"], horizontal=True)
    
    if st.button("▶ ЗАПУСТИТЬ ЦИКЛ"):
        if not st.session_state.tasks:
            st.error("Нет потоков для выполнения.")
        else:
            pool = st.session_state.tasks.copy()
            progress = st.progress(0)
            log_box = st.empty()
            
            if mode == "Линейная (Тактовое время)":
                # Линейная обработка (медленно и всё подряд)
                for i, task in enumerate(pool):
                    log_box.code(f"[CPU] Обработка PID {task['PID']}... (Линейное ожидание)")
                    time.sleep(0.2) 
                    progress.progress((i + 1) / len(pool))
                st.session_state.tasks = []
                st.warning(f"⚠️ Линейный цикл завершен. Ресурсы потрачены на шум и ожидание.")
                
            else:
                # Сфиральная обработка (умная)
                log_box.code("[S-KERNEL] Расчет весов энтропии...")
                time.sleep(0.5)
                
                # S-Gate: Оставляем только важное (>50)
                critical = [t for t in pool if t['Вес (Энтропия)'] > 50]
                noise_count = len(pool) - len(critical)
                
                # Сортировка по важности
                critical.sort(key=lambda x: x['Вес (Энтропия)'], reverse=True)
                
                progress.progress(100)
                st.session_state.tasks = []
                
                st.success(f"✅ S-Цикл завершен. Обработано: {len(critical)}. Шум подавлен: {noise_count}.")
                if critical:
                    st.dataframe(pd.DataFrame(critical), use_container_width=True)
