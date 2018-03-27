import sys
import pygame
from bullet import Bullet

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
		#创建一颗子弹，并将其加入到编组bullets中
		if len(bullets)<ai_settings.bullets_allowed:
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)

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

def update_screen(ai_settings,screen,ship,bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	pygame.display.flip()