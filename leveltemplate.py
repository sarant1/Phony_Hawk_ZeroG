if self.state == 'levelX':
    time = 0
    while self.state == 'levelX':
        time += 1
        print(time)
        clock.tick(FPS)
        rolling_screen(scroll)
        scroll -= 1
        if abs(scroll) > bg.get_width():
            scroll = 0

        p.draw(screen)
        p.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.quit()

        pygame.display.update()
        pygame.display.flip()