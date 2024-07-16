from enum import Enum


# ------ global funcitons ------

def formatTable(data, order='alphabet', reverse=False):
    # Get all unique keys (column names) from the list of dictionaries
    columns = sorted({key for item in data for key in item.keys()})
    
    # Order columns based on the 'order' parameter
    if order == 'alphabet':
        columns.sort()
    elif order is not None:
        # If order is None, columns remain arbitrarily ordered
        pass
    
    # Reverse columns if 'reverse' parameter is True
    if reverse:
        columns.reverse()
    
    # Determine the width of each column
    column_widths = {}
    for col in columns:
        max_length = max((len(str(item.get(col, ''))) for item in data), default=0)
        column_widths[col] = max(max_length, len(col), 4)
    
    # Function to create a row with proper spacing
    def create_row(row_data):
        return ' '.join(f'{str(row_data.get(col, "")).ljust(column_widths[col])}' for col in columns)
    
    # Create the header row
    header_row = create_row({col: col for col in columns})
    
    # Create the separator row
    separator_row = ' '.join('-' * column_widths[col] for col in columns)
    
    # Create the data rows
    data_rows = [create_row(item) for item in data]
    
    # Combine all parts into the final table
    table = '\n'.join([header_row, separator_row] + data_rows) + '\n'
    
    return table

# ------ global classes ------


class Status(Enum):
    Unknown = 0
    Unresponsive = 1
    Error = 2
    NotReady = 3
    Ready = 4
    Rendering = 5

class renderSlave():
    def __init__(self, name, ip) -> None:
        self.name = ""
        self.ip = ""
        self.status = Status.Unknown
