# encoding: utf-8
'''
Created on 2018年8月25日

@author: Administrator
'''
class Settings(object):
    """store all settings"""
    def __init__(self):
        
        # screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_factor = 1.5
        
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowd = 3