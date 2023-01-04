#include "lists.h"

/**
 * insert_node - Function
 * @head: Head
 * @number: Number
 *
 * Description: Inserts an integer number to
 * a singly linked list.
 * Return: added, the adress of number; NULL, otherwise.
 * On error, stderr.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *init = NULL, *added;

	if (head == NULL)
		return (NULL);
	temp = *head;
	added = malloc(sizeof(listint_t));
	if (added == NULL)
		return (NULL);
	added->n = number;
	added->next = NULL;
	while (temp != NULL)
	{
		if (temp->n > number)
		{
			if (init != NULL)
			{
				added->next = temp->next;
				init->next = added;
			}
			else
			{
				added->next = temp;
				*head = added;
			}
			return (added);
		}
		init = temp;
		temp = temp->next;
	}
	if (*head == NULL)
		*head = added;
	else
	{
		added->next = init->next;
		init->next = added;
	}

	return (added);
}
