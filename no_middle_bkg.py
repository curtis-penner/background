import os


def top(fp):
    fp.write('''d
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
    fp.write('</background>')


def main(fp):
    duration = 300.0
    pic_dir = '/home/cpenner/data/Pictures/Wallpapers'

    for root, dirs, files in os.walk(pic_dir):
        for name in files:
            filename = os.path.join(root, name)
            if '&' in filename or filename.endswith('.db'):
                continue
            fp.write(f'''  <static>
    <duration>{duration}</duration>
    <file>{filename}</file>
  </static>
''')


if __name__ == '__main__':
    outfile = 'wallpaper.xml'
    with open(outfile, 'w') as f:
        top(f)
        main(f)
        bottom(f)
