# Alien invasion game development instructions (development instructions in Windows)
## 1.Install pygame
      1. Check whether the PIP is installed after installing the python 3.6.3 environment
### $python -m PIP -version can see that the version information has been installed, and if you find no installation using python get-pip.py
      2. Install pygame module
### Python -m PIP install -user pygame
## 2.Start the game project
   1. Create the Pygame window and respond to user input
   2. Set the background color
   3. Create the Settings class
   4. Add ship images
   5. Create Ship class
   6. Draw a spaceship on the screen
   7. Refactor the previously scattered code and use two functions to encapsulate it
## 3. Three, flying a ship
   1. Response button
   2. Allow continuous movement
   3. Left and right movement
   4.Adjust the speed of the ship
   5. Limit the scope of the spacecraft's activities
   6. Use check_events() to refactor the previous code
## Summary:
   1. Alien_indom.py is the file of the game, creating a series of objects to be used throughout the game
   2. Settings. Py contains the Settings class, which initializes the properties of the game's appearance and speed of the ship
   3. Ship. Py contains the ship class, the method update() to manage the ship's location, and the main method of the ship,                   updat_screen() on screen.
## 4. Four, shooting
   1. Add bullet Settings
   2. Create Bullet
   3. Store the bullets in the marshalling
   4. Fire at 4.
   5. Remove the lost bullet
   6. Limit the number of bullets
   7. Create function updat_bullets()
   8. Create the function fire_bullet()
## 5. Alien objects
   1. Create the first Alien and create the Alien class
   Create an Alien instance
   3. Let the aliens appear on the screen
   4. Create a group of aliens
   5. Determine how many aliens can fit in a row
   6. Create multi-line aliens
   7. Create an alien crowd
   8. Refactor create_fleet()
   9. Add line
   10. Let the aliens move
   11. Move aliens to the right
   12. Create Settings that represent the direction of the alien movement
   13 Move the alien population down and change direction
   14. Shoot aliens and test the collision of bullets with aliens
   15. Create large bullets for testing
   16. Generate new alien populations
   17. Improving the speed of the bullet
   18. Reconfiguration updat_bullets()
   19. End the game
   20. Detect aliens and ship collisions
   21. Response to alien and ship collisions
   22. An alien reaches the bottom of the screen
   23. Game over
# 6. Add the scoring function
   Follow up to complete...

# 外星人入侵游戏开发说明（在windows系统中开发说明）
# 一、安装pygame
## 1.在安装好Python3.6.3环境后，检查pip是否安装 ##
###   $python -m pip --version  能看到版本信息说明已经安装,若发现没有安装使用python get-pip.py进行安装 ###
## 2.安装pygame模块 ##
###   python -m pip install --user pygame ###
# 二、开始游戏项目
##    1.创建Pygame窗口以及响应用户输入
##    2.设置背景色
##    3.创建设置类
##    4.添加飞船图像
##    5.创建Ship类
##    6.在屏幕上绘制飞船
##    7.重构前面分散的代码，使用两个函数进行封装
# 三、驾驶飞船
##    1.响应按键
##    2.允许不断移动
##    3.左右移动
##    4.调整飞船的速度
##    5.限制飞船的活动范围
##    6.使用check_events()进行前面代码的重构
# 小总结：
##    1.alien_invasion.py是游戏的文件，创建一系列整个游戏都要用到的对象
##    2.settings.py包含Settings类，初始化控制游戏外观和飞船速度的属性
##    3.ship.py包含Ship类，管理飞船位置的方法update()以及在屏幕上绘制飞船主方法updat_screen()
# 四、射击
##    1.添加子弹设置
##    2.创建Bullet类
##    3.将子弹存储到编组中
##    4.开火
##    5.删除已消失的子弹
##    6.限制子弹的数量
##    7.创建函数updat_bullets()
##    8.创建函数fire_bullet()
# 五、外星人对象
##    1.创建第一个外星人，创建Alien类
##    2.创建Alien实例
##    3.让外星人出现在屏幕上
##    4.创建一群外星人
##    5.确定一行可容纳多少个外星人
##    6.创建多行外星人
##    7.创建外星人群
##    8.重构create_fleet()
##    9.添加行
##    10.让外星人移动
##    11.向右移动外星人
##    12.创建表示外星人移动方向的设置
##    13.向下移动外星人群并改变移动方向
##    14.射杀外星人，检测子弹与外星人的碰撞
##    15.为测试创建大子弹
##    16.生成新的外星人群
##    17.提高子弹的速度
##    18.重构updat_bullets()
##    19.结束游戏
##    20.检测外星人和飞船碰撞
##    21.响应外星人和飞船碰撞
##    22.有外星人到达屏幕底端
##    23.游戏结束
# 六、添加记分功能
## 后续补充完成...
