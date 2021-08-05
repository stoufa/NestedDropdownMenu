# you can also save the following structure in a JSON file

menu_structure = [
    {'label': 'Item 1', 'href': 'item-1'},
    {'label': 'Item 2', 'href': 'item-2'},
    {
        'label': 'Item 3',
        'children': [
            {'label': 'Item 3.1', 'href': 'item-3.1'},
            {
                'label': 'Item 3.2',
                'children': [
                    {'label': 'Item 3.2.1', 'href': 'item-3.2.1'},
                    {'label': 'Item 3.2.2', 'href': 'item-3.2.2'},
                    {'label': 'Item 3.2.3', 'href': 'item-3.2.3'},
                    {
                        'label': 'Item 3.2.4',
                        'children': [
                            {'label': 'Item 3.2.4.1', 'href': 'item-3.2.4.1'},
                            {'label': 'Item 3.2.4.2', 'href': 'item-3.2.4.2'},
                        ]
                    },
                ]
            },
            {'label': 'Item 3.3', 'href': 'item-3.3'},
        ]
    },
]
