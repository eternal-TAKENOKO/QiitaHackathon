// #include <stdio.h>
// #include <locale.h>
#include <wchar.h>

int	check_str(wchar_t *str)
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
