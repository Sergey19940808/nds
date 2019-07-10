from math import ceil


class Report:
    @staticmethod
    def get_transaction_novalid_nds(transactions):
        msg = []
        for transaction in transactions:
            nds_sum = ceil(transaction.get('Netto') * transaction.get('VAT rate') / 100)
            if nds_sum != transaction.get('VAT sum'):
                msg.append(transaction)
        return msg