def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Determines if the player can eat a ghost."""
    return power_pellet_active and touching_ghost

def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Determines if the player scored."""
    return touching_power_pellet or touching_dot

def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Determines if the player loses."""
    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Determines if the player wins."""
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
