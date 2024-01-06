#include "lists.h"

/**
 * palindrom - recursive palind or not
 * @head: head of a list
 * Return: 0 if not palind, 1 if plaind
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - function to know if it is palindrome
 * @head: head of a list
 * @end: end of a list
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
