#include <iostream>
#include <string>
#include <bitset>

using namespace std;

// Function to convert hexadecimal string to binary string
string hex_to_bin(const string& hex_str) {
    bitset<4> bits;
    string bin_str = "";
    for (char hex_char : hex_str) {
        bits = bitset<4>(stoi(string(1, hex_char), nullptr, 16));
        bin_str += bits.to_string();
    }
    return bin_str;
}

// Function to count the number of matching bits between two binary strings
int count_matching_bits(const string& hash1, const string& hash2) {
    int matching_bits = 0;
    string bin_hash1 = hex_to_bin(hash1);
    string bin_hash2 = hex_to_bin(hash2);
    for (size_t i = 0; i < bin_hash1.size(); ++i) {
        if (bin_hash1[i] == bin_hash2[i]) {
            matching_bits++;
        }
    }
    return matching_bits;
}

int main() {
    string hash1 = "be9321e93ada409862432d73370ddb58";
    string hash2 = "e46152896b927bf8725ffa84a6e263c1";

    int matching_bits = count_matching_bits(hash1, hash2);
    cout << "Number of matching bits for -md5: " << matching_bits << endl; // Number of matching bits for -md5 65 
    
    hash1 = "c89c5aa89c6d0a8b97e418a279a4e6225adb09b8043a980575f8b48e5b3674fc";
    hash2 = "fce0d20c16ba9b6f0eb9c5b70ba06a92d8174b8a534a2e766a634826f3732e4c";
    
    matching_bits = count_matching_bits(hash1, hash2);
    cout << "Number of matching bits for -sha256: " << matching_bits << endl; // Number of matching bits for -sha256 137

    return 0;
}

