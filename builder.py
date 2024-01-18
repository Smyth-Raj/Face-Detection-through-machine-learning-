import mimetypes

print(mimetypes.guess_type('test.jpg'))
# ('image/jpeg', None)

print(type(mimetypes.guess_type('test.jpg')))
# <class 'tuple'>

print(mimetypes.guess_type('test.jpg')[0])
# image/jpeg

print(type(mimetypes.guess_type('test.jpg')[0]))
# <class 'str'>
