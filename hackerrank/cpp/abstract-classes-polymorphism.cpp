/**
* problem: https://www.hackerrank.com/challenges/abstract-classes-polymorphism
*
* @author Shovra Das    
*/
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

class LRUCache : Cache{
private:
    int count = 0;
public:
    LRUCache(int capacity){
        this->cp = capacity;
    }
    
    void set(int key, int value){
        if(Cache::mp.find(key) != mp.end()){
            Cache::mp[key]->value = value;
        }
        else{
            Node* node = new Node(key, value);
            Cache::mp[key] = node;
            node->next = Cache::head;
            Cache::head = node;
            if(count==0)
                Cache::tail = node;
            ++count;
            
            if(count == Cache::cp+1){
                Cache::mp.erase(tail->key);
                Cache::tail = Cache::tail->prev;
            }
        }
    }
    
    int get(int key){
        if(Cache::mp.find(key) == mp.end())
            return -1;
        return Cache::mp[key]->value;
    }
};

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}