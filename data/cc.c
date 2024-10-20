#include <stdio.h>

void encrypt(char text[], int shift) {
    for (int i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (ch >= 'A' && ch <= 'Z') {
            ch = (ch - 'A' + shift) % 26 + 'A';
            //ch = (ch - 'A' - shift + 26) % 26 + 'A';
            
        }
        else if (ch >= 'a' && ch <= 'z') {
            ch = (ch - 'a' + shift) % 26 + 'a';
            //ch = (ch - 'a' - shift + 26) % 26 + 'a';
        
            
        }
        
        text[i] = ch;
    }
}
int main() {
    char text[100];
    int shift;

    printf("Enter a message: ");
    gets(text);  

    printf("Enter shift value: ");
    scanf("%d", &shift);

    encrypt(text, shift);

    printf("Encrypted message: %s\n", text);

    return 0;
}
