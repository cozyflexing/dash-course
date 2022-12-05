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


def total_open_interest_commercial(df):
    result = abs(df.CommercialLong) + abs(df.CommercialShort)
    return result


def total_open_interest_noncommercial(df):
    result = abs(df.NoncommercialLong) + abs(df.NoncommercialShort)
    return result


def total_open_interest_nonreportable(df):
    result = abs(df.NonreportablePositionsLong) + abs(df.NonreportablePositionsShort)
    return result


def total_open_interest(df):
    result = (
        total_open_interest_commercial(df)
        + total_open_interest_noncommercial(df)
        + total_open_interest_nonreportable(df)
    )
    return result
