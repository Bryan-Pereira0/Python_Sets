#task1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

Shared_Routes = our_routes.intersection(competitor_routes)
print ("These are our shared routes: ", Shared_Routes)

Our_Unique = our_routes.difference(competitor_routes)
print ("These are our unique routes: ", Our_Unique)

all_routes = our_routes.union(competitor_routes)
routes_not_shared = all_routes.difference(Shared_Routes)
print("Routes that are not shared: ", routes_not_shared)

