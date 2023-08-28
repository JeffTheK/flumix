#include "lexer.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::vector<std::string> tokenize(const std::string& chars) {
    std::string modifiedChars = chars;
    
    // Replace '(' with ' ( ' and ')' with ' ) '
    size_t pos = modifiedChars.find("(");
    while (pos != std::string::npos) {
        modifiedChars.replace(pos, 1, " ( ");
        pos = modifiedChars.find("(", pos + 3);
    }

    pos = modifiedChars.find(")");
    while (pos != std::string::npos) {
        modifiedChars.replace(pos, 1, " ) ");
        pos = modifiedChars.find(")", pos + 3);
    }
    
    // Split the modified string into tokens
    std::istringstream iss(modifiedChars);
    std::vector<std::string> tokens;
    std::string token;
    
    while (iss >> token) {
        tokens.push_back(token);
    }
    
    return tokens;
}