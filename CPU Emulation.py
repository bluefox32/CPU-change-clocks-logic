import time
import random

class CPU:
    def __init__(self, base_clock, max_multiplier):
        self.base_clock = base_clock
        self.max_multiplier = max_multiplier
        self.current_multiplier = 1
        self.current_clock = self.base_clock * self.current_multiplier
        self.load = 0

    def adjust_clock(self):
        # 簡単な負荷に基づくクロック速度調整
        if self.load > 75:
            self.current_multiplier = min(self.max_multiplier, self.current_multiplier + 1)
        elif self.load < 25:
            self.current_multiplier = max(1, self.current_multiplier - 1)
        self.current_clock = self.base_clock * self.current_multiplier

    def simulate_load(self):
        # ランダムな負荷の生成
        self.load = random.randint(0, 100)
        print(f"Current load: {self.load}%")

    def run(self):
        # 簡単なシミュレーションループ
        for _ in range(10):  # 10サイクル実行
            self.simulate_load()
            self.adjust_clock()
            print(f"Current clock speed: {self.current_clock} MHz")
            time.sleep(1)  # 1秒待つ

# ベースクロックが100 MHz、最大マルチプライヤーが35のCPUをシミュレート
cpu = CPU(base_clock=100, max_multiplier=35)
cpu.run()