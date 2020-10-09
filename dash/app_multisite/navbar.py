# -*- coding: utf-8 -*-

# Script of the navigation bar

import dash_bootstrap_components as dbc
import config

def Navbar():
    """
    Create a Bootstrap navigation bar
    Return:
        navbar (Bootstrap NavbarSimple): navigation bar
    """

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Training", href=config.training_url)),
            dbc.NavItem(dbc.NavLink("Classification", href=config.classification_url)),
            dbc.NavItem(dbc.NavLink("Login", href=config.login_url)),
            # dbc.DropdownMenu(
            #     nav=True,
            #     in_navbar=True,
            #     label="Menu",
            #     children=[
            #         dbc.DropdownMenuItem("Entry 1"),
            #         dbc.DropdownMenuItem("Entry 2"),
            #         dbc.DropdownMenuItem(divider=True),
            #         dbc.DropdownMenuItem("Entry 3"),
            #         ],
            #     ),
            ],
            brand="Home",
            brand_href=config.home_url,
            sticky="top",
    )
    return navbar