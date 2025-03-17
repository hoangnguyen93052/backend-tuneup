import time
import random
import math


class Drone:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)  # x, y, z coordinates
        self.battery_level = 100  # Battery percentage
        self.is_flying = False

    def take_off(self):
        if self.battery_level > 5:
            self.is_flying = True
            print(f"{self.name} is taking off.")
        else:
            print(f"{self.name} cannot take off. Battery is too low.")

    def land(self):
        if self.is_flying:
            self.is_flying = False
            print(f"{self.name} has landed.")
        else:
            print(f"{self.name} is not flying.")

    def fly_to(self, x, y, z):
        if self.is_flying:
            if self.battery_level > 0:
                current_pos = self.position
                self.position = (x, y, z)
                self.battery_level -= self.calculate_battery_usage(current_pos, self.position)
                print(f"{self.name} flew to position: {self.position}. Battery level: {self.battery_level}%")
            else:
                print(f"{self.name} has no battery left to fly.")
                self.land()
        else:
            print(f"{self.name} is not flying. Cannot change position.")

    def calculate_battery_usage(self, start_pos, end_pos):
        distance = math.sqrt((end_pos[0] - start_pos[0]) ** 2 +
                             (end_pos[1] - start_pos[1]) ** 2 +
                             (end_pos[2] - start_pos[2]) ** 2)
        battery_usage = distance * 0.1  # 10% battery usage per unit distance
        return battery_usage

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is fully recharged.")

    def get_status(self):
        return {
            "name": self.name,
            "position": self.position,
            "battery_level": self.battery_level,
            "is_flying": self.is_flying
        }


class Obstacles:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, position):
        self.obstacles.append(position)
        print(f"Obstacle added at position: {position}")

    def detect_obstacles(self, drone_position):
        detected = []
        for obs in self.obstacles:
            distance = math.sqrt((drone_position[0] - obs[0]) ** 2 +
                                 (drone_position[1] - obs[1]) ** 2 +
                                 (drone_position[2] - obs[2]) ** 2)
            if distance < 5:  # If the obstacle is within 5 units
                detected.append(obs)
        return detected


def main():
    drone1 = Drone("Drone1")
    maze_obstacles = Obstacles()

    # Add some obstacles
    maze_obstacles.add_obstacle((1, 1, 0))
    maze_obstacles.add_obstacle((3, 2, 0))
    maze_obstacles.add_obstacle((7, 5, 0))
    maze_obstacles.add_obstacle((2, 8, 0))

    # Drone actions
    drone1.take_off()
    drone1.fly_to(2, 2, 0)

    detected = maze_obstacles.detect_obstacles(drone1.position)
    if detected:
        print("Obstacles detected:", detected)
        drone1.land()
    else:
        drone1.fly_to(5, 5, 0)
        detected = maze_obstacles.detect_obstacles(drone1.position)
        if detected:
            print("Obstacles detected:", detected)
            drone1.land()
        else:
            drone1.fly_to(10, 10, 0)
            drone1.land()

    drone1.recharge()
    drone1.take_off()
    drone1.fly_to(0, 0, 0)


def simulate_drone_operations(drone):
    for _ in range(5):
        if drone.battery_level > 0:
            x, y, z = random.randint(-10, 10), random.randint(-10, 10), random.randint(0, 5)
            drone.fly_to(x, y, z)
            time.sleep(1)
        else:
            print(f"{drone.name} is out of battery. Stopping simulation.")
            break


if __name__ == "__main__":
    main()
    # Uncomment below line to run a simulation
    # simulate_drone_operations(drone1)