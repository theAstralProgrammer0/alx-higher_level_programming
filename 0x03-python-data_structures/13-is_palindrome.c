#include "lists.h"
void tte(listint_t* temp, listint_t* tail, int* ret)
{
	if (tail->next == NULL)
		return;
	tte(temp, tail->next, ret);
	if (temp->n == tail->n)
	{
		temp = temp->next;
		*ret = 1;
	}
}


int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *tail = NULL;
	int ret = 0; 

	if (head == NULL || *head == NULL)
		return (1);
	temp = tail = *head;
	tte(temp, tail, &ret);
	return (ret);
}
