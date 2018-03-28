import sys
import pygame
from pygame.sprite import Group



from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 设置背景颜色
	#bg_color=(230,230,230)
	
	# 创建一艘飞船
	ship=Ship(ai_settings,screen)
	
	bullets=Group()
	
	# 创建一个外星人
	#alien=Alien(ai_settings,screen)
	aliens=Group()
	gf.create_fleet(ai_settings,screen,aliens)
	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		#for event in pygame.event.get():
		#	if event.type==pygame.QUIT:
		#		sys.exit()
		
		gf.check_events(ai_settings,screen,ship,bullets)
		# 每次循环时都重新绘制屏幕
		#screen.fill(ai_settings.bg_color)
		#ship.blitme()
		# 让最近绘制的屏幕可见
		#pygame.display.flip()
		ship.update()
		#bullets.update()
		#删除已消失的子弹
		#for bullet in bullets.copy():
		#	if bullet.rect.bottom<=0:
		#		bullets.remove(bullet)
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()