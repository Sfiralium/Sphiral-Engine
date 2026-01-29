import streamlit as st
import pandas as pd
import numpy as np
import time

# --- НАСТРОЙКИ (Имя вкладки браузера) ---
st.set_page_config(page_title="Time-OS Kernel", layout="wide", page_icon="⏳")

# --- ЗАГОЛОВОК (Внутри приложения) ---
st.title("⏳ Time-OS: Event Kernel")
st.caption("Demonstration of Non-Linear S-Scheduling")

# --- 1. ТЕОРИЯ ---
with st.expander("ℹ️ Architecture Reference"):
    st.markdown("""
    * **Kernel:** S-Logic RTOS v0.1
    * **Scheduler:** Entropy-based (Non-linear time)
    * **Status:** Simulation Mode
    """)

# --- 2. ГЕНЕРАТОР ЗАДАЧ ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📥 Input Stream")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    if st.button("⚡ Inject Entropy (Chaos)", type="primary"):
        new_tasks = [
            {"pid": np.random.randint(100, 999), 
             "type": np.random.choice(["Sensor_Noise", "CRITICAL_S-GATE", "Bio_Folding", "Ping"]), 
             "weight": np.random.randint(1, 100)} 
            for _ in range(5)
        ]
        st.session_state.tasks.extend(new_tasks)

    if st.session_state.tasks:
        st.dataframe(pd.DataFrame(st.session_state.tasks), hide_index=True)
    else:
        st.info("Buffer Empty. Waiting for signals...")

# --- 3. ЯДРО (KERNEL) ---
with col2:
    st.subheader("⚙️ Kernel Processing")
    
    mode = st.radio("Scheduling Logic:", ["Linear (Clock-Time)", "Sfiral (Event-Time)"], horizontal=True)
    
    if st.button("▶ EXECUTE CYCLE"):
        if not st.session_state.tasks:
            st.error("No threads to execute.")
        else:
            pool = st.session_state.tasks.copy()
            progress = st.progress(0)
            log_box = st.empty()
            
            if mode == "Linear (Clock-Time)":
                # Линейная обработка (медленно и всё подряд)
                for i, task in enumerate(pool):
                    log_box.code(f"[CPU] Processing PID {task['pid']}... (Linear Wait)")
                    time.sleep(0.2) 
                    progress.progress((i + 1) / len(pool))
                st.session_state.tasks = []
                st.warning(f"⚠️ Linear Cycle Completed. Resources wasted on noise.")
                
            else:
                # Сфиральная обработка (умная)
                log_box.code("[S-KERNEL] Calculating Entropy Weights...")
                time.sleep(0.5)
                
                # S-Gate: Оставляем только важное (>50)
                critical = [t for t in pool if t['weight'] > 50]
                noise_count = len(pool) - len(critical)
                
                # Сортировка по важности
                critical.sort(key=lambda x: x['weight'], reverse=True)
                
                progress.progress(100)
                st.session_state.tasks = []
                
                st.success(f"✅ S-Cycle Completed. Processed: {len(critical)}. Noise Suppressed: {noise_count}.")
                if critical:
                    st.dataframe(pd.DataFrame(critical))
