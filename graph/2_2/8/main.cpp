/*

Суровые феодальные времена переживала некогда великая островная страна Байтландия. За главенство над всем островом борются два самых сильных барона. Таким образом, каждый город страны контролируется одним из правителей. Как водится издревле, некоторые из городов соединены двусторонними дорогами. Бароны очень не любят друг друга и стараются делать как можно больше пакостей. В частности, теперь для того чтобы пройти по дороге, соединяющей города различных правителей, надо заплатить пошлину — один байтландский рубль.

Программист Вася живет в городе номер 1. С наступлением лета он собирается съездить в город N на Всебайтландское сборище программистов. Разумеется, он хочет затратить при этом как можно меньше денег и помочь ему здесь, как обычно, предлагается Вам.

Формат ввода
В первой строке входного файла записано два числа N и M (1<=N, M<=100000) — количество городов и количество дорог соответсвенно.

В следующий строке содержится информация о городах — N чисел 1 или 2 — какому из баронов принадлежит соответствующий город.

В последних M строках записаны пары 1<=a,b<=N, a!=b. Каждая пара означает наличие дороги из города a в город b. По дорогам Байтландии можно двигаться в любом направлении.

Формат вывода
Если искомого пути не существует, выведите единственное слово impossible. В противном случае в первой строке напишите минимальную стоимость и количество посещенных городов.

Sample Input:
7 8
1 1 1 1 2 2 1
1 2
2 5
2 3
5 4
4 3
4 7
1 6
6 7

Sample Output:
0 5

*/

#include <iostream>
#include <vector>
#include <deque>

using namespace std;


void printAnswer(int n, vector<vector<pair<int, int>>> & cities) {
    for (int i = 0; i < n; i++) {
        cout << "city: " << i + 1 << endl;
        cout << "related:" << endl;
        for (int j = 0; j < cities[i].size(); j++) {
            cout << "city: " << cities[i][j].first + 1 << " distance: " << cities[i][j].second << "; ";
        }
        cout << endl << endl;
    }

    vector<int> distance(n, -1);
    vector<int> parent(n, -1);
    deque<int> tripQueue;

    distance[0] = 0;
    tripQueue.push_back(0);

    while (!tripQueue.empty()) {
        int city = tripQueue.front();
        tripQueue.pop_front();

        // if (city == n - 1) {
        //     break;
        // }

        for (int i = 0; i < cities[city].size(); i++) {
            pair<int, int> nextCity = cities[city][i];
            int newDist = distance[city] + nextCity.second;

            if (distance[nextCity.first] == -1 || distance[nextCity.first] > newDist) {
                if (nextCity.second == 0) {
                    tripQueue.push_front(nextCity.first);
                } else {
                    tripQueue.push_back(nextCity.first);
                }

                distance[nextCity.first] = newDist;
                parent[nextCity.first] = city;
            }
        }
    }

    if (distance.back() == -1) {
        cout << "impossible" << endl;
        return;
    }

    cout << endl << "-------------------------------" << endl << endl;

    for (int i = 0; i < n; i++) {
        cout << "city " << i + 1 << " parent " << parent[i] + 1 << " distance " << distance[i] << endl;
    }

    cout << endl << "-------------------------------" << endl << endl;


    int past = n - 1;
    vector<int> allPath;
    allPath.push_back(n - 1);
    while (past != 0) {
        past = parent[past];
        allPath.push_back(past);
    }

    for (int i = 0; i < allPath.size(); i++) {
        cout << allPath[i] + 1 << " ";
    }
    cout << endl;

    cout << endl << "-------------------------------" << endl << endl;

    cout << distance.back() << " " << allPath.size() << endl;
}

int main () {
    int n, m;

    cin >> n >> m;

    vector<int> owners(n);
    vector<vector<pair<int, int>>> cities(n);

    for (int i = 0; i < n; i++) {
        int owner;
        cin >> owner;
        owners[i] = owner;
    }

    for (int i = 0; i < m; i++) {
        int start, end;
        cin >> start >> end;
        --start;
        --end;

        int dist = owners[start] == owners[end] ? 0 : 1;


        cities[start].push_back(pair<int, int>(end, dist));
        cities[end].push_back(pair<int, int>(start, dist));
    }

    printAnswer(n, cities);

    return 0;

    cout << endl << "-------------------------------" << endl << endl;

    for (int i = 0; i < n; i++) {
        cout << "city: " << i << " owner: " << owners[i] << endl;
        cout << "related:" << endl;
        for (int j = 0; j < cities[i].size(); j++) {
            cout << "city: " << cities[i][j].first << " distance: " << cities[i][j].second << "; ";
        }
        cout << endl << endl;
    }

    cout << endl << "-------------------------------" << endl << endl;

    return 0;
}