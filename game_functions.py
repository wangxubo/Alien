import sys,pygame
from time import sleep
from pygame.locals import *
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''响应按键'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		

def check_keyup_events(event,ship):
	'''松开按键'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left= False

def check_events(ai_settings,screen,ship,bullets):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# check_keydown_events(event,ship)
				check_keydown_events(event,ai_settings,screen,ship,bullets)
				# if event.key == pygame.K_RIGHT:
				# 	#在玩家按下右箭头键时响应的方式，不直接调整飞船的位置，而只是将moving_right设置为True
				# 	ship.moving_right = True
				#玩家松开右箭头键K_PIGHT时，将moving_right设置为False
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				# if event.key == pygame.K_RIGHT:
				# 	ship.moveing_right = False

def update_screen(ai_settings,screen,ship,aliens,bullets):
	'''更新屏幕上的图像，并切换到新屏幕'''
	#用ai_settings实例的bg_color背景填充屏幕
	screen.fill(ai_settings.bg_color)
	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#调用ship.blitme()将飞船绘制到屏幕上，确定它出现在背景前面
	ship.blitme()
	#在屏幕上绘制编组中的每个外星人
	aliens.draw(screen)
	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	'''更新子弹的位置，并删除已消失的子弹'''
	#更新子弹位置
	bullets.update()
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	"""响应子弹和外星人的碰撞"""
	# 删除发生碰撞的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) == 0:  #检查编组aliens是否为空
		#删除现有的子弹并新建一群外星人
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
	'''如果还没有到达限制，就发射一颗子弹'''
	#创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def get_number_aliens_x(ai_settings,alien_width):
	'''计算每行可容纳多少个外星人'''
	available_space_x = ai_settings.screen_width -2 * alien_width
	number_aliens_x = int(available_space_x /(2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	'''创建一个外星人并将其放在当前行'''
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x=alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	'''创建外星人群'''
	#创建一个外星人，并计算一行可容纳多少个外星人
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	#创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
	'''计算屏幕可容纳多少行外星人'''
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def check_fleet_edges(ai_settings,aliens):
	'''有外星人到达边缘时采取相应的措施'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	'''将整群外星人下移，并改变它们的方向'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	'''响应被外星人撞到的飞船'''
	if stats.ships_left > 0:
		#将ships_left减1
		stats.ships_left -= 1

		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群外星人，并将飞船放到屏幕底端中央
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		#暂停0.5秒
		sleep(0.5)
	else:
		stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	'''检查是否有外星人到达了屏幕底端'''
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#像飞船被撞到一样进行处理
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	'''检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置'''
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	#检查外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
		print("Ship hit!!!")
	#检测外星人是否有到达屏幕底端
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

