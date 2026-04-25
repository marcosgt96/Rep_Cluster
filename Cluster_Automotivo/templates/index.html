<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>CAN Cluster</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Rajdhani:wght@300;400;600;700&display=swap');

  :root {
    --bg:        #050608;
    --panel:     #0a0c10;
    --border:    #1a1f2e;
    --accent:    #e8630a;
    --accent2:   #f5a623;
    --warn:      #ffcc00;
    --danger:    #e8200a;
    --safe:      #0ae86b;
    --blue:      #0a8ee8;
    --text:      #c8d0e0;
    --dim:       #4a5568;
    --glow:      rgba(232,99,10,0.35);
    --glow2:     rgba(232,99,10,0.15);
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  html, body {
    width:100%; height:100%;
    background: var(--bg);
    font-family: 'Rajdhani', sans-serif;
    color: var(--text);
    overflow: hidden;
    user-select: none;
  }

  body {
    background:
      radial-gradient(ellipse 80% 50% at 50% -10%, rgba(232,99,10,0.08) 0%, transparent 70%),
      repeating-linear-gradient(
        0deg,
        transparent,
        transparent 39px,
        rgba(255,255,255,0.018) 39px,
        rgba(255,255,255,0.018) 40px
      ),
      repeating-linear-gradient(
        90deg,
        transparent,
        transparent 39px,
        rgba(255,255,255,0.018) 39px,
        rgba(255,255,255,0.018) 40px
      ),
      var(--bg);
  }

  /* ── LAYOUT ─────────────────────────────────────────── */
  .cluster {
    display: grid;
    width: 100vw; height: 100vh;
    grid-template-columns: 1fr 1.35fr 1fr;
    grid-template-rows: auto 1fr auto;
    gap: 10px;
    padding: 20px;
  }

  /* Top bar */
  .topbar {
    grid-column: 1 / -1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4px 16px;
    border-bottom: 1px solid var(--border);
  }

  .logo {
    font-family: 'Orbitron', monospace;
    font-weight: 900;
    font-size: 0.85rem;
    letter-spacing: 0.35em;
    color: var(--accent);
    text-shadow: 0 0 12px var(--accent);
  }

  .topbar-center {
    display: flex; gap: 28px; align-items: center;
  }

  .gear-display {
    font-family: 'Orbitron', monospace;
    font-size: 3.2rem;
    font-weight: 900;
    color: var(--accent2);
    text-shadow: 0 0 18px var(--accent2);
    line-height: 1;
  }

  .gear-label {
    font-size: 0.9rem;
    letter-spacing: 0.2em;
    color: var(--dim);
    text-transform: uppercase;
  }

  .panel-gear {
    position: absolute;
    right: 119PX;
    bottom: 18px;
    text-align: center;
  }

  .panel-gear .gear-display {
    margin: 0;
  }

  .panel-gear .gear-label {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: var(--dim);
    text-transform: uppercase;
    margin-top: 2px;
  }

  .topbar-stat {
    display: flex; flex-direction: column; align-items: center;
    gap: 2px;
  }

  .topbar-val {
    font-family: 'Orbitron', monospace;
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text);
  }

  .topbar-lbl {
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    color: var(--dim);
    text-transform: uppercase;
  }

  .clock {
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    font-weight: 600;
    color: var(--dim);
    letter-spacing: 0.12em;
  }

  .status-led {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--safe);
    box-shadow: 0 0 8px var(--safe);
    animation: pulse-led 2s ease-in-out infinite;
  }

  @keyframes pulse-led {
    0%,100% { opacity:1; } 50% { opacity:0.4; }
  }

  /* ── PANELS ─────────────────────────────────────────── */
  .panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px;
  }

  .panel::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 60% 30% at 50% 0%, rgba(232,99,10,0.07) 0%, transparent 70%);
    pointer-events: none;
  }

  .panel-title {
    font-size: 0.8rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--dim);
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    white-space: nowrap;
  }

  /* ── CANVAS GAUGES ──────────────────────────────────── */
  canvas { display: block; }

  /* ── CENTER SPEED PANEL ─────────────────────────────── */
  .panel-center {
    grid-column: 2;
    grid-row: 2;
    border-color: rgba(232,99,10,0.3);
    box-shadow:
      inset 0 0 40px rgba(0,0,0,0.6),
      0 0 30px rgba(232,99,10,0.12);
  }

  .speed-value {
    font-family: 'Orbitron', monospace;
    font-size: clamp(3.5rem, 7vw, 6rem);
    font-weight: 900;
    color: #fff;
    line-height: 1;
    text-shadow:
      0 0 30px rgba(255,255,255,0.25),
      0 0 60px rgba(232,99,10,0.3);
    letter-spacing: -0.02em;
  }

  .speed-unit {
    font-family: 'Orbitron', monospace;
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 0.3em;
    margin-top: 2px;
  }

  .speed-sub {
    display: flex; gap: 24px; margin-top: 8px;
  }

  .speed-sub-item {
    display: flex; flex-direction: column; align-items: center;
  }

  .speed-sub-val {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent2);
  }

  .speed-sub-lbl {
    font-size: 0.55rem;
    letter-spacing: 0.15em;
    color: var(--dim);
    text-transform: uppercase;
    margin-top: 1px;
  }

  /* ── WARNING LIGHTS BAR ─────────────────────────────── */
  .warn-bar {
    grid-column: 1 / -1;
    grid-row: 3;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    padding: 6px 16px;
    border-top: 1px solid var(--border);
  }

  .warn-light {
    display: flex; flex-direction: column; align-items: center; gap: 3px;
  }

  .warn-icon {
    width: 28px; height: 28px;
    border-radius: 50%;
    background: #111;
    border: 1.5px solid #2a2f3e;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.6rem;
    font-weight: 900;
    letter-spacing: 0.05em;
    color: #2a2f3e;
    transition: all 0.3s ease;
  }

  .warn-icon.active-warn   { background: var(--warn);   border-color: var(--warn);   color: #000; box-shadow: 0 0 10px var(--warn);   }
  .warn-icon.active-danger { background: var(--danger);  border-color: var(--danger);  color: #fff; box-shadow: 0 0 10px var(--danger);  }
  .warn-icon.active-safe   { background: var(--safe);   border-color: var(--safe);   color: #000; box-shadow: 0 0 10px var(--safe);   }
  .warn-icon.active-blue   { background: var(--blue);   border-color: var(--blue);   color: #fff; box-shadow: 0 0 10px var(--blue);   }

  .warn-lbl {
    font-size: 0.5rem;
    letter-spacing: 0.1em;
    color: var(--dim);
    text-transform: uppercase;
  }

  /* ── MINI GAUGES (bottom row panels) ────────────────── */
  .mini-grid {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 8px;
  }

  /* ── HORIZONTAL BAR GAUGE ───────────────────────────── */
  .bar-gauge {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 0px;
  }

  .bar-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }

  .bar-name {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--dim);
  }

  .bar-reading {
    font-family: 'Orbitron', monospace;
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--text);
  }

  .bar-unit {
    font-size: 0.7rem;
    color: var(--dim);
    margin-left: 2px;
  }

  .bar-track {
    width: 100%;
    height: 7px;
    background: rgba(255,255,255,0.06);
    border-radius: 3px;
    overflow: hidden;
    position: relative;
  }

  .bar-fill {
    height: 100%;
    border-radius: 3px;
    transition: width 0.3s ease;
    position: relative;
  }

  .bar-fill::after {
    content: '';
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 4px;
    background: rgba(255,255,255,0.6);
    border-radius: 2px;
  }

  .bar-ticks {
    display: flex;
    justify-content: space-between;
  }

  .bar-tick {
    font-size: 0.80rem;
    color: #414550;
  }

  /* ── RPM PANEL ──────────────────────────────────────── */
  .rpm-value {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 900;
    color: var(--accent);
    text-shadow: 0 0 20px var(--glow);
    line-height: 1;
  }

  .rpm-unit {
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    color: var(--dim);
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* ── VOLTAGE ────────────────────────────────────────── */
  .volt-value {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 900;
    line-height: 1;
    transition: color 0.4s, text-shadow 0.4s;
  }

  .volt-good { color: var(--safe); text-shadow: 0 0 16px var(--safe); }
  .volt-warn { color: var(--warn); text-shadow: 0 0 16px var(--warn); }
  .volt-bad  { color: var(--danger); text-shadow: 0 0 16px var(--danger); }

  /* ── ODOMETER STRIP ─────────────────────────────────── */
  .odo-strip {
    display: flex; gap: 2px; align-items: center;
  }

  .odo-digit {
    background: #0d0f15;
    border: 1px solid #2a2f3e;
    border-radius: 3px;
    width: 22px; height: 30px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent2);
  }

  .odo-digit:last-child {
    color: var(--accent);
    border-color: var(--accent);
    background: rgba(232,99,10,0.08);
  }

  .odo-label {
    font-size: 0.55rem;
    letter-spacing: 0.15em;
    color: var(--dim);
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  /* ── SEPARATOR ───────────────────────────────────────── */
  .v-sep {
    width: 1px;
    background: var(--border);
    margin: 0 4px;
    align-self: stretch;
  }

  /* ── TEMP RING ───────────────────────────────────────── */
  .temp-badge {
    display: flex; flex-direction: column; align-items: center; gap: 2px;
  }

  .temp-val {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.4rem, 2.5vw, 2rem);
    font-weight: 900;
    line-height: 1;
    transition: color 0.4s, text-shadow 0.4s;
  }

  .temp-ok   { color: var(--safe);   text-shadow: 0 0 14px var(--safe); }
  .temp-warm { color: var(--accent2); text-shadow: 0 0 14px var(--accent2); }
  .temp-hot  { color: var(--danger);  text-shadow: 0 0 14px var(--danger); }

  .temp-unit {
    font-size: 0.55rem;
    letter-spacing: 0.18em;
    color: var(--dim);
    text-transform: uppercase;
  }

  /* RPM LED bar */
  .rpm-leds {
    display: flex; gap: 3px; margin-top: 5px;
  }

  .rpm-led {
    width: 12px; height: 5px;
    border-radius: 2px;
    background: rgba(255,255,255,0.06);
    transition: background 0.1s, box-shadow 0.1s;
  }

  .rpm-led.on-green  { background: var(--safe);   box-shadow: 0 0 6px var(--safe); }
  .rpm-led.on-yellow { background: var(--warn);   box-shadow: 0 0 6px var(--warn); }
  .rpm-led.on-red    { background: var(--danger);  box-shadow: 0 0 6px var(--danger); }

  /* CAN activity blip */
  .can-activity {
    display: flex; align-items: center; gap: 5px;
  }

  .can-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--safe);
  }

  @keyframes can-blip {
    0%   { opacity: 1; transform: scale(1); }
    50%  { opacity: 0.2; transform: scale(0.6); }
    100% { opacity: 1; transform: scale(1); }
  }

  .can-dot.active { animation: can-blip 0.15s ease; }

  .can-label {
    font-size: 0.55rem;
    letter-spacing: 0.2em;
    color: var(--dim);
    font-family: 'Orbitron', monospace;
  }

  /* divider accent line */
  .accent-line {
    width: 40px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    border-radius: 1px;
    margin: 6px 0;
  }

  /* scroll animation on load */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .panel { animation: fadeUp 0.5s ease both; }
  .panel:nth-child(1)  { animation-delay: 0.05s; }
  .panel:nth-child(2)  { animation-delay: 0.10s; }
  .panel:nth-child(3)  { animation-delay: 0.15s; }
  .panel:nth-child(4)  { animation-delay: 0.20s; }
  .panel:nth-child(5)  { animation-delay: 0.25s; }

  /* boost badge */
  .boost-row {
    display: flex; align-items: baseline; gap: 4px;
  }

  .boost-sign {
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--accent);
  }

  .boost-num {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.4rem, 2.5vw, 2rem);
    font-weight: 900;
    color: var(--accent);
    text-shadow: 0 0 14px var(--glow);
  }
