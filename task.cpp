#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

/*
  Basic Algorithm:
   1. Read necessary lines as string.
   2. Extract the time in that line as seconds and store it in a integer array.
   3. Evaluate the lists to get the required results.
*/

// This function rounds off upto three decimal places.
// It is being called due to inaccuracy of float (trailing decimal places might not be zero).
float round(float x) {
  float var = (int)(x * 1000 + .5);
  return (float)var / 1000;
}

void extractTime(string line, float *list, int &index) {
  int minutes = 0, milliseconds = 0;
  float seconds = 0;
  bool min = true;

  for (int i = 4;; i++) {
    if (line[i] == 115)
      break;
    else if (line[i] == 109)
      min = false;
    else if ((line[i] > 47) && (line[i] < 58)) {
      if (min) {
        minutes *= 10;
        minutes += line[i] - 48;
      } else {
        milliseconds *= 10;
        milliseconds += line[i] - 48;
      }
    }
  }
  seconds = (minutes * 60) + (float(milliseconds) / 1000);

  list[index] = seconds;
  index++;

  return;
}

int analyzeTime(float *list, int n, float &mean, float &std_dev) {
  float total = 0.0;
  float variance_numerator = 0.0;
  mean = 0.0;
  std_dev = 0.0;

  for (int i = 0; i < n; i++)
    total += list[i];

  mean = float(total) / n;
  mean = round(mean);

  for (int i = 0; i < n; i++)
    variance_numerator += (list[i] - mean) * (list[i] - mean);

  std_dev = sqrt(variance_numerator / n);
  std_dev = round(std_dev);

  int count = 0;
  for (int i = 0; i < n; i++)
    if ((list[i] >= mean - std_dev) && (list[i] <= mean + std_dev))
      count += 1;

  return count;
}

int main() {
  fstream file("timestat.txt", ios::in);

  if (!file.is_open()) {
    cout << "Error\n";
    return -1;
  }

  string line;
  float real[100], user[100], sys[100];
  int real_count = 0, user_count = 0, sys_count = 0;
  while (getline(file, line)) {
    if (line[0] == 114)
      extractTime(line, real, real_count);
    else if (line[0] == 117)
      extractTime(line, user, user_count);
    else if (line[0] == 115)
      extractTime(line, sys, sys_count);
  }

  int no_of_runs = real_count;

  int count[3];
  float mean[3], std_dev[3];

  count[0] = analyzeTime(real, no_of_runs, mean[0], std_dev[0]);
  count[1] = analyzeTime(user, no_of_runs, mean[1], std_dev[1]);
  count[2] = analyzeTime(sys, no_of_runs, mean[2], std_dev[2]);

  cout << "Total number of runs: " << no_of_runs;
  cout << "\n\nAverage Time Statistics:";
  cout << "\nreal " << mean[0] << "s";
  cout << "\nuser " << mean[1] << "s";
  cout << "\nsys  " << mean[2] << "s";
  cout << "\n\nStandard deviation of Time statistics:";
  cout << "\nreal " << std_dev[0] << "s";
  cout << "\nuser " << std_dev[1] << "s";
  cout << "\nsys  " << std_dev[2] << "s";
  cout << "\n\nNumber of runs within average - standard deviation to "
          "average + standard deviation:";
  cout << "\nreal " << count[0];
  cout << "\nuser " << count[1];
  cout << "\nsys  " << count[2];
  cout << endl;

  return 0;
}
