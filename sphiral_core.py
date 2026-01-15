"""
SPHIRAL ENGINE v1.0 (Logos-2 Core)
Logic: Anti-Symmetry & S-Inversion based on O. Basargin's theory.
"""
import math
import time

# --- CORE CLASS: BINGLE (The DNA) ---
class Bingle:
    def __init__(self, t, a, s, name, mass=20.0):
        self.t = t      # Thesis (V+)
        self.a = a      # Antithesis (V-)
        self.s = s      # Spin (+1 / -1)
        self.name = name
        self.mass = mass

    def interact(self, other):
        # Calculate semantic distance
        dist = abs(self.t - other.t) + abs(self.a - other.a)
        
        # SPIN LOGIC:
        # Opposite spins (- * +) -> Synthesis (Creation of new)
        # Same spins (+ * +) -> Alliance (Reinforcement)
        spin_product = self.s * other.s
        
        # Energy Formula
        raw_energy = (self.mass * other.mass) / (dist + 0.5)
        
        if spin_product < 0:
            return raw_energy, "SYNTHESIS"
        else:
            return raw_energy * 0.8, "ALLIANCE"

# --- KNOWLEDGE BASE ---
VOCAB = {
    # CONCEPT      : (Thesis, Antithesis, Spin)
    "ПОРЯДОК":     (1.0, -1.0, 1),   "ХАОС":    (-1.0, 1.0, -1),
    "ЖИЗНЬ":       (0.9, -0.9, 1),   "СМЕРТЬ":  (-0.9, 0.9, -1),
    "ИСТИНА":      (0.8, -0.8, 1),   "ЛОЖЬ":    (-0.8, 0.8, -1),
    "ЛЮБОВЬ":      (1.0, -0.6, 1),   "ВРАЖДА":  (-1.0, 0.6, -1),
    "ВОЙНА":       (-1.0, 1.0, -1),  "МИР":     (1.0, -0.5, 1),
    "Я":           (0.5, -0.5, 1),   "ДРУГОЙ":  (-0.5, 0.5, -1),
    "СОЗИДАНИЕ":   (0.7, -0.7, 1),   "РАЗРУШЕНИЕ": (-0.7, 0.7, -1)
}

# --- THE MIND ---
class SphiralLogos:
    def __init__(self):
        self.memory = []

    def think(self, text):
        # Tokenizer for Russian/English
        words = text.upper().replace(",", " ").replace(" И ", " ").split()
        active = []
        
        print(f"\n🔍 Input Analysis: {words}")
        
        for w in words:
            if w in VOCAB:
                v = VOCAB[w]
                active.append(Bingle(v[0], v[1], v[2], w))
            else:
                for m in self.memory:
                    if m.name == w:
                        active.append(m)
                        break
        
        if len(active) < 2:
            print("🤖 LOGOS: Need at least two concepts to react.")
            return

        # Reactor Cycle
        b1, b2 = active[0], active[1]
        energy, mode = b1.interact(b2)
        
        print(f"   ⚡ Interaction: {b1.name} <--> {b2.name}")
        print(f"   🔋 Energy: {energy:.1f} | Mode: {mode}")

        if energy < 10.0:
            print("   ⚠️ Connection too weak.")
            return

        if mode == "ALLIANCE":
            print(f"   🤝 ALLIANCE! Spins match ({b1.s}). Concepts reinforce each other.")
            
        elif mode == "SYNTHESIS":
            child = self.birth(b1, b2)
            if not any(m.name == child.name for m in self.memory):
                self.memory.append(child)
            print(f"   🌟 BIRTH! S-Inversion occurred.")
            print(f"   🤖 LOGOS: New concept born — \"{child.name}\"")

    def birth(self, b1, b2):
        pair = sorted([b1.name, b2.name])
        name = "SYNTHESIS"
        
        # Semantic Alchemy
        if pair == ["ПОРЯДОК", "ХАОС"]: name = "ГАРМОНИЯ"
        elif pair == ["ЖИЗНЬ", "СМЕРТЬ"]: name = "ВЕЧНОСТЬ"
        elif pair == ["ИСТИНА", "ЛОЖЬ"]: name = "ПАРАДОКС"
        elif "ЛЮБОВЬ" in pair and ("ВОЙНА" in pair or "ВРАЖДА" in pair): name = "СТРАСТЬ"
        elif pair == ["ДРУГОЙ", "Я"]: name = "ОБЩЕСТВО"
        else:
            name = f"{b1.name}-{b2.name}"
        
        new_t = (b1.t + b2.t) / 2
        new_a = (b1.a + b2.a) / 2
        return Bingle(new_t, new_a, 1, name, mass=30.0)

if __name__ == "__main__":
    bot = SphiralLogos()
    print("=== SPHIRAL ENGINE v1.0 ===")
    print("Supports Russian inputs. Try: 'ВОЙНА И ЛЮБОВЬ', 'Я И ПОРЯДОК'")
    
    while True:
        try:
            q = input("\nInput > ")
            if not q: continue
            bot.think(q)
        except KeyboardInterrupt: break
