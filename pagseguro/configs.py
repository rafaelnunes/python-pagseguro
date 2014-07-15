# coding: utf-8


class Config(object):
    def get(self, key, default=None):
        return getattr(self, key, default)

    def __init__(self, **kwargs):
      self.BASE_URL =  kwargs.get('BASE_URL', 'https://ws.pagseguro.uol.com.br')
      self.VERSION = "/v2/"
      self.CHECKOUT_SUFFIX = self.VERSION + "checkout"
      self.CHARSET = "UTF-8"  # ISO-8859-1
      self.NOTIFICATION_SUFFIX = self.VERSION + "transactions/notifications/%s"
      self.TRANSACTION_SUFFIX = self.VERSION + "transactions/%s"
      self.CHECKOUT_URL = self.BASE_URL + self.CHECKOUT_SUFFIX
      self.NOTIFICATION_URL = self.BASE_URL + self.NOTIFICATION_SUFFIX
      self.TRANSACTION_URL = self.BASE_URL + self.TRANSACTION_SUFFIX
      self.CURRENCY = "BRL"
      self.CTYPE = "application/x-www-form-urlencoded; charset={0}".format(self.CHARSET)
      self.HEADERS = {"Content-Type": self.CTYPE}
      self.REFERENCE_PREFIX = "REF%s"
      self.PAYMENT_HOST = "https://pagseguro.uol.com.br"
      self.PAYMENT_URL = self.PAYMENT_HOST + self.CHECKOUT_SUFFIX + "/payment.html?code=%s"
      self.DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
