#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Define Token Types
typedef enum {
    TOKEN_INT, TOKEN_ID, TOKEN_OP, TOKEN_EOF, TOKEN_UNKNOWN
} TokenType;

void scan(char *code) {
    int i = 0;
    while (code[i] != '\0') {
        // 1. Skip Whitespace
        if (isspace(code[i])) {
            i++;
            continue;
        }

        // 2. Identify Numbers
        if (isdigit(code[i])) {
            printf("Token: NUMBER\tValue: ");
            while (isdigit(code[i])) {
                putchar(code[i++]);
            }
            printf("\n");
        }
        
        // 3. Identify Keywords/Identifiers (Words)
        else if (isalpha(code[i])) {
            char buffer[32];
            int b_idx = 0;
            while (isalnum(code[i])) {
                buffer[b_idx++] = code[i++];
            }
            buffer[b_idx] = '\0';
            
            // Simple check for keyword
            if (strcmp(buffer, "int") == 0 || strcmp(buffer, "return") == 0) {
                printf("Token: KEYWORD\tValue: %s\n", buffer);
            } else {
                printf("Token: ID\tValue: %s\n", buffer);
            }
        }

        // 4. Identify Operators
        else if (strchr("+-=*", code[i])) {
            printf("Token: OPERATOR\tValue: %c\n", code[i++]);
        }

        // 5. Error Handling
        else {
            printf("Token: UNKNOWN\tValue: %c\n", code[i++]);
        }
    }
}

int main() {
    char source[] = "int x = 50 + y";
    printf("Scanning source: %s\n\n", source);
    scan(source);
    return 0;
}
