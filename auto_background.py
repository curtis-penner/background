import os


def top(fp):
    fp.write('''
<background>
  <starttime>
    <year>2020</year>
    <month>09</month>
    <day>10</day>
    <hour>01</hour>
    <minute>10</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->
''')


def bottom(fp):
    fp.write('  <transition>')
    fp.write('</background>')


def main(fp):
    old_filename = ''
    duration = 1795.0
    tran = 2.0
    pic_dir = '/home/cpenner/data/Pictures/Wallpapers'

    dir_list = os.listdir(pic_dir)
    for filename in dir_list:
        if old_filename:
            fp.write(f'    <to>{pic_dir  + "/" + filename}</to>\n')
            fp.write(f'  </transition>\n')
        fp.write(f'''  <static>
    <duration>{duration}</duration>
    <file>{pic_dir + '/' + filename}</file>
  </static>
  <transition>
    <duration>{tran}</duration>
    <from>{pic_dir + '/' + filename}</from>\n''')
        old_filename = filename


if __name__ == '__main__':
    outfile = 'new_h.xml'
    with open(outfile, 'w') as fp:
        top(fp)
        main(fp)
        bottom(fp)