</style>
<script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
</head>
<body>

<div class="cluster" id="cluster">

  <!-- ─── TOP BAR ──────────────────────────────────────── -->
  <div class="topbar">
    <div class="logo">CAN CLUSTER v2.1</div>

    <div class="topbar-center">
      <div class="topbar-stat">
        <div class="topbar-val" id="top-coolant">--</div>
        <div class="topbar-lbl">COOLANT C</div>
      </div>
      <div class="v-sep"></div>

      <div>
        <div class="gear-display" id="gear-disp">3</div>
        <div class="gear-label">GEAR</div>
        
      </div>

      <div class="v-sep"></div>
      <div class="topbar-stat">
        <div class="topbar-val" id="top-odo">--</div>
        <div class="topbar-lbl">ODO  KM</div>
      </div>
    </div>

    <div style="display:flex;align-items:center;gap:14px;">
      <div class="can-activity">
        <div class="can-dot" id="can-dot"></div>
        <span class="can-label">CAN BUS</span>
      </div>
      <div class="status-led" id="status-led"></div>
      <div class="clock" id="clock">00:00:00</div>
    </div>
  </div>

  <!-- ─── LEFT PANEL: RPM ──────────────────────────────── -->
  <div class="panel" style="grid-column:1; grid-row:2; animation-delay:0.3s">
    <span class="panel-title">TACÔMETRO</span>
    <canvas id="rpmGauge" width="275" height="275"></canvas>
    <div class="rpm-leds" id="rpm-leds">
      <!-- JS generated -->
    </div>
    <div style="margin-top:10px; display:flex; flex-direction:column; align-items:center;">
      <div class="rpm-value" id="rpm-val">1</div>
      <div class="rpm-unit">RPM x 1000</div>
    </div>
  </div>

  <!-- ─── CENTER PANEL: SPEEDOMETER ───────────────────── -->
  <div class="panel panel-center" style="grid-row:2; animation-delay:0.2s">
    <span class="panel-title">VELOCÍMETRO</span>
    <canvas id="speedGauge" width="315" height="315"></canvas>
    <div style="position:absolute; bottom: 15%; display:flex; flex-direction:column; align-items:center;">
      <div class="speed-value" id="speed-val">0</div>
      <div class="speed-unit">KM/H</div>
      <div class="accent-line"></div>
      <div class="speed-sub">
        <div class="speed-sub-item">
          <div class="speed-sub-val" id="tripA-val">0.0</div>
          <div class="speed-sub-lbl">TRIP A</div>
        </div>
        <div class="v-sep" style="height:30px; align-self:center;"></div>
        <div class="speed-sub-item">
          <div class="speed-sub-val" id="tripB-val">0.0</div>
          <div class="speed-sub-lbl">TRIP B</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ─── RIGHT PANEL: GAUGES ──────────────────────────── -->
  <div class="panel" style="grid-column:3; grid-row:2; gap:10px; animation-delay:0.3s">
    <span class="panel-title">INSTRUMENTOS</span>

    <!-- Fuel -->
    <div class="bar-gauge" style="width:90%;">
      <div class="bar-header">
        <span class="bar-name">Combustivel</span>
        <span><span class="bar-reading" id="fuel-val">75</span><span class="bar-unit">%</span></span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" id="fuel-bar" style="width:75%; background: linear-gradient(90deg, var(--safe), #05c956);"></div>
      </div>
      <div class="bar-ticks">
        <span class="bar-tick">E</span>
        <span class="bar-tick">1/4</span>
        <span class="bar-tick">1/2</span>
        <span class="bar-tick">3/4</span>
        <span class="bar-tick">F</span>
      </div>
    </div>

    <div class="accent-line"></div>

    <!-- Water Temp Engine -->
    <div class="bar-gauge" style="width:90%;">
      <div class="bar-header">
        <span class="bar-name">Temp. Agua Motor</span>
        <span><span class="bar-reading" id="oiltemp-val">92</span><span class="bar-unit">C</span></span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" id="oiltemp-bar" style="width:55%; background: linear-gradient(90deg, var(--accent), var(--accent2));"></div>
      </div>
      <div class="bar-ticks">
        <span class="bar-tick">40</span>
        <span class="bar-tick">80</span>
        <span class="bar-tick">125</span>
      </div>
    </div>

    <div class="accent-line"></div>

    <!-- Engine Oil Pressure -->
    <div class="bar-gauge" style="width:90%;">
      <div class="bar-header">
        <span class="bar-name">Pressão Oleo Motor</span>
        <span><span class="bar-reading" id="oilpressure-val">2.8</span><span class="bar-unit">bar</span></span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" id="oilpressure-bar" style="width:45%; background: linear-gradient(90deg, var(--blue), #3ab5ff);"></div>
      </div>
      <div class="bar-ticks">
        <span class="bar-tick">0</span>
        <span class="bar-tick">2.7</span>
        <span class="bar-tick">5.4</span>
      </div>
    </div>

    <div class="accent-line"></div>

    <!-- Average Consumption -->
    <div style="display:flex; align-items:center; justify-content:space-between; width:90%;">
      <div class="bar-gauge" style="flex:1;">
        <div class="bar-header">
          <span class="bar-name">Consumo Médio</span>
          <span><span class="bar-reading" id="consumption-val">8.5</span><span class="bar-unit">km/l</span></span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" id="consumption-bar" style="width:53%; background: linear-gradient(90deg, var(--accent2), var(--warn));"></div>
        </div>
        <div class="bar-ticks">
          <span class="bar-tick">0</span>
          <span class="bar-tick">7.5</span>
          <span class="bar-tick">15</span>
        </div>
      </div>
    </div>

    <div class="accent-line"></div>

    <!-- Battery Voltage -->
    <div style="display:flex; align-items:center; gap:80px; width:90%;">
      <div style="display:flex; flex-direction:column; align-items:flex-start; flex:1;">
        <span class="bar-name">Bateria</span>
        <div style="display:flex; align-items:baseline; gap:4px; margin-top:3px;">
          <div class="volt-value volt-good" id="volt-val">14.2</div>
          <span style="font-size:0.6rem; color:var(--dim);">V</span>
        </div>
      </div>
      <canvas id="voltMini" width="70" height="70"></canvas>
    </div>

  </div>

  <!-- ─── BOTTOM WARNING LIGHTS BAR ─────────────────────── -->
  <div class="warn-bar">
    <div class="warn-light">
      <div class="warn-icon" id="wl-oil">OIL</div>
      <span class="warn-lbl">Oleo</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-temp">TMP</div>
      <span class="warn-lbl">Temp</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-bat">BAT</div>
      <span class="warn-lbl">Bateria</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-abs">ABS</div>
      <span class="warn-lbl">ABS</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-esp">ESP</div>
      <span class="warn-lbl">ESP</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-eng">ENG</div>
      <span class="warn-lbl">Motor</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-fuel">FUL</div>
      <span class="warn-lbl">Combust.</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-door">DOR</div>
      <span class="warn-lbl">Porta</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-belt">BLT</div>
      <span class="warn-lbl">Cinto</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-tpms">TPM</div>
      <span class="warn-lbl">Pneu</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon active-safe" id="wl-can">CAN</div>
      <span class="warn-lbl">CAN OK</span>
    </div>
    <div class="warn-light">
      <div class="warn-icon" id="wl-park">PRK</div>
      <span class="warn-lbl">Freio</span>
    </div>

    <div style="margin-left:auto; display:flex; flex-direction:column; align-items:flex-end; gap:2px;">
      <div class="odo-label">HODOMETRO</div>
      <div class="odo-strip" id="odo-strip"></div>
    </div>
  </div>

</div>

<script>
/* ─────────────────────────────────────────────────────────
   CANVAS GAUGE HELPER
───────────────────────────────────────────────────────── */
const PI = Math.PI;

function drawArcGauge(ctx, cx, cy, r, startAngle, endAngle, value, minVal, maxVal, opts = {}) {
  const {
    bgColor   = 'rgba(255,255,255,0.05)',
    arcWidth  = 14,
    zones     = [],      // [{from,to,color}]
    needleColor = '#fff',
    showNeedle  = true,
    innerGlow   = true,
  } = opts;

  const frac = Math.min(1, Math.max(0, (value - minVal) / (maxVal - minVal)));
  const sweep = endAngle - startAngle;
  const curAngle = startAngle + frac * sweep;

  ctx.clearRect(cx - r - 20, cy - r - 20, (r + 20) * 2, (r + 20) * 2);

  // background arc
  ctx.save();
  ctx.beginPath();
  ctx.arc(cx, cy, r, startAngle, endAngle);
  ctx.strokeStyle = bgColor;
  ctx.lineWidth = arcWidth;
  ctx.lineCap = 'round';
  ctx.stroke();
  ctx.restore();

  // colored zones
  if (zones.length) {
    zones.forEach(z => {
      const za = startAngle + ((z.from - minVal) / (maxVal - minVal)) * sweep;
      const ze = startAngle + ((z.to   - minVal) / (maxVal - minVal)) * sweep;
      ctx.save();
      ctx.beginPath();
      ctx.arc(cx, cy, r, za, ze);
      ctx.strokeStyle = z.color;
      ctx.lineWidth = arcWidth;
      ctx.lineCap = 'butt';
      ctx.globalAlpha = 0.25;
      ctx.stroke();
      ctx.restore();
    });
  }

  // active arc
  ctx.save();
  const grad = ctx.createConicalGradient ? null : null; // fallback
  ctx.beginPath();
  ctx.arc(cx, cy, r, startAngle, curAngle);
  ctx.strokeStyle = opts.fillColor || '#e8630a';
  ctx.lineWidth = arcWidth;
  ctx.lineCap = 'round';
  ctx.shadowColor = opts.fillColor || '#e8630a';
  ctx.shadowBlur = 14;
  ctx.stroke();
  ctx.restore();

  // tick marks
  const tickCount = opts.ticks || 9;
  for (let i = 0; i <= tickCount; i++) {
    const t = i / tickCount;
    const a = startAngle + t * sweep;
    const isMajor = i % Math.ceil(tickCount / 8) === 0;
    const inner = r - arcWidth - (isMajor ? 12 : 10);
    const outer = r - arcWidth - -1;
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(cx + Math.cos(a) * inner, cy + Math.sin(a) * inner);
    ctx.lineTo(cx + Math.cos(a) * outer, cy + Math.sin(a) * outer);
    ctx.strokeStyle = isMajor ? 'rgba(200,208,224,0.5)' : 'rgba(200,208,224,0.18)';
    ctx.lineWidth = isMajor ? 2 : 1;
    ctx.stroke();
    ctx.restore();
  }

  // needle
  if (showNeedle) {
    const needleLen   = r - arcWidth - 22;
    const needleBase  = 10;
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(curAngle);
    ctx.beginPath();
    ctx.moveTo(-needleBase, 0);
    ctx.lineTo(needleLen, 0);
    ctx.strokeStyle = needleColor;
    ctx.lineWidth = 2.5;
    ctx.lineCap = 'round';
    ctx.shadowColor = needleColor;
    ctx.shadowBlur = 12;
    ctx.stroke();
    ctx.restore();

    // center cap
    ctx.save();
    ctx.beginPath();
    ctx.arc(cx, cy, 7, 0, PI * 2);
    ctx.fillStyle = '#0a0c10';
    ctx.fill();
    ctx.strokeStyle = opts.fillColor || '#e8630a';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();
  }
}

// Conical gradient polyfill for canvas
CanvasRenderingContext2D.prototype.createConicalGradient = undefined;

/* ─────────────────────────────────────────────────────────
   GAUGE SETUP
───────────────────────────────────────────────────────── */
const rpmCanvas   = document.getElementById('rpmGauge');
const speedCanvas = document.getElementById('speedGauge');
const voltCanvas  = document.getElementById('voltMini');

const rpmCtx   = rpmCanvas.getContext('2d');
const speedCtx = speedCanvas.getContext('2d');
const voltCtx  = voltCanvas.getContext('2d');

const START_ANGLE = (PI * 0.80);
const END_ANGLE   = (PI * 2.21);

function renderRPM(val) {
  const cx = rpmCanvas.width  / 2;
  const cy = rpmCanvas.height / 2;
  const r  = 120;

  drawArcGauge(rpmCtx, cx, cy, r, START_ANGLE, END_ANGLE, val, 0, 7000, {
    arcWidth: 9,
    fillColor: val > 5500 ? '#e8200a' : val > 3000 ? '#ffcc00' : '#1af86b',
    needleColor: '#ffffff',
    ticks: 21,
    zones: [
      { from: 0,    to: 3000, color: '#0ae86b' },
      { from: 3000, to: 5500, color: '#e8630a' },
      { from: 5500, to: 7000, color: '#e8200a' },
    ]
  });

  // RPM label inside
  rpmCtx.save();
  rpmCtx.font = '600 11px Orbitron, monospace';
  rpmCtx.fillStyle = 'rgba(200,208,224,0.7)';
  rpmCtx.textAlign = 'center';
  const ticks = [0, 1, 2, 3, 4, 5, 6, 7];
  ticks.forEach((t, i) => {
    const frac = i / (ticks.length - 1);
    const a = START_ANGLE + frac * (END_ANGLE - START_ANGLE);
    const lbl_r = r - 15 - 20;
    rpmCtx.fillText(t, cx + Math.cos(a) * lbl_r, cy + Math.sin(a) * lbl_r + 4);
  });
  rpmCtx.restore();
}

function renderSpeed(val) {
  const cx = speedCanvas.width  / 2;
  const cy = speedCanvas.height / 2;
  const r  = 140;

  drawArcGauge(speedCtx, cx, cy, r, START_ANGLE, END_ANGLE, val, 0, 220, {
    arcWidth: 11,
    fillColor: val > 179 ? '#e8200a' : val > 119 ? '#ffcc00' : '#1af86b',
    needleColor: '#ffffff',
    ticks: 40,
    zones: [
      { from: 0,   to: 120, color: '#0ae86b' },
      { from: 120, to: 180, color: '#e8630a' },
      { from: 180, to: 220, color: '#e8200a' },
    ]
  });

  // Speed labels
  speedCtx.save();
  speedCtx.font = '600 15px Orbitron, monospace';
  speedCtx.fillStyle = 'rgba(200,208,224,0.7)';
  speedCtx.textAlign = 'center';
  [0, 0, 20, 40, 40, 60, 80, 80, 100, 120, 120, 140, 160, 160, 180, 200, 200, 220].forEach((s, i) => {
    const frac = s / 220;
    const a = START_ANGLE + frac * (END_ANGLE - START_ANGLE);
    const lbl_r = r - 13 - 30;
    speedCtx.fillText(s, cx + Math.cos(a) * lbl_r, cy + Math.sin(a) * lbl_r + 4);
  });
  speedCtx.restore();
}

function renderVoltMini(val) {
  const cx = 35; const cy = 35; const r = 26;
  const good = val >= 13.5;
  const warn = val >= 11.5 && val < 13.5;
  const col = good ? '#0ae86b' : warn ? '#ffcc00' : '#e8200a';

  voltCtx.clearRect(0, 0, 70, 70);

  // bg ring
  voltCtx.beginPath();
  voltCtx.arc(cx, cy, r, 0, PI * 2);
  voltCtx.strokeStyle = 'rgba(255,255,255,0.06)';
  voltCtx.lineWidth = 6;
  voltCtx.stroke();

  // fill
  const frac = Math.min(1, Math.max(0, (val - 10) / 8));
  voltCtx.beginPath();
  voltCtx.arc(cx, cy, r, -PI/2, -PI/2 + frac * PI * 2);
  voltCtx.strokeStyle = col;
  voltCtx.lineWidth = 6;
  voltCtx.lineCap = 'round';
  voltCtx.shadowColor = col;
  voltCtx.shadowBlur = 10;
  voltCtx.stroke();
}

/* ─────────────────────────────────────────────────────────
   RPM LED BAR
───────────────────────────────────────────────────────── */
const rpmLedsContainer = document.getElementById('rpm-leds');
const LED_COUNT = 14;
for (let i = 0; i < LED_COUNT; i++) {
  const d = document.createElement('div');
  d.className = 'rpm-led';
  d.id = `rled-${i}`;
  rpmLedsContainer.appendChild(d);
}

function updateRPMLeds(rpm) {
  const max = 7000;
  const frac = rpm / max;
  const lit = Math.round(frac * LED_COUNT);
  for (let i = 0; i < LED_COUNT; i++) {
    const el = document.getElementById(`rled-${i}`);
    el.className = 'rpm-led';
    if (i < lit) {
      if (rpm > 5100) el.classList.add('on-red');
      else if (rpm > 3500) el.classList.add('on-yellow');
      else el.classList.add('on-green');
    }
  }
}

/* ─────────────────────────────────────────────────────────
   UPDATE DISPLAY FUNCTION
───────────────────────────────────────────────────────── */
function updateDisplay(data) {
  // RPM
  document.getElementById('rpm-val').textContent = Math.round(data.rpm / 1000);
  renderRPM(data.rpm);
  updateRPMLeds(data.rpm);

  // Speed
  document.getElementById('speed-val').textContent = Math.round(data.speed);
  renderSpeed(data.speed);

  // Fuel
  document.getElementById('fuel-val').textContent = Math.round(data.fuel);
  document.getElementById('fuel-bar').style.width = data.fuel + '%';

  // coolant temp (Water Temperature)
  document.getElementById('oiltemp-val').textContent = data.coolant;
  const oilPerc = ((data.coolant - 40) / (125 - 40)) * 100;
  document.getElementById('oiltemp-bar').style.width = Math.max(0, Math.min(100, oilPerc)) + '%';

  // Oil pressure
  document.getElementById('oilpressure-val').textContent = (data.oil_pressure || 2.8).toFixed(1);
  const oilPressPerc = ((data.oil_pressure || 2.8) / 5.4) * 100;
  document.getElementById('oilpressure-bar').style.width = Math.max(0, Math.min(100, oilPressPerc)) + '%';

  // Fuel consumption
  document.getElementById('consumption-val').textContent = (data.fuel_consumption || 8.5).toFixed(1);
  const consumptionPerc = ((data.fuel_consumption || 8.5) / 15) * 100;
  document.getElementById('consumption-bar').style.width = Math.max(0, Math.min(100, consumptionPerc)) + '%';

  // Voltage
  document.getElementById('volt-val').textContent = data.battery.toFixed(1);
  const voltEl = document.getElementById('volt-val');
  voltEl.className = 'volt-value';
  if (data.battery >= 13.5) voltEl.classList.add('volt-good');
  else if (data.battery >= 11.5) voltEl.classList.add('volt-warn');
  else voltEl.classList.add('volt-bad');
  renderVoltMini(data.battery);

  // Gear
  document.getElementById('gear-disp').textContent = data.gear === 0 ? 'N' : data.gear;

  // Odometer
  const odoStr = Math.round(data.odo).toString().padStart(6, '0');
  const odoStrip = document.getElementById('odo-strip');
  odoStrip.innerHTML = '';
  for (let digit of odoStr) {
    const d = document.createElement('div');
    d.className = 'odo-digit';
    d.textContent = digit;
    odoStrip.appendChild(d);
  }

  // Top bar
  document.getElementById('top-coolant').textContent = Math.round(data.coolant);
  document.getElementById('top-odo').textContent = Math.round(data.odo);

  // Trip
  document.getElementById('tripA-val').textContent = data.tripA.toFixed(1);
  document.getElementById('tripB-val').textContent = data.tripB.toFixed(1);

  // Clock
  const now = new Date();
  document.getElementById('clock').textContent = now.toTimeString().slice(0, 8);

  // Warnings
  const warnings = data.warnings || {};
  document.getElementById('wl-oil').className = 'warn-icon' + (warnings.oil ? ' active-danger' : '');
  document.getElementById('wl-temp').className = 'warn-icon' + (warnings.temp ? ' active-danger' : '');
  document.getElementById('wl-bat').className = 'warn-icon' + (warnings.bat ? ' active-danger' : '');
  // Add more as needed

  // CAN activity
  const canDot = document.getElementById('can-dot');
  canDot.classList.add('active');
  setTimeout(() => canDot.classList.remove('active'), 150);
}

/* ─────────────────────────────────────────────────────────
   SOCKET.IO OR SIMULATION
───────────────────────────────────────────────────────── */
let socket;
let simulationInterval;

function startSimulation() {
  simulationInterval = setInterval(() => {
    const data = {
      rpm: Math.random() * 7000,
      speed: Math.random() * 240,
      fuel: Math.random() * 100,
      coolant: 80 + Math.random() * 40,
      oil_pressure: Math.random() * 5.4,
      fuel_consumption: 5 + Math.random() * 10,
      battery: 12 + Math.random() * 4,
      gear: Math.floor(Math.random() * 7),
      odo: Math.random() * 100000,
      tripA: Math.random() * 1000,
      tripB: Math.random() * 1000,
      warnings: {
        oil: Math.random() > 0.9,
        temp: Math.random() > 0.9,
        bat: Math.random() > 0.9,
      }
    };
    updateDisplay(data);
  }, 100);
}

try {
  socket = io();
  socket.on('update', (data) => {
    updateDisplay(data);
  });
  socket.on('connect', () => {
    console.log('Connected to server');
    if (simulationInterval) {
      clearInterval(simulationInterval);
      simulationInterval = null;
    }
  });
  socket.on('disconnect', () => {
    console.log('Disconnected, starting simulation');
    startSimulation();
  });
} catch (e) {
  console.log('Socket.IO not available, starting simulation');
  startSimulation();
}

// Initial render
updateDisplay({
  rpm: 3000,
  speed: 110,
  fuel: 90,
  coolant: 90,
  oil_pressure: 2.8,
  fuel_consumption: 8.5,
  battery: 14.2,
  gear: 4,
  odo: 12345,
  tripA: 12.3,
  tripB: 45.6,
  warnings: {}
});

</script>
</script>
</body>
</html>