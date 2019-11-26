from PIL import Image

ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

def color_to_char(color):
    gray = (color[0] + color[1] + color[2]) / 3
    char = int(gray * (len(ascii) - 1) / 255)
    return ascii[char]

def ascii_art(img):
    w, h = img.size
    img = img.resize((w, h // 2))
    w, h = img.size

    text = ''
    for y in range(h):
        for x in range(w):
            text += color_to_char(img.getpixel((x, y)))
            # print(img.getpixel((x, y)))
        text += '\n'
    return text

def main():
    src = Image.open('img/src.jpg')
    with open("aart.txt", "w") as text_file:
        print(ascii_art(src), file=text_file)

if __name__ == "__main__":
    main()