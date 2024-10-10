#display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1602
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

#Imgaes
BG_IMAGE_PATH = 'bg/bg.png'
GAME_INDICES = [1, 2, 3,]
SYM_PATH = "icons"

symbols = {
    'HTML': f"{SYM_PATH}/HTML.png",
    'CSS': f"{SYM_PATH}/CSS.png",
    'Java': f"{SYM_PATH}/Java.png",
    'JS': f"{SYM_PATH}/JS.png",
    'PHP': f"{SYM_PATH}/PHP.png",
    'react': f"{SYM_PATH}/react.png",
    'PYTHON': f"{SYM_PATH}/PYTHON.png",
    'Angular': f"{SYM_PATH}/Angular.png"
}
multipliers = {
    'icons/HTML.png': 1.5,
    'icons/CSS.png': 2.0,
    'icons/Java.png': 3.0,
    'icons/JS.png': 2.5,
    'icons/PHP.png': 1.8,
    'icons/react.png': 2.2,
    'icons/PYTHON.png': 4.0,
    'icons/Angular.png': 1.7
}