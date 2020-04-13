from random import randint


def words_generator(words_count):
    text = ' '
    for i in range(words_count):
        word = ''
        for a in range(randint(1, 30)):
            char = chr(randint(65, 126))
            word += char
        text += ' {}'.format(word)

    return text


def book_generator(chapters_count, chapter_length_range):
    with open('generated_book.txt', 'a') as f:
        chapters = 0
        while chapters < chapters_count:
            chapters += 1
            content = "# Chapter {}\n".format(chapters)
            chapter = words_generator(chapter_length_range)
            content += chapter + '\n'
            f.write(content)
            f.write('\n')


book_generator(2, 500)
