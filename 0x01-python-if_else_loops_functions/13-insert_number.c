#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - insert a new node
 * @head: a linked list
 * @number: a new number
 *
 * Return: a linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *curr, *new;

        curr = *head;
	new = malloc(sizeof(*new));
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
        while (curr != NULL)
        {
                if (curr->n <= number && curr->next->n >= number)
                {
                        new->next = curr->next;
                        curr->next = new;
                        new = NULL;
                        curr = NULL;
                        break;
                }
                else
			if (curr->n >= number)
			{
				new->next = curr;
				*head = new;
				curr = NULL;
				new = NULL;
				break;
			}
			else
                        	curr = curr->next;
		if (curr->next == NULL)
		{
			new->next = NULL;
			curr->next = new;
			curr = NULL;
		}
        }
        return (*head);
}
