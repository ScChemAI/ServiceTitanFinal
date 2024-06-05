import pandas as pd


class DataExtractor:
    def load_data(self, data):
        output = []
        for r in data:
            for item in r:
                n_item = {
                    'id': item['item']['id'],
                    'name': item['item']['name'],
                    'unit_price': item['item']['unit_price'],
                    'type': item['item']['type'],
                    'quantity': item['quantity']
                }
                output.append(n_item)
        #
        # df = df.astype({
        #     'invoice_id': int,
        #     'created_on': 'datetime64[ns]',
        #     'invoiceitem_id': int,
        #     'invoiceitem_name': str,
        #     'type': str,
        #     'unit_price': int,
        #     'total_price': int,
        #     'percentage_in_invoice': float,
        #     'is_expired': bool
        # })
        return df
#%%
