# Сгенерить исходные данные
# Сотрудники в куче. Босс 1
python3 generate_data.py heap
# Сотрудники в линию. Босс N
python3 generate_data.py line

# Запустить профилировщик. Заимпортить свой код и вызов расчета внутри
python3 runner.py

# Сравнить результат
# Предварительно записав результаты работы в текстовый файл
# Результат дополнительно не сортируется. Ожидается что сотрудники указаны в порядке возрастания для каждого варианта

# python3 check_res.py [путь к файлу с контрольным результатом]  [путь к файлу с тестируемым результатом]

python3 check_res.py output.txt ../Informatics_AIS_RPI/output.txt
