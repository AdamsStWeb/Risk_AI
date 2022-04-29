class Continent:
    territories = []

    def __init__(self,name,bonus):
        self.name = name
        self.bonus = bonus
    
    def __repr__(self):
        return f'Continet(name={self.name}, bonus={self.bonus})'

class Territory:
    def __init__(self, id, name, x_cord, y_cord, adj_list, units = 0, color=(255,255,255)):
        self.id = id
        self.color = color
        self.name = name
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.units = units
        self.adj_list = adj_list
    
    def __repr__(self):
        return f'Territory(name={self.name}, id={self.id}, units={self.units}, color={self.color}, x_cord={self.x_cord}, y_cord={self.y_cord}, adj_list={self.adj_list})'

def ReadFile():
    with open("./Tinfo.txt") as file:
        territories = []
        continents  = []
        
        line = file.readline()
        line = line.split(" ")
        c = Continent(line[0],line[1])

        for line in file:
             line = line.strip()
             line = line.split(" ")
      
             if str.isdigit(line[0]):
                c.territories.append(line[0])
                coords = line[2].split(",")
                adj_list = line[3].split(",")
                adj_list = list(map(int, adj_list))            
                t = Territory(int(line[0]), line[1], int(coords[0]), int(coords[1]), adj_list)
                territories.append(t) 
             
             else:
                continents.append(c)
                c = Continent(line[0], int(line[1]))
        
        continents.append(c)    
        return continents, territories
    