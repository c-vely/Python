# LED가 shift되면서 켜짐 

from i2c_class import read_i2c
from i2c_class import write_i2c
import I2C_LCD_driver
import time

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100
RELAY_1 = 0b00010000
RELAY_2 = 0b00100000

textLcd = I2C_LCD_driver.lcd()
textLcd.lcd_display_string("KOPO AISW", 1)
textLcd.lcd_display_string("I2C_BUS TEST", 2)

adc = read_i2c()
write = write_i2c()

print("VR:"+str(adc.vr_read()) +" %")
print("CdS:"+str(adc.cds_read()) + " %")
print("GAS:"+str(adc.gas_read())+ " GAS")
print("Distance:"+str(adc.psd_read())+ " cm")
textLcd.lcd_display_string(str(adc.vr_read())+" %" + str(adc.cds_read()) + " %", 2)


write.On(RELAY_1 | RELAY_2)
time.sleep(0.5)
write.Off(RELAY_1 | RELAY_2)
time.sleep(0.5)

state = RED_LED

try:
    while(1):
        write.On(state)
        textLcd.lcd_display_string("KOPO AISW", 1)
        textLcd.lcd_display_string("VR:"+str(adc.vr_read())+"%" + "CDS:"+str(adc.cds_read()) + "%", 2)
        time.sleep(1)
        write.Off(state)
        state = state << 1
        if state == 0x08:
            state = RED_LED
        textLcd.lcd_clear()
        textLcd.lcd_display_string("KOPO AISW", 1)
        textLcd.lcd_display_string("GAS:"+str(adc.gas_read())+"%" + "DIS:"+str(adc.psd_read()) + "%", 2)
        time.sleep(1)
        textLcd.lcd_clear()
except KeyboardInterrupt:
    pass
