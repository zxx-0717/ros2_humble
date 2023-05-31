#include "rclcpp/rclcpp.hpp"
#include <string>
using namespace std;

class DynamicParams : public rclcpp::Node
{
public:
DynamicParams(string name);
~DynamicParams();

void initParams();
void printParams();

private:
int param1 = 1;
float param2 = 2.0f;
string param3 = "empty string";
};