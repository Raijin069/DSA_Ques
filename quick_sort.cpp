#include <iostream>
using namespace std;

int partation(int arr[], int left, int right) {
  int i, j, pivot;
  i = left;
  j = right - 1;
  pivot = arr[right];

  while (i < j) {
    while (i < right && arr[i] < pivot) {
      i += 1;
    }
    while (j > left && arr[j] >= pivot) {
      j -= 1;
    }
    if (i < j) {
      swap(arr[i], arr[j]);
    }
  }
  if (arr[i] > pivot) {
    swap(arr[i], arr[right]);
  }
  return i;
}

void quick_sort(int arr[], int left, int right) {
  int partation_pos;
  if (left < right) {
    partation_pos = partation(arr, left, right);
    quick_sort(arr, left, partation_pos - 1);
    quick_sort(arr, partation_pos + 1, right);
  }
}

int main() { 
    int n,i;
    cout << "enter size of array: ";
    cin >> n;
    cout << endl;
    
    int arr[n];
    cout << "enter array: \n";
    for(i=0;i<n;i++)
    {
        cin >> arr[i];
    }
    cout << endl;
    // int arr[]={1,9,8,3,4,83,3483,77,5414,87,987,7};
    // int n = sizeof(arr)/sizeof(arr[0])-1;
    quick_sort(arr,0,n-1);
    for(i = 0;i<n;i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n\n";
    return 0; 
}