
class Gun:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bullets = 0

    def add_bullet(self, num_bullets):
        if num_bullets > 12:
            raise OverflowError("Bullet size can not exceed 12")
        self.bullets += num_bullets

    def reload_bullet(self):
        self.bullets = self.capacity

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "Bang!"
        else:
            return "Click..."

