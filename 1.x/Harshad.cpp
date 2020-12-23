#include <iostream>
#include <string>
using namespace std;

bool test_harsh(int num){

    bool result = false;
    int digit_sum = 0;
    string num_string = to_string(num);
    for (int i = 0; i < num_string.length(); i++){      
        digit_sum += num_string[i] - '0';
    }
    if ((num % digit_sum) == 0){
        result = true;
    }

    return result;
}


int main(){

    int num;
    cin >> num;
    bool Harshad = false;

    while (Harshad == false){
        // Test each number if it's divisible by its digit sum
        Harshad = test_harsh(num);
        if (Harshad == false){
            num++; 
        }
    }

    cout << num << endl;
	return 0;
}