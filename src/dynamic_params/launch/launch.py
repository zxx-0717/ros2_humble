from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from nav2_common.launch import RewrittenYaml
import os

def generate_launch_description():
        
        ld = LaunchDescription()
        
        param1_arg = DeclareLaunchArgument("param1", default_value=TextSubstitution(text='11'))
        # param2_arg = DeclareLaunchArgument("param2", default_value=TextSubstitution(text='12.0'))
        # param3_arg = DeclareLaunchArgument("param3", default_value=TextSubstitution(text='13 text'))

        pkg_path = get_package_share_directory('dynamic_params')
        params_file = LaunchConfiguration("params_file", default=os.path.join(pkg_path, 'params', 'params.yaml'))
        param1 = LaunchConfiguration("param1")
        param2 = LaunchConfiguration("param2", default=222.0)
        param3 = LaunchConfiguration("param3", default='333 text')

        configured_params_file = RewrittenYaml(
                source_file=params_file,
                param_rewrites={
                        'use_sim_time': 'False',
                },
                convert_types=False,
                )

        dynamic_params_node = Node(
                package='dynamic_params',
                executable='dynamic_params_node',
                name='dynamic_params_node',
                namespace='',
                parameters=[ configured_params_file, {'param1': param1,}, {'param2': param2, 'param3': param3}, ],
                arguments=[],
        )

        ld.add_action(param1_arg)
        # ld.add_action(param2_arg)
        # ld.add_action(param3_arg)
        ld.add_action(dynamic_params_node)

        return ld