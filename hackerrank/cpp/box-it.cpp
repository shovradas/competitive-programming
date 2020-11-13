// https://www.hackerrank.com/challenges/box-it/problem

/**
    @author Shovra Das
*/

#include<bits/stdc++.h>

using namespace std;

class Box{
private:
    int l, b, h;
    
public:
    Box():l(0),b(0),h(0){}    
    Box(int l,int b, int h) : l(l), b(b), h(h){}    
    Box(const Box& box) : l(box.l), b(box.b), h(box.h){}
    
    int getLength(){ return this->l; }
    
    int getBreadth(){ return this->b; }
    
    int getHeight(){ return this->h; }
    
    long long CalculateVolume(){ 
        return this->l * (long long)this->b * this->h;
    }

    bool operator<(Box& b){
        if((this->l < b.l)
            || (this->l == b.l && this->b < b.b)
            || (this->l == b.l && this->b == b.b && this->h < b.h))
            return true;
        else
            return false;
    }

    friend ostream& operator<<(ostream& out, Box& B){
        return out<<B.l<<" "<<B.b<<" "<<B.h;
    }
};

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}