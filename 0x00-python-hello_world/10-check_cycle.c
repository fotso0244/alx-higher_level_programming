#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;
	int res = 0;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			res = 1;
			break;
		}
	}
	return (res);
}
