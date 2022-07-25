#include <iostream>
#include <sys/types.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <string>

using namespace std;

int main(int argc, char *argv[]){
    
    //	Create a socket
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1){
        cout<<"Erro\n";
        return 1;
    }
     //	Create a hint structure for the server we're connecting with
    if(argc < 3) {
        cout << "Erro\n";
        return 1;
        
    }
    
    int port = stoi(argv[1]);
    string ipAddress = argv[2];
   
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(port);
    inet_pton(AF_INET, ipAddress.c_str(), &hint.sin_addr);

    //	Connect to the server on the socket
    int connectRes = connect(sock, (sockaddr*)&hint, sizeof(hint));
    
    if (connectRes == -1){
       cout<<"Erro ao conectar\n";
        return 1;
    }
        //	While loop:
    char buf[4096];
    string userInput, teste;
    int sendRes, bytesReceived; 
    
    do {
        //		Enter lines of text
        cout << "Deseja fazer consulta ou sair? (digite 'sim' para continuar e 'sair' para sair ) :";
        cin >> teste;
        if (teste == "sair"){
            cout << "Fechando o cliente!\n";
            sendRes = send(sock, teste.c_str(), teste.size(), 0);
            break;
        }
        string idade;
        cout << "Digite a idade:  ";
        cin >> idade;
        
        string msg;
        msg = idade;
        sendRes = send(sock, msg.c_str(), msg.size(), 0);

        memset(buf, 0, 4096);
        bytesReceived = recv(sock, buf, 4096, 0);
        if (bytesReceived == -1)
            cout << "Ocorreu um erro\r\n";
        else
            cout << "SERVER> \n" << string(buf, bytesReceived) << "\r\n";
        } while(true);

    //	Close the socket
    close(sock);
    return 0;
}    
