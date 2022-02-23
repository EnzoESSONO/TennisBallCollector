import os
from glob import glob
from setuptools import setup

package_name = 'bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf*')),
    ],
    install_requires=['setuptools', "rclpy"],
    zip_safe=True,
    maintainer='florian',
    maintainer_email='florian.gaurier@ensta-bretagne.org',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "bot_controler=bot.robot_control:main",
        "gate_controler=bot.box_control:main"
        ],
    },
)
