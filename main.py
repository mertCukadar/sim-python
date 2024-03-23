from src.map import Map
from src.prey import Prey
import numpy as np 

def main() -> None:
    map = Map(800, 600)
    
    preys = []
    for i in range(3):
        preys.append(Prey(np.random.uniform(0 , 800), np.random.uniform(0 , 600)))

    map.init_player(preys)
    map.start_screen()
  
    
       

       


if __name__ == "__main__":
    main()