#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 5

char charTable[SIZE][SIZE];
int positions[26][2];

void prepareText(char *s, int chgJtoI) {
    int len = strlen(s), j = 0;
    for (int i = 0; i < len; i++) {
        if (isalpha(s[i])) {
            s[j] = toupper(s[i]);
            if (chgJtoI && s[j] == 'J') s[j] = 'I'; // Change J to I
            else if (!chgJtoI && s[j] == 'Q') continue; // Skip Q if needed
            j++;
        }
    }
    s[j] = '\0'; // Null terminate the string
}

void createTbl(const char *key, int chgJtoI) {
    int used[26] = {0};
    int k = 0;
    char s[100];
    
    strcpy(s, key);
    strcat(s, "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    prepareText(s, chgJtoI);
    
    for (int i = 0; s[i]; i++) {
        char c = s[i];
        if (!used[c - 'A']) {
            charTable[k / SIZE][k % SIZE] = c;
            positions[c - 'A'][0] = k / SIZE;
            positions[c - 'A'][1] = k % SIZE;
            used[c - 'A'] = 1;
            k++;
        }
    }
}

void codec(char *txt, int dir) {
    int len = strlen(txt);
    for (int i = 0; i < len; i += 2) {
        char a = txt[i], b = txt[i + 1];
        int row1 = positions[a - 'A'][0], col1 = positions[a - 'A'][1];
        int row2 = positions[b - 'A'][0], col2 = positions[b - 'A'][1];
        
        if (row1 == row2) {
            col1 = (col1 + dir + SIZE) % SIZE;
            col2 = (col2 + dir + SIZE) % SIZE;
        } else if (col1 == col2) {
            row1 = (row1 + dir + SIZE) % SIZE;
            row2 = (row2 + dir + SIZE) % SIZE;
        } else {
            int temp = col1;
            col1 = col2;
            col2 = temp;
        }
        
        txt[i] = charTable[row1][col1];
        txt[i + 1] = charTable[row2][col2];
    }
}

void encode(char *txt) {
    char result[100] = "";
    int len = strlen(txt);
    int i, j = 0;
    
    for (i = 0; i < len; i += 2) {
        result[j++] = txt[i];
        if (i + 1 == len || txt[i] == txt[i + 1]) {
            result[j++] = 'X';
            i--;
        } else {
            result[j++] = txt[i + 1];
        }
    }
    result[j] = '\0';
    strcpy(txt, result);
    codec(txt, 1);
}

void decode(char *txt) {
    codec(txt, -1);
}

int main() {
    char key[100], txt[100];
    int chgJtoI = 1; // Change J to I
    
    printf("Enter the key for Playfair Cipher: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = 0; // Remove newline character
    
    printf("Enter the message to encode: ");
    fgets(txt, sizeof(txt), stdin);
    txt[strcspn(txt, "\n")] = 0; // Remove newline character
    
    createTbl(key, chgJtoI);
    prepareText(txt, chgJtoI);
    
    char encodedTxt[100];
    strcpy(encodedTxt, txt);
    
    encode(encodedTxt);
    printf("Input Message : %s\n", txt);
    printf("Encrypted Message : %s\n", encodedTxt);
    
    decode(encodedTxt);
    printf("Decrypted Message : %s\n", encodedTxt);
    
    return 0;
}
