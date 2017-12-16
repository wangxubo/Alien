'''创建一个空的窗口，并响应用户输入'''
import pygame
from pygame.sprite import Group
from setting import Settings  #导入Settings类
from game_stats import GameStats  #导入记分类
from ship import Ship   #导入飞船ship类
from alien import Alien

import game_functions as gf
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	#创建一个Settings类的实例，并将其存储在变量ai_settings中
	ai_settings=Settings()
	#用上面的实例属性来创建屏幕
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#设置窗口的标题
	pygame.display.set_caption("Alien Invasion")
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一组用于存储子弹的编组
	bullets = Group()
	#创建一个外星人编组
	aliens=Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#设置背景色
	# bg_color = (230,230,230)
	#开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		

run_game()