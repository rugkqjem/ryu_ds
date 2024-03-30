#define _CRT_SECURE_NO_WARNINGS
#define strdup _strdup
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define ListNode structure
typedef struct ListNode {
    char* page;
    struct ListNode* next;
} ListNode;

// Define CircularLinkedList structure
typedef struct {
    ListNode* head;
    ListNode* tail;
    int size;
} CircularLinkedList;

// Initialize CircularLinkedList
void initCircularLinkedList(CircularLinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

// Append a node to CircularLinkedList
void append(CircularLinkedList* list, char* page) {
    ListNode* new_node = (ListNode*)malloc(sizeof(ListNode));
    new_node->page = strdup(page);
    new_node->next = NULL;

    if (list->size == 0) {
        list->head = new_node;
        list->tail = new_node;
        new_node->next = new_node; // circular reference
    }
    else {
        list->tail->next = new_node;
        new_node->next = list->head;
        list->tail = new_node;
    }
    list->size++;
}

// Remove the first occurrence of a node with given page from CircularLinkedList
void removeNode(CircularLinkedList* list, char* page) {
    if (list->size == 0)
        return;

    ListNode* current = list->head;
    ListNode* prev = NULL;

    do {
        if (strcmp(current->page, page) == 0) {
            if (current == list->head && current == list->tail) {
                list->head = NULL;
                list->tail = NULL;
            }
            else if (current == list->head) {
                list->head = current->next;
                list->tail->next = list->head;
            }
            else if (current == list->tail) {
                list->tail = prev;
                prev->next = list->head;
            }
            else {
                prev->next = current->next;
            }

            free(current->page);
            free(current);
            list->size--;
            return;
        }
        prev = current;
        current = current->next;
    } while (current != list->head);
}

// Pop the first node from CircularLinkedList
void pop(CircularLinkedList* list) {
    if (list->size == 0)
        return;

    ListNode* temp = list->head;
    if (list->size == 1) {
        list->head = NULL;
        list->tail = NULL;
    }
    else {
        list->head = list->head->next;
        list->tail->next = list->head;
    }

    free(temp->page);
    free(temp);
    list->size--;
}

// Get the size of CircularLinkedList
int size(CircularLinkedList* list) {
    return list->size;
}

// Define CacheSimulator structure
typedef struct {
    int cache_slots;
    CircularLinkedList cache;
    int cache_hit;
    int tot_cnt;
} CacheSimulator;

// Initialize CacheSimulator
void initCacheSimulator(CacheSimulator* sim, int cache_slots) {
    sim->cache_slots = cache_slots;
    initCircularLinkedList(&(sim->cache));
    sim->cache_hit = 0;
    sim->tot_cnt = 0;
}

// Perform simulation
void do_sim(CacheSimulator* sim, char* page) {
    sim->tot_cnt++;
    ListNode* current = sim->cache.head;

    // Check if the page is already in cache
    while (current != NULL) {
        if (strcmp(current->page, page) == 0) {
            sim->cache_hit++;
            removeNode(&(sim->cache), page);
            append(&(sim->cache), page);
            return;
        }
        current = current->next;
        if (current == sim->cache.head) // Reached the end of circular list
            break;
    }

    // If cache is full, evict the least recently used page
    if (size(&(sim->cache)) == sim->cache_slots)
        pop(&(sim->cache));

    // Add the new page to cache
    append(&(sim->cache), page);
}

// Print simulation statistics
void print_stats(CacheSimulator* sim) {
    printf("cache_slot = %d, cache_hit = %d, hit ratio = %f\n", sim->cache_slots, sim->cache_hit, (float)sim->cache_hit / sim->tot_cnt);
}

int main() {
    FILE* data_file = fopen("linkbench.trc", "r");
    char line[256];
    int cache_slots;

    for (cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        CacheSimulator cache_sim;
        initCacheSimulator(&cache_sim, cache_slots);

        while (fgets(line, sizeof(line), data_file)) {
            char* page = strtok(line, " ");
            do_sim(&cache_sim, page);
        }

        print_stats(&cache_sim);
        rewind(data_file); // Reset file pointer to the beginning
    }

    fclose(data_file);
    return 0;
}
