# області видимості
# LEGB (local, enclosing, global, build-in)
# Організація пам'яті - стек і купа
# hotkey ctrl+shift+alt+L - редагує неправильні відступи, робить по РЕР8
# дістати можна будь яку змінну нижчу за глобальну, змінити - не можемо
# першими аргументами пишемо наші валсні, потім -опціональні(ті що є в пітоні)

def some_func(word, text=None):
    return word + text


# text = input('write some data: ')
some_func(text='all', word='ALL')
