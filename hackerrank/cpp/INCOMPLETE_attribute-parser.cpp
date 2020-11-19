// <tag1 value = "HelloWorld"><tag2 name = "Name1"></tag2></tag1>

#include<vector>
#include<deque>
#include<iostream>
#include<map>
#include<algorithm>
using namespace std;

struct Tag{
    string name;
    map<string, string> attributes;
};

vector<Tag> parse(string hrml){
    vector<Tag> tags;
    vector<string> tags_;
    
    string tag = "";
    for(int i=0; i<hrml.length(); ++i){
        tag += hrml[i];
        if(hrml[i]=='>'){
            tags_.push_back(tag);
            tag = "";
        }
    }
    
    for(int i=0; i<tags_.size(); ++i)
        cout<<tags_[i]<<endl;
        
    
    return tags;
}

int main() {    
    int n, q, i, j, found;
    string markup="";
    string line, qtag, qattribute;
    
    cin>>n>>q;
    getline(cin, line); // ignore extra CRLF
    for(i=0; i<n; ++i){
        getline(cin, line);
        markup += line;
    }
    
    vector<Tag> tags = parse(markup);
    return 0;
    
    // query
    for(i=0; i<q; ++i){
        cin>>line;
        qtag = "", qattribute="";
        for(j=0; line[j] != '~'; ++j)
            qtag += line[j];
        for(++j; line[j] != '\0'; ++j)
            qattribute += line[j];
        
        found = false;
        for(auto tag: tags)
            if(tag.name == qtag){
                cout<<tag.attributes[qattribute]<<endl;
                found = true;          
                break;
            }
        if(!found)
            cout<<"Not Found!"<<endl;
    }
    
    return 0;
}


//*******************************************************

#include<iostream>
#include<vector>
#include<map>
#include<sstream>
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

string trim(string str){
    int start, end;
    for(start=0; str[start]==' ' || str[start]=='\t' || str[start]=='\r' || str[start]=='\n'; ++start);
    for(end=str.size()-1; str[end]==' ' || str[end]=='\t' || str[end]=='\n'; --end);
    return str.substr(start, end-start+1);
}

int main() {
    cout<<trim("\r\r\na\rc");
    return 0;
    string tag_str = "<tag1 name=\"TAG1\"><tag2 name=\"TAG21\"><tag3 name=\"TAG3\" value=\"3\">";
 
    vector<string> parts = split(tag_str, '>');
    string name = "";
    for(auto part: parts)
        name +=  "." + split(part, ' ')[0].substr(1);
    name = name.substr(1);
    cout<<name<<endl;
      
    string attribute_str = "";
    size_t pos = parts.back().find(" ");
    if(pos != string::npos)
        attribute_str = parts.back().substr(pos);
    attribute_str = trim(attribute_str)
    cout<<trim(attribute_str);
    for(int i=0; i<attribute_str.size(); ++i){
        if(attribute_str[i]=="")
    }
    
    
    // for(auto part: parts)
    //     cout<<part<<endl;
    // map<string, string> attributes;
    // for(int i=1; i<lastPart.size(); ++i){
    //     vector<string> parts1 = split(lastPart[i], '=');
    //     attributes.insert(make_pair(parts1[0], parts1[1]));
    // }       
    
    
    // for (const auto &[k, v] : attributes)
    //     cout<<k<<v<<endl;
    
    return 0;
}
