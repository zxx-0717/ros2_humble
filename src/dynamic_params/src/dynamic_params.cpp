
#include "dynamic_params/dynamic_params.hpp"
#include <iostream>

DynamicParams::DynamicParams(string name) : rclcpp::Node(name)
{
        initParams();
        printParams();
}

DynamicParams::~DynamicParams()
{
}

void DynamicParams::initParams()
{
	this->declare_parameter<int>("param1", 311);
	this->declare_parameter<float>("param2", 322.0);
	this->declare_parameter<string>("param3", string("333 text"));

	
	param1 = this->get_parameter_or("param1", 31);
	param2 = this->get_parameter_or("param2", 32.0);
	param3 = this->get_parameter_or("param3", string("33 text"));
}

void DynamicParams::printParams()
{
	RCLCPP_INFO(this->get_logger(), "param1 value: %d", param1);
	RCLCPP_INFO(this->get_logger(), "param2 value: %f", param2);
	RCLCPP_INFO(this->get_logger(), "param3 value: %s", param3.c_str());
}