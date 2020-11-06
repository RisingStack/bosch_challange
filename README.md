## Automotive executable

Automotive executable is a runtime environment built to test your code
for the bosch hackathon challenge. It enables you to use any programming
language you would like to as long as you provide the complier used to run
your program on your local machine and your work's entry file.

## Challenges

For each task, you'll have to implement a program that will be tested against
the requirements. You can either provide an already executable (precompiled)
file or a compiler and your program's path, such as "python" and "example.py".
For more information, run the following command on Windows:
```sh
./automotive.exe -h
```

For the tasks, you are given a json file, which includes a map. This map has to
be used to navigate your car from "A1" point to "D1". Your job will be to implement
an application that, based on the actual traffic conditions, finds the most optimal
route and navigates your self-driving car from start to destination. To read a more
detailed description on how the first task works run the following command:
```sh
./automotive.exe help taskone
```

Once you successfully implemented a solution for the first task, you can move to
the second task. To read a more detailed description on how the second task works
run the following command:
```sh
./automotive.exe help tasktwo
```

## How to run your code

You can test your program by providing the path of an executeable:
```sh
./automotive.exe <taskname> ./my_precomplied_program.exe
```
or a compiler and your program's entry point:
```sh
./automotive.exe <taskname> python ./my_python_file.py
```