import streamlit as st
import pandas as pd
import numpy as np
import time

# --- НАСТРОЙКИ ---
st.set_page_config(page_title="Sphiral Kernel v0.1", layout="wide", page_icon="🧠")
st.title("🧠 SPHIRAL ENGINE: Event-Driven RTOS")
st.caption("Demonstration of Non-Linear Task Scheduling (Time-Genetics Core)")

# --- 1. ТЕОРИЯ (Сфиральный Триггер) ---
with st.expander("ℹ️ Справка: Чем S-планировщик отличается от Linux?"):
    st.markdown("""
    * **Classic OS:** Round-Robin (Все задачи равны, выполняются по очереди).
    * **Sfiral OS:** Event-Density (Задачи имеют "вес". Система сжимает время для важных событий).
    """)

# --- 2. ГЕНЕРАТОР ЗАДАЧ ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Входящий Поток")
    st.info("Симуляция потока данных от сенсоров и модулей.")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Кнопка генерации случайного хаоса
    if st.button("⚡ Генерировать События (Chaos)", type="primary"):
        # Создаем 5 случайных задач
        new_tasks = [
            {"id": np.random.randint(1000, 9999), 
             "type": np.random.choice(["Sensor Noise", "CRITICAL ERROR", "Bio-Data", "Keep-Alive"]), 
             "entropy": np.random.randint(1, 100)} # Энтропия (Важность)
            for _ in range(5)
        ]
        st.session_state.tasks.extend(new_tasks)

    # Показать "сырую" очередь
    if st.session_state.tasks:
        df = pd.DataFrame(st.session_state.tasks)
        st.dataframe(df, hide_index=True, use_container_width=True)
        st.caption(f"В буфере: {len(st.session_state.tasks)} процессов")
    else:
        st.write("Буфер пуст.")

# --- 3. ЯДРО ОБРАБОТКИ (S-LOGIC) ---
with col2:
    st.subheader("⚙️ S-Logic Kernel (Processing)")
    
    mode = st.radio("Режим Планировщика:", ["Линейный (Standard)", "Сфиральный (S-Trigger)"], horizontal=True)
    
    if st.button("▶ ЗАПУСТИТЬ ЦИКЛ ОБРАБОТКИ"):
        if not st.session_state.tasks:
            st.error("Нет задач для обработки!")
        else:
            task_pool = st.session_state.tasks.copy()
            processed_log = []
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # --- ЛОГИКА ОБРАБОТКИ ---
            if mode == "Линейный (Standard)":
                # Обработка FIFO (Первый пришел - первый ушел)
                for i, task in enumerate(task_pool):
                    status_text.text(f"Processing PID {task['id']}...")
                    time.sleep(0.3) # Имитация задержки
                    processed_log.append(task)
                    progress_bar.progress((i + 1) / len(task_pool))
                
                st.session_state.tasks = [] # Очистка
                st.error(f"❌ Линейное время: Потрачено {len(task_pool) * 0.3:.1f} сек. Обработан и шум, и важные данные.")
                
            else:
                # --- SFIRAL LOGIC (S-CASCADE) ---
                # 1. Сортировка по "Энергии" (Энтропии)
                # 2. Фильтрация "Шума" (S-Gate)
                
                status_text.text("Applying S-Filter...")
                time.sleep(0.5) # Быстрый анализ
                
                important_tasks = [t for t in task_pool if t['entropy'] > 40] # Отсекаем шум
                sorted_tasks = sorted(important_tasks, key=lambda x: x['entropy'], reverse=True) # Самые важные первыми
                
                processed_log = sorted_tasks
                progress_bar.progress(100)
                
                st.session_state.tasks = []
                
                dropped = len(task_pool) - len(processed_log)
                st.success(f"✅ Сфиральное время: Обработано мгновенно. Шум отсечен ({dropped} пакетов). Приоритет соблюден.")

            # Вывод результата
            st.write("### 📊 Результат Выполнения")
            if processed_log:
                res_df = pd.DataFrame(processed_log)
                st.dataframe(res_df, use_container_width=True)
            else:
                st.warning("Все задачи были классифицированы как ШУМ и удалены.")
