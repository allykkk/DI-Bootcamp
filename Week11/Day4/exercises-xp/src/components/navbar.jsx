import React from "react";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <ul className="nav nav-pills">
      <li>
        <NavLink className="nav-link" activeclassname="active" to="/">
          Home
        </NavLink>
      </li>
      <li>
        <NavLink className="nav-link" activeclassname="active" to="/profile">
          Profile
        </NavLink>
      </li>
      <li>
        <NavLink className="nav-link" activeclassname="active" to="/shop">
          Shop
        </NavLink>
      </li>
    </ul>
  );
};

export default NavBar;
