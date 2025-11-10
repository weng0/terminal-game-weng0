# printf '\033[?25l' hide cursor
printf '\033[2J' clear screen
printf '\033[1;1H' move to 1,1

printf '###########'
printf '\033[2;1H'  # move
printf '#         #'
printf '\033[3;1H'
printf '#         #'
printf '\033[4;1H'
printf '#         #'
printf '\033[5;1H'
printf '###########'