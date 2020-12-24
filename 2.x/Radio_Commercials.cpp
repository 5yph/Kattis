#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <numeric>
using namespace std;

int find_max_subvec(vector<int> vect, int price){
    // Using Kadane's Algorithm
    int local_max = 0;
    int global_max = 0;
    int cost = 0;
    int last_index = 0;
    vector<int> new_vect;

    // We edit our vector such that it represents net profit
    for (int j = 0; j < vect.size(); j++){
    	new_vect.push_back(vect[j] - price);
    }

    for (int i = 0; i < new_vect.size(); i++){
        local_max = max(new_vect[i], new_vect[i] + local_max); // Max ending at this index
        if (local_max > global_max){
            global_max = local_max;
            last_index = i;            
        }

    }

    return global_max;
}


int main(){
    int commercials;
    int price;
    int students;
    vector<int> total_students;
    cin >> commercials;
    cin >> price;

    // Create vector of students per break
    for (int i = 0; i < commercials; i++){
        cin >> students;
        total_students.push_back(students);
    }

    int profit = find_max_subvec(total_students, price);
    cout << profit << endl;

	return 0;
}