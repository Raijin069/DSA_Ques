read -p "enter file name: " fie
echo -e "\n\t\t\t\t\t\t\t\t\t\t\t  Executing $fie.cpp\n\n"
s="$fie.cpp"
g++ -O3 $s
mv a.out "Output/$fie.out"
./"Output/$fie.out"
echo -e "\n\n\n\t\t\t\t\t\t\t\t\t\t* * * * Executed $fie.cpp * * * * \n\n"
