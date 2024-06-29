import psutil  # psutilパッケージを使用してシステムの情報を取得する
import time
import random

class CPU:
    def __init__(self, base_clock, max_multiplier):
        self.base_clock = base_clock
        self.max_multiplier = max_multiplier
        self.current_multiplier = 1
        self.current_clock = self.base_clock * self.current_multiplier

    def adjust_clock(self, system_load):
        # システムの負荷状態に基づいてクロック速度を調整
        if system_load > 75:
            self.current_multiplier = min(self.max_multiplier, self.current_multiplier + 1)
        elif system_load < 25:
            self.current_multiplier = max(1, self.current_multiplier - 1)
        self.current_clock = self.base_clock * self.current_multiplier

    def simulate_system_load(self):
        # psutilを使ってシステムの負荷を取得する
        system_load = psutil.cpu_percent(interval=1)  # CPUの負荷を1秒間隔で取得
        print(f"System load: {system_load}%")
        return system_load

    def run(self):
        while True:
            system_load = self.simulate_system_load()
            self.adjust_clock(system_load)
            print(f"Current clock speed: {self.current_clock} MHz")
            time.sleep(1)  # 1秒待つ

# ベースクロックが1000 MHz、最大マルチプライヤーが350のCPUをシミュレート
cpu = CPU(base_clock=1000, max_multiplier=350)
cpu.run()