queue<int> modifyQueue(queue<int> q, int k) {
    int n = q.size()-k,i;
    queue<int> q1;
    stack<int> s;
    
    for(i=0;i<k;i++)
    {
        s.push(q.front());
        q.pop();
    }
    
    for(i=0;i<n;i++)
    {
        q1.push(q.front());
        q.pop();
    }
    
    while(k>0)
    {
        q.push(s.top());
        s.pop();
        k--;
    }
    
    while(n>0)
    {
        q.push(q1.front());
        q1.pop();
        n--;
    }
    return q;
}