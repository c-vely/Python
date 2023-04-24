#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int main(void) {
    int fd;
    int prev, a2dVal[4];
    float a2dVol;
    float Vref = 5.0;

    printf("[ADC/DAC Module testing........]\n");
    
    if ((fd = wiringPiI2CSetup(0x48)) < 0) {
        printf("wiringPiI2CSetup failed:\n");
    }

    while (1) {
        wiringPiI2CWrite(fd,0x44); 
        prev = wiringPiI2CRead(fd); // Previously byte, garvage
        for (int i = 0; i<4 ; i++) a2dVal[i] = wiringPiI2CRead(fd);
        a2dVol = a2dVal[0] * 100.0 / 255;  # <-- 여기만 바껴짐
        printf("VAR = %3.0f %\n", a2dVol);
        delay(500); 
    }
}
