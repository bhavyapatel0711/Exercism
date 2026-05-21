def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type: int, person_name: str) -> list:
    """Add a person to the appropriate queue based on the ticket type."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue
    
def find_my_friend(queue: list, friend_name: str) -> int:
    """Find the index of a friend in the queue."""
    for i in range(len(queue)):
        if queue[i] == friend_name:
            return i
    return -1   

def add_me_with_my_friends(queue: list, index: int, person_name: str) -> list:
    """Add a person to the queue at a specific index."""
    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue: list, person_name: str) -> list:
    """Remove a person from the queue."""
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue: list, person_name: str) -> int:
    """Count how many times a person appears in the queue."""
    count = 0
    for i in range(len(queue)):
        if queue[i] == person_name:
            count += 1
    return count

def remove_the_last_person(queue: list) -> list:
    """Remove the last person from the queue."""
    return queue.pop()

def sorted_names(queue: list) -> list:
    """Return a sorted list of names in the queue."""
    return sorted(queue)    