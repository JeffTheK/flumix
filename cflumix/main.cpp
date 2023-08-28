#include <iostream>
#include <fstream>
#include "lexer.hpp"

void exec_file(std::string file_path) {
    std::ifstream file(file_path);
    std::string file_contents((std::istreambuf_iterator<char>(file)), (std::istreambuf_iterator<char>()));
    auto tokens = tokenize(file_contents);
    for (const std::string& str : tokens) {
        std::cout << str << ",";
    }
}

int main(int argc, char const *argv[])
{
    std::string file_path = argv[1];
    exec_file(file_path);
    return 0;
}
