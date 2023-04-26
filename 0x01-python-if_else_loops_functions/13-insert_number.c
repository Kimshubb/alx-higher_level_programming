#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	/*create new node and allocate memory*/
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (new_node == NULL)
	{
		return NULL;
	}
	new_node->n = number;
	new_node->next = NULL;
	/*IF THE LIST IS EMPTY insert the new node at the beginning*/
	if (*head == NULL)
	{
		*head = new_node;
		return new_node;
	}
	/*to insert node at the beginning*/
	if (number < (*head)->data)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}
	listint_t *current = *head;
	/*transverse through list to find insertion point*/
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	return new_node;

}
