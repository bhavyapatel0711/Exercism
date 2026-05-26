def get_coordinate(treasure_coordinates: tuple) -> str:
    """Extract the coordinates from the treasure record."""
    return treasure_coordinates[1]

def convert_coordinate(coordinates: str) -> tuple:
    """Split the given string of comma-separated coordinates into a tuple."""
    return (coordinates[0], coordinates[1])

def compare_records(treasure_coordinates: tuple, record_coordinates: tuple) -> bool:
    """Compare the coordinates of the treasure and the record."""
    return convert_coordinate(treasure_coordinates[1]) == convert_coordinate(record_coordinates[1])

def create_record(treasure_coordinates: tuple, record_coordinates: tuple) -> tuple:
    """Create a combined record if the coordinates match."""
    if convert_coordinate(treasure_coordinates[1]) == convert_coordinate(record_coordinates[1]):
        return treasure_coordinates + record_coordinates
    else:
        return "not a match"
    
def clean_up(combined_record: tuple) -> str:
    """Clean up a combined record into a multi-line string."""
    report = ""
    for record in combined_record:
        cleaned_record = record[:1] + record[2:]

        report += str(cleaned_record) + "\n"
    
    return report
