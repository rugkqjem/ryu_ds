#ifndef CIRCULAR_LINKED_LIST_H
#define CIRCULAR_LINKED_LIST_H

#include <stdio.h>
#include <stdlib.h>

// Define a structure for a node in the circular linked list
struct ListNode {
    char* data;
    struct ListNode* next;
};

// Function to create a new node
struct ListNode* createNode(char* data);

// Function to insert a node at the end of the circular linked list
void append(struct ListNode** head, char* data);

// Function to remove a node from the circular linked list
void removeNode(struct ListNode** head, char* data);

// Function to print the circular linked list
void printList(struct ListNode* head);

// Function to free memory allocated to the circular linked list
void freeList(struct ListNode** head);

#endif





