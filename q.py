'''
1)      Класса который производит легковые автомобили – они будут нам нужны для класса «таксопарк».

Создайте 100 машин, из которых класс сам будет выпускать каждый третий автомобиль дизельным (остальные, соответственно, бензиновые),
стандартный бензобак будет 60 литров, а каждый пятый авто – с баком на 75 литров.!!!

Стоимость каждой машины будет 10.000$.!!! Каждая машина должна иметь тахограф (он считает пройденный километраж), который нельзя
сбрасывать/уменьшать.!!?
Каждая 1.000 км пробега снижает стоимость бензиновой машины на 9.5$, дизельной – на 10.5$, при этом увеличивая расход топлива на 1%.!!!

Максимальный пробег до капремонта бензиновой – 100.000 километров, дизельной – 150.000 км. Пробег без капремонта
не может быть превышен – при попытке это сделать машина должна быть сначала отозвана в СТО и проведен капремонт.
Его стоимость для бензиновой машины 500$, для дизельной – 700$.

Расход топлива у бензиновой – 8 л/100 км, расход дизеля – 6 л/100 км.!!!
Стоимость литра бензина 2,4$, дизеля – 1,8$.!!!
- Первые 50.000 км. пробега, машины с бензиновым двигателем должны заправляться АИ92 (2.2$/литр),
 и только потом – АИ95 (2.4$/литр).

2)Создайте уникальный маршрут случайной длины для каждой машины (от 55.000 до 286.000 км), требуя заправлять полный бак авто
каждый раз, как он опустеет.!!!

Машины должны уметь предоставлять сведения о себе:

- пробег

- остаточная стоимость

- сколько было потрачено на топливо за всю поездку

- сколько раз машина заправлялась

- сколько осталось пробега до утилизации


После пробега отсортируйте машины: дизельные – по остаточной стоимости, бензиновые – по тому сколько им осталось ездить.

Посчитайте суммарную стоимость машин а автопарке после пробега.

Внезапно, появилось пара Feature request-ов:

- Дайте возможность заменить двигатель на новый, в случае 100% износа, вместо того чтобы отправить машину в утиль.
Стоимость замены пусть будет равна 3000$ для любого типа двигателей, разрешено уводить стоимость машины в минус
(ака в кредит, сумма кредитов должны быть подсчитана для всего автопарка).
'''