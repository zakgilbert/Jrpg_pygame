class Animator:
    def __init__(self, speed):
        self.frame = 0
        self.timer = 0.0
        self.speed = speed
    
    def time_to_animate(self, time, frames):
        self.timer += time / 1000.0
        if self.timer >= self.speed:
            self.frame = (self.frame + 1) % frames 
            self.timer = 0.0
            return True
        return False
