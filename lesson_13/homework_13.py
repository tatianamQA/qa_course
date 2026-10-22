"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest

from lesson_03.homework_03 import result


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)



class TestLogger(unittest.TestCase):
    def test_success_log_event(self):
        with self.assertLogs("log_event", level="INFO") as logs:
            log_event("Andras", "success")
        self.assertEqual(logs.output, ["INFO:log_event:Login event - Username: Andras, Status: success"])


    def test_warning_log_event(self):
        with self.assertLogs("log_event", level="WARNING") as logs:
            log_event("Andras", "expired")
        self.assertEqual(logs.output, ["WARNING:log_event:Login event - Username: Andras, Status: expired"])


    def test_failed_log_event(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("Andras", "failed")
        self.assertEqual(logs.output, ["ERROR:log_event:Login event - Username: Andras, Status: failed"])

    def test_empty_username_log_event(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("", "failed")
        self.assertEqual(logs.output, ["ERROR:log_event:Login event - Username: , Status: failed"])


    def test_wrong_status_log_event(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("Andras", "full")
        self.assertEqual(logs.output, ["ERROR:log_event:Login event - Username: Andras, Status: full"])

