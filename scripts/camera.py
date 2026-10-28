from scripts import settings

camerax = 0
cameray = 0

def track(coords:tuple[float, float]):
    global camerax, cameray
    camerax += (coords[0] - settings.screen_w / 2 - camerax) / settings.camera_sensitivity
    cameray += (coords[1] - settings.screen_h / 2 - cameray) / settings.camera_sensitivity