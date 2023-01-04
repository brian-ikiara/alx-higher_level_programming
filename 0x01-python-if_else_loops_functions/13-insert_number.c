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
	listint_t *temp = NULL, *init = NULL, *added = NULL;

	/* Edge case: head is NULL */
	if (head == NULL)
		return (NULL);
	/* Assign temp the address of head */
	temp = *head;
	/* Allocate memory to added */
	added = malloc(sizeof(listint_t));
	/* Edge case: added is NULL */
	if (added == NULL)
		return (NULL);
	/* Assign number to member n and NULL to member next */
	added->n = number, added->next = NULL;
	/* Create the new node */
	while (temp != NULL)
	{
		if (temp->n > number)
		{
			if (init != NULL)
				added->next = temp->next, init->next = added;
			else
				added->next = temp, *head = added;
			return (added);
		}
		init = temp, temp = temp->next;
	}
	/* Edge case: dereferenced head is NULL */
	if (*head == NULL)
		*head = added;
	else
		added->next = init->next, init->next = added;

	return (added);
}
