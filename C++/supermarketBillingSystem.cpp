#include<iostream>
#include<fstream>

class shopping
{
private:
    int pcode;
    float price, discount;
    std::string prodName;
public:
    void menu();
    void administrator();
    void buyer();
    void add();
    void edit();
    void remove();
    void list();
    void recipt();
};

void shopping :: menu(){
    m:
    int choice;
    std::string email, password;
    std::cout<<"\t\t\t\t______________________________________\n";
    std::cout<<"\t\t\t\t                                      \n";
    std::cout<<"\t\t\t\t          Supermarket Main Menu       \n";
    std::cout<<"\t\t\t\t                                      \n";
    std::cout<<"\t\t\t\t                                      \n";
    std::cout<<"\t\t\t\t______________________________________\n";
    std::cout<<"\t\t\t\t                                      \n";
    std::cout<<"\t\t\t\t| 1)Administrator |\n";
    std::cout<<"\t\t\t\t|                 |\n";
    std::cout<<"\t\t\t\t| 2)Buyer         |\n";
    std::cout<<"\t\t\t\t|                 |\n";
    std::cout<<"\t\t\t\t| 3)Exit          |\n";
    std::cout<<"\t\t\t\t|                 |\n";
    std::cout<<"\n\t\t\tPlease Select!";
    std::cin>>choice;
    
    switch (choice)
    {
    case 1:
        std::cout<<"\t\t\t Please Login!\n";
        std::cout<<"\t\t\t Enter email  \n";
        std::cin>>email;
        std::cout<<"\t\t\t Password \n";
        std::cin>>password;
        if (email == "robby@email.com" && password == "123")
        {
            administrator();
        }
        else
        {
            std::cout<<"Invalid username or password!\n";
        }
        break; 
        
    case 2:
        buyer();
    
    case 3:
        exit(0);
    
    default:
        std::cout<<"Please select from the given options!\n";
    }
goto m;
}

void shopping :: administrator()
{
    m:
    int choice;
    std::cout<<"\n\n\n\t\t\t Administrator Menu ";
    std::cout<<"\n\t\t\t|____1)Add the Product____|";
    std::cout<<"\n\t\t\t|                         |";
    std::cout<<"\n\t\t\t|____2)Modify the Product_|";
    std::cout<<"\n\t\t\t|                         |";
    std::cout<<"\n\t\t\t|____3)Delete the Product_|";
    std::cout<<"\n\t\t\t|                         |";
    std::cout<<"\n\t\t\t|____4)Back to Main Menu__|";
    std::cout<<"\n\n\t Please Enter your choice:";
    std::cin>>choice;
    switch (choice)
    {
    case 1:
        add();
        break;
    
    case 2:
        edit();
        break;

    case 3:
        remove();
        break;

    case 4:
        menu();
        break;
        
    default:
        std::cout<<"\nInvalid Choice!";
        break;
    }
    goto m;
}
void shopping :: buyer()
{
    int choice;
    
}