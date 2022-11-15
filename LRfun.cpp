#include <bits/stdc++.h>
using namespace std;
bool custom_sort(double a, double b){
	double a1=abs(a-0);
	double b1=abs(b-0);
	return a1<b1;
}

int main()
{
	double x[]={1,2,3,4,5};
	double y[]={1,3,3,2,5};
	vector<double>error;
	double devi;
	double b0=0;
	double b1=0;
	double learnRate=0.01;
	for(int i=0; i<20;i++){
		int index =i%5;
		double p=b0+b1*x[index];
		devi=p-y[index];
		b0=b0-learnRate*devi;
		b1=b1-learnRate *devi*x[index];
		cout<<"B0="<<b0<<"B1="<<b1<<" "<< "error="<<devi<<endl;
		error.push_back(devi);

}
	sort(error.begin(), error.end(), custom_sort);
	cout<<"Optimal values are: "<< "B0="<< b0<< "B1="<<b1<< " "<< "error="<<error[0]<<endl;
	cout<<"enter test value";
	double test;
	cin>>test;
	double pred=b0+b1*test;
	cout<<endl;
	cout<<"the value predicted by the model"<<pred;
}
