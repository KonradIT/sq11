#include <iostream>
#include <cmath>
#include <string> 
using namespace std;
int main () {
   int i = 1;
   while( std::to_string(pow(i,2)).substr(std::to_string(i).length() - 2 ) != '11' ) {
      cout << std::to_string(pow(i,2)).substr(std::to_string(i).length() - 2 ) << endl;
      i++;
   }
   return 0;
}
