import datetime
from file_utils import write_line_to_file, read_lines

def start_session():
    now = datetime.datetime.now()
    write_line_to_file("== " + now.strftime("%Y-%m-%d") + " ==")

def print_current_session():
    lines = read_lines()
    current_session_lines = []
    for line in reversed(lines):
        if line.startswith('=='):
            break
        current_session_lines.append(line)
    
    if len(current_session_lines) > 0:
        print("Operacje w obecnej sesji:")
        for line in reversed(current_session_lines):
            print(line)
    else:
        print("Brak operacji w obecnej sesji.")
