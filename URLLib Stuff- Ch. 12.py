import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen(input('Enter URL of image: '))
fhand = open('img.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
