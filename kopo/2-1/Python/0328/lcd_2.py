import I2C_LCD_driver

# I2C_LCD_Driver 모듈을 사용하는 예제
textLcd = I2C_LCD_driver.lcd()

# 16자 이내 아스키코드, 1은 첫 번째 줄이고 2는 두 번째 줄이다
textLcd.lcd_display_string("ABCDEFG", 1, 2)
textLcd.lcd_display_string("123456", 2, 6)
