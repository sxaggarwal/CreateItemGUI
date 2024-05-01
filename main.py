import tkinter as tk
from tkinter import ttk, messagebox
from src.item import Item

class AddItemGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ADD Buyer")
        self.geometry("500x500")
        self.item_table = Item()
        self.item_type = ["Standard", "Outside-Processing", "Material"]
        self.make_combobox()
        
    
    def make_combobox(self):
        tk.Label(self, text="Part Number: ").grid(row=0, column=0)
        self.part_number_box = tk.Entry(self, width=20)
        self.part_number_box.grid(row=0, column=1)

        tk.Label(self, text="Description: ").grid(row=1, column=0)
        self.description_box = tk.Entry(self, width=20)
        self.description_box.grid(row=1, column=1)

        tk.Label(self, text="Item Type: ").grid(row=2, column=0 )
        self.item_type_box = ttk.Combobox(self, values=self.item_type, state="readonly")
        self.item_type_box.grid(row=2, column=1)

        tk.Label(self, text="Stock Length: ").grid(row=3, column=0)
        self.stock_length_box = tk.Entry(self, width=20)
        self.stock_length_box.grid(row=3, column=1)

        tk.Label(self, text="Stock Width: ").grid(row=4, column=0)
        self.stock_width_box = tk.Entry(self, width=20)
        self.stock_width_box.grid(row=4, column=1)

        tk.Label(self, text="Thickness: ").grid(row=5, column=0)
        self.thickness_box = tk.Entry(self, width=20)
        self.thickness_box.grid(row=5, column=1)

        tk.Label(self, text="Weight: ").grid(row=6, column=0)
        self.weight_box = tk.Entry(self, width = 20)
        self.weight_box.grid(row=6, column=1)

        add_item_button = tk.Button(self, text="ADD Item", command=self.add_item)
        add_item_button.grid(row=7, column=1)
    
    def add_item(self):
        """ """
        if self.part_number_box.get() and self.item_type_box.get():
            if self.item_type_box.get() == "Standard": 
                item_type_fk=1
            elif self.item_type_box.get() == "Material":
                item_type_fk=2
            else:
                item_type_fk=5
            
            description = self.description_box.get()
            part_number = self.part_number_box.get()
            stock_length = self.stock_length_box.get()
            stock_width = self.stock_width_box.get()
            thickness = self.thickness_box.get()
            weight = self.weight_box.get()
            self.create_item(part_number, stock_width, stock_length, thickness, weight, item_type_fk=item_type_fk, description=description)
            messagebox.showinfo("Success", "Item created successfully!")
        else:
            messagebox.showerror("ERROR", "Enter Part Number and Select Item Type")

    def create_item(self, part_number, stock_width, stock_length, thickness, weight, item_type_fk=1, mps_item=1, purchase=1, forecast_on_mrp=1, mps_on_mrp=1, service_item=1, unit_of_measure_set_fk=1, vendor_unit=1.0, manufactured_item=0, calculation_type_fk=1, inventoriable=1, purchase_order_comment=None,  description=None, comment=None, only_create=None, bulk_ship=1, ship_loose=1, cert_reqd_by_supplier=0, can_not_create_work_order=0, can_not_invoice=0, general_ledger_account_fk=100, purchase_account_fk=116, cogs_acc_fk=116):
        item_info_dict = {
                    "PartNumber": part_number, 
                    "ItemTypeFK": item_type_fk, 
                    "Description" : description, 
                    "Comment": comment, 
                    "MPSItem": mps_item,
                    "Purchase": purchase, 
                    "ForecastOnMRP": forecast_on_mrp, 
                    "MPSOnMRP": mps_on_mrp, 
                    "ServiceItem": service_item, 
                    "PurchaseOrderComment": purchase_order_comment, 
                    "UnitOfMeasureSetFK": unit_of_measure_set_fk,
                    "VendorUnit": vendor_unit, 
                    "ManufacturedItem": manufactured_item, 
                    "CalculationTypeFK": calculation_type_fk, 
                    "Inventoriable": inventoriable, 
                    "BulkShip": bulk_ship, 
                    "ShipLoose": ship_loose,
                    "CertificationsRequiredBySupplier": cert_reqd_by_supplier,
                    "CanNotCreateWorkOrder": can_not_create_work_order,
                    "CanNotInvoice": can_not_invoice,
                    "GeneralLedgerAccountFK": general_ledger_account_fk,
                    "PurchaseGeneralLedgerAccountFK" : purchase_account_fk,
                    "SalesCogsAccountFK": cogs_acc_fk,
                    "StockWidth": stock_width,
                    "StockLength": stock_length,
                    "Weight": weight,
                    "Thickness": thickness
                }
        self.item_table.insert_item(item_info_dict)


if __name__ == "__main__":
    r = AddItemGUI()
    r.mainloop()