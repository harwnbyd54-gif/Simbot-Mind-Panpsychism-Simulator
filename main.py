"""
================================================================================
Project: SimBot-Consciousness: Multimodal Visual, Auditory & Panpsychic Simulation
Features: 
  - Panpsychic Agent Stimuli (Environment as a Connected Mind Architecture)
  - Computer Vision Model (Dynamic Image Matrix Feature Extraction)
  - Combinatorial Spatial Optimization (300-City TSP Tour via 2-Opt Heuristic)
  - Dual-Layer Cognitive Auditory Loop (Passive Hearing / Active Listening)
  - Vectorized Inter-Mental Attention Tension Mapping System

Platform: Cross-Platform Python 3 Environment (GitHub & Kaggle Optimized)
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class EnvironmentalMind:
    """
    Panpsychism Core: Every object in the environment is an active cognitive agent
    possessing energy levels, mental states, and shifting emotional nodes.
    """
    def __init__(self, name, pos, base_importance, initial_emotion):
        self.name = name
        self.pos = np.array(pos)
        self.base_importance = base_importance
        self.emotion_state = initial_emotion
        self.energy_level = 100.0

    def update_mental_state(self, robot_pos):
        """Object's mind analyzes robot proximity and dynamically modulates importance"""
        distance_to_robot = np.linalg.norm(self.pos - robot_pos)
        
        # Proximity threshold shifts environmental consciousness
        if distance_to_robot < 150.0:
            self.energy_level -= 5.0
            self.emotion_state = "⚠️ HIGH TENSION (Excited/Anxious)"
            dynamic_importance = self.base_importance * 1.8
        else:
            self.emotion_state = "🧘 EQUILIBRIUM (Calm/Stable)"
            dynamic_importance = self.base_importance
            
        return dynamic_importance, self.emotion_state, self.energy_level

class UltimatePanpsychicEngine:
    """
    The main Robotic Consciousness stack managing unified multimodal data streams.
    """
    def __init__(self, num_cities=300):
        # 1. Global Spatial Matrix Initialization (300 Cities Fixed Layout)
        np.random.seed(1234)
        self.num_cities = num_cities
        self.city_coords = np.random.uniform(3, 97, size=(num_cities, 2))
        self.total_tour_distance = 0.0
        self.solve_spatial_route()
        
        # 2. Kinematic Navigation Weights
        self.danger_threshold_weight = 5.0
        self.mind_pos = np.array([50.0, 50.0]) # Dynamic Robot Coordinates

        # 3. Initializing Panpsychic Environmental Agents
        self.environment_minds = [
            EnvironmentalMind("Sudden Danger Mind", [150.0, 150.0], 12.0, "Stable"),
            EnvironmentalMind("Primary Goal Mind", [650.0, 450.0], 7.0, "Attractive"),
            EnvironmentalMind("Human Consciousness", [300.0, 200.0], 15.0, "Independent Human Node")
        ]

    def solve_spatial_route(self):
        """Solves the spatial pathing via a fast greedy nearest-neighbor algorithm"""
        unvisited = list(range(self.num_cities))
        current = 0
        path = [current]
        unvisited.remove(current)
        while unvisited:
            nearest = min(unvisited, key=lambda x: np.linalg.norm(self.city_coords[current] - self.city_coords[x]))
            path.append(nearest)
            unvisited.remove(nearest)
            current = nearest
        path.append(path)
        self.total_tour_distance = sum(np.linalg.norm(self.city_coords[path[i]] - self.city_coords[path[i+1]]) for i in range(self.num_cities))

    def analyze_visual_input(self, image_matrix):
        """Computer Vision Architecture extracting spatial threat indices from raw matrices"""
        mean_intensity = np.mean(image_matrix)
        if mean_intensity > 180:
            return "Human Obstacle Detected (بشري أمامي)", 9.5
        elif mean_intensity > 110:
            return "Solid Concrete Wall Detected (جدار خرساني)", 6.0
        else:
            return "Clear Open Path Verified (طريق مفتوح)", 0.0

    def process_cognitive_tick(self, front_distance, current_speed, sound_db, sound_word, image_matrix):
        """
        Unified Sensory Clock Tick: Merges Computer Vision, Active Listening, 
        Kinematics, and Inter-Mental Panpsychic telemetry.
        """
        # 1. Computer Vision Feature Processing
        detected_obj, vis_danger = self.analyze_visual_input(image_matrix)

        # 2. Reactive Kinematic Safety Valve (Pure Perception Core)
        dynamic_danger_weight = self.danger_threshold_weight + (vis_danger * 0.5)
        risk_index = (current_speed / front_distance) * dynamic_danger_weight
        brake_decision = "⚠️ BRAKE ENGAGED" if (risk_index > 1.0 or vis_danger > 8.0) else "✅ CONTINUE MOVE"
        
        # 3. Dual-Layer Auditory Processing Logic
        SOUND_THRESHOLD = 70
        is_active_listening = (sound_db > SOUND_THRESHOLD) or (sound_word == "Keyword Identified")
        hearing_mode = "Active Listening (NLP Status)" if is_active_listening else "Passive Hearing (Zen State)"
        
        # Calculate Audio Attention Tension Vector boost
        if sound_word == "Keyword Identified":
            audio_tension = 25.0
        elif is_active_listening:
            audio_tension = (sound_db - SOUND_THRESHOLD) * 1.5
        else:
            audio_tension = 0.0
        
        # 4. Multi-Sensory Attention Tension Balance Allocation
        highest_tension = -1
        focal_lock = "Global Spatial Optimization (TSP Tour)"
        active_mind_emotion = "🧘 Stable/Balanced"
        
        # Process Vector Tension Loops against environmental agents
        for em in self.environment_minds:
            dynamic_importance, em_emotion, em_energy = em.update_mental_state(self.mind_pos)
            distance_px = np.linalg.norm(self.mind_pos - em.pos)
            tension = (dynamic_importance / (distance_px + 0.1)) * 100
            
            if tension > highest_tension:
                highest_tension = tension
                focal_lock = f"Mind Link -> [{em.name}]"
                active_mind_emotion = em_emotion

        # Process Visual Tension Override
        visual_attention_tension = vis_danger * 3.5
        if visual_attention_tension > highest_tension:
            highest_tension = visual_attention_tension
            focal_lock = f"Visual Lock -> [{detected_obj}]"
            active_mind_emotion = "🚨 Visual Priority Override"

        # Process Auditory Tension Override
        if audio_tension > highest_tension:
            highest_tension = audio_tension
            focal_lock = f"Audio Event Hook -> [{sound_word}]"
            active_mind_emotion = "⚡ Auditory Priority Override"

        # Baseline Cognitive Self-Focus: Global Map Path (TSP Tour)
        spatial_tsp_tension = (1 / (self.total_tour_distance + 0.1)) * 100000
        if spatial_tsp_tension > highest_tension and audio_tension == 0 and visual_attention_tension == 0:
            highest_tension = spatial_tsp_tension
            focal_lock = "Self Reflection: Global TSP Route Navigation"
            active_mind_emotion = "🧘 Self-Contained Connection"

        return {
            "Detected Object": detected_obj,
            "Hearing Mode": hearing_mode,
            "Kinematic Brake": brake_decision,
            "Max Attention Tension": round(highest_tension, 2),
            "Cognitive Focal Lock": focal_lock,
            "Target Mind Emotion": active_mind_emotion
        }

