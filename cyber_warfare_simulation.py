import random
import time
import json
import threading

class CyberEntity:
    def __init__(self, name, firewall_strength, vulnerabilities):
        self.name = name
        self.firewall_strength = firewall_strength
        self.vulnerabilities = vulnerabilities
        self.attacks_received = 0

    def defend(self, attack_strength):
        # Determine if the attack is successful
        if attack_strength > self.firewall_strength:
            self.attacks_received += 1
            return False
        return True

    def __str__(self):
        return f"Entity: {self.name}, Firewall strength: {self.firewall_strength}, Vulnerabilities: {self.vulnerabilities}, Attacks Received: {self.attacks_received}"


class AttackSimulation:
    def __init__(self, attacker_name, attack_strength, targets):
        self.attacker_name = attacker_name
        self.attack_strength = attack_strength
        self.targets = targets

    def launch_attack(self):
        for target in self.targets:
            print(f"{self.attacker_name} is launching an attack on {target.name}")
            successful_defense = target.defend(self.attack_strength)
            if not successful_defense:
                print(f"Attack on {target.name} was successful!")
            else:
                print(f"{target.name} successfully defended against the attack.")
            time.sleep(random.uniform(0.5, 1.5))


class DefenseSimulation:
    def __init__(self, defender_name, defensive_actions):
        self.defender_name = defender_name
        self.defensive_actions = defensive_actions

    def implement_defense(self):
        print(f"{self.defender_name} is implementing defense strategies.")
        for action in self.defensive_actions:
            print(f"{self.defender_name} is executing: {action}")
            time.sleep(random.uniform(0.5, 1.5))


class SimulationManager:
    def __init__(self):
        self.entities = []
        self.attack_threads = []
        self.defense_threads = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def start_attack(self, attacker_name, attack_strength, target_names):
        targets = [entity for entity in self.entities if entity.name in target_names]
        attack_sim = AttackSimulation(attacker_name, attack_strength, targets)
        attack_thread = threading.Thread(target=attack_sim.launch_attack)
        attack_thread.start()
        self.attack_threads.append(attack_thread)

    def start_defense(self, defender_name, defensive_actions):
        defense_sim = DefenseSimulation(defender_name, defensive_actions)
        defense_thread = threading.Thread(target=defense_sim.implement_defense)
        defense_thread.start()
        self.defense_threads.append(defense_thread)

    def wait_for_completion(self):
        for thread in self.attack_threads:
            thread.join()
        for thread in self.defense_threads:
            thread.join()

    def report(self):
        print("\nSimulation Report:")
        for entity in self.entities:
            print(entity)


if __name__ == "__main__":
    simulation = SimulationManager()
    
    # Add entities
    entity1 = CyberEntity("Server A", 80, {"SQL Injection", "XSS"})
    entity2 = CyberEntity("Server B", 60, {"Buffer Overflow"})
    entity3 = CyberEntity("Server C", 50, {"Phishing"})
    
    simulation.add_entity(entity1)
    simulation.add_entity(entity2)
    simulation.add_entity(entity3)

    # Start attacks
    simulation.start_attack("Attacker 1", 75, ["Server A", "Server B"])
    simulation.start_attack("Attacker 2", 90, ["Server C"])

    # Start defenses
    simulation.start_defense("Defender 1", ["Update firewall", "Patch vulnerabilities"])
    simulation.start_defense("Defender 2", ["Conduct security awareness training", "Monitor network traffic"])

    # Wait for attacks and defenses to complete
    simulation.wait_for_completion()

    # Report results
    simulation.report()

    # Save the simulation state to a JSON file
    with open('simulation_report.json', 'w') as report_file:
        json.dump([vars(entity) for entity in simulation.entities], report_file, indent=4)

    print("Simulation state saved to 'simulation_report.json'.")