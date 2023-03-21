from enum import Enum
import utils

class MapEntity(Enum):
    EMPTY = 0
    OBSTACLE = 1
    LOOT = 2
    ENEMY = 3
    DEAD_ENEMY = 4
    PROJECTILE = 5
    HERO = 6
    
class Map:
    map = {} #tuple indexed dict as 2d array
    width = 0
    height = 0
    def __init__(self, map_state, map_resource):
        self.height = map_state["map"]["height"]
        self.width = map_state["map"]["width"]
        
        #init blank
        for x in range(self.width):
            for y in range(self.height):
                self.map[(x,y)] = MapEntity.EMPTY
    
        #set obstacles
        obstacles = map_resource["compressedObstacles"]["coordinateMap"]
        print(obstacles)
        for x in obstacles:
            for y in obstacles[x]:
                x = int(x)
                self.map[(x,y)] = MapEntity.OBSTACLE
                
        self.update_state(map_state)

    def update_state(self, map_state):
        treasures = map_state["map"]["treasures"]
        for i in treasures:
            if(i["collectedByHeroId"] is None):
                self.map[(i["position"]["x"], i["position"]["y"])] = MapEntity.LOOT
            else:
                self.map[(i["position"]["x"], i["position"]["y"])] = MapEntity.EMPTY
        
        enemies = map_state["map"]["enemies"]
        for x in enemies:
            if(x["health"] > 0):
                self.map[(x["position"]["x"], x["position"]["y"])] = MapEntity.ENEMY
            else:
                self.map[(x["position"]["x"], x["position"]["y"])] = MapEntity.DEAD_ENEMY
                
        hero = map_state["heroes"][0]
        self.map[(hero["position"]["x"], hero["position"]["y"])] = MapEntity.HERO
            

    def __repr__(self) -> str:
        out = ""
        line_sep = '#' * (self.width * 4 + 1)
        charmap = {
            MapEntity.EMPTY: ' ',
            MapEntity.OBSTACLE: 'O',
            MapEntity.LOOT: 'L',
            MapEntity.ENEMY: 'E',
            MapEntity.DEAD_ENEMY: 'D',
            MapEntity.PROJECTILE: '!',
            MapEntity.HERO: 'H'
        }

        for y in range(self.height-1, 0 ,-1):
            out += line_sep + '\n'
            for x in range(self.width):
                char = charmap[self.map[(x,y)]]
                out += f"# {char} "
            out += "#\n"
        out += line_sep + '\n'
        return out
