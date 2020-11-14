// https://www.hackerrank.com/challenges/rectangle-area/problem

/**
    @author Shovra Das
*/

#include <iostream>
using namespace std;

class Rectangle{
protected:
    int width, height;
    
public:
    void display(){
        cout<<this->width<<" "<<this->height<<endl;
    }
};

class RectangleArea: public Rectangle{
public:
    void read_input(){
        cin>>Rectangle::width>>Rectangle::height;
    }
    
    void display(){
        cout<<this->width*this->height;
    }
};


int main(){
    RectangleArea r_area;
    
    r_area.read_input();
    r_area.Rectangle::display();
    r_area.display();
    
    return 0;
}