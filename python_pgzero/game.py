import pgzero
import pgzrun
from random import randint

# Configurações do jogo
TITLE = "Plataforma Simples"
WIDTH = 800
HEIGHT = 600

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Classe do jogador
class Player(Actor):
    def __init__(self, image, pos):
        super().__init__(image, pos)
        self.vy = 0
        self.jumping = False
        self.score = 0
        self.lives = 3

    def update(self):
        # Gravidade
        self.vy += 0.4
        self.y += self.vy

        # Controle do jogador
        if keyboard.left:
            self.x -= 5
        if keyboard.right:
            self.x += 5

        # Limites da tela
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y > HEIGHT - 50:  # Chão
            self.y = HEIGHT - 50
            self.vy = 0
            self.jumping = False

# Classe dos obstáculos
class Obstacle(Actor):
    def __init__(self, image, pos):
        super().__init__(image, pos)
        self.speed = 3

    def update(self):
        self.x -= self.speed
        if self.x < -50:
            self.x = WIDTH + 50
            self.y = randint(100, HEIGHT - 100)

# Classe dos coletáveis
class Collectible(Actor):
    def __init__(self, image, pos):
        super().__init__(image, pos)

    def update(self):
        self.x -= 2
        if self.x < -50:
            self.x = WIDTH + 50
            self.y = randint(100, HEIGHT - 100)

# Inicialização do jogo
player = Player('player', (100, HEIGHT - 50))
obstacles = [Obstacle('obstacle', (WIDTH + i * 300, HEIGHT - 100)) for i in range(3)]
collectibles = [Collectible('collectible', (WIDTH + i * 200, HEIGHT - 150)) for i in range(3)]
game_over = False
game_won = False

def update():
    global game_over, game_won
    
    if not game_over and not game_won:
        player.update()
        
        # Atualiza obstáculos
        for obstacle in obstacles:
            obstacle.update()
            if player.colliderect(obstacle):
                player.lives -= 1
                if player.lives <= 0:
                    game_over = True
                else:
                    player.x = 100
                    player.y = HEIGHT - 50
        
        # Atualiza coletáveis
        for collectible in collectibles:
            collectible.update()
            if player.colliderect(collectible):
                player.score += 1
                collectible.x = WIDTH + 50
                collectible.y = randint(100, HEIGHT - 100)
                if player.score >= 10:
                    game_won = True

def draw():
    screen.fill(WHITE)
    
    # Desenha o chão
    screen.draw.filled_rect(Rect((0, HEIGHT - 40), (WIDTH, 40)), BLACK)
    
    # Desenha elementos do jogo
    player.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for collectible in collectibles:
        collectible.draw()
    
    # Desenha informações do jogo
    screen.draw.text(f"Vidas: {player.lives}", (20, 20), color=BLACK)
    screen.draw.text(f"Pontos: {player.score}", (20, 50), color=BLACK)
    
    # Mensagens de fim de jogo
    if game_over:
        screen.draw.text("GAME OVER!", (WIDTH//2 - 100, HEIGHT//2), color=RED, fontsize=60)
    elif game_won:
        screen.draw.text("VITÓRIA!", (WIDTH//2 - 80, HEIGHT//2), color=GREEN, fontsize=60)

def on_key_down(key):
    if key == keys.UP and not player.jumping:
        player.vy = -15
        player.jumping = True

pgzrun.go()
