#include <iostream>

int main()
{
	int number_of_sundays = 0;
	bool leapYear = false;
	int first_day = 0; // Monday
	int month = 0; // January
	int year = 1900;
	int DayIncrementer = 0;
	int MonthIncrementer = 0;

	while (year != 2001)
	{
		if (year % 400 == 0) leapYear = true;

		if (/*April*/(month == 3) || /*june*/(month == 5) || /*Sep*/(month == 7) ||/*nov*/ (month == 10))
		{
			//Months with 30 days
			first_day += 3;
		}
		else if (month == 1)
		{
			if (leapYear)
			{
				first_day += 2;
				leapYear = false;
			}
			else first_day += 1;
		}
		else
		{
			//Months with 31 days
			first_day += 4;
			if (month == 11) year += 1;
		}

		first_day = (first_day % 7);

		month++;
		month = (month % 12);

		if (first_day == 6)
			number_of_sundays += 1;

	}

	printf("The number of sundays is: %d", number_of_sundays);

	return 0;
}