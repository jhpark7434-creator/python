import pygame
import random
import sys

pygame.init()

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (255, 0, 255),  # 자주
    (0, 255, 255),  # 청록
    (255, 165, 0),  # 주황
]

# 테트로미노 모양
SHAPES = [
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1, 1]],    # I
    [[1, 0], [1, 1], [0, 1]],  # Z
    [[0, 1], [1, 1], [1, 0]],  # S
    [[1, 0, 0], [1, 1, 1]],    # L
    [[0, 0, 1], [1, 1, 1]],    # J
    [[0, 1, 0], [1, 1, 1]],    # T
]

class Tetromino:
    def __init__(self, shape):
        self.shape = [row[:] for row in shape]
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def get_blocks(self):
        blocks = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    blocks.append((self.x + x, self.y + y))
        return blocks

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("테트리스")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino(random.choice(SHAPES))
        self.score = 0
        self.level = 1
        self.fall_speed = 1

    def check_collision(self, piece, offset_x=0, offset_y=0):
        for x, y in piece.get_blocks():
            new_x, new_y = x + offset_x, y + offset_y
            if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                return True
            if new_y >= 0 and self.grid[new_y][new_x]:
                return True
        return False

    def place_piece(self):
        for x, y in self.current_piece.get_blocks():
            if 0 <= y < GRID_HEIGHT:
                self.grid[y][x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = Tetromino(random.choice(SHAPES))
        if self.check_collision(self.current_piece):
            return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * GRID_WIDTH)
                lines_cleared += 1
            else:
                y -= 1
        
        if lines_cleared:
            self.score += lines_cleared * 100
            self.level = 1 + self.score // 500
            self.fall_speed = 1 + self.level * 0.2

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not self.check_collision(self.current_piece, -1, 0):
                        self.current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    if not self.check_collision(self.current_piece, 1, 0):
                        self.current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    if not self.check_collision(self.current_piece, 0, 1):
                        self.current_piece.y += 1
                if event.key == pygame.K_SPACE:
                    self.current_piece.rotate()
                    if self.check_collision(self.current_piece):
                        self.current_piece.rotate()
        return True

    def update(self):
        if not self.check_collision(self.current_piece, 0, 1):
            self.current_piece.y += 1
        else:
            return self.place_piece()
        return True

    def draw(self):
        self.screen.fill(BLACK)
        
        # 그리드 그리기
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect, 1)
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x], rect)

        # 현재 피스 그리기
        for x, y in self.current_piece.get_blocks():
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, self.current_piece.color, rect)

        # 점수 표시 (텍스트)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        running = True
        fall_counter = 0
        
        while running:
            running = self.handle_input()
            
            fall_counter += 1
            if fall_counter >= int(10 - self.fall_speed):
                fall_counter = 0
                running = self.update()
            
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()