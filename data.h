# include<iostream>
# include<string>
# include<ctime>
using namespace std;
void print(){
	srand(int(time(0)));
	string data[11] = {"You have nothing to eat!",
    	               "Your joke is less funny than your father's!",
    	               "BOOOOOOOOOOOOOOOOOM",
    	               "You died because you are too poor.",
		       "Your Mum kill you because you haven't do your homework yet.",
		       "You died of fear.",
		       "You died because you didn't do your homework.",
                       "You're dead. There's no reason",
                       "Virus invasion!",
                       "Reject a face-saving offer.",
                       "Get ready for your death!"};
	cout << data[rand()%11];
}
