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
    duration = 178.0
    tran = 2.0
    pic_dir = '/home/cpenner/data/Pictures'

    for root, dirs, files in os.walk(pic_dir):
        for name in files:
            filename = os.path.join(root, name)
            if '&' in filename or filename.endswith('.db'):
                continue
            if old_filename:
                fp.write(f'    <to>{filename}</to>\n')
                fp.write(f'  </transition>\n')
            fp.write(f'''  <static>
    <duration>{duration}</duration>
    <file>{filename}</file>
  </static>
  <transition>
    <duration>{tran}</duration>
    <from>{filename}</from>\n''')
            old_filename = filename


if __name__ == '__main__':
    outfile = 'big_h.xml'
    with open(outfile, 'w') as f:
        top(f)
        main(f)
        bottom(f)
