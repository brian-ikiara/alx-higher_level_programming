#include "lists.h"

/**
 * check_cycle - Function
 * @list: Head
 *
 * Description: Checks for a loop/cycle in a linked
 * list.
 * Return: 1, if there's a loop; 0, if none.
 * On error, stderr.
 */

int check_cycle(listint_t *list)
{
	listint_t *init = list, *final = list;

	while (init && final && final->next)
	{
		init = init->next, final = final->next->next;
		if (init == final)
			return (1);
	}

	return (0);
}
