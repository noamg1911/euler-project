/*
@FileName: Summation of primes
@Author: N.G 29.3.21
@Purpose: Find the sum of all the primes below two million
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <Windows.h>

#define LIMIT (2000000)

bool is_prime(num)
{
	if (num <= 3)
	{
		return num > 1;
	}

	if ((num % 2 == 0) || (num % 3 == 0))
	{
		return false;
	}

	unsigned int i = 0;
	for (i = 5; i < sqrt(num) + 1; i += 6)
	{
		if ((num % i == 0) || (num % (i + 2) == 0))
		{
			return false;
		}
	}
	return true;
}

int main(void)
{
	double time = GetTickCount64();
	unsigned int i = 0;
	unsigned long long sum = 2;
	for (i = 3; i < LIMIT; i += 2)
	{
		if (is_prime(i))
		{
			sum += i;
		}
	}
	printf("%lld\n", sum);
	printf("%f", (GetTickCount64() - time) / 1000);
}
