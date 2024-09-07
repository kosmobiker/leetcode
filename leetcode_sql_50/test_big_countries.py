import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
	filtered = world[(world['population'] > 25000000) | (world['area'] > 3000000)]
	return filtered[['name', 'population', 'area']]


def test_find_products():
	# given
	data = [
		['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
		['Albania', 'Europe', 28748, 2831741, 12960000000],
		['Algeria', 'Africa', 2381741, 37100000, 188681000000],
		['Andorra', 'Europe', 468, 78115, 3712000000],
		['Angola', 'Africa', 1246700, 20609294, 100990000000],
	]
	world = pd.DataFrame(
		data, columns=['name', 'continent', 'area', 'population', 'gdp']
	).astype(
		{
			'name': 'object',
			'continent': 'object',
			'area': 'int64',
			'population': 'int64',
			'gdp': 'int64',
		}
	)
	# when
	result = big_countries(world)
	# then
	expected = pd.DataFrame(
		{
			'name': ['Afghanistan', 'Algeria'],
			'population': [25500100, 37100000],
			'area': [652230, 2381741],
		}
	)
	assert (
		result.reset_index(drop=True)
		.sort_values(by='name')
		.equals(expected.sort_values(by='name'))
	)
