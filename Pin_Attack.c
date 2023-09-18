#include <string.h>
#include <stdio.h>

int find_password(pin){
// test every combination of letters until we find the password
// create a list holding ascii characters using string header
    char letters[] = "01234566789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0; i < strlen(letters); i++){
        for (int j = 0; j < strlen(letters); j++){
            for (int k = 0; k < strlen(letters); k++){
                // put the letters together to form a password
                char password[4];
                password[0] = letters[i];
                password[1] = letters[j];
                password[2] = letters[k];
                password[3] = '\0';
                // test the password = to pin
                if (pin == hash(password)){
                    printf("%s", password);
                    return 0;
                }
                else:
                    print(password)}}}
}

void main(){
    char pin[] = scanf("Enter a 3 digit pin: ");
    // if pin is size 3 then run find_password
    if (strlen(pin) == 3){
        printf("your password is ",find_password(pin));}
    else{
        printf("Pin must be 3 digits");}
}