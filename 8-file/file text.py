# import csv
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         # Process row
#         ...


import re
import PIL


# from translate import Translator


def old_to_new_event():
    old_text = 'event.txt'
    new_text = 'new_event.txt'
    with open(new_text, 'w') as new_f:
        with open(old_text, 'r') as f:
            print('printing')
            for line in f.readlines():
                new_line = re.sub('([^\u4e00-\u9fa5]|^\W)+', "", line)
                if not new_line == '':
                    # translator = Translator(to_lang="en", from_lang='zh')
                    # translation = translator.translate(new_line)
                    # new_f.write(translation + ',' + new_line + ',' + '1' + '\n')
                    new_f.write('e' + ',' + new_line + ',' + '1' + '\n')

            print('Done')


def new_event_file_remove_space():
    old_text = 'new_event.txt'
    new_text = 'new_event_2.txt'
    with open(new_text, 'w') as new_f:
        with open(old_text, 'r') as f:
            print('printing')
            for line in f.readlines():
                items = re.split(' ', line)
                new_line = ''.join([item.capitalize() for item in items])
                if not new_line == '':
                    # translator = Translator(to_lang="en", from_lang='zh')
                    # translation = translator.translate(new_line)
                    # new_f.write(translation + ',' + new_line + ',' + '1' + '\n')
                    new_line = multiple_replace(new_line, {' ': '', 'Click': 'Action'})
                    new_f.write('to' + new_line + '\n')

            print('Done')


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, text)


if __name__ == '__main__':
    new_event_file_remove_space()
