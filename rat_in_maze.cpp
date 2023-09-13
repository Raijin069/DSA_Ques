#include <iostream>
using namespace std;

bool is_safe(int **arr, int x, int y, int n) {
  if (x < n && y < n && arr[x][y] == 1) {
    return true;
  }
  return false;
}

bool rat_in_maze(int **arr, int x, int y, int n, int **sol_arr) {
  if (x == n - 1 && y == n - 1) {
    sol_arr[x][y] = 1;
    return true;
  }

  if (is_safe(arr, x, y, n)) {
    sol_arr[x][y] = 1;
    if (rat_in_maze(arr, x + 1, y, n, sol_arr)) {
      return true;
    }
    if (rat_in_maze(arr, x, y + 1, n, sol_arr)) {
      return true;
    }
    sol_arr[x][y] = 0;
    return false;
  }
  return false;
}

int main() {
  int n, i, j;
  cin >> n;

  int **arr = new int *[n];
  for (i = 0; i < n; i++) {
    arr[i] = new int[n];
  }

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      cin >> arr[i][j];
    }

  }

    cout << "\n\n";

  int **sol_arr = new int *[n];
  for (i = 0; i < n; i++) {
    sol_arr[i] = new int[n];
    for (j = 0; j < n; j++) {
      sol_arr[i][j] = 0;
    }
  }

  if (rat_in_maze(arr, 0, 0, n, sol_arr)) {
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        cout << sol_arr[i][j] << " ";
      }
      cout << endl;
    }
    cout << endl;
  }
  return 0;
}