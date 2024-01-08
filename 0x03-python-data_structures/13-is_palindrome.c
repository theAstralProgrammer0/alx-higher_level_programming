#include "lists.h"
int tte(listint_t** temp, listint_t* tail, int ret)
{
	if (tail->next == NULL)
		return (0);
	tte(temp, tail->next, ret);
	if ((*temp)->n == tail->n)
	{
		*temp = (*temp)->next;
		ret = 1;
	}
	else
		return (0);
	return (ret);
}


int is_palindrome(listint_t **head)
{
	listint_t **temp = NULL;
	listint_t *tail = NULL;
	int ret = 0; 

	if (head == NULL || *head == NULL)
		return (1);
	tail = *head;
	temp = head;
	ret = tte(temp, tail, ret);
	return (ret);
}
