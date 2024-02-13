/*

В этой и последующих задачах мы создадим свой простой аналог стандартного класса string для удобной работы со строками.
Начнем мы с написания конструктора. В этой задаче вам требуется реализовать конструктор, который принимает на вход C-style строку, вычисляет ее размер (без учета завершающего 0 символа) и сохраняет его в поле size, кроме того, конструктор должен аллоцировать память достаточную для хранения копии переданной строки (вместе с завершающим 0 символом), копирует переданную строку в выделенную память и сохраняет указатель на начало этой области памяти в поле str. Т.е. в результате работы конструктора в поле str должен оказаться указатель на C-строку c копией исходной строки, а в поле size — длина строки без учета завершающего нулевого символа.
Требования к решению: при выполнении задания вам не нужно вводить или выводить что-либо. При выполнении задания не нужно определять функцию main. Для аллокации памяти не используйте функции из cstdlib (malloc, calloc и realloc).

*/

#include <iostream>
#include <cstddef> // size_t
#include <cstring> // strlen, strcpy

using namespace std;

struct String {

	/* Реализуйте этот конструктор */
	String(const char *str = "") {
		size = this->strlen(str);
		this->copy(str);
	}

	size_t size;
	char *str;

	private:
		unsigned strlen(const char *str)
		{
			int length = 0;
			while (*(str + length) != '\0') {
				length += 1;
			}
			return length;
		}

		void copy(const char *str)
		{
			this->str = new char[this->size + 1];
			for (int i = 0; i < this->size; i++) {
				this->str[i] = str[i];
			}
			this->str[this->size] = '\0';
		}
};

int main () {
    char str[] = "aaaaaccccccccccccccccccccccccc";
    String strObj(str);

    cout << "strObj.str " << strObj.str << " strObj.size " << strObj.size << endl;

    return 0;
}
