#include <iostream>
#include <string>
using namespace std;

int factorial(int x) // Calculates factorial using recursion
{
    if (x == 1) // Base case
    {
        return x;
    }
    else
    {
        return x * factorial(x - 1);
    }
}

int main()
{
    int tests;
    cin >> tests;

    for (int i = 0; i < tests; i++)
    {
    int x;
    cin >> x;
    int fact = factorial(x);
    // Convert fact to a character array for iterating
    string factorial = to_string(fact);
    cout << factorial.back() << endl;
    }

	return 0;
}