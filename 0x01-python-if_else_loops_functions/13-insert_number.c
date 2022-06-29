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
        while (curr != NULL)
        {
                if (curr->n <= number && curr->next->n >= number)
                {
                        new = malloc(sizeof(*new));
                        new->n = number;
                        new->next = curr->next;
                        curr->next = new;
                        new = NULL;
                        curr = NULL;
                        break;
                }
                else
                        curr = curr->next;
        }
        return (*head);
}
