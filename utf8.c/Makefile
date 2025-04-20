CC?=gcc
.PHONY: clean

test: utf8.o test.o
	$(CC) -O3 -o test utf8.o test.o

utf8.o: utf8.c utf8.h
	$(CC) -O3 -c utf8.c

test.o: test.c utf8.h
	$(CC) -O3 -c test.c

clean:
	rm -f test *.o
