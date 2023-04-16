# Для того чтобы компьютеры поддерживали актуальное время, они могут обращаться к серверам точного времени
# SNTP (Simple Network Time Protocol). К сожалению, компьютер не может просто получить время у сервера,
# потому что информация по сети передаётся не мгновенно: пока сообщение с текущим временем дойдёт до компьютера,
# оно потеряет свою актуальность. Протокол взаимодействия клиента (компьютера, запрашивающего точное время)
# и сервера (компьютера, выдающего точное время) выглядит следующим образом:
#
# 1. Клиент отправляет запрос на сервер и запоминает время отправления A (по клиентскому времени).
# 2. Сервер получает запрос в момент времени B (по точному серверному времени) и отправляет клиенту сообщение, содержащее время B.
# 3. Клиент получает ответ на свой запрос в момент времени C (по клиентскому времени) и запоминает его.
# Теперь клиент, из предположения, что сетевые задержки при передаче сообщений от клиента серверу и от сервера клиенту одинаковы,
# может определить и установить себе точное время, используя известные значения A, B, C.
#
# Вам предстоит реализовать алгоритм, с точностью до секунды определяющий точное время для установки на клиенте по известным A, B и C.
# При необходимости округлите результат до целого числа секунд по правилам арифметики (в меньшую сторону, если дробная часть числа меньше 1/2,
# иначе в большую сторону).
#
# Возможно, что, пока клиент ожидал ответа, по клиентскому времени успели наступить новые сутки, однако известно,
# что между отправкой клиентом запроса и получением ответа от сервера прошло менее 24 часов.

from sys import stdin


class Timestamp:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_seconds(self, seconds):
        sum_seconds = self.seconds + seconds
        seconds = sum_seconds % 60
        sum_minutes = self.minutes + (sum_seconds // 60)
        minutes = sum_minutes % 60
        sum_hours = self.hours + (sum_minutes // 60)
        hours = sum_hours % 24
        return Timestamp(hours, minutes, seconds)

    def represent(self):
        def convert_to_str_with_zeros(time):
            return str(time // 10) + str(time % 10)

        representation = []
        representation.append(convert_to_str_with_zeros(self.hours))
        representation.append(convert_to_str_with_zeros(self.minutes))
        representation.append(convert_to_str_with_zeros(self.seconds))
        return ":".join(representation)


def compute_seconds_delta(earlier, later):
    hours_delta = later.hours - earlier.hours
    if hours_delta < 0:
        hours_delta += 24
    minutes_delta = later.minutes - earlier.minutes
    if minutes_delta < 0:
        minutes_delta += 60
        hours_delta -= 1
    seconds_delta = later.seconds - earlier.seconds
    if seconds_delta < 0:
        seconds_delta += 60
        minutes_delta -= 1
    return seconds_delta + minutes_delta * 60 + hours_delta * 3600


def main(A, B, C):
    def convert_to_timestamp(time_str):
        hh, mm, ss = list(map(int, time_str.split(":")))
        return Timestamp(hh, mm, ss)

    def arithmetic_round(positive_num):
        return int(positive_num + 0.5)

    client_sending_time = convert_to_timestamp(A)
    client_recieving_time = convert_to_timestamp(C)
    seconds_one_way = arithmetic_round(
        compute_seconds_delta(client_sending_time, client_recieving_time) / 2
    )
    server_time = convert_to_timestamp(B)
    answer_timestamp = server_time.add_seconds(seconds_one_way)
    print(answer_timestamp.represent())


if __name__ == "__main__":
    A, B, C = stdin.readlines()
    main(A, B, C)

