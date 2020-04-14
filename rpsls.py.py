# -*- coding: UTF-8 -*-
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植产四班张顺杰
日期：2020年4月12日
"""
import random# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
number=random.randint(0,5)


def name_to_number(choice_name):# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	if choice_name=='石头':
		player_choice_number=0
	elif choice_name=='史波克':
		player_choice_number=1
	elif choice_name=='纸':
		player_choice_number=2
	elif choice_name=='蜥蜴':
		player_choice_number=3
	elif choice_name=='剪刀':
		player_choice_number=4
	else:
		print("Error:NO Correct Name")
	return player_choice_number
	
	
def number_to_name(comp_number):# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	if comp_number==0:# 使用if/elif/else语句将不同的整数对应到游戏的不同对象
		comp_name='石头'
	elif comp_number==1:
		comp_name='史波克'# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
	elif comp_number==2:
		comp_name='纸'
	elif comp_number==3:
		comp_name='蜥蜴'
	else:
		comp_name='剪刀'
	return comp_name
	
	
def rpsls(player_choice_number,comp_number):
	if (player_choice_number==0 and comp_number==4)or(player_choice_number==0 and comp_number==3)or(player_choice_number==1 and comp_number==4)or(player_choice_number==1 and comp_number==0)or(player_choice_number==2 and comp_number==0)or(player_choice_number==2 and comp_number==1)or(player_choice_number==3 and comp_number==1)or(player_choice_number==3 and comp_number==2)or(player_choice_number==4 and comp_number==2)or(player_choice_number==4 and comp_number==3):
		result=print("您赢了")
	elif player_choice_number==comp_number:# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
		result=print("您和计算机出的一样呢")
	else:
		print("机器赢了")
		
		
print("欢迎使用RPSLS游戏")# 对程序进行测试
print("----------------") # 输出"-------- "进行分割
print("请输入您的选择:")
player_choice_name = input() # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
player_choice_number = name_to_number(player_choice_name)
comp_number = random.randint(0,4)
comp_name = number_to_name(comp_number)
print("计算机的选择为：%s" %(comp_name))# 在屏幕上显示计算机选择的随机对象
result=rpsls(player_choice_number,comp_number)


