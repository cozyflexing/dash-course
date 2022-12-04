# calculations
def commercial_short_percentage(df):
    result = (df.CommercialShort / (df.CommercialLong + df.CommercialShort)) * 100
    return result


def commercial_long_percentage(df):
    result = (df.CommercialLong / (df.CommercialLong + df.CommercialShort)) * 100
    return result


def non_commercial_short_percentage(df):
    result = (
        df.NoncommercialShort / (df.NoncommercialLong + df.NoncommercialShort)
    ) * 100
    return result


def non_commercial_long_percentage(df):
    result = (
        df.NoncommercialLong / (df.NoncommercialLong + df.NoncommercialShort)
    ) * 100
    return result


def nonreportable_short_percentage(df):
    result = (
        df.NonreportablePositionsShort
        / (df.NonreportablePositionsLong + df.NonreportablePositionsShort)
    ) * 100
    return result


def nonreportable_long_percentage(df):
    result = (
        df.NonreportablePositionsLong
        / (df.NonreportablePositionsLong + df.NonreportablePositionsShort)
    ) * 100
    return result
