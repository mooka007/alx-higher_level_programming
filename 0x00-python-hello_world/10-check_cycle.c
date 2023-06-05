#include "lists.h"

/**
 * check_cycle - singly linked list contains a cycle or not
 * Owned By MoOka
 * @list: pointer to the head of a singly linked list
 * Return: 1 if cycled, 0 if not
 */


int check_cycle(listint_t *list)
{
	if (list == NULL)
	{
		return (0);
	}

	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
