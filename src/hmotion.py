import numpy as np
import matplotlib.pyplot as plt

class HorizontalMotion:
    
    def __init__(self, k, m, v0, x0, time, t_max):
        k = 10
        m = 1
        x0 = 1
        v0 = 0
        time = 0.01
        t_max = 10
        
        x = x0
        v = v0
        
        t_data = np.arange(0, t_max, time)
        x_data = []
        
        for spot in t_data :
            a = -k/m * x
            v += a * time
            x += v * time
            x_data.append(x)
            
        plt.plot(t_data, x_data)
        plt.xlabel("Time (s)")
        plt.ylabel("Displacement (m)")
        plt.title("Harmonic Motion")
        plt.grid(True)
        plt.show()
    
    
    # matplotlib.pyplot.plot(t_data, x_data)
    
    # if __name__ == "__main__":
    #     HorizontalMotion(k=10, m=1, v0=0, x
    
    
        
        
        