from scripts import settings

camerax = 0
cameray = 0

def track(coords:tuple[float, float]):
    global camerax, cameray
    camerax += (coords[0] - settings.screen_w / 2 - camerax) / settings.camera_sensitivity
    cameray += (coords[1] - settings.screen_h / 2 - cameray) / settings.camera_sensitivity
    if cameray > (settings.level_height - settings.screen_h):
        cameray = settings.level_height - settings.screen_h
    if cameray < 0:
        cameray = 0
    if camerax < 0:
        camerax = 0
    if camerax > (settings.level_width - settings.screen_w):
        camerax = settings.level_width - settings.screen_w