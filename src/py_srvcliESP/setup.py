from setuptools import find_packages, setup

package_name = 'py_srvcliESP'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kubu',
    maintainer_email='kubu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'minimal_service = py_srvcliESP.serviesp:main',  # Asegúrate de que esta sea la función principal en serviesp.py
            'minimal_client = py_srvcliESP.cliesp:main',     # Asegúrate de que esta sea la función principal en cliesp.py
        ],
    },
)
