#include "lists.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * Reverse_list - reverses a linked list
 * @curr: current
 * @prev: previous
 * @head: a list
 */
void Reverse_list(listint_t *curr, listint_t *prev, listint_t **head)
{
	listint_t *next;
	if (!curr->next)
	{
		*head = curr;
		curr->next = prev;
		return;
	}
	next = curr->next;
	curr->next = prev;
	Reverse_list(next, curr, head);
}
/**
 * @head: a linked list
 */
void ReverseLL(listint_t **head)
{
	if (!head)
		return;
	Reverse_list(*head, NULL, head);
}
/**
 * length - computes length of a linked list
 * @head: a list
 *
 * Return: length of a list
 */
int length(listint_t **head)
{
	int i = 0;
	listint_t *curr = *head;

	while (curr != NULL)
	{
		i++;
		curr = curr->next;
	}
	return (i);
}
/**
 * is_palindrome - checks a palindrome list
 * @head: a list
 *
 *Return: an int
 */
int is_palindrome(listint_t **head)
{
	int res = 1, i, *str1, *str2;
	listint_t *curr1 = *head, *curr2;

	str1 = malloc(sizeof(*str1) * length(head));
	for  (i = 0; i <= length(head) - 1; i++)
	{
		str1[i] = curr1->n;
		curr1 = curr1->next;
	}
	ReverseLL(head);
	str2 = malloc(sizeof(*str2) * length(head));
	curr2 = *head;
	for (i = 0; i <= length(head) - 1; i++)
	{
		str2[i] = curr2->n;
		curr2 = curr2->next;
	}
	for (i = 0; i <= length(head) - 1; i++)
	{
		if (str2[i] != str1[i])
			return (0);
	}
	return (res);
}
