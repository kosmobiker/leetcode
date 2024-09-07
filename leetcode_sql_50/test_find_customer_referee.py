import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
	return customer[
		(customer['referee_id'].isna()) | (customer['referee_id'] != 2)
	].loc[:, ['name']]


def test_find_customer_referee():
	# given
	data = [
		[1, 'Will', None],
		[2, 'Jane', None],
		[3, 'Alex', 2],
		[4, 'Bill', None],
		[5, 'Zack', 1],
		[6, 'Mark', 2],
	]
	customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype(
		{'id': 'Int64', 'name': 'object', 'referee_id': 'Int64'}
	)

	# when
	result = find_customer_referee(customer)

	# then
	assert result.reset_index(drop=True).equals(
		pd.DataFrame(['Will', 'Jane', 'Bill', 'Zack'], columns=['name']).astype(
			{'name': 'object'}
		)
	)
