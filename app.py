import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim
import time
import pandas as pd
import numpy as np

# Импорт логики Смыслов (если есть)
try:
    from sfiral_core import SfiralLogos, VOCAB
    CORE_AVAILABLE = True
except ImportError:
    CORE_AVAILABLE = False

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="Sfiral Engine II", page_icon="🌀", layout="wide")

# СТИЛЬ (Cyberpunk / Basargin Style)
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1 { color: #ff2b2b; text-shadow: 0 0 10px #ff2b2b; font-family: 'Courier New'; }
    .stButton button { background-color: #ff2b2b; color: white; border-radius: 5px; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { background-color: #1a1a1a; border-radius: 5px; color: white; }
    .stTabs [aria-selected="true"] { background-color: #ff2b2b; }
</style>
""", unsafe_allow_html=True)

st.title("🌀 SFIRAL ENGINE: DUAL CORE")
st.caption("Architecture: Logos-4 Omni | Physics: Mirror Anti-Symmetry")

# --- ВКЛАДКИ ---
tab1, tab2 = st.tabs(["🧬 ЛОГОС (Душа)", "🧠 НЕЙРОКОРТЕКС (Тело)"])

# ==========================================
# Вкладка 1: ЛИНГВИСТИЧЕСКИЙ ЧАТ
# ==========================================
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Диалог с Абсолютом")
        if 'history' not in st.session_state: st.session_state.history = []
        if 'logos' not in st.session_state and CORE_AVAILABLE:
            st.session_state.logos = SfiralLogos()

        # Вывод чата
        for msg in st.session_state.history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

        # Ввод
        prompt = st.chat_input("Введите пару (например: ХАОС И ПОРЯДОК)...")
        if prompt:
            st.session_state.history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.write(prompt)
            
            with st.chat_message("assistant"):
                if CORE_AVAILABLE:
                    # Перехват print() из ядра
                    import io
                    from contextlib import redirect_stdout
                    f = io.StringIO()
                    with redirect_stdout(f):
                        st.session_state.logos.think(prompt)
                    response = f.getvalue().replace("\n", "  \n") # Markdown formatting
                    st.markdown(response)
                    st.session_state.history.append({"role": "assistant", "content": response})
                else:
                    st.error("Ядро sfiral_core.py не найдено.")
    
    with col2:
        st.info("💡 **Справка:**\nЭто модуль семантики. Он ищет смысл слов и рождает новые понятия через S-Инверсию.")

# ==========================================
# Вкладка 2: НЕЙРОСЕТЬ (FSIN VISUALIZER)
# ==========================================
with tab2:
    st.subheader("Визуализация обучения ФСИН")
    st.write("Демонстрация работы **Зеркальной Антисимметрии** на реальных данных.")
    
    col_ctrl, col_graph = st.columns([1, 3])
    
    with col_ctrl:
        epochs = st.slider("Количество Эпох", 50, 500, 100)
        lr = st.number_input("Скорость обучения", value=0.01, format="%.3f")
        if st.button("ЗАПУСТИТЬ ОБУЧЕНИЕ 🚀"):
            
            # --- ОПРЕДЕЛЕНИЕ МОДЕЛИ ПРЯМО ЗДЕСЬ ---
            class FsinLayer(nn.Module):
                def __init__(self, n_in, n_out):
                    super().__init__()
                    self.plus = nn.Linear(n_in, n_out)
                    self.minus = nn.Linear(n_in, n_out)
                    self.act = nn.LeakyReLU()
                def forward(self, x):
                    return self.act(self.plus(x)) + (-self.act(self.minus(x)))

            # Подготовка данных
            status = st.empty()
            progress = st.progress(0)
            chart = col_graph.line_chart([])
            
            # Генерация (Сигнал + Шум)
            torch.manual_seed(42)
            X = torch.rand(200, 10)
            Y = torch.sum(X, dim=1, keepdim=True) + torch.randn(200, 1) * 0.2
            
            model = nn.Sequential(FsinLayer(10, 32), nn.Linear(32, 1))
            opt = optim.Adam(model.parameters(), lr=lr)
            loss_fn = nn.MSELoss()
            
            loss_history = []
            
            for i in range(epochs):
                opt.zero_grad()
                pred = model(X)
                loss = loss_fn(pred, Y)
                loss.backward()
                opt.step()
                
                loss_history.append(loss.item())
                
                # Обновляем график каждые 5 эпох
                if i % 5 == 0:
                    status.text(f"Эпоха {i}/{epochs} | Ошибка: {loss.item():.5f}")
                    progress.progress(i/epochs)
                    # Живой график падения ошибки
                    df = pd.DataFrame(loss_history, columns=["Ошибка (Loss)"])
                    chart.line_chart(df)
                    time.sleep(0.01) # Для анимации
            
            status.success(f"✅ Обучение завершено! Финальная ошибка: {loss.item():.5f}")
            st.balloons()
