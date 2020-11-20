/**
* problem: https://www.hackerrank.com/challenges/attending-workshops
*
* @author Shovra Das
*/
#include<bits/stdc++.h>

using namespace std;

struct Workshop{
    int start_time;
    int end_time;
    
    Workshop(int start_time, int duration){
        this->start_time = start_time;
        this->end_time = start_time + duration;
    }
    
    string toString(){
        stringstream ss;
        ss<<this->start_time<<" "<<this->end_time;
        return ss.str();
    }
};

struct Available_Workshops{
    vector<Workshop*> workshops;
};

Available_Workshops* initialize(int* start_time, int* duration, int n){
    Available_Workshops* aw = new Available_Workshops();
    for(int i=0; i<n; ++i)
        aw->workshops.push_back(new Workshop(start_time[i], duration[i]));
    return aw;
}

int CalculateMaxWorkshops(Available_Workshops* aw){    
    // Greedy solution => https://en.wikipedia.org/wiki/Interval_scheduling#Greedy_polynomial_solution
    vector<Workshop*> candiates = aw->workshops;
    
    auto cmp = [](Workshop* w1, Workshop* w2){ return w1->end_time < w2->end_time; };
    sort(candiates.begin(), candiates.end(), cmp);

    int x_count = 0;
    while(candiates.size()){
        auto x = candiates.begin();
        for(auto it=x+1; it!=candiates.end(); ++it){
            if((*it)->start_time < (*x)->end_time){
                candiates.erase(it);
                --it;  // adjusting iterator after erase
            }
        }
        candiates.erase(x);
        x_count++;  // picking only the counts. however workshop = *x
    }
    
    return x_count;
}

int main(int argc, char *argv[]) {
    int n; // number of workshops
    cin >> n;
    // create arrays of unknown size n
    int* start_time = new int[n];
    int* duration = new int[n];

    for(int i=0; i < n; i++){
        cin >> start_time[i];
    }
    for(int i = 0; i < n; i++){
        cin >> duration[i];
    }

    Available_Workshops * ptr;
    ptr = initialize(start_time,duration, n);
    cout << CalculateMaxWorkshops(ptr) << endl;
    return 0;
}