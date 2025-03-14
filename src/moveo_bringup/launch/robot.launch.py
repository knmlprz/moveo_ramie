import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, LifecycleNode


def generate_launch_description():
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('moveo_description'), 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    rviz_config_path = os.path.join(
        get_package_share_directory('moveo_rviz'), 'config', 'urdf_model.rviz'
    )
    rviz_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('moveo_rviz'), 'launch', 'rviz.launch.py')
            ),
            launch_arguments={'rviz_config': rviz_config_path}.items()
        )


    ld = LaunchDescription()
    ld.add_action(rviz_launch)
    ld.add_action(rsp)
    return ld