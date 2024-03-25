from src.map import Map
from src.prey import Prey
import numpy as np 
from src.hunter import Hunter

def main() -> None:
    map = Map(800, 800)
    
    preys = []
    for i in range(50):
        preys.append(Prey(np.random.uniform(0 , 800), np.random.uniform(0 , 800)))

        
    hunter = Hunter(400, 400)

    map.init_hunter(hunter)
    map.init_player(preys)
    map.start_screen()
  
if __name__ == "__main__":
    main()
    
