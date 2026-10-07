import pygame
from game.game_engine import GameEngine


# ---------------------------------
# INITIALIZE PYGAME
# ---------------------------------

pygame.init()

try:
    pygame.mixer.init()
except pygame.error:
    pass


# ---------------------------------
# SCREEN SETTINGS
# ---------------------------------

WIDTH = 640
HEIGHT = 560

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Brick Breaker Game"
)

clock = pygame.time.Clock()


# ---------------------------------
# FONTS
# ---------------------------------

title_font = pygame.font.SysFont(
    "Arial",
    50,
    bold=True
)

font = pygame.font.SysFont(
    "Arial",
    30
)

small_font = pygame.font.SysFont(
    "Arial",
    22
)


# ---------------------------------
# DIFFICULTY MENU
# TASK 3
# ---------------------------------

def difficulty_menu():

    while True:

        screen.fill(
            (15, 15, 25)
        )

        title = title_font.render(
            "BRICK BREAKER",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 100)
        )

        screen.blit(
            title,
            title_rect
        )

        easy = font.render(
            "1 - Easy",
            True,
            (255, 255, 255)
        )

        medium = font.render(
            "2 - Medium",
            True,
            (255, 255, 255)
        )

        hard = font.render(
            "3 - Hard",
            True,
            (255, 255, 255)
        )

        exit_text = font.render(
            "Q - Exit",
            True,
            (255, 255, 255)
        )

        screen.blit(
            easy,
            (WIDTH // 2 - 80, 190)
        )

        screen.blit(
            medium,
            (WIDTH // 2 - 80, 240)
        )

        screen.blit(
            hard,
            (WIDTH // 2 - 80, 290)
        )

        screen.blit(
            exit_text,
            (WIDTH // 2 - 80, 340)
        )

        instruction = small_font.render(
            "Choose a difficulty",
            True,
            (255, 255, 255)
        )

        instruction_rect = instruction.get_rect(
            center=(WIDTH // 2, 420)
        )

        screen.blit(
            instruction,
            instruction_rect
        )

        pygame.display.flip()

        # -----------------------------
        # MENU INPUT
        # -----------------------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    return "Easy"

                if event.key == pygame.K_2:
                    return "Medium"

                if event.key == pygame.K_3:
                    return "Hard"

                if event.key == pygame.K_q:
                    return None

        clock.tick(60)


# ---------------------------------
# GAME LOOP
# ---------------------------------

def run_game(difficulty):

    game = GameEngine(
        WIDTH,
        HEIGHT,
        difficulty
    )

    running = True

    while running:

        # -----------------------------
        # EVENTS
        # -----------------------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                # After game ends
                if game.game_over:

                    if (
                        event.key == pygame.K_RETURN
                        or
                        event.key == pygame.K_SPACE
                    ):
                        return True

                    if event.key == pygame.K_ESCAPE:
                        return False

        # -----------------------------
        # GAME INPUT
        # -----------------------------

        game.handle_input()

        # -----------------------------
        # UPDATE
        # -----------------------------

        game.update()

        # -----------------------------
        # DRAW
        # -----------------------------

        game.render(screen)

        pygame.display.flip()

        clock.tick(60)

    return False


# ---------------------------------
# MAIN PROGRAM
# ---------------------------------

while True:

    # Show difficulty menu.
    difficulty = difficulty_menu()

    # User selected Q or closed window.
    if difficulty is None:
        break

    # Start game.
    play_again = run_game(
        difficulty
    )

    # If False, exit the program.
    if not play_again:
        break


# ---------------------------------
# QUIT
# ---------------------------------

pygame.quit()