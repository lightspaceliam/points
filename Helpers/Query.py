class Query:
    customerCode: str = ''

    # Constructor.
    def __init__(self, code):
        self.customerCode = code

    queryString = """
SELECT	T.OrderNo
		, T.CustomerCode
		, T.CustomerName
		, T.CustomerType
		, T.InvoiceDate
		, T.InvoiceNo
		, T.TransactionType
		, T.OrderStatus
		, LTRIM(RTRIM(TL.bi_stock_code)) AS 'ProductCode'
		, LTRIM(RTRIM(TL.long_descript)) AS 'ProductName'
		, LTRIM(RTRIM(TL.bi_sf_sol_stk_unit_desc)) AS 'Uom'
		, TL.bi_sf_sol_item_price AS 'ItemPricePerUnit'
		, TL.[value] AS 'AmountExGst'
		, TL.value_inc_tax AS 'AmountIncGst'
		, TL.bi_sf_sol_ship_sales_tax_amt AS 'TaxAmount'
		, TL.bi_sf_sol_tax_rate AS 'TaxRate'
		, TL.bi_sf_sol_stk_unit_conversion AS 'ConversionFactor'
		, TL.bi_sf_sol_shipped_qty AS 'ShippedQty'
		, TL.bi_sf_sol_shipped_amount AS 'ShippedAmount'
FROM	bi_so_fact_all_v AS TL
		INNER JOIN (
				SELECT	CONVERT(INT, bi_so_order_no) AS 'OrderNo'
						, LTRIM(RTRIM(bi_sd_so_cust_code)) AS 'CustomerCode'
						, LTRIM(RTRIM(bill_to_shortname)) AS 'CustomerName'
						, LTRIM(RTRIM(bi_sd_so_cust_type)) AS 'CustomerType'
						, CONVERT(DATETIME, bi_sd_so_invoice_date) AS 'InvoiceDate'
						, LTRIM(RTRIM(bi_sd_so_invoice_no)) AS 'InvoiceNo'
						, CASE
							WHEN bi_sd_so_credit_note_no = 0 THEN 'Invoice'
							ELSE 'Credit'
						END AS 'TransactionType'
						, LTRIM(RTRIM(bi_sd_so_order_status)) AS 'OrderStatus'
						, CASE
							WHEN CHARINDEX('C', bi_sd_so_invoice_no) > 0 THEN 'Cancelled'
							ELSE ''
						END AS 'IsCancelled'
				FROM	bi_so_dim_v_st AS T
				WHERE	T.bi_so_order_no IS NOT NULL
						AND T.bi_sys_comp_code = 1
						AND LTRIM(RTRIM(T.bi_sd_so_cust_code)) = '{0}'
						AND T.bi_sd_so_invoice_date IS NOT NULL
						AND CONVERT(DATETIME, T.bi_sd_so_invoice_date) BETWEEN N'2018-07-01' AND N'2019-06-30'
		) AS T 
			ON T.OrderNo = CONVERT(INT, TL.bi_so_order_no)
				AND TL.bi_so_order_no IS NOT NULL
ORDER BY CONVERT(DATETIME, T.InvoiceDate) ASC
		, CONVERT(INT, T.OrderNo) ASC;
"""

    def addCode(self):
        return self.queryString.format(self.customerCode)