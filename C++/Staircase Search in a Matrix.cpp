#include <iostream>
#include <algorithm>
using namespace std;

void display(int a[][1000], int n, int k)
{
    int smallest=a[0][0], largest=a[n-1][n-1]; 
    
    int i=0, j=n-1;
    for(i=0;j<n;)
    {
        if(n==0)
        {
            cout << "-1";
            break;
        }
        if(k<smallest || k>largest)
        {
            cout << "-1";
            break;
        }
        if(a[i][j]==k)
        {
        cout << "Found " << i << " " << j;
        break;
        }
        if(a[i][j]>k)
        j--;
        else
        i++;
    }
}

int main() 
{
    int n, i, j, k;
    cin >> n >> k;
    int a[1000][1000];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cin >> a[i][j];
        }
    }
    display(a, n, k);
}