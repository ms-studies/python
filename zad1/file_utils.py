def write_line_to_file(result):
    file = open('history.txt', 'a') # a - open for writing, appending to the end of the file if it exists
    file.write(result + '\n')
    file.close()