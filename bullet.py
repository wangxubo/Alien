import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''一个对飞船发射的子弹进行管理的类'''
	def __init__(self,ai_settings,screen,ship):
		'''在飞船所处的位置创建一个子弹对象'''
		super(Bullet,self).__init__()
		self.screen = screen

		#在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
		#设置子弹的属性rect,使用pygame.Rect()类从空白开始创建一个矩形，在创建这个类的实例时必须提供矩形左上角
		#的x坐标和y坐标，还有矩形的宽度和高度
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		#将子弹的centerx设置为飞船的rect.centerx
		self.rect.centerx = ship.rect.centerx
		#因为应子弹从飞船顶部射出，将子弹的rect的top属性设置为飞船的rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数表示的子弹位置,方便微调子弹的速度
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	#定义update()方法管理子弹的位置
	def update(self):
		'''向上移动子弹'''
		#更新表示子弹位置的小数值
		self.y -= self.speed_factor
		#更新表示子弹的rect的位置
		self.rect.y = self.y

	def draw_bullet(self):
		'''在屏幕上绘制子弹'''
		pygame.draw.rect(self.screen,self.color,self.rect)