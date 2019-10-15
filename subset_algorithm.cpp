/*
增量构造法的本质是这样的，每次从0~n-1中挑选出一个元素来，每挑选一次，就是一个子集。
然后再给这个已经挑选出来的子集中挑选元素，这次挑选出来的元素必须比之前的元素要大。
*/
#include <cstdio>

using namespace std;

const int maxn = 100 + 10;
int ans[maxn];
int n;

void print_sub_set(int cur)
{
    for(int i = 0; i < cur; i++)
    {
        printf("%d ", ans[i]);
    }
    printf("\n");
    int s = cur ? ans[cur - 1] + 1 : 0;
    for(int i = s;i < n; i++)
    {
        ans[cur] = i;
        print_sub_set(cur +1);
    }
}

int main()
{
    n = 8;
    print_sub_set(0);
    return 0;
}