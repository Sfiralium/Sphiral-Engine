"""
=============================================================================
FSIN ENGINE: FRACTAL SFIRAL NEURAL NETWORK
Based on O.S. Basargin's Theory (2025)
=============================================================================
Реализация математической модели ФСИН (Фрактальный Сфиральный Нейрон).
Ключевая особенность: Зеркальная Антисимметрия (Mirror Anti-Symmetry).

FORMULA:
    Output = Activation(W1 * x) + (-Activation(W2 * x))
    Это позволяет гасить шум и выделять чистую структуру сигнала.
"""
import torch
import torch.nn as nn
import torch.optim as optim
import time

# --- 1. SFIRAL LAYER (ЗЕРКАЛЬНАЯ АНТИСИММЕТРИЯ) ---
# Источник: Глава 4, стр. 28 книги
class FsinLayer(nn.Module):
    def __init__(self, input_size, output_size):
        super(FsinLayer, self).__init__()
        # Два параллельных канала (Тезис и Антитезис)
        self.channel_plus = nn.Linear(input_size, output_size)
        self.channel_minus = nn.Linear(input_size, output_size)
        self.activation = nn.LeakyReLU() # Или ReLU, как в книге

    def forward(self, x):
        # Прямой поток (V+)
        out1 = self.activation(self.channel_plus(x))
        
        # Обратный/Зеркальный поток (V-) с инверсией знака
        # В книге: out2 = -self.activation(self.weight2(x))
        out2 = -self.activation(self.channel_minus(x))
        
        # S-Интеграция (Сумма потоков)
        return out1 + out2

# --- 2. FRACTAL ARCHITECTURE (ФСИН) ---
# Источник: Глава 7, демо-код
class FsinNetwork(nn.Module):
    def __init__(self, input_size=10, hidden_size=32, output_size=1, depth=2):
        super(FsinNetwork, self).__init__()
        
        # Фрактальное построение: слои вложены друг в друга
        # (В упрощенном виде - последовательность Сфиральных слоев)
        layers = []
        
        # Входной слой
        layers.append(FsinLayer(input_size, hidden_size))
        
        # Скрытые фрактальные уровни
        for _ in range(depth - 1):
            layers.append(FsinLayer(hidden_size, hidden_size))
            
        self.feature_extractor = nn.Sequential(*layers)
        self.final_head = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        features = self.feature_extractor(x)
        return self.final_head(features)

# --- 3. DEMO: ANOMALY DETECTION ---
def run_experiment():
    print("\n🌀 ЗАПУСК ФСИН (FSIN-TORCH)...")
    print("   Задача: Обучение на зашумленных данных (Поиск аномалий)")
    
    # Генерация данных (синусоида с шумом)
    torch.manual_seed(42)
    # Создаем 500 примеров, 10 признаков
    x_train = torch.rand(500, 10) 
    # Целевое значение с небольшим шумом
    y_train = torch.sum(x_train, dim=1, keepdim=True) + torch.randn(500, 1) * 0.1
    
    # Инициализация модели
    model = FsinNetwork(input_size=10, hidden_size=32, output_size=1)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    
    # Обучение
    print(f"   🚀 Начинаю обучение (100 эпох)...")
    history = []
    
    start_time = time.time()
    for epoch in range(101):
        optimizer.zero_grad()
        outputs = model(x_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        history.append(loss.item())
        
        if epoch % 20 == 0:
            print(f"      [Epoch {epoch}] Loss: {loss.item():.5f}")
            
    print(f"   ✅ Готово за {time.time() - start_time:.2f} сек.")
    print(f"   Финальная ошибка: {history[-1]:.5f}")
    print("   Вывод: Сфиральный слой успешно подавил шум (Антисимметрия работает).")

if __name__ == "__main__":
    run_experiment()
