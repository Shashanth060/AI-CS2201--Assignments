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

State stack[MAX];
int top = -1;

bool visited[4][4][2];

void push(State s) {
    if (top < MAX - 1) {
        stack[++top] = s;
    }
}

State pop() {
    return stack[top--];
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
    
    print_path(stack[index].parent);
    printf("(%dM, %dC, Boat:%s)\n",
           stack[index].m_left,
           stack[index].c_left,
           stack[index].boat == 0 ? "Left" : "Right");
}

bool dfs() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 2; k++)
                visited[i][j][k] = false;
    
    State start = {3, 3, 0, -1};
    push(start);
    visited[3][3][0] = true;
    
    int moves[5][2] = {
        {1,0}, {2,0}, {0,1}, {0,2}, {1,1}
    };
    
    int current_index = 0;
    
    while (current_index <= top) {
        State current = stack[current_index];
        current_index++;
        
        
        if (current.m_left == 0 && 
            current.c_left == 0 && 
            current.boat == 1) {
            
            printf("Solution Found!\n\n");
            print_path(current_index - 1);
            return true;
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
                
                State next = {new_m, new_c, new_boat, current_index - 1};
                push(next);
            }
        }
    }
    
    printf("No Solution Found\n");
    return false;
}

int main() {
    dfs();
    return 0;
}