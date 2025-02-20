# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import heapq

class Graph:
    def __init__(self):
        self.vtces = {}

    def add_vertex(self, vname):
        if vname not in self.vtces:
            self.vtces[vname] = {}

    def remove_vertex(self, vname):
        if vname in self.vtces:
            for nbr in self.vtces[vname]:
                del self.vtces[nbr][vname]
            del self.vtces[vname]

    def add_edge(self, vname1, vname2, value):
        if vname1 in self.vtces and vname2 in self.vtces:
            self.vtces[vname1][vname2] = value
            self.vtces[vname2][vname1] = value

    def contains_vertex(self, vname):
        return vname in self.vtces

    def display_stations(self):
        print("\n***********************************************************************")
        for i, station in enumerate(self.vtces.keys(), start=1):
            print(f"{i}. {station}")
        print("***********************************************************************")

    def display_map(self):
        print("\t Delhi Metro Map")
        print("\t------------------")
        for station, nbrs in self.vtces.items():
            print(f"{station} => ", end="")
            for nbr, distance in nbrs.items():
                print(f"{nbr} ({distance} km) ", end="")
            print()
        print("\t------------------")

    def dijkstra(self, src, des, time_flag):
        distances = {vname: float('inf') for vname in self.vtces}
        distances[src] = 0
        
        min_heap = [(0, src)]
        
        while min_heap:
            dist, vname = heapq.heappop(min_heap)
            
            if dist > distances[vname]:
                continue
            
            if vname == des:
                return dist
            
            for nbr, weight in self.vtces[vname].items():
                new_dist = dist + (weight * 40 + 120 if time_flag else weight)
                
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    heapq.heappush(min_heap, (new_dist, nbr))
        
        return -1  # Not reachable

    @staticmethod
    def create_metro_map(g):
        g.add_vertex("Noida Sector 62~B")
        g.add_vertex("Botanical Garden~B")
        g.add_vertex("Yamuna Bank~B")
        g.add_vertex("Rajiv Chowk~BY")
        g.add_vertex("Vaishali~B")
        g.add_vertex("Moti Nagar~B")
        g.add_vertex("Janak Puri West~BO")
        g.add_vertex("Dwarka Sector 21~B")
        g.add_vertex("Huda City Center~Y")
        g.add_vertex("Saket~Y")
        g.add_vertex("Vishwavidyalaya~Y")
        g.add_vertex("Chandni Chowk~Y")
        g.add_vertex("New Delhi~YO")
        g.add_vertex("AIIMS~Y")
        g.add_vertex("Shivaji Stadium~O")
        g.add_vertex("DDS Campus~O")
        g.add_vertex("IGI Airport~O")
        g.add_vertex("Rajouri Garden~BP")
        g.add_vertex("Netaji Subhash Place~PR")
        g.add_vertex("Punjabi Bagh West~P")

        g.add_edge("Noida Sector 62~B", "Botanical Garden~B", 8)
        g.add_edge("Botanical Garden~B", "Yamuna Bank~B", 10)
        g.add_edge("Yamuna Bank~B", "Vaishali~B", 8)
        g.add_edge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
        g.add_edge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
        g.add_edge("Moti Nagar~B", "Janak Puri West~BO", 7)
        g.add_edge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
        g.add_edge("Huda City Center~Y", "Saket~Y", 15)
        g.add_edge("Saket~Y", "AIIMS~Y", 6)
        g.add_edge("AIIMS~Y", "Rajiv Chowk~BY", 7)
        g.add_edge("Rajiv Chowk~BY", "New Delhi~YO", 1)
        g.add_edge("New Delhi~YO", "Chandni Chowk~Y", 2)
        g.add_edge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
        g.add_edge("New Delhi~YO", "Shivaji Stadium~O", 2)
        g.add_edge("Shivaji Stadium~O", "DDS Campus~O", 7)
        g.add_edge("DDS Campus~O", "IGI Airport~O", 8)
        g.add_edge("Moti Nagar~B", "Rajouri Garden~BP", 2)
        g.add_edge("Punjabi Bagh West~P", "Rajouri Garden~BP", 2)
        g.add_edge("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)

def main():
    g = Graph()
    Graph.create_metro_map(g)

    while True:
        print("\n\t\t\t\t~~LIST OF ACTIONS~~")
        print("1. LIST ALL THE STATIONS IN THE MAP")
        print("2. SHOW THE METRO MAP")
        print("3. GET SHORTEST DISTANCE FROM A 'SOURCE' TO 'DESTINATION'")
        print("4. GET SHORTEST TIME TO REACH FROM A 'SOURCE' TO 'DESTINATION'")
        print("5. EXIT THE MENU")
        choice = input("ENTER YOUR CHOICE FROM THE ABOVE LIST (1 to 5): ")

        if choice == '1':
            g.display_stations()
        
        elif choice == '2':
            g.display_map()

        elif choice == '3':
            src = input("ENTER SOURCE STATION: ")
            dest = input("ENTER DESTINATION STATION: ")
            if not g.contains_vertex(src) or not g.contains_vertex(dest):
                print("THE INPUTS ARE INVALID")
            else:
                distance = g.dijkstra(src, dest, False)
                if distance != -1:
                    print(f"SHORTEST DISTANCE FROM {src} TO {dest} IS {distance} KM")
                else:
                    print(f"NO PATH EXISTS FROM {src} TO {dest}")

        elif choice == '4':
            src = input("ENTER SOURCE STATION: ")
            dest = input("ENTER DESTINATION STATION: ")
            if not g.contains_vertex(src) or not g.contains_vertex(dest):
                print("THE INPUTS ARE INVALID")
            else:
                time = g.dijkstra(src, dest, True)
                if time != -1:
                    print(f"SHORTEST TIME FROM {src} TO {dest} IS {time // 60} MINUTES")
                else:
                    print(f"NO PATH EXISTS FROM {src} TO {dest}")

        elif choice == '5':
            print("EXITING...")
            break

        else:
            print("Please enter a valid option!")

if __name__ == "__main__":
    main()