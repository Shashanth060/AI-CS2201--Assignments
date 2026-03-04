#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
    int m_left;
    int c_left;
    int boat;
    int parent;
} State;

State queue[MAX];
int front = 0, rear = 0;

bool visited[4][4][2];

void enqueue(State s) {
    if (rear < MAX) {
        queue[rear++] = s;
    }
}

State dequeue() {
    return queue[front++];
}

bool is_valid(int m_left, int c_left) {
    int m_right = 3 - m_left;
    int c_right = 3 - c_left;

    if (m_left < 0 || m_left > 3 || c_left < 0 || c_left > 3)
        return false;

    if (m_left > 0 && m_left < c_left)
        return false;

    if (m_right > 0 && m_right < c_right)
        return false;

    return true;
}

void print_path(int index) {
    if (index == -1)
        return;

    print_path(queue[index].parent);
    printf("(%dM, %dC, Boat:%s)\n",
           queue[index].m_left,
           queue[index].c_left,
           queue[index].boat == 0 ? "Left" : "Right");
}

void bfs() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 2; k++)
                visited[i][j][k] = false;
    
    State start = {3, 3, 0, -1};
    enqueue(start);
    visited[3][3][0] = true;

    int moves[5][2] = {
        {1,0}, {2,0}, {0,1}, {0,2}, {1,1}
    };

    while (front < rear) {
        int current_index = front;
        State current = dequeue();

        if (current.m_left == 0 &&
            current.c_left == 0 &&
            current.boat == 1) {

            printf("Solution Found!\n\n");
            print_path(current_index); 
            return;
        }

        for (int i = 0; i < 5; i++) {
            int new_m = current.m_left;
            int new_c = current.c_left;
            int new_boat = 1 - current.boat;

            if (current.boat == 0) {
                new_m -= moves[i][0];
                new_c -= moves[i][1];
            } else { 
                new_m += moves[i][0];
                new_c += moves[i][1];
            }

            if (is_valid(new_m, new_c) &&
                !visited[new_m][new_c][new_boat]) {

                visited[new_m][new_c][new_boat] = true;

                State next = {new_m, new_c, new_boat, current_index};
                enqueue(next);
            }
        }
    }

    printf("No Solution Found\n");
}

int main() {
    bfs();
    return 0;
}