#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::string;
using std::vector;

//compute prefix function
vector<int> compute_prefix(string p)
{
    vector<int>s (p.size());
    s[0] = 0;
    int border = 0;
    for (int i=1; i<p.size(); i++)
    {
        while(border>0 && p[i] != p[border])
        {
            border = s[border -1];
        }

        if (p[i] == p[border])
        {
            border = border + 1;
        }
        else
        {
            border = 0;
        }
        s[i] = border;
    }
    return s;
}

// Find all occurrences of the pattern in the text and return a
// vector with all positions in the text (starting from 0) where
// the pattern starts in the text.

vector<int> find_pattern(const string& pattern, const string& text) {
    vector<int> result;
    string st = pattern+'$'+text;
    vector<int>pre = compute_prefix(st);
    for (int i=pattern.size()+1; i<st.size(); i++)
    {
        if (pre[i] == pattern.size())
        {
            result.push_back(i-2*pattern.size());
        }
    }
    return result;
}

int main() {
    string pattern, text;
    cin >> pattern;
    cin >> text;

    vector<int> result = find_pattern(pattern, text);
    for (int i = 0; i < result.size(); ++i) {
        printf("%d ", result[i]);
    }
    printf("\n");

    return 0;
}
