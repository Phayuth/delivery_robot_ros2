# Build only one specific package
```
clear && colcon build --packages-select aljnu_controllers
```

# Build the package dependencies first and then the package later
```
clear && colcon build --packages-up-to aljnu_mobile_manipulator
```

# Build test
```
colcon test --event-handlers console_direct+ --packages-select aljnu_controllers
```