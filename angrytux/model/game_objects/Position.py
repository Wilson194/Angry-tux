import math

from angrytux.config.Config import Config


class Position:
    """
    Class for position of any object
    """


    def __init__(self, x_position: float, y_position: float):
        self.__x_position = x_position
        self.__y_position = y_position


    @property
    def x_position(self) -> float:
        """
        :return: x position of object
        """
        return self.__x_position


    @property
    def y_position(self) -> float:
        """
        :return: y position of object
        """
        return self.__y_position


    def compute_distance_from(self, position) -> float:
        """
        Compute distance from another position of another object
        :param position: position ob another object
        :return: distance of positions
        """
        return math.sqrt((position.x_position - self.__x_position) ** 2 + (position.y_position - self.__y_position) ** 2)


    def move(self, angle: float, distance: float) -> None:
        """
        Move object in direction of angle by distance
        :param angle: direction of moving
        :param distance: distance of moving
        """
        norm_x, norm_y = self.__compute_normalize_translation(angle, distance)

        x, y = self.__denormalize_translation(norm_x, norm_y, -angle)

        self.__x_position += x
        self.__y_position += y


    def __denormalize_translation(self, x: float, y: float, origin_angle: float) -> tuple:
        """
        Denormalize x and y coordinates based on origin angle
        :param x: x coordinate
        :param y: y coordinate
        :param origin_angle: origin angle
        :return: new values of x and y
        """
        if abs(origin_angle) > 90:
            x = -x

        if origin_angle < 0:
            y = -y

        return x, y


    def __compute_normalize_translation(self, angle: float, distance: float) -> tuple:
        """
        Compute normalize translation in direction of angle by distance
        :param angle: direction of translation
        :param distance: distance of translation
        :return: new x,y coordinates
        """
        radian_angle = self.__degree_to_radian(self.__normalize_angle(angle))
        x = distance * math.cos(radian_angle)
        y = distance * math.sin(radian_angle)

        return x, y


    def __degree_to_radian(self, degree: float) -> float:
        """
        Convert degree to radian
        :param degree: input degree value
        :return: radian value
        """
        return math.radians(degree)


    def __normalize_angle(self, angle: float) -> float:
        """
        Normalize angle (we want values only in range 0 - 180)
        :param angle: input angle
        :return: normalized angle
        """
        return 180 - abs(angle) if abs(angle) > 180 else abs(angle)


    def out_of_window(self) -> bool:
        """
        Check, if position is out of window
        :return: True if out of window, False otherwise
        """
        x, y = Config()['windows_size']

        if self.__x_position < 0:
            return True

        if self.__x_position > x or self.__y_position > y:
            return True

        return False


    def to_rect(self) -> tuple:
        """
        Convert position to tuple of x,y values
        :return:
        """
        return self.x_position, self.y_position


    def __repr__(self):
        return '<Position> x: {}, y: {}'.format(self.__x_position, self.__y_position)
