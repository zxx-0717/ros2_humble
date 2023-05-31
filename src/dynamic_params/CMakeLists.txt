cmake_minimum_required(VERSION 3.8)
project(dynamic_params)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

set(dependencies ament_cmake rclcpp)
include_directories(include)
add_executable(dynamic_params_node src/dynamic_params.cpp src/dynamic_params_node.cpp)
ament_target_dependencies( dynamic_params_node ${dependencies})
target_link_libraries(dynamic_params_node ${colcon_LIBRARIES})

install(TARGETS
  dynamic_params_node
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY params launch
  DESTINATION share/${PROJECT_NAME}
  )

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
