// https://www.hackerrank.com/challenges/virtual-functions/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
protected:
    string name;
    int age;    
public:
    virtual void getdata(){
        cin>>Person::name>>Person::age;
    }
    virtual void putdata(){
        cout<<Person::name<<" "<<Person::age;
    };    
};

class Professor: public Person{
private:
    static int counter;
    int id;
    int publications;
public:
    void getdata(){
        Person::getdata();
        cin>>this->publications;
        this->id = ++Professor::counter;
    }
    void putdata(){
        Person::putdata();
        cout<<" "<<this->publications<<" "<<this->id<<endl;
    }
};

class Student: public Person{
private:
    static int counter;
    int id;
    int marks[6];
    
    int totalmarks(){
        int sum = 0;
        for(int i=0; i<6; ++i)
            sum += this->marks[i];
        return sum;
    }
public:
    void getdata(){
        Person::getdata();
        for(int i=0; i<6; ++i)
            cin>>this->marks[i];
        this->id = ++Student::counter;
    }
    void putdata(){
        Person::putdata();
        cout<<" "<<this->totalmarks()<<" "<<this->id<<endl; 
    }
};

int Professor::counter = 0;
int Student::counter = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
