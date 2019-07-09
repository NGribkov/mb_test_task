#define function, 
#input data : orders & order_line (pd.dataframes), also you can input number of lines to show (default is 10)
#returns: pd.dataframe with most popular products over last month with sum price over orders, num sales, average order sum
def popular_products(orders, order_line, num_results=10):
  
    date=(datetime.now()+relativedelta(months=-1)).strftime('%Y-%m-%d')
    joined = order_lines.merge(orders, on='OrderId', how='left')
    joined=joined.loc[joined['DateTime']>=date]
    joined['count']=1
  
    #define 2 new dataframes, groupped by different fields of merged table:
    #1. summarize product prices and count products, sort by popularity
    #2. summarize orders total sum
    groupped1=joined.groupby('ProductId').agg({'Price': 'sum', 'count': 'sum'}).sort_values('count', ascending=False)
    groupped2=joined.groupby('OrderId').agg({'Price': 'sum'}).reset_index()
  
    ProductList=groupped1.index.to_list()
  
    #define dictionary with values as list of orders and productId as key
    ol={}
    for product in ProductList:
        odf=(order_lines.query('ProductId == {}'.format(product)))
        ol[product]=odf['OrderId'].values.tolist()
        #assign average order value for each product
        groupped1.at[product, 'AvgInvoice']=groupped2['Price'].loc[groupped2['OrderId'].isin(ol[product])].mean()
    return(groupped1.head(num_results))