import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ respond to keypresses and mouse events """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        button_clicked = pygame.K_p
        if button_clicked and not stats.game_active:
            start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
def check_keyup_events(event, ship):
    """ respond to keypresses and mouse events """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ respond to keypresses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, sb, ship, alien, bullets, play_button):
    """ update images on the screen and flip to the new screen"""
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    
    # draw the score information
    sb.show_score()

    # draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ update position of bullets and get rid of old ones """
    # update bullet positions
    bullets.update()

    # get rid of bullets when they disappear
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)    

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ respond to bullet-alien collisions """
    # remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        
    if len(aliens) == 0:
        # if the entire fleet is destroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()

        # increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """ fire a bullet if the limit is not reached"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        gunshot()

def get_number_aliens_x(ai_settings, alien_width):
    """ determine the number of aliens that fit in a row """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """ determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ create an alien and place it in the row """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """ create a fleet of aliens"""
    # create and alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """ respond appropriately if any aliens have reached an edge """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ drop the entire fleet and change the fleet's direction """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ check if the fleet is at an edge, and then update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,screen, stats, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ respond to ship being hit by alien """
    if stats.ships_left > 0:
        crash()
        # decrement ships_left
        stats.ships_left -= 1

        # update scoreboard
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(1.0) 

        # start music after first life is over
        # intro_music()

    else:
        crash()
        stats.game_active = False
        pygame.mouse.set_visible(True)
        save_high_score(stats.score)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            crash()
            # treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ start a new game when the player clicks Play """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # reset the game settings
    ai_settings.initialize_dynamic_settings()
    # hide the mouse cursor
    pygame.mouse.set_visible(False)
    # reset the game statistics
    stats.reset_stats()
    stats.game_active = True

    # reset the scoreboard images
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # empty the list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # create new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_high_score(stats, sb):
    """ check to see if there's a new high score """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        
def get_high_score():
    with open('/Users/spacetrav/Documents/Files/Python/alien_invasion/high_score.txt') as file_object:
        load_high_score = file_object.read()

    return int(load_high_score)

def save_high_score(score):
    with open('/Users/spacetrav/Documents/Files/Python/alien_invasion/high_score.txt', 'w') as file_object:
        file_object.write(str(score))

def intro_music():
    pygame.mixer.music.load('/Users/spacetrav/Documents/Files/Python/alien_invasion/sounds/DK_2.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

def game_music():
    pygame.mixer.music.load('/Users/spacetrav/Documents/Files/Python/alien_invasion/sounds/DK.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

def gunshot():
    shot_sound = pygame.mixer.Sound('/Users/spacetrav/Documents/Files/Python/alien_invasion/sounds/laser.wav')
    pygame.mixer.Sound.play(shot_sound)
    # pygame.mixer.Sound allows us to fire bullets while keeping the background music, but I cannot
    # figure out how to control the volume

def crash():
    crash_sound = pygame.mixer.Sound('/Users/spacetrav/Documents/Files/Python/alien_invasion/sounds/Explosion.wav')
    pygame.mixer.Sound.play(crash_sound)
    