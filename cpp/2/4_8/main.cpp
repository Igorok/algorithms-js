/*
Напишите функцию поиска первого вхождения шаблона в текст. В качестве первого параметра функция принимает текст (C-style строка), в которой нужно искать шаблон. В качестве второго параметра строку-шаблон (C-style строка), которую нужно найти. Функция возвращает позицию первого вхождения строки-шаблона, если он присутствует в строке (помните, что в C++ принято считать с 0), и -1, если шаблона в тексте нет.

Учтите, что пустой шаблон (строка длины 0) можно найти в любом месте текста.

Требования к реализации: при выполнении данного задания вы можете определять любые вспомогательные функции, если они вам нужны. Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.

Напишите программу. Тестируется через stdin → stdout
*/

#include <iostream>
using namespace std;

unsigned strlen(const char *str)
{
    int length = 0;
    while (*(str + length) != '\0') {
        length += 1;
    }
    return length;
}

bool comparator (const char *start1, const char *start2, int size) {
    for (int i = 0; i < size; i++) {
        if (*(start1 + i) != *(start2 + i)) {
            return false;
        }
    }
    return true;
}

int strstr(const char *text, const char *pattern)
{
    if (*pattern == '\0') {
        return 0;
    }

    if (*text == '\0') {
        return -1;
    }

    unsigned textLength = strlen(text);
    unsigned patternLength = strlen(pattern);

    if (textLength < patternLength) {
        return -1;
    }

    int i = 0;
    while (textLength - i >= patternLength) {
        if (comparator(text + i, pattern, patternLength)) {
            return i;
        }
        i++;
    }

    return -1;
}

int main()
{
    char str1[]{ "" };
    char str2[]{ "abcde" };
    int idx1 = strstr(str1, str2);
    cout << "idx1 " << idx1 << endl;

    char str3[]{ "abcde" };
    char str4[]{ "" };
    int idx2 = strstr(str3, str4);
    cout << "idx2 " << idx2 << endl;

    char str5[]{ "abcde" };
    char str6[]{ "cd" };
    int idx3 = strstr(str5, str6);
    cout << "idx3 " << idx3 << endl;


    struct test{
        int ret_value;
        const char *text;
        const char *pattern;
    };
    test tests[] = {
        {0, "", ""}, //0
        {0, "a", ""}, //1
        {0, "a", "a"}, //2
        {-1, "a", "b"}, //3
        {0, "aa", ""}, //4
        {0, "aa", "a"}, //5
        {0, "ab", "a"}, //6
        {1, "ba", "a"}, //7
        {-1, "bb", "a"}, //8
        {0, "aaa", ""}, //9
        {0, "aaa", "a"}, //10
        {1, "abc", "b"}, //11
        {2, "abc", "c"}, //12
        {-1, "abc", "d"}, //13
        {-1, "a", "aa"}, //14
        {-1, "a", "ba"}, //15
        {-1, "a", "ab"}, //16
        {-1, "a", "bb"}, //17
        {-1, "a", "aaa"}, //18
        {-1, "aa", "aaa"}, //19
        {0, "aaa", "aaa"}, //20
        {0, "aaab", "aaa"}, //21
        {1, "baaa", "aaa"}, //22
        {1, "baaaa", "aaa"}, //23
        {1, "baaab", "aaa"}, //24
        {-1, "abd", "abc"}, //25
        {2, "ababc", "abc"}, //26
        {3, "abdabc", "abc"}, //27
        {-1, "", "a"}, //28
        {2, "asasaf", "asaf"}, //29
        {2, "ababac", "abac"} //30
    };
    for (int i = 0; i < sizeof(tests) / sizeof(tests[0]); ++i) {
        int ret = strstr(tests[i].text, tests[i].pattern);
        (tests[i].ret_value == ret) ? cout << "OK" : cout << "Failed";
        cout << " : " << i << " (" << tests[i].ret_value << " : " << ret << ")" << endl;
    }


    return 0;
}
