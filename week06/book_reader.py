def chapters_reader(fileName):
    for name in fileName:
        with open(name, 'r') as f:
            read_data = ''

            for line in f:
                if '# Chapter' in line:
                    if not read_data:
                        read_data += line
                    else:
                        yield read_data
                        read_data = line
                else:
                    read_data += line
            yield read_data


def book_reader(fileName):
    for book in chapters_reader(fileName):
        print(book)
        key = ''
        while key != ' ':
            key = input('Press space and enter for next chapter: ')


book_reader(('001.txt', '002.txt'))
