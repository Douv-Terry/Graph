import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GTA5Map:
    def __init__(self):
        self.G = nx.Graph()
        self.locations = {}
        self.create_map()
    
    def create_map(self):
        """Crée la carte de GTA 5 avec toutes les coordonnées"""
        
        # ========== LOS SANTOS (SUD) ==========
        self.locations['Los Santos International Airport'] = (15, 8)
        self.locations['Terminal'] = (18, 5)
        self.locations['Del Perro'] = (20, 15)
        self.locations['Vespucci'] = (22, 12)
        self.locations['Pacific Bluffs'] = (12, 22)
        self.locations['Downtown'] = (30, 18)
        self.locations['Pillbox Hill'] = (32, 20)
        self.locations['Legion Square'] = (28, 22)
        self.locations['Little Seoul'] = (26, 24)
        self.locations['Rockford Hills'] = (24, 28)
        self.locations['Vinewood'] = (30, 30)
        self.locations['Vinewood Hills'] = (32, 35)
        self.locations['West Vinewood'] = (28, 32)
        self.locations['La Mesa'] = (38, 22)
        self.locations['Cypress Flats'] = (40, 18)
        self.locations['El Burro Heights'] = (42, 26)
        self.locations['Murrieta Heights'] = (40, 30)
        self.locations['Elysian Island'] = (35, 10)
        self.locations['Port'] = (38, 12)
        self.locations['Terminal Island'] = (32, 8)
        
        # ========== BLAINE COUNTY ==========
        self.locations['Banham Canyon'] = (18, 38)
        self.locations['Tongva Hills'] = (20, 45)
        self.locations['Tongva Valley'] = (22, 50)
        self.locations['Richman Glen'] = (16, 32)
        self.locations['Great Chaparral'] = (25, 55)
        self.locations['Lago Zancudo'] = (18, 58)
        self.locations['Fort Zancudo'] = (16, 55)
        self.locations['Mount Josiah'] = (28, 58)
        self.locations['Mount Chiliad'] = (28, 70)
        self.locations['Chiliad Wilderness'] = (25, 75)
        self.locations['Paleto Bay'] = (20, 85)
        self.locations['Paleto Forest'] = (28, 82)
        self.locations['Alamo Sea'] = (42, 60)
        self.locations['Stab City'] = (48, 58)
        self.locations['Grand Senora Desert'] = (55, 55)
        self.locations['Sandy Shores'] = (58, 62)
        self.locations['Harmony'] = (52, 50)
        self.locations['Grand Senora Oilfields'] = (60, 68)
        self.locations['Grapeseed'] = (58, 75)
        self.locations['Mount Gordo'] = (68, 82)
        self.locations['San Chianski'] = (72, 58)
        self.locations['Tataviam Mountains'] = (65, 45)
        self.locations['Palomino Highlands'] = (70, 50)
        
        # Points routiers
        self.locations['Route 68 Junction'] = (45, 52)
        self.locations['Senora Freeway North'] = (62, 70)
        self.locations['Senora Freeway South'] = (52, 40)
        self.locations['Great Ocean Highway North'] = (22, 65)
        self.locations['Great Ocean Highway South'] = (15, 28)
        
        for location, coords in self.locations.items():
            self.G.add_node(location, pos=coords)
        
        # Définition des routes
        roads = [
            ('Los Santos International Airport', 'Vespucci', 2.0),
            ('Vespucci', 'Del Perro', 1.5),
            ('Del Perro', 'Downtown', 2.5),
            ('Downtown', 'Pillbox Hill', 1.0),
            ('Pillbox Hill', 'La Mesa', 2.0),
            ('La Mesa', 'Cypress Flats', 1.5),
            ('Cypress Flats', 'Port', 2.0),
            ('Port', 'Elysian Island', 1.5),
            ('Elysian Island', 'Terminal Island', 1.5),
            ('Terminal Island', 'Terminal', 1.5),
            ('Terminal', 'Los Santos International Airport', 2.0),
            ('Downtown', 'Legion Square', 1.0),
            ('Legion Square', 'Little Seoul', 1.0),
            ('Little Seoul', 'Rockford Hills', 1.5),
            ('Rockford Hills', 'West Vinewood', 1.5),
            ('West Vinewood', 'Vinewood', 1.0),
            ('Vinewood', 'Vinewood Hills', 1.5),
            ('Pillbox Hill', 'Vinewood', 2.0),
            ('La Mesa', 'El Burro Heights', 2.0),
            ('El Burro Heights', 'Murrieta Heights', 1.5),
            ('Del Perro', 'Great Ocean Highway South', 2.0),
            ('Great Ocean Highway South', 'Pacific Bluffs', 1.5),
            ('Pacific Bluffs', 'Richman Glen', 2.0),
            ('Richman Glen', 'Banham Canyon', 2.0),
            ('Banham Canyon', 'Tongva Hills', 2.0),
            ('Tongva Hills', 'Tongva Valley', 2.0),
            ('Tongva Valley', 'Great Ocean Highway North', 1.5),
            ('Great Ocean Highway North', 'Lago Zancudo', 2.5),
            ('Lago Zancudo', 'Fort Zancudo', 1.0),
            ('Lago Zancudo', 'Mount Chiliad', 3.5),
            ('Mount Chiliad', 'Chiliad Wilderness', 2.0),
            ('Chiliad Wilderness', 'Paleto Bay', 2.5),
            ('Vinewood Hills', 'Banham Canyon', 2.5),
            ('Vinewood Hills', 'Great Chaparral', 4.0),
            ('Great Chaparral', 'Mount Josiah', 1.5),
            ('Mount Josiah', 'Route 68 Junction', 2.5),
            ('Route 68 Junction', 'Harmony', 2.0),
            ('Harmony', 'Grand Senora Desert', 2.0),
            ('Grand Senora Desert', 'Sandy Shores', 2.5),
            ('Murrieta Heights', 'Senora Freeway South', 2.5),
            ('Senora Freeway South', 'Tataviam Mountains', 2.0),
            ('Tataviam Mountains', 'Palomino Highlands', 2.0),
            ('Palomino Highlands', 'San Chianski', 2.5),
            ('San Chianski', 'Grand Senora Desert', 2.5),
            ('Grand Senora Desert', 'Harmony', 2.0),
            ('Sandy Shores', 'Grand Senora Oilfields', 2.0),
            ('Grand Senora Oilfields', 'Senora Freeway North', 1.5),
            ('Senora Freeway North', 'Grapeseed', 2.0),
            ('Grapeseed', 'Mount Gordo', 2.5),
            ('Mount Gordo', 'Paleto Forest', 4.0),
            ('Paleto Forest', 'Paleto Bay', 2.0),
            ('Route 68 Junction', 'Alamo Sea', 2.0),
            ('Alamo Sea', 'Stab City', 1.5),
            ('Stab City', 'Sandy Shores', 2.0),
            ('Alamo Sea', 'Grand Senora Desert', 2.5),
            ('Great Chaparral', 'Alamo Sea', 3.0),
            ('Mount Chiliad', 'Mount Josiah', 3.0),
            ('Mount Chiliad', 'Route 68 Junction', 4.5),
            ('Paleto Forest', 'Grapeseed', 3.5),
            ('Grapeseed', 'Alamo Sea', 3.0),
        ]
        
        for road in roads:
            self.G.add_edge(road[0], road[1], weight=road[2])

    def show_all_locations(self):
        """Affiche les lieux par catégories dans le terminal"""
        print("\n" + "="*80)
        print("📍 LIEUX DISPONIBLES")
        print("="*80)
        
        categories = {
            '🏙️  LOS SANTOS': ['Downtown', 'Airport', 'Terminal', 'Vespucci', 'Vinewood', 'Rockford Hills', 'Pillbox', 'Legion', 'Little Seoul', 'Mesa', 'Cypress', 'Burro', 'Murrieta', 'Island', 'Port'],
            '🏜️  DESERT / NORD': ['Sandy Shores', 'Grapeseed', 'Paleto', 'Alamo Sea', 'Stab City', 'Chaparral', 'Harmony', 'Senora', 'Chiliad', 'Zancudo', 'Gordo'],
            '🛣️  ROUTES / CANYONS': ['Highway', 'Freeway', 'Junction', 'Canyon', 'Hills', 'Valley', 'Mountains', 'Highlands']
        }
        
        for cat, keywords in categories.items():
            print(f"\n{cat}:")
            current_locs = []
            for loc in sorted(self.locations.keys()):
                if any(k.lower() in loc.lower() for k in keywords):
                    current_locs.append(loc)
            
            for loc in current_locs:
                print(f"  • {loc}")
        print("\n" + "="*80 + "\n")

    def draw_map(self, path=None, start=None, end=None):
        """Dessine la carte avec tous les labels affichés"""
        fig, ax = plt.subplots(figsize=(18, 20))
        ax.set_facecolor('#E8F4F8')
        pos = nx.get_node_attributes(self.G, 'pos')

        # Routes de base
        for edge in self.G.edges():
            x = [pos[edge[0]][0], pos[edge[1]][0]]
            y = [pos[edge[0]][1], pos[edge[1]][1]]
            ax.plot(x, y, color='#AAAAAA', linewidth=2, alpha=0.4, zorder=1)

        # Tracé du chemin GPS
        if path:
            for i in range(len(path) - 1):
                x = [pos[path[i]][0], pos[path[i+1]][0]]
                y = [pos[path[i+1]][1], pos[path[i+1]][1]] # Correction de typo ici
                # Correction réelle pour le tracé
                x_coords = [pos[path[i]][0], pos[path[i+1]][0]]
                y_coords = [pos[path[i]][1], pos[path[i+1]][1]]
                ax.plot(x_coords, y_coords, color='#00FF00', linewidth=6, zorder=5)

        # Noeuds
        nx.draw_networkx_nodes(self.G, pos, node_size=80, node_color='#333333', alpha=0.7, ax=ax)

        # AFFICHAGE DE TOUS LES LABELS
        labels = {node: node for node in self.locations.keys()}
        nx.draw_networkx_labels(self.G, pos, labels, font_size=7, font_weight='bold', 
                                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7), ax=ax)

        ax.set_title('CARTE GPS GTA 5 - TOUS LES POINTS RÉPERTORIÉS', fontsize=18)
        ax.set_xlim(8, 78)
        ax.set_ylim(0, 92)
        ax.set_aspect('equal')
        return fig

    def gps_navigation(self, start, end):
        if start not in self.locations or end not in self.locations:
            print("\n❌ L'un des lieux n'existe pas. Tapez 'liste' pour vérifier.")
            return
        
        try:
            path = nx.shortest_path(self.G, start, end, weight='weight')
            dist = nx.shortest_path_length(self.G, start, end, weight='weight')
            
            print("\n" + "🛣️  ITINÉRAIRE TROUVÉ")
            print(f"📏 Distance totale : {dist:.1f} km")
            for i, step in enumerate(path, 1):
                print(f"  {i}. {step}")
            
            self.draw_map(path=path, start=start, end=end)
            plt.show()
        except nx.NetworkXNoPath:
            print("\n❌ Aucun chemin possible.")

def main():
    gta = GTA5Map()
    print("\n" + "="*50)
    print("🎮 GPS INTERACTIF SAN ANDREAS")
    print("="*50)
    
    while True:
        print("\n--- MENU ---")
        print("Entrez le DÉPART (ou 'liste' pour voir les lieux, 'carte' pour voir tout, 'q' pour quitter)")
        choix = input("📍 DÉPART : ").strip()
        
        if choix.lower() in ['q', 'quit', 'exit']: break
        if choix.lower() in ['liste', 'l']:
            gta.show_all_locations()
            continue
        if choix.lower() in ['carte', 'c']:
            gta.draw_map()
            plt.show()
            continue
            
        arrivee = input("🎯 ARRIVÉE : ").strip()
        gta.gps_navigation(choix, arrivee)

if __name__ == "__main__":
    main()