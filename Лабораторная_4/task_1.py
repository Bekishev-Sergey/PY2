if __name__ == "__main__":
    class Furniture:
        """Родительский класс"""

        def __init__(self, material: str, length: int, width: int, height: int, color: str, brand: str):
            """Метод-конструктор

            Keyword arguments:
            material -- Материал
            length -- длина, мм
            width -- ширина, мм
            height -- высота, мм
            color -- цвет
            brand -- марка производителя

            """
            self.material = material
            self.length = length
            self.width = width
            self.height = height
            self.color = color
            self.brand = brand

        def __str__(self) -> str:
            """Метод, возвращающий строку с материалом, размерами и цветом предмета мебели"""
            return f'Материал: {self.material}. Длина: {self.length}. Ширина: {self.width}. Высота: {self.height}.' \
                   f' Цвет: {self.color}. Марка производителя: {self.brand}.'

        def __repr__(self) -> str:
            """Метод, возвращающий валидную Python строку, точно такого же экзампляра"""
            return f'{self.__class__.__name__}(material={self.material!r}, length={self.length!r},' \
                   f' height={self.height}, width={self.width!r}, color={self.color!r}, brand={self.brand!r})'

        def repainting(self, new_color):
            """Метод, изменяющий цвет прдмета мебели"""
            self.color = new_color


    class Chair(Furniture):
        """Дочерний класс"""

        def __init__(self, material: str, length: int, width: int, height: int, color: str, brand: str, skin_color: str,
                     destination: str):
            """Метод-конструктор

            Keyword arguments:
            skin_color -- цвет обшивки стула
            destination -- тип стула. Например: барный, компьютерный, кухонный и т.д.

            """
            super().__init__(material, length, width, height, color, brand)
            self.destination = destination
            self.skin_color = skin_color

        def __str__(self) -> str:
            """Метод, возвращающий экземпляр класса"""
            tstr = super().__str__()
            return f'Предмет мебели: {self.__class__.__name__}. {tstr} Цвет обшивки: {self.skin_color}. ' \
                   f'Тип стула: {self.destination}'

        def __repr__(self) -> str:
            """Метод, возвращающий валидную Python строку точно такого же экземпляра"""
            return f'{self.__class__.__name__}(material={self.material!r}, length={self.length!r},' \
                   f' height={self.height!r}, width={self.width!r}, color={self.color!r}, brand={self.brand!r},' \
                   f' skin_color={self.skin_color!r}, destination={self.destination!r})'

        def repainting(self, new_color: str, skin_color: str):
            """Метод, изменяющий основной цвет стула, а также цвет его обшивки"""
            super().repainting(new_color)  # изменение основного цвета происходит точно также как и родительском классе
            self.skin_color = skin_color
