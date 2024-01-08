#include "lists.h"
listint_t* tte(listint_t* tail)
{
	if (tail->next == NULL)
		return (tail);
	return (tte(tail->next));
}

listint_t* cttp(listint_t* current, listint_t* tail)
{
	if (current->next == tail)
		return (current);
	return (cttp(current->next, tail));
}

int pali_recur(listint_t* current, listint_t* temp, listint_t* tail)
{
	if (temp == tail || tail->next == temp)
		return (1);
	if (temp->n == tail->n)
	{
		current = temp;
		temp = temp->next;
		tail = cttp(current, tail);
		return (pali_recur(current, temp, tail));
	}
	return (0);
}

int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *tail = NULL;
	listint_t *current = NULL;
	int ret;

	if (head == NULL || *head == NULL)
		return (1);
	temp = current = tail = *head;
	tail = tte(tail);
	ret = pali_recur(current, temp, tail);
	return (ret);
}
