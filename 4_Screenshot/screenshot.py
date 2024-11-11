# pip install pyscreenshot
# https://github.com/ponty/pyscreenshot
# https://www.guru99.com/es/how-to-install-pip-on-windows.html
# C:\Users\#####\AppData\Local\Programs\Python\Python313>python -m pip install pillow

# import sys
# print(sys.executable)

import pyscreenshot

image = pyscreenshot.grab()
image.show()
image.save("./4_Screenshot/full.png")

image2 = pyscreenshot.grab(bbox=(100, 100, 500, 500))
image2.show()
image2.save("./4_Screenshot/part.png")
