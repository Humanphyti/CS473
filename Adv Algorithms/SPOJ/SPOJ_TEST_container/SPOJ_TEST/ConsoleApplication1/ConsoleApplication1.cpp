#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

int main() {
	
	int num = 0;
	while (scanf("%d\n", &num) > 0 && num != 42) {
		printf("%d\n", num);
	}
	return 0;
}