#include <iostream>
#include <vector>
using namespace std;

struct Coordinate{
    int x;
    int y;
    Coordinate(int xVal, int yVal) : x(xVal), y(yVal) {}

};

class Part{
    private:
        bool isValid;
        int numbers;
        vector<Coordinate*> coordinates;
    
    public:
        void addCoordinate(int x, int y){
            coordinates.push_back(new Coordinate(x, y));
        };

        bool checkValidity(vector<vector<string>> input){
            for (int coordinate = 0; coordinate < coordinates.size(); coordinate++){
                
            }
        };

};


int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}