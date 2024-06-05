import pandas as pd
import numpy as np
import pickle
from datetime import datetime

class DataExtractor:
    def toflat_data(self, invoice_file, expired_file):
        item_list = []
        type_conversion = {0: 'Material', 1: 'Equipment', 2: 'Service', 3: 'Other'}

        for invoice in self.invoices:
            invoice_id = invoice['id']
            created_on = pd.to_datetime(invoice['creation_date'])
            invoice_total = sum(item['unit_price'] * item['quantity'] for item in invoice['items'])
            is_expired = invoice_id in self.expired_invoices

            for item in invoice['items']:
                outp = {
                    'invoice_id': invoice_id,
                    'created_on': created_on,
                    'invoiceitem_id': item['id'],
                    'invoiceitem_name': item['name'],
                    'type': type_conversion[item['type']],
                    'unit_price': item['unit_price'],
                    'total_price': item['unit_price'] * item['quantity'],
                    'percentage_in_invoice': (item['unit_price'] * item['quantity']) / invoice_total,
                    'is_expired': is_expired
                }
                item_list.append(outp)

        df = pd.DataFrame(item_list)
        df = df.astype({
            'invoice_id': int,
            'created_on': 'datetime64[ns]',
            'invoiceitem_id': int,
            'invoiceitem_name': str,
            'type': str,
            'unit_price': int,
            'total_price': int,
            'percentage_in_invoice': float,
            'is_expired': bool
        })

        df = df.sort_values(by=['invoice_id', 'invoiceitem_id']).reset_index(drop=True)
        return df

#%%

#%%
