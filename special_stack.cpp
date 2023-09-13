void push(stack<int>& s, int a){
	s.push(a);
}

bool isFull(stack<int>& s,int n){
	return s.size() == n;
}

bool isEmpty(stack<int>& s){
	return s.empty();
}

int pop(stack<int>& s){
    int p = s.top();
    s.pop();
	return p;
}

int getMin(stack<int>& s){
   
	stack<int> t;
	t = s;
	int min=s.top();
	while(!t.empty())
	{
	    if( min>t.top()){
	        min = t.top();
	    }
	    t.pop();
	}
	return min;
}