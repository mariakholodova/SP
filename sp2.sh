echo 'Автор: Холодова Мария, 737'
echo '
Разработать скрипт, который:

•	запрашивает путь к файлу
•	для данного файла выводит построчно временные метки в формате:
	o	время последнего доступа
	o	время последнего изменения
	o	время изменения индексного дескриптора
Для выполнения задания используйте команды ls или stat.'

while true
do
	echo 'Введите путь к файлу:'
	read filepath

	stat $filepath --format="Время последнего доступа: %x"
	stat $filepath --format="Время последнего изменения: %y"
	stat $filepath --format="Время изменения индексного дескриптора: %z"

	echo 'Продолжить? y/n'

	read continue

	if  [[ "$continue" = [yY] || "$continue" = [yY][eE][sS] ]]
        then
		continue
        elif [ "$continue" = "n" ]
        then
		break
        else
		echo "Unrecognized command" >$2
        fi
done
