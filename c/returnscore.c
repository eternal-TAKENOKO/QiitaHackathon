// #include <stdio.h>

long	return_score(long num_ans)
{
	long	score = 0;

	score = num_ans + num_ans / 5;
	return (score);
}

// int	main(void)
// {
// 	printf("%ld\n", return_score(-1));
// 	printf("%ld\n", return_score(0));
// 	printf("%ld\n", return_score(1));
// 	printf("%ld\n", return_score(2));
// 	printf("%ld\n", return_score(5));
// 	printf("%ld\n", return_score(1000));
// 	printf("%ld\n", return_score(2147483647));
// 	return (0);
// }