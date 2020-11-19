/**
* problem: https://www.hackerrank.com/challenges/attribute-parser
*
* @author Shovra Das    
*/
#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<stack>
using namespace std;

vector<string> split(string str, char delimiter){
    vector<string> tokens;
    
    stringstream ss(str);
    string token;
    while(getline(ss, token, delimiter)){
        tokens.push_back(token);
    }
    
    return tokens;
}

vector<string> split(string str, string delimiter){
    vector<string> tokens;
    
    size_t pos;
    while((pos = str.find(delimiter)) != string::npos){
        tokens.push_back(str.substr(0, pos));
        str = str.substr(pos+delimiter.size());
    }
    tokens.push_back(str);
    
    return tokens;
}

void print(vector<string> v){   
    for (auto item : v) cout<<item<<endl;
}

void print(map<string, string> m){
    for (const auto &[k, v] : m) cout<<k<<"="<<v<<endl;
}
    
string trim(string str){
    int start, end;
    for(start=0; str[start]==' ' || str[start]=='\t' || str[start]=='\r' || str[start]=='\n'; ++start);
    for(end=str.size()-1; str[end]==' ' || str[end]=='\t' || str[end]=='\n'; --end);
    return str.substr(start, end-start+1);
}

string strip(string str, char ch){
    string stripped = "";
    for(auto c : str) if(c != ch) stripped += c;    
    return stripped;
}

int main() {
    int n, q, i, j, found;
    string markup="";
    string line, qtag, qattribute;
    
    cin>>n>>q;
    getline(cin, line); // ignore extra CRLF
    
    stack<string> stack_;
    vector<string> tags;
    for(i=0; i<n; ++i){
        getline(cin, line);
        
        if(stack_.empty()){
            stack_.push(line);
            continue;
        }
        if(line.rfind("</") != string::npos){
            tags.push_back(stack_.top());
            stack_.pop();
        }            
        else
            stack_.push(stack_.top() + line);        
    }  
    // print(tags);  
    
    map<string, map<string, string>> tag_map;    
    for(auto tag_str: tags){
        string name_str = "";
        bool append = false;
        int index = 0;
        for(int i=0; i<tag_str.size(); ++i){
            if(tag_str[i]=='<') append = true;
            else if (tag_str[i]==' ') append = false;
            if(append){
                name_str += tag_str[i];
                index = i;
            }
        }
        name_str.erase(0, 1);
        name_str = strip(name_str, '>');
        string name="";
        for(auto c: name_str) name += c=='<'? '.' : c;
                
        string attribute_str = tag_str.substr(index+1);
        attribute_str = trim(strip(attribute_str, '>'));
        // cout<<name<<endl<<attribute_str<<endl<<endl;
        
        map<string, string> attribute_map;
        if(attribute_str != ""){        
            vector<string> parts;
            string key, value;
            for(auto attr: split(attribute_str, "\" ")){
                parts = split(attr, '=');
                key = strip(parts[0], '"');
                value = strip(parts[1], '"');
                attribute_map[trim(key)] = trim(value);
            }            
        }
        
        tag_map[name] = attribute_map;
    }
    
    // query
    for(i=0; i<q; ++i){
        cin>>line;
        qtag = "", qattribute="";
        for(j=0; line[j] != '~'; ++j)
            qtag += line[j];
        for(++j; line[j] != '\0'; ++j)
            qattribute += line[j];
        
        map<string, string> attribute_map = tag_map[qtag];
        if(attribute_map.find(qattribute) == attribute_map.end())
            cout<<"Not Found!"<<endl;
        else
            cout<<attribute_map[qattribute]<<endl;
    }

    return 0;
}