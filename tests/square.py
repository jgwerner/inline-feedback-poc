test = {
	"name": "square",
	"points": 1,
	"hidden": False,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> square(1) == 1
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> square(0) == 0
					True
					""",
					"hidden": False,
					"locked": False,
				},
                {
					"code": r"""
					>>> square(2) == 4
					True
					""",
					"hidden": False,
					"locked": False,
				},
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}