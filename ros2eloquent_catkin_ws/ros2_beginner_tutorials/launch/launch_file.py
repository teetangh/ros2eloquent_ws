from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turlesim',
            node_executable='turtlesim_node',
            node_namespace='turtlesim1',
            node_name='first'
        ),
        Node(
            package='turlesim',
            node_executable='turtlesim_node',
            node_namespace='turtlesim2',
            node_name='second'
        ),
        Node(
            package='turlesim',
            node_executable='mimic',
            node_name='mimic',

            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel')
            ]
        )
    ])

