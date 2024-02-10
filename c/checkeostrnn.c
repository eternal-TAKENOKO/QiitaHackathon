// #include <stdio.h>
// #include <locale.h>
#include <wchar.h>

int	check_eostr_nn(wchar_t *str)
{
	long	i;

	i = 0;
	while (str[i] != L'\0')
		i++;
	if (str[i - 1] == L'ん')
		return (1);
	else
		return (0);
}

// int	main(void)
// {
// 	setlocale(LC_ALL, "en_US.UTF-8");

// 	wchar_t	string[] = L"たけのこ";

// 	printf("%d\n", check_eostr_nn(string));
// 	return (0);
// }