import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-warning p-3 border-bottom ">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1 text-dark">Home</span>
				</Link>
				<Link to="/cardpage.js">cardpage</Link>
				<div className="ml-auto">
					<Link to="/userpage.js">Userpage</Link>
				</div>
			</div>
		</nav>
	);
};
