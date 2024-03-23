from src.map import Map
from src.prey import Prey
import numpy as np 
from src.obst import Obsticle

def main() -> None:
    map = Map(800, 800)
    
    preys = []
    for i in range(15):
        preys.append(Prey(np.random.uniform(0 , 800), np.random.uniform(0 , 800)))

    map.init_player(preys)
    map.start_screen()
  
if __name__ == "__main__":
    main()
    
