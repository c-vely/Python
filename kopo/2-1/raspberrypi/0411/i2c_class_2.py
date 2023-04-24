import smbus
import math

class read_i2c:
    bus = None
    i2c_address = 0x48
    command = 0x44

    def __init__(self):
        self.bus = smbus.SMBus(1)

    def vr_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        VrValue = adc_data[1]
        VrValue = VrValue * 100 / 255
        VrValue = round(VrValue, 2)
        return VrValue
    
    def cds_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        CdsValue = adc_data[2]
        CdsValue = CdsValue * 100 / 255
        CdsValue = round(CdsValue, 2)
        return CdsValue
    
    def gas_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        GasValue = adc_data[3]
        return GasValue
    
    def psd_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        Psdvalue = (adc_data[4] / 255.0 * 3.3) * 3 / 2
        Psdvalue = 29.988 * math.pow(Psdvalue , -1.173)
        Psdvalue = round(Psdvalue, 2)
        return Psdvalue

class write_i2c:
    state = 0b00000000
    bus = None

    def __init__(self):
        self.bus = smbus.SMBus(1)
    def On(self, cmd):
        self.state = (self.state | cmd) 
        print(self.state)
        self.bus.write_byte(0x20, self.state) 
    def Off(self, cmd):
        self.state = (self.state & (~cmd)) 
        print(self.state)
        self.bus.write_byte(0x20, self.state)
