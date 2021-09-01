#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <class T>
void printArray(vector<T> int_vector){
    for(int i=0; i<int_vector.size(); i++)
        cout<<int_vector[i]<<endl;
}

int main() {
	int n;
	
	// cin >> n;
	vector<int> int_vector(3);
	int_vector[0] = 1;
	int_vector[1] = 2;
	int_vector[2] = 3;
	// for (int i = 0; i < n; i++) {
	// 	int value;
	// 	cin >> value;
	// 	int_vector[i] = value;
	// }
	
	// cin >> n;
	vector<string> string_vector(2);
	string_vector[0] = "Hello";
	string_vector[1] = "World";
	// for (int i = 0; i < n; i++) {
	// 	string value;
	// 	cin >> value;
	// 	string_vector[i] = value;
	// }

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}