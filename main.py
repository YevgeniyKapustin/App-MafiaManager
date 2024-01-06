"""Программа для помощи при игре в мафию.

Основной класс MafiaManager, через него осуществляется имплементация всех
методов.
"""
from random import shuffle


class MafiaManager(object):
    """Менеджер для игры в мафию.

    Поля:
    count_of_roles - словарь формата название роли: количество в партии
    player_roles - список названий ролей всех игроков, названия повторяются

    Методы:
    enter_roles - просит заполнить в консоли информацию для count_of_roles
    get_count_of_players - возвращает количество игроков
    fill_player_roles - заполняет player_roles на основе count_of_roles
    print_player_roles - выводит в консоль роли по индексам
    """
    __slots__ = ('count_of_roles', 'player_roles')

    def __init__(self):
        self.count_of_roles: dict[str, int] = {
            'мирный': 0,  # название роли: количество в партии
            'мафия': 0,
            'шериф': 0,
            'доктор': 0
        }
        self.player_roles: list[str] = []

    def get_count_of_players(self) -> int:
        """Возвращает количество всех игроков."""
        return sum([self.count_of_roles.get(i) for i in self.count_of_roles])

    def enter_roles(self) -> None:
        """Просит пользователя ввести в консоль количество всех ролей."""
        for role_name in self.count_of_roles:
            count_of_role: int = int(input(f'количество роли {role_name}: '))
            self.count_of_roles[role_name] = count_of_role

    def fill_player_roles(self) -> None:
        """Заполняет коллекцию ролей игроков."""
        self.enter_roles() if self.get_count_of_players() == 0 else ...
        while self.count_of_roles:
            role_of_player: str = list(self.count_of_roles)[0]
            if self.count_of_roles.get(role_of_player) > 0:
                self.player_roles.append(role_of_player)
                self.count_of_roles[role_of_player] -= 1
            else:
                self.count_of_roles.pop(role_of_player)
        shuffle(self.player_roles)

    def print_player_roles(self) -> None:
        """Выводит коллекцию ролей игроков по индексам в консоль."""
        self.fill_player_roles() if len(self.player_roles) == 0 else ...
        for index, player_role in enumerate(self.player_roles):
            print(f'{index + 1} {player_role}')


if __name__ == '__main__':
    while True:
        MafiaManager().print_player_roles()
        input()
