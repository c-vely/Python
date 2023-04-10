#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

#define RELAY_1 0x10
#define RELAY_2 0x20

char state = 0x0;
int fd;


void relay_init() {

	if (wiringPiI2CWriteReg8(fd, 0x20, 0) == -1) {
		printf("write failed...\n");
	}
	else printf("relay_init OK \n");

}

void relayOn(char cmd) {

	state = state | cmd;

	if (wiringPiI2CWriteReg8(fd, 0x20, state) == -1) {
		printf("relay On failed...\n");
	}
	else printf("relay_on OK[%x] \n", state);
}
void relayOff(char cmd) {

	state = state & ~cmd;

	if (wiringPiI2CWriteReg8(fd, 0x20, state) == -1) {
		printf("relay On failed...\n");
	}
	else printf("relay_off OK[%x] \n", state);



}
int main(void) {

	if (wiringPiSetup() == -1) {
		fprintf(stderr, "wiringPiSetup() is failed : %s\n", strerror(errno));
		return 1;
	}

	fd = wiringPiI2CSetup(0x20);
	if (fd == -1) {
		fprintf(stderr, "wiringPiI2CSetup() is failed : %s\n", strerror(errno));
		return 1;
	}

	relay_init();

	delay(500);
	relayOn(RELAY_1);
	delay(500);
	relayOff(RELAY_1);
	delay(500);

	relayOn(RELAY_2);
	delay(500);
	relayOff(RELAY_2);
	delay(500);


	relayOn(RELAY_1 | RELAY_2);
	delay(500);
	relayOff(RELAY_1 | RELAY_2);
	delay(500);



	// write cycle time
	delay(5);

	return 0;
}
