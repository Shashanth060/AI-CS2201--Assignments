#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100
#define MAX_DEPTH 20

typedef struct {
    int m_left;
    int c_left;
    int boat;
    int parent;
    int depth;
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
    printf("  Depth %2d: (%dM, %dC, Boat:%s)\n",
           stack[index].depth,
           stack[index].m_left,
           stack[index].c_left,
           stack[index].boat == 0 ? "Left" : "Right");
}

bool depth_limited_search(int max_depth) {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 2; k++)
                visited[i][j][k] = false;
    
    top = -1;
    
    State start = {3, 3, 0, -1, 0};
    push(start);
    visited[3][3][0] = true;
    
    int moves[5][2] = {
        {1,0}, {2,0}, {0,1}, {0,2}, {1,1}
    };
    
    int current_index = 0;
    
    while (current_index <= top) {
        State current = stack[current_index];
        current_index++;

        if (current.m_left == 0 && current.c_left == 0 && current.boat == 1) {
            return true;
        }

        if (current.depth >= max_depth) {
            continue;
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
            
            if (is_valid(new_m, new_c)) {
                int new_depth = current.depth + 1;
                
                if (!visited[new_m][new_c][new_boat]) {
                    visited[new_m][new_c][new_boat] = true;
                    State next = {new_m, new_c, new_boat, current_index - 1, new_depth};
                    push(next);
                }
            }
        }
    }
    
    return false;
}

bool iterative_deepening_dfs() {
    printf("\n");
    
    for (int depth_limit = 1; depth_limit <= MAX_DEPTH; depth_limit++) {
        printf("Iterative %d: ", depth_limit);
        fflush(stdout);
        
        if (depth_limited_search(depth_limit)) {
            printf("FOUND\n\n");
            
            printf("SOLUTION PATH\n");
            for (int i = 0; i <= top; i++) {
                if (stack[i].m_left == 0 && stack[i].c_left == 0 && stack[i].boat == 1) {
                    print_path(i);
                    break;
                }
            }
            
            printf("Solution found at depth limit: %d\n", depth_limit);
            return true;
        } else {
            printf("Not found\n");
        }
    }
    
    printf("\nNo Solution Found within maximum depth %d\n", MAX_DEPTH);
    return false;
}

int main() {
    iterative_deepening_dfs();
    
    return 0;
}