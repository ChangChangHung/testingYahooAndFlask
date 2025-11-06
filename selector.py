# selector.py
import pygame
import datetime
import sys

def select_date(title="Select Date"):
    pygame.init()

    WIDTH, HEIGHT = 500, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)

    FONT = pygame.font.SysFont(None, 48)
    SMALL_FONT = pygame.font.SysFont(None, 28)
    WHITE = (255, 255, 255)
    GRAY = (180, 180, 180)
    BLACK = (0, 0, 0)
    BLUE = (100, 150, 255)

    date = datetime.date.today()
    selected_field = 0  # 0=year, 1=month, 2=day

    def draw_text_center(text, font, color, center):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=center)
        screen.blit(surf, rect)
        return rect

    def adjust_date(field, delta):
        nonlocal date
        try:
            if field == 0:
                date = date.replace(year=date.year + delta)
            elif field == 1:
                new_month = (date.month - 1 + delta) % 12 + 1
                year_change = (date.month - 1 + delta) // 12
                date = date.replace(year=date.year + year_change, month=new_month)
            elif field == 2:
                date += datetime.timedelta(days=delta)
        except ValueError:
            pass

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        draw_text_center(title, SMALL_FONT, BLACK, (WIDTH // 2, 40))

        y_center = HEIGHT // 2
        spacing = 150
        fields = [str(date.year), str(date.month).zfill(2), str(date.day).zfill(2)]
        labels = ["Year", "Month", "Day"]

        for i, field in enumerate(fields):
            x_center = WIDTH // 2 - spacing + i * spacing
            color = BLUE if i == selected_field else BLACK
            draw_text_center(field, FONT, color, (x_center, y_center))
            draw_text_center("▲", SMALL_FONT, GRAY, (x_center, y_center - 50))
            draw_text_center("▼", SMALL_FONT, GRAY, (x_center, y_center + 50))
            draw_text_center(labels[i], SMALL_FONT, BLACK, (x_center, y_center + 90))

        draw_text_center("Press ENTER to Confirm", SMALL_FONT, BLACK, (WIDTH // 2, HEIGHT - 40))
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_field = (selected_field + 1) % 3
                elif event.key == pygame.K_LEFT:
                    selected_field = (selected_field - 1) % 3
                elif event.key == pygame.K_UP:
                    adjust_date(selected_field, 1)
                elif event.key == pygame.K_DOWN:
                    adjust_date(selected_field, -1)
                elif event.key == pygame.K_RETURN:
                    pygame.quit()
                    return date
                elif event.key == pygame.K_KP_ENTER:
                    pygame.quit()
                    return date

        clock.tick(30)