#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	int res = 0;

	while (curr != NULL)
	{
		if (curr->next != list)
			curr = curr->next;
		else
		{
			res = 1;
			break;
		}
	}
	return (res);
}
