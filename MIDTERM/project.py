import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# --- ADJUSTABLE PARAMETERS ---
SOLAR_MASSES = 1.0  # 1.0 = Our Sun, 10.0 = Large Star, 4000000.0 = Supermassive
G = 6.674e-11
M = SOLAR_MASSES * 1.989e30  # Actual mass in kg
c = 3e8                      # Speed of light
Rs = (2 * G * M) / (c**2)    # Schwarzschild Radius

# --- Simulation Settings ---
dt = (Rs / c) * 0.05
substeps = 40  
START_DIST = 12 * Rs 

# Beam of photons setup
NUM_PHOTONS = 10
Y_STARTS = np.linspace(Rs * 1.5, Rs * 4.5, NUM_PHOTONS)
COLORS = plt.cm.plasma(np.linspace(0.2, 0.8, NUM_PHOTONS))

class BlackHolePhoton:
    def __init__(self, y_start, color):
        self.pos = np.array([-START_DIST, y_start, 0.0])
        self.vel = np.array([c, 0.0, 0.0])
        self.path = []
        self.captured = False
        self.color = color

    def get_accel(self, p, v):
        r_vec = -p
        r = np.linalg.norm(r_vec)
        if r < Rs: return np.zeros(3)
        a_mag = (G * M) / (r**2)
        angular_momentum_sq = np.linalg.norm(np.cross(p, v))**2
        correction = 1 + (3 * angular_momentum_sq) / (r**2 * c**2)
        return (a_mag * correction) * (r_vec / r)

    def update(self):
        if self.captured: return
        p, v = self.pos, self.vel
        k1_v = self.get_accel(p, v) * dt
        k1_p = v * dt
        k2_v = self.get_accel(p + k1_p/2, v + k1_v/2) * dt
        k2_p = (v + k1_v/2) * dt
        k3_v = self.get_accel(p + k2_p/2, v + k2_v/2) * dt
        k3_p = (v + k2_v/2) * dt
        k4_v = self.get_accel(p + k3_p, v + k3_v) * dt
        k4_p = (v + k3_v) * dt
        
        self.vel += (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
        self.pos += (k1_p + 2*k2_p + 2*k3_p + k4_p) / 6
        self.path.append(self.pos.copy())
        # Stop moving if inside the event horizon
        if np.linalg.norm(self.pos) < Rs: self.captured = True

# --- Visualization Setup ---
photons = [BlackHolePhoton(y, color) for y, color in zip(Y_STARTS, COLORS)]
fig, ax = plt.subplots(figsize=(9, 9), facecolor='#050505')
ax.set_facecolor('#050505')

# Axis and Grid Styling
ax.grid(True, color='white', linestyle=':', alpha=0.3)
for spine in ax.spines.values():
    spine.set_edgecolor('white')
    spine.set_alpha(0.5)
ax.tick_params(axis='both', colors='white', labelsize=8)

# Visual Layers
horizon_circ = plt.Circle((0, 0), Rs, color='white', fill=False, ls='--', lw=1, alpha=0.6)
core_circ = plt.Circle((0, 0), Rs * 0.95, color='black', zorder=10)
ax.add_patch(horizon_circ)
ax.add_patch(core_circ)

# Photon paths (low zorder)
lines = [ax.plot([], [], color=p.color, lw=1.5, alpha=0.7, zorder=5)[0] for p in photons]
points = [ax.plot([], [], 'o', markersize=3, color=p.color, zorder=6)[0] for p in photons]
status_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, color='white', family='monospace', zorder=20)

# --- Progress Bar Elements ---
# Added zorder=20 to ensure text and bar appear over the photon lines
bar_label = ax.text(0.5, 0.08, 'PROGRESS TO SINGULARITY', transform=ax.transAxes, 
                    color='white', alpha=0.8, ha='center', fontsize=9, family='monospace', zorder=20)

progress_bg = patches.Rectangle((0.1, 0.05), 0.8, 0.02, transform=ax.transAxes, 
                                color='grey', alpha=0.3, zorder=19)
progress_fill = patches.Rectangle((0.1, 0.05), 2.8, 0.02, transform=ax.transAxes, 
                                 color='#00FFCC', alpha=1.0, zorder=20)
ax.add_patch(progress_bg)
ax.add_patch(progress_fill)

tracking = {"min_dist_ever": START_DIST}

def animate(i):
    for p in photons:
        for _ in range(substeps):
            p.update()
    
    current_dists = [np.linalg.norm(p.pos) for p in photons]
    min_dist_now = min(current_dists)
    
    if min_dist_now < tracking["min_dist_ever"]:
        tracking["min_dist_ever"] = min_dist_now

    # Camera zoom
    view_size = max(Rs * 4.5, tracking["min_dist_ever"] * 1.5) 
    ax.set_xlim(-view_size, view_size)
    ax.set_ylim(-view_size, view_size)
    
    for p, line, pt in zip(photons, lines, points):
        if p.path:
            pts = np.array(p.path)
            line.set_data(pts[:, 0], pts[:, 1])
            if p.captured:
                pt.set_visible(False)
            else:
                pt.set_data([pts[-1, 0]], [pts[-1, 1]])

    # Progress Calculation
    progress = np.clip((START_DIST - min_dist_now) / (START_DIST - Rs), 0, 1)
    progress_fill.set_width(progress * 0.8)
    
    if progress > 0.95:
        bar_label.set_color('#FF4444')
        bar_label.set_alpha(1.0)
    
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_alpha(0.5)
        
    status_text.set_text(
        f"BH MASS: {SOLAR_MASSES} Suns\n"
        f"PHOTONS: {NUM_PHOTONS}\n"
        f"MIN DIST:{tracking['min_dist_ever']/Rs:.2f} Rs\n"
        f"ZOOM:    {START_DIST/view_size:.1f}x"
    )
        
    return lines + points + [status_text, progress_fill, bar_label]

ani = FuncAnimation(fig, animate, frames=700, interval=25, blit=False)
plt.show()