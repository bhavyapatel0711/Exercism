def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Verify criticality is balanced."""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage: int, current: int, theoretical_max_power: int) -> str:
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'
    
def fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str:  
    """Assess and return the status code for the reactor."""
    product = temperature * neutrons_produced_per_second

    if product < 0.9 * threshold:
        return 'LOW'
    elif 0.9*threshold <= product <= 1.1 * threshold:
        return 'NORMAL'
    else:     return 'DANGER'   
 # Expected output: 'NORMAL'