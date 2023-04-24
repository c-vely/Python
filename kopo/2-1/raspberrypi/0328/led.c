#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int main(void) {
    int ret,fd;
    char red_led = 0x01;
    char green_led = 0x02;
    char blue_led = 0x04;
    char state = red_led | green_led | blue_led;

    if (wiringPiSetup() == -1) {
    fprintf(stderr, "wiringPiSetup() is failed : %s\n", strerror(errno));
    return 1;
    }

    fd = wiringPiI2CSetup(0x20);
    if (fd == -1) {
    fprintf(stderr, "wiringPiI2CSetup() is failed : %s\n", strerror(errno));
    return 1;
    }

    if (wiringPiI2CWriteReg8(fd, 0x20, 0) == -1) {
    printf("write failed...\n");
    }
    delay(1000);

    if (wiringPiI2CWriteReg8(fd, 0x20, state) == -1) {
    printf("write failed...\n");
    }

    // write cycle time
    delay(5);
    
    return 0;
}
