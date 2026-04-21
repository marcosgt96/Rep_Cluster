"""
GUI do Cluster Automotivo - Modelo Profissional
Exibe RPM como medidor analógico + barras horizontais para outros sensores
Otimizado para Raspberry Pi
"""

import tkinter as tk
from tkinter import font, Frame, Label, Button, Canvas
from datetime import datetime
from vehicle_sensors import VehicleSensorSimulator, VehicleData
import threading
import time
import math


class RPMGauge(Canvas):
    """Medidor circular de RPM com agulha"""
    
    def __init__(self, parent, width=280, height=280, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        
        self.width = width
        self.height = height
        self.current_value = 0
        self.max_value = 7000
        self.center_x = width / 2
        self.center_y = height / 2
        self.radius = min(width, height) / 2 - 25
        
        self.configure(bg='#1a1a1a', highlightthickness=0)
        self.draw_gauge()
    
    def draw_gauge(self):
        """Desenha o medidor circular"""
        self.delete("all")
        
        # Fundo interno (cinza)
        self.create_oval(
            self.center_x - self.radius + 5,
            self.center_y - self.radius + 5,
            self.center_x + self.radius - 5,
            self.center_y + self.radius - 5,
            fill='#333333',
            outline="#00ff00",
            width=2
        )
        
        # Desenhar marcas e números (0-8) - 0 na direita, máximo no topo
        num_marks = 8
        for i in range(num_marks):
            # 0 na direita (0°), 8 no topo (270°), passando por baixo (180°)
            angle = (i / 8) * 270 + 150 # 0 a 270 graus
            rad = math.radians(angle)
            
            # Posição da marca
            x1 = self.center_x + (self.radius - 20) * math.cos(rad)
            y1 = self.center_y + (self.radius - 20) * math.sin(rad)
            x2 = self.center_x + self.radius * math.cos(rad)
            y2 = self.center_y + self.radius * math.sin(rad)
            
            # Cor: vermelho para zona vermelha (6-8)
            color = '#ff0000' if i >= 6 else '#00ff00'
            
            self.create_line(x1, y1, x2, y2, fill=color, width=3)
            
            # Número
            text_x = self.center_x + (self.radius + 15) * math.cos(rad)
            text_y = self.center_y + (self.radius + 15) * math.sin(rad)
            self.create_text(
                text_x, text_y,
                text=str(i),
                fill='#ffffff',
                font=("Arial", 18, "bold")
            )
        
        # Linha vermelha (redline)
        angle_red = math.radians(90)
        x_red = self.center_x + (self.radius - 5) * math.cos(angle_red)
        y_red = self.center_y + (self.radius - 5) * math.sin(angle_red)
        self.create_line(
            x_red + 15, y_red,
            x_red - 15, y_red,
            fill='#ff0000',
            width=4
        )
    
    def set_value(self, value, gear_change=False):
        """Atualiza agulha e valor"""
        self.current_value = max(0, min(self.max_value, value))
        
        # Remover agulha anterior
        self.delete("needle")
        self.delete("value_display")
        self.delete("rpm_text")
        
        # Calcular ângulo (0 RPM = 0° (direita), 7000 RPM = 270° (topo))
        percentage = self.current_value / self.max_value
        angle = percentage * 270  # De 0° a 270°
        rad = math.radians(angle)
        
        # Desenhar agulha
        needle_length = self.radius - 30
        end_x = self.center_x + needle_length * math.cos(rad)
        end_y = self.center_y + needle_length * math.sin(rad)
        
        self.create_line(
            self.center_x, self.center_y,
            end_x, end_y,
            fill='#ffffff',
            width=4,
            tags="needle"
        )
        
        # Centro da agulha (bolinha)
        self.create_oval(
            self.center_x - 8, self.center_y - 8,
            self.center_x + 8, self.center_y + 8,
            fill='#ffff00',
            outline='#ffffff',
            width=2,
            tags="needle"
        )
        

        
        # Texto "RPM"
        self.create_text(
            self.center_x, self.center_y + 50,
            text=f"{int(self.current_value)} RPM",
            fill='#ffff00',
            font=("Arial", 12, "bold"),
            tags="rpm_text"
        )
        
        # Pontos indicadores (6 pontos amarelos)
        num_dots = int((self.current_value / self.max_value) * 6)
        dot_y = self.center_y + 70
        dot_spacing = 15
        
        for i in range(6):
            dot_x = self.center_x - (dot_spacing * 2.5) + (i * dot_spacing)
            
            # Se gear_change=True, piscar em verde
            if gear_change:
                color = '#00ff00'  # Verde para mudança de marcha
            else:
                color = '#ffff00' if i < num_dots else '#333333'
            
            self.create_oval(
                dot_x - 3, dot_y - 3,
                dot_x + 3, dot_y + 3,
                fill=color,
                outline='#666666',
                tags="needle"
            )


class SpeedGauge(Canvas):
    """Medidor circular de velocidade"""
    
    def __init__(self, parent, width=280, height=280, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        
        self.width = width
        self.height = height
        self.current_value = 0
        self.max_value = 240
        self.center_x = width / 2
        self.center_y = height / 2
        self.radius = min(width, height) / 2 - 25
        
        self.configure(bg='#1a1a1a', highlightthickness=0)
        self.draw_gauge()
    
    def draw_gauge(self):
        """Desenha o medidor circular"""
        self.delete("all")
        
        # Fundo interno (cinza)
        self.create_oval(
            self.center_x - self.radius + 5,
            self.center_y - self.radius + 5,
            self.center_x + self.radius - 5,
            self.center_y + self.radius - 5,
            fill='#333333',
            outline='#00ff00',
            width=2
        )
        
        # Desenhar marcas e números (0-240, de 20 em 20) - 0 na direita, máximo no topo
        for i in range(13):  # 0, 20, 40, ..., 240
            speed = i * 20
            # 0 na direita (0°), 240 no topo (270°), passando por baixo (180°)
            angle = (speed / 240) * 270  # 0 a 270 graus
            rad = math.radians(angle)
            
            # Posição da marca
            x1 = self.center_x + (self.radius - 20) * math.cos(rad)
            y1 = self.center_y + (self.radius - 20) * math.sin(rad)
            x2 = self.center_x + self.radius * math.cos(rad)
            y2 = self.center_y + self.radius * math.sin(rad)
            
            # Cor: vermelho para zona alta (180-240)
            color = '#ff0000' if speed >= 180 else '#00ff00'
            
            self.create_line(x1, y1, x2, y2, fill=color, width=3)
            
            # Número (apenas alguns para não poluir)
            if speed % 40 == 0:
                text_x = self.center_x + (self.radius + 15) * math.cos(rad)
                text_y = self.center_y + (self.radius + 15) * math.sin(rad)
                self.create_text(
                    text_x, text_y,
                    text=str(speed),
                    fill='#ffffff',
                    font=("Arial", 12, "bold")
                )
    
    def set_value(self, value):
        """Atualiza agulha e valor"""
        self.current_value = max(0, min(self.max_value, value))
        
        # Remover agulha anterior
        self.delete("needle")
        self.delete("value_display")
        
        # Calcular ângulo (0 km/h = 0° (direita), 240 km/h = 270° (topo))
        percentage = self.current_value / self.max_value
        angle = percentage * 270  # De 0° a 270°
        rad = math.radians(angle)
        
        # Desenhar agulha
        needle_length = self.radius - 30
        end_x = self.center_x + needle_length * math.cos(rad)
        end_y = self.center_y + needle_length * math.sin(rad)
        
        self.create_line(
            self.center_x, self.center_y,
            end_x, end_y,
            fill='#ffffff',
            width=4,
            tags="needle"
        )
        
        # Centro da agulha (bolinha)
        self.create_oval(
            self.center_x - 8, self.center_y - 8,
            self.center_x + 8, self.center_y + 8,
            fill='#00ffff',
            outline='#ffffff',
            width=2,
            tags="needle"
        )
        
        # Display grande do valor
        self.create_text(
            self.center_x, self.center_y - 10,
            text=str(int(self.current_value)),
            fill='#ffffff',
            font=("Arial", 50, "bold"),
            tags="value_display"
        )
        
        # Texto "KM/H"
        self.create_text(
            self.center_x, self.center_y + 50,
            text="KM/H",
            fill='#00ffff',
            font=("Arial", 12, "bold"),
            tags="needle"
        )


class GearIndicator(Frame):
    """Indicador de marcha"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg='#1a1a1a', **kwargs)
        
        self.current_gear = 0  # 0 = ponto morto, 1-6 = marchas
        
        # Frame principal
        self.configure(bg='#222222', relief='raised', borderwidth=2)
        
        # Label "MARCHA"
        label_font = font.Font(family="Arial", size=10, weight="bold")
        Label(self, text="MARCHA", font=label_font, bg='#222222', 
              fg='#ffff00').pack(pady=2)
        
        # Display da marcha
        self.gear_label = Label(self, text="N", font=("Arial", 36, "bold"),
                               bg='#222222', fg='#00ff00', width=3)
        self.gear_label.pack(pady=5)
        
        # Frame para pontos indicadores de marcha
        self.dots_frame = Frame(self, bg='#222222')
        self.dots_frame.pack(pady=2)
        
        self.dots = []
        for i in range(6):
            dot = Canvas(self.dots_frame, width=20, height=20, bg='#222222', 
                        highlightthickness=0)
            dot.grid(row=0, column=i, padx=2)
            # Desenhar círculo
            dot.create_oval(2, 2, 18, 18, fill='#333333', outline='#666666')
            self.dots.append(dot)
    
    def set_gear(self, gear, gear_change=False):
        """Atualiza a marcha"""
        self.current_gear = max(0, min(6, gear))
        
        # Atualizar texto
        if self.current_gear == 0:
            self.gear_label.config(text="N", fg='#ffff00')
        else:
            self.gear_label.config(text=str(self.current_gear), 
                                 fg='#00ff00' if not gear_change else '#00ff00')
        
        # Atualizar pontos indicadores
        for i, dot in enumerate(self.dots):
            dot.delete("all")
            if gear_change:
                # Piscar em verde quando mudança de marcha
                dot.create_oval(2, 2, 18, 18, fill='#00ff00', outline='#00ff00')
            elif i < self.current_gear:
                dot.create_oval(2, 2, 18, 18, fill='#00ff00', outline='#00ff00')
            else:
                dot.create_oval(2, 2, 18, 18, fill='#333333', outline='#666666')


class HorizontalGauge(Frame):
    """Indicador horizontal com barra lateral (tipo painel real)"""
    
    def __init__(self, parent, label="", unit="", min_val=0, max_val=100, **kwargs):
        super().__init__(parent, bg='#1a1a1a', **kwargs)
        
        self.label_text = label
        self.unit = unit
        self.min_val = min_val
        self.max_val = max_val
        self.current_value = min_val
        
        # Frame superior: Label + Valor
        top_frame = Frame(self, bg='#1a1a1a')
        top_frame.pack(fill='x', padx=5, pady=2)
        
        label_font = font.Font(family="Arial", size=9, weight="bold")
        Label(top_frame, text=label, font=label_font,
              bg='#1a1a1a', fg='#ffff00').pack(side='left')
        
        value_font = font.Font(family="Arial", size=14, weight="bold")
        self.value_label = Label(top_frame, text="0.0", font=value_font,
                                bg='#1a1a1a', fg='#00ff00')
        self.value_label.pack(side='left', padx=10)
        
        unit_font = font.Font(family="Arial", size=8)
        Label(top_frame, text=unit, font=unit_font,
              bg='#1a1a1a', fg='#00ff00').pack(side='left')
        
        # Frame inferior: Barra horizontal
        bar_frame = Frame(self, bg='#1a1a1a', height=20)
        bar_frame.pack(fill='x', padx=5, pady=3)
        bar_frame.pack_propagate(False)
        
        # Canvas para barra
        self.bar_canvas = Canvas(bar_frame, height=16, bg='#1a1a1a', 
                                highlightthickness=1, highlightbackground='#333333')
        self.bar_canvas.pack(fill='x')
        self.bar_canvas.bind('<Configure>', self._on_resize)
        
        # Labels de min e max na barra
        min_max_frame = Frame(self, bg='#1a1a1a')
        min_max_frame.pack(fill='x', padx=5, pady=0)
        
        min_font = font.Font(family="Arial", size=7)
        Label(min_max_frame, text=str(int(min_val)), font=min_font,
              bg='#1a1a1a', fg='#666666').pack(side='left')
        
        Label(min_max_frame, text="", bg='#1a1a1a').pack(side='left', expand=True)
        
        Label(min_max_frame, text=str(int(max_val)), font=min_font,
              bg='#1a1a1a', fg='#666666').pack(side='right')
    
    def _on_resize(self, event):
        """Atualizar barra quando redimensionar"""
        self._update_bar()
    
    def _update_bar(self):
        """Desenha a barra de progresso"""
        self.bar_canvas.delete("bar")
        
        width = self.bar_canvas.winfo_width()
        if width < 2:
            return
        
        height = self.bar_canvas.winfo_height()
        
        # Calcular posição da barra
        percentage = (self.current_value - self.min_val) / (self.max_val - self.min_val)
        bar_width = width * max(0, min(1, percentage))
        
        # Cor adaptativa
        if percentage < 0.33:
            color = '#0066ff'  # Azul
        elif percentage < 0.66:
            color = '#00ff00'  # Verde
        else:
            color = '#ff6600'  # Laranja
        
        # Desenhar fundo (escuro)
        self.bar_canvas.create_rectangle(0, 0, width, height, 
                                        fill='#222222', outline='#444444')
        
        # Desenhar barra preenchida
        self.bar_canvas.create_rectangle(0, 1, bar_width, height - 1,
                                        fill=color, outline=color, tags="bar")
        
        # Linha divisória no meio
        mid_x = width / 2
        self.bar_canvas.create_line(mid_x, 0, mid_x, height,
                                   fill='#333333', dash=(2, 2))
    
    def set_value(self, value):
        """Atualiza valor e barra"""
        self.current_value = max(self.min_val, min(self.max_val, value))
        self.value_label.config(text=f"{self.current_value:.1f}")
        self._update_bar()


class ClusterDisplay(tk.Tk):
    """Interface visual do cluster automotivo - Modelo profissional"""
    
    def __init__(self, use_hardware=False, fullscreen=True):
        super().__init__()
        
        self.title("Cluster Automotivo - Profissional")
        self.geometry("1280x720")
        
        if fullscreen:
            self.attributes('-fullscreen', True)
        
        # Inicia sensor
        self.sensor = VehicleSensorSimulator()
        self.use_hardware = use_hardware
        self.running = True
        self.update_interval = 100  # ms
        
        # Estado do acelerador
        self.throttle_pressed = False
        self.throttle_thread = None
        
        # Marcha atual (0 = ponto morto, 1-6 = marchas)
        self.current_gear = 0
        
        # Velocidade baseada na marcha
        self.current_speed = 0
        
        # Flag para mudança de marcha
        self.gear_change_active = False
        self.gear_change_timer = None
        
        # Configurar estilo
        self.configure(bg='#1a1a1a')
        
        # Criar UI
        self._create_widgets()
        
        # Iniciar atualização
        self._update_display()
        
        # Tratar fechamento
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.bind('<Escape>', lambda e: self._on_closing())
        
        # Bind para teclado
        self.bind('<KeyPress-Up>', lambda e: self._start_throttle())
        self.bind('<KeyRelease-Up>', lambda e: self._stop_throttle())
        self.bind('<KeyPress-w>', lambda e: self._start_throttle())
        self.bind('<KeyRelease-w>', lambda e: self._stop_throttle())
        self.bind('<KeyPress-Right>', lambda e: self._shift_up())
        self.bind('<KeyPress-Left>', lambda e: self._shift_down())
    
    def _create_widgets(self):
        """Cria os widgets da interface"""
        
        # Frame principal
        main_frame = Frame(self, bg='#1a1a1a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Título
        title_font = font.Font(family="Arial", size=14, weight="bold")
        title = Label(main_frame, text="⚙️ CLUSTER AUTOMOTIVO", 
                     font=title_font, bg='#1a1a1a', fg='#00ff00')
        title.pack(pady=5)
        
        # Container principal
        content_frame = Frame(main_frame, bg='#1a1a1a')
        content_frame.pack(fill='both', expand=True)
        
        # ============= ESQUERDA: Velocidade =============
        speed_frame = Frame(content_frame, bg='#1a1a1a')
        speed_frame.pack(side='left', fill='both', padx=5)
        
        self.speed_gauge = SpeedGauge(speed_frame, width=350, height=350, bg='#1a1a1a')
        self.speed_gauge.pack()
        
        # ============= CENTRO: Indicadores + Marcha =============
        center_frame = Frame(content_frame, bg='#1a1a1a')
        center_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        # Indicador de marcha no topo do centro
        self.gear_indicator = GearIndicator(center_frame, width=200, height=120)
        self.gear_indicator.pack(pady=5)
        
        # Indicadores horizontais (4 indicadores empilhados verticalmente, 70% largura)
        indicators_frame = Frame(center_frame, bg='#1a1a1a', width=200)
        indicators_frame.pack(fill='both', expand=True, pady=5)
        indicators_frame.pack_propagate(False)
        
        indicators_data = [
            ("COMBUSTÍVEL", "%", 0, 100, 0),
            ("TEMP", "°C", 0, 150, 1),
            ("PRESSÃO ÓLEO", "BAR", 0, 5, 2),
            ("BATERIA", "V", 10, 16, 3),
        ]
        
        self.indicators = {}
        
        for label, unit, min_v, max_v, idx in indicators_data:
            row = idx // 2
            col = idx % 2
            
            indicator = HorizontalGauge(indicators_frame, label=label, unit=unit,
                                       min_val=min_v, max_val=max_v)
            indicator.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            indicators_frame.grid_columnconfigure(col, weight=1)
            indicators_frame.grid_rowconfigure(row, weight=1)
            
            self.indicators[label] = indicator
        
        # ============= DIREITA: RPM =============
        rpm_frame = Frame(content_frame, bg='#1a1a1a')
        rpm_frame.pack(side='right', fill='both', padx=5)
        
        rpm_label = Label(rpm_frame, text="RPM", font=("Arial", 12, "bold"),
                         bg='#1a1a1a', fg='#00ff00')
        rpm_label.pack()
        
        self.rpm_gauge = RPMGauge(rpm_frame, width=350, height=350, bg='#1a1a1a')
        self.rpm_gauge.pack()
        
        # Frame status/botões
        footer = Frame(main_frame, bg='#1a1a1a')
        footer.pack(fill='both', pady=10)
        
        # Botões de controle
        btn_frame = Frame(footer, bg='#1a1a1a')
        btn_frame.pack(side='left', padx=5)
        
        if not self.use_hardware:
            btn_style = {
                'font': ("Arial", 8, "bold"),
                'padx': 6,
                'pady': 3,
                'border': 0
            }
            
            Button(btn_frame, text="▶ LIGAR", command=self._start_engine,
                   bg='#00aa00', fg='white', **btn_style).pack(side='left', padx=2)
            Button(btn_frame, text="⏹ DESLIGAR", command=self._stop_engine,
                   bg='#cc0000', fg='white', **btn_style).pack(side='left', padx=2)
            
            # Botão único para acelerador (pressionar = acelerar, soltar = desacelerar)
            self.throttle_btn = Button(btn_frame, text="⬆ ACELERAR (segure)",
                                      command=self._toggle_throttle,
                                      bg='#ff6600', fg='white', **btn_style)
            self.throttle_btn.pack(side='left', padx=2)
            
            # Botões de câmbio
            Button(btn_frame, text="▲ MARCHA +", command=self._shift_up,
                   bg='#00aa00', fg='white', **btn_style).pack(side='left', padx=5)
            Button(btn_frame, text="▼ MARCHA -", command=self._shift_down,
                   bg='#cc0000', fg='white', **btn_style).pack(side='left', padx=2)
        
        # Status
        status_frame = Frame(footer, bg='#1a1a1a')
        status_frame.pack(side='right', padx=5)
        
        status_font = font.Font(family="Arial", size=8)
        self.status_label = Label(status_frame, text="Inicializando...",
                                  font=status_font, bg='#1a1a1a', fg='#ffff00')
        self.status_label.pack()
    
    def _calculate_speed_from_rpm_and_gear(self, rpm, gear):
        """Calcula velocidade baseada no RPM e marcha"""
        if gear == 0:  # Ponto morto
            return 0
        
        # Ranges de velocidade por marcha
        gear_ranges = {
            1: (0, 60),
            2: (60, 90),
            3: (90, 120),
            4: (120, 160),
            5: (160, 200),
            6: (200, 220),
        }
        
        min_speed, max_speed = gear_ranges[gear]
        
        # RPM válido de 1000 a 7000
        rpm_normalized = max(0, min(7000, rpm) - 1000) / 6000  # 0 a 1
        
        # Calcular velocidade baseada no RPM
        speed = min_speed + (max_speed - min_speed) * rpm_normalized
        
        return min(max_speed, speed)
    
    def _auto_shift(self):
        """Mudança automática de marcha quando RPM >= 5500"""
        if self.current_gear < 6 and self.sensor.rpm >= 5500:
            self._shift_up()
            return True
        return False
    
    def _trigger_gear_change_animation(self):
        """Ativa animação de mudança de marcha"""
        self.gear_change_active = True
        
        # Cancelar timer anterior se existir
        if self.gear_change_timer:
            self.after_cancel(self.gear_change_timer)
        
        # Desativar após 500ms
        self.gear_change_timer = self.after(500, self._end_gear_change_animation)
    
    def _end_gear_change_animation(self):
        """Encerra animação de mudança de marcha"""
        self.gear_change_active = False
    
    def _update_display(self):
        """Atualiza os valores no display"""
        if not self.running:
            return
        
        # Consumir combustível se motor ligado
        if self.sensor.engine_running:
            self.sensor.consume_fuel(0.01)
        
        # Mudança automática desativada - apenas mudança manual via botões
        
        # Obter dados
        data = self.sensor.get_current_data()
        
        # Calcular velocidade baseada na marcha
        if self.current_gear > 0 and self.sensor.engine_running:
            self.current_speed = self._calculate_speed_from_rpm_and_gear(
                data.rpm, self.current_gear
            )
        else:
            self.current_speed = 0
        
        # Atualizar gauges
        self.rpm_gauge.set_value(data.rpm, gear_change=self.gear_change_active)
        self.speed_gauge.set_value(self.current_speed)
        
        # Atualizar indicador de marcha
        self.gear_indicator.set_gear(self.current_gear, gear_change=self.gear_change_active)
        
        # Atualizar indicadores horizontais
        self.indicators["COMBUSTÍVEL"].set_value(data.fuel_level)
        self.indicators["TEMP"].set_value(data.coolant_temp)
        self.indicators["PRESSÃO ÓLEO"].set_value(data.oil_pressure)
        self.indicators["BATERIA"].set_value(13.5)
        
        # Atualizar status
        gear_text = f" | Marcha: {self.current_gear}" if self.current_gear > 0 else " | N"
        status = "🟢 MOTOR LIGADO" if self.sensor.engine_running else "⚫ MOTOR DESLIGADO"
        self.status_label.config(text=f"{status}{gear_text} | {datetime.now().strftime('%H:%M:%S')}")
        
        # Agendar próxima atualização
        self.after(self.update_interval, self._update_display)
    
    def _start_engine(self):
        """Inicia o motor"""
        self.sensor.start_engine()
    
    def _stop_engine(self):
        """Para o motor"""
        self.sensor.stop_engine()
        self.current_speed = 0
        self.current_gear = 0
    
    def _toggle_throttle(self):
        """Alterna estado do acelerador"""
        if self.throttle_pressed:
            self._stop_throttle()
        else:
            self._start_throttle()
    
    def _start_throttle(self):
        """Inicia aceleração"""
        if not self.throttle_pressed and self.sensor.engine_running:
            self.throttle_pressed = True
            self.throttle_btn.config(text="▼ DESACELERAR (segure)", bg='#0066ff')
            self.throttle_thread = threading.Thread(target=self._throttle_thread, daemon=True)
            self.throttle_thread.start()
    
    def _stop_throttle(self):
        """Para aceleração"""
        self.throttle_pressed = False
        self.throttle_btn.config(text="⬆ ACELERAR (segure)", bg='#ff6600')
        
        # Desacelerar
        if self.sensor.engine_running:
            thread = threading.Thread(target=self._decelerate_thread, daemon=True)
            thread.start()
    
    def _throttle_thread(self):
        """Thread para manter aceleração enquanto pressionado"""
        while self.throttle_pressed and self.sensor.engine_running:
            self.sensor.accelerate(150)
            time.sleep(0.05)
    
    def _decelerate_thread(self):
        """Thread para desacelerar suavemente"""
        for _ in range(15):
            if not self.sensor.engine_running:
                break
            self.sensor.decelerate(100)
            time.sleep(0.08)
    
    def _shift_up(self):
        """Sobe a marcha"""
        if self.current_gear < 6:
            self.current_gear += 1
            self._trigger_gear_change_animation()
    
    def _shift_down(self):
        """Diminui a marcha"""
        if self.current_gear > 0:
            self.current_gear -= 1
            self._trigger_gear_change_animation()
    
    def _on_closing(self):
        """Tratamento ao fechar a janela"""
        self.running = False
        self.throttle_pressed = False
        self.sensor.stop_engine()
        self.destroy()


if __name__ == "__main__":
    # Teste em modo simulação (sem hardware real)
    app = ClusterDisplay(use_hardware=False, fullscreen=False)
    app.mainloop()