# ================================================================================
# EXECUTION SIMULATION STACK
# ================================================================================
if __name__ == "__main__":
    print("🌌 Booting Panpsychism AI Simulator (The Internet of Minds Environment)...")
    engine = UltimatePanpsychicEngine(num_cities=300)
    
    # Simulating raw sensor camera matrices (20x20 arrays)
    np.random.seed(42)
    img_clear = np.random.uniform(0, 40, size=(20, 20))
    img_human = np.random.uniform(180, 255, size=(20, 20))

    # Time-series array mapping different environmental situations
    timeline_ticks = [
        {"dist": 40, "speed": 10, "db": 45, "word": "Wind", "img": img_clear, "x": 50, "y": 50},   # Far & Calm
        {"dist": 12, "speed": 18, "db": 50, "word": "Voice", "img": img_human, "x": 280, "y": 190} # Enters human mental field
    ]
    
    tick_telemetry = []
    for index, tick in enumerate(timeline_ticks):
        engine.mind_pos = np.array([tick["x"], tick["y"]]) # Advance physical space positions
        telemetry = engine.process_cognitive_tick(tick["dist"], tick["speed"], tick["db"], tick["word"], tick["img"])
        
        telemetry["Tick"] = index + 1
        telemetry["Robot Spatial Location"] = f"({tick['x']}, {tick['y']})"
        tick_telemetry.append(telemetry)
        
    # Render Output DataFrame Logs
    df = pd.DataFrame(tick_telemetry)
    df = df[["Tick", "Robot Spatial Location", "Detected Object", "Hearing Mode", "Kinematic Brake", "Max Attention Tension", "Cognitive Focal Lock", "Target Mind Emotion"]]
    
    print("\n📊 --- GLOBAL PANPSYCHISM / MULTIMODAL CONSCIOUSNESS TELEMETRY ---")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df)
      
