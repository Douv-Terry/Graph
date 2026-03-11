import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import sys

class GTA5FinalGPS:
    def __init__(self, root):
        self.root = root
        self.root.title("GTA V - GPS Navigation System v3.1")
        self.root.geometry("1300x850")
        self.root.configure(bg="#1a1a1a")
        
        # --- GESTION DE LA FERMETURE ---
        # Cette ligne force l'arrêt complet du script quand on clique sur la croix
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.G = nx.Graph()
        self.locations = {}
        self.setup_map_data()
        self.create_widgets()
        self.render_map()

    def on_closing(self):
        """Fonction appelée à la fermeture de la fenêtre"""
        plt.close('all') # Ferme les figures Matplotlib en mémoire
        self.root.destroy() # Détruit la fenêtre Tkinter
        sys.exit() # Arrête le processus Python proprement

    def setup_map_data(self):
        self.locations = {
            'Los Santos International Airport': (15, 8), 'Terminal': (18, 5),
            'Del Perro': (20, 15), 'Vespucci': (22, 12), 'Downtown': (30, 18),
            'Pillbox Hill': (32, 20), 'Vinewood': (30, 30), 'Rockford Hills': (24, 28),
            'Fort Zancudo': (16, 55), 'Sandy Shores': (58, 62), 'Paleto Bay': (20, 85),
            'Grapeseed': (58, 75), 'Mount Chiliad': (28, 70), 'Alamo Sea': (42, 60),
            'Grand Senora Desert': (55, 55), 'Pacific Bluffs': (12, 22),
            'Legion Square': (28, 22), 'Little Seoul': (26, 24), 'Vinewood Hills': (32, 35),
            'West Vinewood': (28, 32), 'La Mesa': (38, 22), 'Cypress Flats': (40, 18),
            'El Burro Heights': (42, 26), 'Murrieta Heights': (40, 30), 'Elysian Island': (35, 10),
            'Port': (38, 12), 'Terminal Island': (32, 8), 'Banham Canyon': (18, 38),
            'Tongva Hills': (20, 45), 'Mount Josiah': (28, 58), 'Route 68 Junction': (45, 52),
            'Harmony': (52, 50), 'Chiliad Wilderness': (25, 75), 'Paleto Forest': (28, 82),
            'Stab City': (48, 58), 'Tongva Valley': (22, 50), 'Richman Glen': (16, 32),
            'San Chianski': (72, 58), 'Tataviam Mountains': (65, 45), 'Palomino Highlands': (70, 50),
            'Great Ocean Highway North': (22, 65), 'Great Ocean Highway South': (15, 28),
            'Senora Freeway North': (62, 70), 'Senora Freeway South': (52, 40), 'Mount Gordo': (68, 82)
        }
        for loc, coords in self.locations.items():
            self.G.add_node(loc, pos=coords)

        roads = [
            ('Los Santos International Airport', 'Terminal', 2.0), ('Los Santos International Airport', 'Vespucci', 2.0),
            ('Terminal', 'Terminal Island', 1.5), ('Terminal Island', 'Elysian Island', 1.0),
            ('Elysian Island', 'Port', 1.0), ('Port', 'Cypress Flats', 2.0), ('Cypress Flats', 'La Mesa', 1.5),
            ('Vespucci', 'Del Perro', 1.0), ('Del Perro', 'Little Seoul', 1.5), ('Little Seoul', 'Pillbox Hill', 1.5),
            ('Pillbox Hill', 'Downtown', 0.5), ('Downtown', 'Legion Square', 0.5), ('Legion Square', 'La Mesa', 2.0),
            ('La Mesa', 'Murrieta Heights', 1.5), ('Murrieta Heights', 'El Burro Heights', 2.0),
            ('Pillbox Hill', 'Vinewood', 1.5), ('Vinewood', 'West Vinewood', 1.0), ('West Vinewood', 'Rockford Hills', 1.0),
            ('Vinewood', 'Vinewood Hills', 2.0), ('Rockford Hills', 'Richman Glen', 1.5),
            ('Richman Glen', 'Great Ocean Highway South', 1.5), ('Del Perro', 'Pacific Bluffs', 1.5),
            ('Pacific Bluffs', 'Great Ocean Highway South', 2.0), ('Great Ocean Highway South', 'Banham Canyon', 2.5),
            ('Banham Canyon', 'Tongva Hills', 2.0), ('Tongva Hills', 'Tongva Valley', 1.5),
            ('Tongva Valley', 'Fort Zancudo', 2.0), ('Fort Zancudo', 'Great Ocean Highway North', 2.0),
            ('Great Ocean Highway North', 'Chiliad Wilderness', 3.0), ('Chiliad Wilderness', 'Paleto Bay', 2.5),
            ('Vinewood Hills', 'Route 68 Junction', 4.0), ('Route 68 Junction', 'Mount Josiah', 1.5),
            ('Mount Josiah', 'Fort Zancudo', 2.5), ('Route 68 Junction', 'Alamo Sea', 2.0),
            ('Alamo Sea', 'Stab City', 1.0), ('Stab City', 'Sandy Shores', 1.5), ('Sandy Shores', 'Grand Senora Desert', 1.5),
            ('Grand Senora Desert', 'Harmony', 1.0), ('Harmony', 'Senora Freeway South', 2.0),
            ('Senora Freeway South', 'Murrieta Heights', 4.0), ('Senora Freeway South', 'Palomino Highlands', 2.0),
            ('Palomino Highlands', 'Tataviam Mountains', 2.0), ('Tataviam Mountains', 'San Chianski', 3.0),
            ('San Chianski', 'Grand Senora Desert', 2.5), ('Sandy Shores', 'Senora Freeway North', 2.0),
            ('Senora Freeway North', 'Grapeseed', 2.0), ('Grapeseed', 'Mount Gordo', 2.0),
            ('Mount Gordo', 'Paleto Forest', 3.0), ('Paleto Forest', 'Paleto Bay', 2.0),
            ('Paleto Forest', 'Mount Chiliad', 2.5), ('Mount Chiliad', 'Chiliad Wilderness', 2.0)
        ]
        self.G.add_weighted_edges_from(roads)

    def create_widgets(self):
        panel = tk.Frame(self.root, width=350, bg="#111", padx=20, pady=20)
        panel.pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(panel, text="🗺️ GPS SAN ANDREAS", font=("Impact", 22), bg="#111", fg="#00ff00").pack(pady=10)
        
        self.start_cb = ttk.Combobox(panel, values=sorted(list(self.locations.keys())), width=35, state="readonly")
        self.start_cb.pack(pady=10)
        self.end_cb = ttk.Combobox(panel, values=sorted(list(self.locations.keys())), width=35, state="readonly")
        self.end_cb.pack(pady=10)
        
        tk.Button(panel, text="LANCER L'ITINÉRAIRE", command=self.calculate_gps, bg="#00ff00", font=("Arial", 10, "bold")).pack(pady=20, fill=tk.X)
        tk.Button(panel, text="QUITTER", command=self.on_closing, bg="#c0392b", fg="white").pack(fill=tk.X)
        
        self.res_lbl = tk.Label(panel, text="", bg="#111", fg="#00ff00", font=("Courier", 10), justify=tk.LEFT)
        self.res_lbl.pack(pady=30)
        
        self.map_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def render_map(self, path=None):
        for w in self.map_frame.winfo_children(): w.destroy()
        fig, ax = plt.subplots(figsize=(10, 10), facecolor='#1a1a1a')
        ax.set_facecolor('#1a1a1a')
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw_networkx_edges(self.G, pos, edge_color="#333", width=1.5, ax=ax)
        
        if path:
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color="#00ff00", width=5, ax=ax)
            nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color="#00ff00", node_size=100, ax=ax)
            
        labels = {n: n for n in self.locations.keys()}
        nx.draw_networkx_labels(self.G, pos, labels, font_size=6, font_color="white", 
                                bbox=dict(boxstyle='round,pad=0.1', facecolor='black', alpha=0.4), ax=ax)
        nx.draw_networkx_nodes(self.G, pos, node_size=20, node_color="#555", ax=ax)
        
        ax.set_xlim(5, 75); ax.set_ylim(0, 95)
        plt.axis('off')
        
        canvas = FigureCanvasTkAgg(fig, master=self.map_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def calculate_gps(self):
        s, e = self.start_cb.get(), self.end_cb.get()
        if not s or not e: return
        try:
            path = nx.shortest_path(self.G, s, e, weight='weight')
            dist = nx.shortest_path_length(self.G, s, e, weight='weight')
            self.res_lbl.config(text=f"✅ ROUTE TROUVÉE\n📏 Dist: {dist:.1f} km\n🚩 {len(path)} étapes")
            self.render_map(path)
        except:
            messagebox.showerror("Erreur", "Itinéraire impossible.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GTA5FinalGPS(root)
    root.mainloop()