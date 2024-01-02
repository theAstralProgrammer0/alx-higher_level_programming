#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);

	do
	{
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

