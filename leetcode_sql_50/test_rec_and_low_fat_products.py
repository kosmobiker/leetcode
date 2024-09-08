import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")].loc[
        :, ["product_id"]
    ]


def test_find_products():
    # given
    data = [
        ["0", "Y", "N"],
        ["1", "Y", "Y"],
        ["2", "N", "Y"],
        ["3", "Y", "Y"],
        ["4", "N", "N"],
    ]
    products = pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
        {"product_id": "int64", "low_fats": "category", "recyclable": "category"}
    )
    # when
    result = find_products(products)
    # then
    assert result.reset_index(drop=True).equals(pd.DataFrame({"product_id": [1, 3]}))
