CONTRACT_METADATA = {
    "address": "0x973cFFcBd1c941A0d6341A4528bD635351e2dF5f",
    "abi": [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"components": [
					{
						"internalType": "string",
						"name": "id",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "addr",
						"type": "address"
					}
				],
				"internalType": "struct Info",
				"name": "employee_info",
				"type": "tuple"
			}
		],
		"name": "addEmployeeToOrganization",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "id",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "addr",
						"type": "address"
					}
				],
				"internalType": "struct Info",
				"name": "org_info",
				"type": "tuple"
			},
			{
				"components": [
					{
						"internalType": "string",
						"name": "id",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "addr",
						"type": "address"
					}
				],
				"internalType": "struct Info[]",
				"name": "employee_infos",
				"type": "tuple[]"
			}
		],
		"name": "addOrganization",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "employee_id",
				"type": "string"
			}
		],
		"name": "removeEmployeeFromOrganization",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			}
		],
		"name": "removeOrganization",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "employee_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "review",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "action_id",
				"type": "string"
			}
		],
		"name": "sendEmployeeReview",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "review",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "action_id",
				"type": "string"
			}
		],
		"name": "sendOrganizationReview",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "employee_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "review",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "action_id",
				"type": "string"
			}
		],
		"name": "sendTipsToEmployee",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "review",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "action_id",
				"type": "string"
			}
		],
		"name": "sendTipsToOrganization",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			}
		],
		"name": "getAllEmployeeInOrganization",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllOrganizations",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "employee_id",
				"type": "string"
			}
		],
		"name": "getEmployeeReviews",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "reviews",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "organization_id",
				"type": "string"
			}
		],
		"name": "getOrganizationReviews",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "reviews",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
}