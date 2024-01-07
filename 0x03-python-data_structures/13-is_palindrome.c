#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *tail = NULL;
	listint_t *current = NULL;

	temp = current = tail = *head;
	if (temp->next == NULL)
		return (1);
	while (tail->next != NULL)
		tail = tail->next;

	while (temp->n == tail->n)
	{
		current = temp;
		temp = temp->next;
		while (current->next != tail)
			current = current->next;
		tail = current;
		if (temp == tail || tail->next == temp)
			return (1);
	}
	return (0);
}

