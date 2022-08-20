def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    allen_word_count = 0
    tom_word_count = 0
    allen_sticker_count = 0
    tom_sticker_count = 0
    allen_image_count = 0
    tom_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count == 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Tom':
            if s[2] == '貼圖':
                tom_sticker_count += 1
            elif s[2] == '圖片':
                tom_image_count += 1
            else:
                for m in s[2:]:
                    tom_word_count += len(m)
    print('Allen說了', allen_word_count, '個字, 傳了', allen_sticker_count, '個貼圖和', allen_image_count, '張圖片')
    print('Tom說了', tom_word_count, '個字, 傳了', tom_sticker_count, '個貼圖和', tom_image_count, '張圖片')

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('line_record.txt')
    lines = convert(lines)
    # write_file('line_record_output.txt', lines)

main()