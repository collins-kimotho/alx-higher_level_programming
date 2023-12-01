#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	/* Traverse the list with two pointers */
	while (slow && fast && fast->next)
	{
		/* Move slow pointer one step and fast pointer two steps */
		slow = slow->next;
		fast = fast->next->next;

		/* If there is a cycle, fast will catch up to slow */
		if (slow == fast)
		{
			return (1);
		}
	}
	/* if there is no cycle, fast will reach the end of the list */
	return (0);
}
