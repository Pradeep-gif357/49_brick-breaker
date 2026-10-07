import pygame
from .paddle import Paddle
from .ball import Ball
from .brick import Brick

WHITE = (255, 255, 255)
BG = (15, 15, 25)

BRICK_COLORS = [
    (200, 60, 60),
    (200, 140, 60),
    (200, 200, 60),
    (80, 180, 80),
    (80, 140, 200),
]


class GameEngine:
    def __init__(self, width, height, difficulty="Medium"):
        self.width = width
        self.height = height
        self.difficulty = difficulty

        # -----------------------------
        # TASK 3 - DIFFICULTY SETTINGS
        # -----------------------------

        if difficulty == "Easy":
            ball_speed = 3
            paddle_width = 120
            paddle_speed = 8

        elif difficulty == "Hard":
            ball_speed = 6
            paddle_width = 80
            paddle_speed = 6

        else:
            # Medium
            ball_speed = 4
            paddle_width = 100
            paddle_speed = 7

        self.ball_speed = ball_speed

        self.paddle = Paddle(
            width // 2 - paddle_width // 2,
            height - 30,
            paddle_width,
            14
        )

        self.paddle.speed = paddle_speed

        self.ball = Ball(
            width // 2,
            height - 50,
            radius=8
        )

        self.ball.vx = ball_speed
        self.ball.vy = -ball_speed

        self.rows = 5
        self.cols = 8

        self.bricks = self._build_bricks(
            self.rows,
            self.cols
        )

        self.lives = 3
        self.score = 0

        self.font = pygame.font.SysFont(
            "Arial",
            28
        )

        self.big_font = pygame.font.SysFont(
            "Arial",
            60,
            bold=True
        )

        self.small_font = pygame.font.SysFont(
            "Arial",
            24
        )

        self.game_over = False
        self.result = None

        # -----------------------------
        # TASK 4 - SOUND
        # -----------------------------

        self.sound_enabled = False

        try:
            pygame.mixer.init()

            self.brick_sound = self._create_sound(
                700,
                0.08
            )

            self.paddle_sound = self._create_sound(
                450,
                0.08
            )

            self.game_over_sound = self._create_sound(
                180,
                0.30
            )

            self.win_sound = self._create_sound(
                900,
                0.30
            )

            self.sound_enabled = True

        except pygame.error:
            # Game still works even if sound
            # cannot be initialized.
            self.sound_enabled = False

    def _create_sound(self, frequency, duration):
        """
        Create a simple sound at runtime.

        No external .wav files are required.
        """

        sample_rate = 44100
        samples = int(sample_rate * duration)

        buffer = bytearray()

        amplitude = 12000

        for i in range(samples):

            value = int(
                amplitude *
                (1 if (i * frequency // sample_rate) % 2 == 0 else -1)
            )

            value = max(
                -32768,
                min(32767, value)
            )

            buffer.extend(
                int(value).to_bytes(
                    2,
                    byteorder="little",
                    signed=True
                )
            )

        return pygame.mixer.Sound(
            buffer=bytes(buffer)
        )

    def _play_sound(self, sound):
        if self.sound_enabled:
            try:
                sound.play()
            except pygame.error:
                pass

    def _build_bricks(self, rows, cols):
        bricks = []

        margin = 30
        gap = 6
        top = 60

        brick_w = (
            self.width
            - margin * 2
            - gap * (cols - 1)
        ) // cols

        brick_h = 22

        for r in range(rows):
            for c in range(cols):

                x = margin + c * (
                    brick_w + gap
                )

                y = top + r * (
                    brick_h + gap
                )

                bricks.append(
                    Brick(
                        x,
                        y,
                        brick_w,
                        brick_h
                    )
                )

        return bricks

    def handle_event(self, event):
        # Main.py handles restarting and
        # difficulty selection.
        pass

    def handle_input(self):

        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            self.paddle.move(
                -self.paddle.speed,
                self.width
            )

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            self.paddle.move(
                self.paddle.speed,
                self.width
            )

    def update(self):

        if self.game_over:
            return

        # Save ball position before movement.
        old_ball_rect = self.ball.rect()

        # Move ball.
        self.ball.move()

        # New ball position.
        new_ball_rect = self.ball.rect()

        # -----------------------------
        # WALL COLLISION
        # -----------------------------

        if (
            self.ball.x - self.ball.radius <= 0
            or
            self.ball.x + self.ball.radius >= self.width
        ):

            self.ball.vx *= -1

            # TASK 4
            self._play_sound(
                self.paddle_sound
            )

        if self.ball.y - self.ball.radius <= 0:

            self.ball.vy *= -1

            # TASK 4
            self._play_sound(
                self.paddle_sound
            )

        # -----------------------------
        # PADDLE COLLISION
        # -----------------------------

        if self.ball.rect().colliderect(
            self.paddle.rect()
        ):

            # Make sure the ball goes upward.
            self.ball.vy = -abs(
                self.ball.vy
            )

            # Change horizontal direction
            # depending on where the ball hits.
            paddle_center = (
                self.paddle.x +
                self.paddle.width / 2
            )

            distance_from_center = (
                self.ball.x -
                paddle_center
            )

            self.ball.vx = (
                distance_from_center /
                (self.paddle.width / 2)
            ) * self.ball_speed

            # Prevent zero horizontal movement.
            if abs(self.ball.vx) < 1:
                self.ball.vx = (
                    1 if self.ball.vx >= 0
                    else -1
                )

            # TASK 4
            self._play_sound(
                self.paddle_sound
            )

        # -----------------------------
        # BRICK COLLISION
        # TASK 1
        # -----------------------------

        for brick in self.bricks:

            if (
                brick.alive
                and
                new_ball_rect.colliderect(
                    brick.rect()
                )
            ):

                brick_rect = brick.rect()

                # Destroy brick.
                brick.alive = False

                # Increase score.
                self.score += 1

                # Ball hit LEFT side.
                if old_ball_rect.right <= brick_rect.left:

                    self.ball.vx *= -1

                # Ball hit RIGHT side.
                elif old_ball_rect.left >= brick_rect.right:

                    self.ball.vx *= -1

                # Ball hit TOP.
                elif old_ball_rect.bottom <= brick_rect.top:

                    self.ball.vy *= -1

                # Ball hit BOTTOM.
                elif old_ball_rect.top >= brick_rect.bottom:

                    self.ball.vy *= -1

                # Corner collision.
                else:

                    if abs(self.ball.vx) > abs(self.ball.vy):
                        self.ball.vx *= -1
                    else:
                        self.ball.vy *= -1

                # TASK 4
                self._play_sound(
                    self.brick_sound
                )

                break

        # -----------------------------
        # BALL FALLS BELOW SCREEN
        # -----------------------------

        if self.ball.y - self.ball.radius > self.height:

            self.lives -= 1

            if self.lives <= 0:

                self.game_over = True
                self.result = "lose"

                # TASK 4
                self._play_sound(
                    self.game_over_sound
                )

            else:

                self._reset_ball()

        # -----------------------------
        # WIN CONDITION
        # -----------------------------

        if all(
            not brick.alive
            for brick in self.bricks
        ):

            self.game_over = True
            self.result = "win"

            # TASK 4
            self._play_sound(
                self.win_sound
            )

    def _reset_ball(self):

        self.ball.x = self.width // 2
        self.ball.y = self.height - 50

        self.ball.vx = self.ball_speed
        self.ball.vy = -self.ball_speed

    def render(self, screen):

        screen.fill(BG)

        # -----------------------------
        # PADDLE
        # -----------------------------

        pygame.draw.rect(
            screen,
            WHITE,
            self.paddle.rect()
        )

        # -----------------------------
        # BALL
        # -----------------------------

        pygame.draw.circle(
            screen,
            WHITE,
            (
                int(self.ball.x),
                int(self.ball.y)
            ),
            self.ball.radius
        )

        # -----------------------------
        # BRICKS
        # -----------------------------

        for i, brick in enumerate(
            self.bricks
        ):

            if brick.alive:

                row = i // self.cols

                color = BRICK_COLORS[
                    row % len(BRICK_COLORS)
                ]

                pygame.draw.rect(
                    screen,
                    color,
                    brick.rect()
                )

        # -----------------------------
        # SCORE
        # -----------------------------

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (10, 10)
        )

        # -----------------------------
        # LIVES
        # -----------------------------

        lives_text = self.font.render(
            f"Lives: {self.lives}",
            True,
            WHITE
        )

        screen.blit(
            lives_text,
            (
                self.width - 130,
                10
            )
        )

        # -----------------------------
        # DIFFICULTY
        # -----------------------------

        difficulty_text = self.small_font.render(
            f"Difficulty: {self.difficulty}",
            True,
            WHITE
        )

        screen.blit(
            difficulty_text,
            (
                10,
                self.height - 30
            )
        )

        # -----------------------------
        # GAME OVER / WIN SCREEN
        # TASK 2
        # -----------------------------

        if self.game_over:

            overlay = pygame.Surface(
                (self.width, self.height)
            )

            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))

            screen.blit(
                overlay,
                (0, 0)
            )

            if self.result == "win":

                result_text = self.big_font.render(
                    "YOU WIN!",
                    True,
                    WHITE
                )

            else:

                result_text = self.big_font.render(
                    "GAME OVER",
                    True,
                    WHITE
                )

            result_rect = result_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 - 80
                )
            )

            screen.blit(
                result_text,
                result_rect
            )

            final_score_text = self.font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            final_score_rect = final_score_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2
                )
            )

            screen.blit(
                final_score_text,
                final_score_rect
            )

            instruction_text = self.small_font.render(
                "Press ENTER or SPACE",
                True,
                WHITE
            )

            instruction_rect = instruction_text.get_rect(
                center=(
                    self.width // 2,
                    self.height // 2 + 55
                )
            )

            screen.blit(
                instruction_text,
                instruction_rect
            )