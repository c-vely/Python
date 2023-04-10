#=======================================
# Makefile
#=======================================
CC = gcc # for raspberrypi
#CC = arm-linux-gnueabihf-gcc # for virtual machine
CFLAGS = -c
LDFLAGS = -lwiringPi
LDLIBS = 

%: %.c
	$(CC) -o $@ $< $(LDFLAGS)
default:
	@echo "Type \"make filename without .c\" to compile..."
clean:
	rm -f *.o
