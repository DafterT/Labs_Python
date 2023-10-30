# TODO Найдите количество книг, которое можно разместить на дискете
number_of_characters_per_line = 25
number_of_lines_per_page = 50
number_of_pages_per_book = 100
number_of_characters_per_book = number_of_characters_per_line * number_of_lines_per_page * number_of_pages_per_book
weight_of_one_character = 4  # байта
book_size = number_of_characters_per_book * weight_of_one_character
floppy_disk_size = 1.44 * (2 ** 10) * (2 ** 10)  # байт
print("Количество книг, помещающихся на дискету:", round(floppy_disk_size // book_size))
