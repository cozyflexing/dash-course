# # from pandas import to_datetime, read_sql
# # from listCreations import engine
# # from functions import total_open_interest


# # selectedColumn = "OpenInterest"

# # df = read_sql("CAD", engine)
# # df.Date = to_datetime(df.Date)

# # change = []

# # for x in range(0, 12):
# #     # change.append(abs(df.NoncommercialLong.iloc[0] - df.NoncommercialLong.iloc[x]))
# #     print(
# #         f"{df.Date.iloc[x]} - Net Noncomm: {(df.NoncommercialLong.iloc[x] - df.NoncommercialShort.iloc[x])} Noncomm diff longs: {(df.NoncommercialLong.iloc[0] - df.NoncommercialLong.iloc[x])} Noncomm diff shorts: {(df.NoncommercialShort.iloc[0] - df.NoncommercialShort.iloc[x])} Net Comm: {(df.CommercialLong.iloc[x] - df.CommercialShort.iloc[x])} Comm diff longs:{(df.CommercialLong.iloc[0] - df.CommercialLong.iloc[x])}  Comm diff shorts:{(df.CommercialShort.iloc[0] - df.CommercialShort.iloc[x])}\n"
# #     )


# # for x in range(0, 12):
# #     if change[x] == max(change):
# #         print(
# #             f"In the past {x} weeks the biggest change was {round((change[x]/(df.CommercialLong.iloc[x]+df.CommercialShort.iloc[x]))*100)}%"
# #         )
