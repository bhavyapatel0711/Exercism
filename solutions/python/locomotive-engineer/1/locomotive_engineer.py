def get_list_of_wagons(*wagons):
    return list(wagons)

def fix_list_of_wagons(wagon_1: list, wagon_2: list) -> list:
   a,b,c,*d = wagon_1
   return [c,*wagon_2,*d,a,b]

def add_missing_stops(route: dict, **stops) -> dict:
        route["stops"] = list(stops.values())
        return route

def extend_route_information(route: dict, details: dict) -> dict:    
    return {**route, **details}

def fix_wagon_depot(wagons: list) -> list:
    return [list(row) for row in zip(*wagons)]

