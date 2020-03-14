#include <fstream>
#include <iostream>

using namespace std;

void extractTime(string line, float list[100], int &index) {
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
  cout << seconds << endl;

  list[index] = seconds;
  index++;

  return;
}

int main() {
  cout << "Hello\n";

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

  return 0;
}
