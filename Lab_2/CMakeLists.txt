cmake_minimum_required(VERSION 3.21) # Проверка версии CMake.
									 # Если версия установленой программы
									 # старее указаной, произайдёт аварийный выход.

set(PROJECT_NAME 2_lab)				 # имя проекта		 
project("${PROJECT_NAME}")


set(CMAKE_CXX_STANDARD 17)			 # устанавливаем 17 стандарт языка
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)


# добавляем директории
include_directories("/")

add_executable("${PROJECT_NAME}" lab_2.cpp 
								
									)
											
target_link_libraries("${PROJECT_NAME}" )

#file(COPY "input.txt" DESTINATION "/")

					


