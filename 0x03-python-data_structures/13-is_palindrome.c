#include "lists.h"

/**
 * list_reverse - Function
 * @head: Head
 *
 * Description: Reverses a linked list.
 * Return: void.
 * On error, stderr.
 */
void list_reverse(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *temp = *head;

	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
}

/**
 * is_palindrome - Function
 * @head: Head
 *
 * Description: Checks if linked list is a palindrome.
 * Return: 1, if palindrome; 0, otherwise.
 * On error, stderr.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	list_reverse(&dup);
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		return (0);
	}
	if (!dup)
		return (1);

	return (0);
}
