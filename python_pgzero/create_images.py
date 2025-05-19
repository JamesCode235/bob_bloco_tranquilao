from PIL import Image, ImageDraw

# Criar imagem do jogador (quadrado azul)
player = Image.new('RGB', (50, 50), 'white')
draw = ImageDraw.Draw(player)
draw.rectangle([(0, 0), (49, 49)], fill='blue')
player.save('images/player.png')

# Criar imagem do obstáculo (quadrado vermelho)
obstacle = Image.new('RGB', (40, 40), 'white')
draw = ImageDraw.Draw(obstacle)
draw.rectangle([(0, 0), (39, 39)], fill='red')
obstacle.save('images/obstacle.png')

# Criar imagem do coletável (círculo verde)
collectible = Image.new('RGB', (30, 30), 'white')
draw = ImageDraw.Draw(collectible)
draw.ellipse([(0, 0), (29, 29)], fill='green')
collectible.save('images/collectible.png') 