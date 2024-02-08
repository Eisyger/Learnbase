class Bullet:
    def fire(self):
        print("Fire Bullet")

    def draw(self):
        print("Draw Bullet")


class BulletV1(Bullet):
    def fire(self):
        super().fire()

    def draw(self):
        print("Draw the Bullet in a nice color.")


class Player:
    def shoot(self, bullet: Bullet):
        bullet.fire()
        bullet.draw()


if __name__ == '__main__':
    player = Player()
    bullet = Bullet()
    bullet_v1 = BulletV1()
    player.shoot(bullet)
    player.shoot(bullet_v1)
