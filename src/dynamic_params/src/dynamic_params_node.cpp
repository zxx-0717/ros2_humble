
#include "dynamic_params/dynamic_params.hpp"
#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
        rclcpp::init(argc, argv);
        auto node = std::make_shared<DynamicParams>("dynamic_params_node");
        rclcpp::executors::SingleThreadedExecutor executor;
        executor.add_node(node);
        executor.spin(); 

        RCLCPP_INFO(node->get_logger(), "Exit.");   

        return 0;
}