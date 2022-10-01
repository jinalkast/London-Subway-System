from itertools import permutations
from python.shortestPath import PathFactory
from python.graph import Itinerary

class SubwayPatrol():     
     # implementation of traveling Salesman Problem
     def travellingSalesmanProblem(graph,subset):
          itineraries = []
          perms_of_stations =  permutations(subset)
          for path in perms_of_stations:
               itinerary = None
               for i in range(len(path)-1):
                    if itinerary == None:
                         itinerary = PathFactory.dijkstra(graph,path[i],path[i+1])
                    else:
                         itinerary = Itinerary.combine_itineraries(itinerary,PathFactory.dijkstra(graph,path[i],path[i+1]))

               # Go from end back to start
               itinerary = Itinerary.combine_itineraries(itinerary,PathFactory.dijkstra(graph,itinerary.finish,itinerary.start))

               itineraries.append(itinerary)    
                
          smallest_path = itineraries[0]
          for i in itineraries:
               if i.total_path_length < smallest_path.total_path_length:
                    smallest_path = i

          return smallest_path 

               
