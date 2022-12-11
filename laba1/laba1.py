import doctest
class Volume:# TODO Написать 3 класса с документацией и аннотацией типов
    def __init__(self, current_volume: int):
        '''
        Создание и подготовка к работе объекта "Громкость звука"

        :param current_volume: Текущая громкость звука
        :raise ValueError: Если громкость звука находится вне диапозона от 0 до 100, то вызываем ошибку

        Пример:
        volume = Volume(50)
        '''
        if not isinstance(current_volume, int):
            raise TypeError("Текущая громоксть звука должна быть типом int")
        if 0 > current_volume or current_volume > 100:
            raise ValueError("Громкость должна находится в диапозоне от 0 до 100")
        self.current_volume = current_volume

    def turn_up_the_sound(self, add_sound: int) -> None:
        """
        Функция которая увеличивет громкость звука

        :param add_sound: Насколько увеличить громкость звука
        :raise ValueError: Если знаечение, на которое увеличивается громокость звука меньше 1, то вызываем ошибку
        :raise ValueError: Если громкость звука выходит из диапозона от 0 до 100 - вызываем ошибку
        :return: Измененная громкость звука

        Пример:
        volume = Volume(50)
        volume.turn_up_the_sound(25)
        """
        if not isinstance(add_sound, int):
            raise TypeError("Значение, на которое уменьшается громкость звука должно быть типом int")
        if add_sound < 1:
            raise ValueError("Значение, на которое увеличивается громкость звука, должно быть положительным")
        if self.current_volume + add_sound > 100:
            raise ValueError("Громкость звука должна находится в диапозоне от 0 до 100")
        ...

    def turn_down_the_sound(self, remove_sound: int) -> None:
        """
        Функция которая убавляет громкость звука

        :param remove_sound: Насколько уменьшить громкость звука
        :raise ValueError: Если значение, на котоое уменьшается громокость звука меньше 1, то вызываем ошибку
        :raise ValueError: Если громкость звука выходит из диапозона от 0 до 100 - вызываем ошибку
        :return: Измененная громоксть звука
        Пример:
        volume = Volume(50)
        volume.turn_down_the_sound(30)
        """
        if not isinstance(remove_sound, int):
            raise TypeError("Значение, на которое увеличивается громкость звука должно быть типом int")
        if remove_sound < 1:
            raise ValueError("Значение, на которое уменьшается громкость звука, должно быть положительным")
        if self.current_volume - remove_sound < 0:
            raise ValueError("Громкость звука должна находится в диапозоне от 0 до 100")
        ...

class Battery:
    def _init__(self, current_charge:int):
        """
        Создание и подготовка к работе объекта "Батарейка"

        :param current_charge: Текущий уровнь заряда батарейки, %
        :raise ValueError: Если уровень заряда батарейки выходит из диапозона от 0 до 100% - вызываем ошибку

        Пример:
        battery = Battery(100)
        """
        if not isinstance(current_charge, int):
            raise TypeError("Уровень текущего заряда батарейки должен быть типом int")
        if 0 > current_charge or current_charge > 100:
            raise ValueError("Уровень заряда батарейки должен быть в пределах от 0 до 100%")
        self.current_charge = current_charge

    def charge(self, charging_amount: int) -> None:
        """
        Функция которая заряжает батарейку

        :param charge: Количество процентов, на которое будет подзаряжена батарейка
        :raise ValueError: Если значение, на которое будет подзаряжена батарейка меньше 1, то вызываем ошибку
        :raise ValueError: Если уровень заряда батарейки выходит из диапозона от 0 до 100% - вызываем ошибку
        :return: Уровень заряда батарейки

        Пример:
        battery = Battery(0)
        battery.charge(60)
        """
        if not isinstance(charging_amount, int):
            raise TypeError("Уровень, на который батарейка будет подзаряжена, должен быть типом int")
        if charging_amount < 0:
            raise ValueError("Количество процентов. на которое будет подзаряжена батарейка, должно быть больше 0")
        if self.current_charge + charging_amount > 100:
            raise ValueError("Уровень заряда батарейки должен быть в пределах от 0 до 100%")
        ...

    def discharge(self, discharging_amount: int) -> None:
        """
        Функция разряда батарейки

        :param discharging_amount: Уровень, на который батарейка будет разряжена, %
        :raise ValueError: Если значение, на котороу будет разряжена батарейка меньше 1 - вызываем ошибку
        :raise ValueError: Если уровень заряда батарейки выходит из диапозона от 0 до 100% - вызываем ошибку
        :return: Уровень заряда батарейки

        Пример:
        battery = Battery(100)
        battery.discharging(70)
        """
        if not isinstance(discharging_amount, int):
            raise TypeError("Уровень, на который батарейка будет разряжена должен быть типом int")
        if discharging_amount < 1:
            raise ValueError("Уровень, на который батарейка будет разряжена должен быть больше 0")
        if self.current_charge - discharging_amount < 0:
            raise ValueError("Уровень заряда батарейки должен быть в пределах от 0 до 100%")
        ...

    def full_charge(self) -> bool:
        """
        Функция которая проверяет является ли батарейка полностью заряжена

        :return: Является ли батарейка полностью заряжена

        Пример:
        battery = Battery(100)
        battery.full_charge()
        """
        ...

class Credit:
    def _init__(self, sum_of_credit: (int, float)):
        """
        Создание и подготовка к работе объекта "Кредит"

        :param sum_of_credit: Сумма кредита

        Пример:
        credit = Credit(10000)
        """
        if not isinstance(sum_of_credit, (int, float)):
            raise TypeError("Сумма кредита должна иметь тип int или float")
        if sum_of_credit < 0:
            raise ValueError("Сумма кредита должна быть положительным числом")
        self.sum_of_credit = sum_of_credit

    def partial_repayment(self, sum_of_repayment: (int, float)) -> None:
        """
        Функция частичного погашения кредита

        :param sum_of_repayment: Сумма, уплаченная в погашение части кредита
        :raise ValueError: Если сумма частичного погашения кредита меньше 1, то вызываем ошибку
        :raise ValueError: Если сумма частичного погашения кредита больше суммы кредита, то вызываем ошибку
        :return: Оставшаяся сумма кредита

        Пример:
        credit = Credit(10000)
        credit.partial_repayment(2000)
        """
        if not isinstance(sum_of_repayment, (int, float)):
            raise TypeError("Сумма, уплаченная в погашение части кредита должна быть типа int или float")
        if sum_of_repayment > self.sum_of_credit:
            raise ValueError("Значение частичного погашения кредита не может быть больше значения всего кредита")
        if sum_of_repayment < 1:
            raise ValueError("Значение частичного погашения кредита должно быть больше 0")
        ...

    def overpayment(self, interest: (int, float)) -> None:
        """
        Функция показывающая переплату за пользование кредитом

        :param interest: Процентная ставка по кредиту, %
        :raise ValueError: Если процентная ставка по кредиту меньше 0, то вызываем ошибку
        :return: Сумма стоимости кредита

        Пример:
        credit = Credit(10000)
        credit.overpayment(13.5)
        """
        if not isinstance(interest, (int, float)):
            raise TypeError("Процентная ставка по кредиту должна быть типом int или float")
        if interest < 0:
            raise ValueError("Процентная ставка должна быть больше 0")
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
