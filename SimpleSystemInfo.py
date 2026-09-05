import platform
import sys
import tkinter as tk
from tkinter import ttk
import psutil

class SimpleSystemInfoApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Simple System Info")
        self.geometry("450x520")
        self.resizable(False, False)

        # Style layout
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Create Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

        # Add tabs
        self._build_cpu_tab()
        self._build_memory_tab()
        self._build_system_tab()

    def _add_info_row(self, parent, label_text, value_text, row):
        lbl = ttk.Label(parent, text=label_text, font=("Consolas", 10, "bold"), anchor="w")
        lbl.grid(row=row, column=0, sticky="w", padx=10, pady=6)
        
        val = ttk.Label(parent, text=value_text, font=("Consolas", 10), anchor="w")
        val.grid(row=row, column=1, sticky="w", padx=10, pady=6)

    def _build_cpu_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="CPU")

        # CPU Details
        cpu_freq = psutil.cpu_freq()
        cur_freq = f"{cpu_freq.current:.1f} MHz" if cpu_freq else "N/A"
        max_freq = f"{cpu_freq.max:.1f} MHz" if cpu_freq and cpu_freq.max else "N/A"

        info = [
            ("Processor:", platform.processor() or "Generic CPU"),
            ("Architecture:", platform.machine()),
            ("Physical Cores:", psutil.cpu_count(logical=False)),
            ("Logical Cores:", psutil.cpu_count(logical=True)),
            ("Current Frequency:", cur_freq),
            ("Max Frequency:", max_freq),
            ("CPU Usage:", f"{psutil.cpu_percent(interval=0.1)}%"),
        ]

        for i, (label, val) in enumerate(info):
            self._add_info_row(tab, label, str(val), i)

    def _build_memory_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Memory")

        # RAM Details
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()

        def to_gb(bytes_val):
            return f"{bytes_val / (1024**3):.2f} GB"

        info = [
            ("Total RAM:", to_gb(ram.total)),
            ("Available RAM:", to_gb(ram.available)),
            ("Used RAM:", f"{to_gb(ram.used)} ({ram.percent}%)"),
            ("Total Swap:", to_gb(swap.total)),
            ("Used Swap:", f"{to_gb(swap.used)} ({swap.percent}%)"),
        ]

        for i, (label, val) in enumerate(info):
            self._add_info_row(tab, label, str(val), i)

    def _build_system_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="System")

        # OS Details
        info = [
            ("OS Name:", platform.system()),
            ("OS Release:", platform.release()),
            ("OS Version:", platform.version()),
            ("Node Name:", platform.node()),
            ("Python Version:", sys.version.split()[0]),
        ]

        for i, (label, val) in enumerate(info):
            self._add_info_row(tab, label, str(val), i)


if __name__ == "__main__":
    app = SimpleSystemInfoApp()
    app.mainloop()