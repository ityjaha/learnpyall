import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_RIGHT:
		#向右移动飞船
		#ship.rect.centerx+=1
		ship.moving_right=True
	if event.key==pygame.K_LEFT:
		#向左移动飞船
		#ship.rect.centerx-=1
		ship.moving_left=True
	if event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	if event.key==pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	if event.key==pygame.K_LEFT:
		ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets):
	"""相应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	#alien.blitme()
	aliens.draw(screen)
	pygame.display.flip()


def update_bullets(bullets):
	"""更新子弹的位置，并删除消失的子弹"""
	#更新子弹的位置
	bullets.update()
	
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	
	
def fire_bullet(ai_settings,screen,ship,bullets):
	#创建一颗子弹，并将其加入到编组bullets中
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)	
	
	
def create_fleet(ai_settings,screen,aliens):
		alien = Alien(ai_settings,screen)
		alien_width=alien.rect.width
		available_space_x=ai_settings.screen_width-2*alien_width
		number_aliens_x=int(available_space_x/(2*alien_width))
		
		#创建第一行外星人
		for alien_number  in range(number_aliens_x):
			#创建一个外星人并将其加入当前行
			alien=Alien(ai_settings,screen)
			alien.x=alien_width+2*alien_width*alien_number
			alien.rect.x=alien.x
			aliens.add(alien)
	
	
	
	
	
	
	