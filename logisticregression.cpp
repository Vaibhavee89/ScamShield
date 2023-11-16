#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

class Account {
public:
  double user_follower_count;
  double user_following_count;
  double user_biography_length;
  double user_media_count;
  bool user_is_private;
  int username_digit_count;
  int username_length;
};

class LogisticRegressionModel {
public:
  LogisticRegressionModel() {}
  ~LogisticRegressionModel() {}

  double predict(const Account& account) {
    // Calculate the linear combination of the features.
    double linear_combination = account.user_follower_count + account.user_following_count + account.user_biography_length + account.user_media_count;

    // Apply the sigmoid function to the linear combination.
    double probability_fake = 1.0 / (1.0 + exp(-linear_combination));

    return probability_fake;
  }
};

int main() {
  // Create a vector to store the accounts that we want to classify.
  vector<Account> accounts;

  // ... populate the vector with accounts...

  // Create a logistic regression model.
  LogisticRegressionModel model;

  // Classify each account as real or fake.
  for (Account& account : accounts) {
    double probability_fake = model.predict(account);

    if (probability_fake > 0.5) {
      cout << "The account " << account.username << " is likely to be fake." << endl;
    } else {
      cout << "The account " << account.username << " is likely to be real." << endl;
    }
  }

  return 0;
}
