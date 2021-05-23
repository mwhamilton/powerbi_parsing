def parse_m(text):
    FILE_READERS = {
        'Excel.Workbook': 'Excel',
    }
    source_line = [x for x in text.split('\n') if 'Source' in x][0]  # we want the first line to define "Source"
    for reader in FILE_READERS:
        if reader in source_line:
            file_path = ')'.join(source_line.split('(', 2)[2].split(')')[:-2])[1:-1]
            return {
                'path': file_path, 
                'type': FILE_READERS[reader],
            }
    else:
        print(source_line)
        exit()


def parse_source(raw_data):
    if raw_data['source']['type'] == 'calculated':
        return  {'type': 'calculated'}
    if raw_data['source']['type'] == 'm':
        return parse_m(raw_data['source']['expression'])
    return BaseSource(raw_data)