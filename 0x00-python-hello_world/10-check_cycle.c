#include "lists.h"

/**
 * check_cycle - Entry Point
 *
 * Description: This function checks if there is a cycle in a singly linked
 * list
 *
 * @list: head pointer of the list
 *
 * Return: 1 if cycle exists, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = NULL;
	listint_t *hare = NULL;

	if (!list || !(list->next))
		return (0);

	tortoise = hare = list;

	do {
		if (tortoise->next && hare->next->next)
		{
			tortoise = tortoise->next;
			hare = hare->next->next;
		}
		else
		{
			return (0);
		}
	} while (tortoise != hare);

	return (1);
}

