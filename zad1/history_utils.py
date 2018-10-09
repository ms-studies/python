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


def print_date_history():
    date = input('Podaj datę w formacie YYYY-MM-DD: ')
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Błędny format daty')
        return

    lines = read_lines()
    date_lines = []
    should_aggregate = False

    for line in lines:
        if line == ('== ' + date + ' ==\n'):
            should_aggregate = True
        elif line.startswith('=='):
            should_aggregate = False
        elif should_aggregate:
            date_lines.append(line)
    
    if len(date_lines) > 0:
        print("Operacje z dnia " + date + ":")
        for line in date_lines:
            print(line)
    else:
        print("Brak operacji z dnia " + date + ":")

