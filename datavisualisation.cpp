#include <iostream>
#include <vector>

// Function to check for null values
bool hasNullValues(const std::vector<std::vector<int>>& data) {
    for (const auto& row : data) {
        for (const auto& value : row) {
            if (value == -1) {  // Assuming -1 represents a null value
                return true;
            }
        }
    }
    return false;
}

int main() {
    // Define your dataset as a 2D vector
    std::vector<std::vector<int>> dataset = {
        {1, 2, 3},
        {4, -1, 6},  // Example row with a null value (-1)
        {7, 8, 9}
    };

    // Check for null values
    if (hasNullValues(dataset)) {
        std::cout << "There are null values in the dataset." << std::endl;
    } else {
        std::cout << "There are no null values in the dataset." << std::endl;
    }

    return 0;
}
