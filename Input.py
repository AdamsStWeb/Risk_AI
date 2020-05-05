import os

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
grey=(100,100,100)
yellow=(255,255,0)
purple = (240,0,255)

class Player:
    def __init__(self, pid = 0, pcolor = (255,255,255), powns = [], pmen = 0):
        self.pid = pid
        self.pcolor = pcolor
        self.powns = []
        self.pmen = pmen
    def get_pid(self):
        return self.pid
    def set_pid(self,PID):
        self.pid = PID   
    def get_color(self):
         return self.pcolor
    def set_pcolor(self,pc):
        self.pcolor = pc
    def get_powns(self):
        return self.powns
    def set_powns(self,owns):
        self.powns = owns
    def get_pmen(self):
        return self.pmen
    def set_pmen(self,men):
        self.pmen = men
    def add_pmen(self,num):
        self.pmen = self.pmen + num
    def remove_pmen(self,num):
        self.pmen = self.pmen - num
    def add_t(self,id):
        self.powns.append(id)
    def remove_t(self,id):
        self.powns.remove(id)

class Continent:
    def __init__(self,name = "",bonus=0,countries =[]):
        self.name = name
        self.bonus = bonus
        self.countries = []
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name=n
    def get_bonus(self):
        return self.bonus
    def set_bonus(self, b):
        self.bonus = b
    def get_countries(self):
        return self.countries
    def add_country(self, c):
        self.countries.append(c)

class Territory:
    def __init__(self, id = 0, color = (255,255,255), name = '', xcord = 0, ycord = 0, num_of_units = 0,adj_list = []):
        self.id = id
        self.color = color
        self.name = name
        self.xcord = xcord
        self.ycord = ycord
        self.num_of_units = num_of_units
        self.adj_list = adj_list

    def get_id(self):
        return self.id
    def set_id(self, d):
        self.id = d
    def get_color(self):
        return self.color
    def set_color(self, c):
        self.color = c
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name = n
    def get_xcord(self):
        return self.xcord
    def set_xcord(self, x):
        self.xcord = x
    def get_ycord(self):
        return self.ycord
    def set_ycord(self, y):
        self.ycord = y
    def get_num_of_units(self):
        return self.num_of_units
    def set_num_of_units(self, mn):
        self.num_of_units = mn
    def add_num_of_units(self, mn):
        self.num_of_units = self.num_of_units + mn
    def get_adj_list(self):
        return self.adj_list
    def set_adj_list(self,x):
        self.adj_list = x

def open_file():
    #Open Tinfo.txt
    __location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
    f = open(os.path.join(__location__,"Tinfo.txt"))
    
    territories = []
    continents  = []
    c = Continent()

    for line in f:
        words = line.split(" ") 
        if str.isdigit(line[0]):
            t = Territory()
            #Id
            t.set_id(int(words[0])) 
            c.add_country(words[0])
            #Name
            t.set_name(words[1])
            #Coords
            coords = words[2].split(",")
            t.set_xcord(int(coords[0])) 
            t.set_ycord(int(coords[1]))
            #AdjList
            adj_list = words[3].split(",")
            adj_list[-1] = adj_list[-1].strip()
            adj_list_clean = []
            for i in adj_list:
                if i != "":
                    i= int(i)
                    adj_list_clean.append(i)
            t.set_adj_list(adj_list_clean)


            territories.append(t)            
        else:
            continents.append(c)
            c = Continent()
            c.set_name(words[0])
            c.set_bonus(int(words[1])) 
    f.close()

    #Add Austrillia 
    continents.append(c)
    del continents[0]    
    return territories,continents
