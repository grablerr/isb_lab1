#include <iostream>
#include <fstream>
#include <random>
#include <string>

using namespace std;

string generateRandomBinarySequence() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(0, 1);

    string sequence;
    for (int i = 0; i < 128; ++i) {
        sequence += (distrib(gen) == 1) ? '1' : '0';
    }
    return sequence;
}

int main() {
    setlocale(LC_ALL, "Russian");
    srand(static_cast<unsigned int>(time(0)));

    string randomSequence = generateRandomBinarySequence();
    ofstream outFile("random_cpp_sequence.txt");
    if (outFile.is_open()) {
        outFile << randomSequence;
        outFile.close();
        cout << "Сгенерированная последовательность записана в файл random_cpp_sequence.txt" << endl;
    }
    else {
        cerr << "Ошибка открытия файла для записи." << endl;
        return 1;
    }

    return 0;
}
