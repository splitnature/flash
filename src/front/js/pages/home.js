import React, { useState, useEffect, useContext } from "react";
import "../../styles/home.scss";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Home = () => {
	const { store, actions } = useContext(Context);
	useEffect(() => {
		// Update the document title using the browser API
		actions.getUsers();
	}, []);
	return (
		<div className="content col-8 text-center mt-5 mx-auto">
			<div className="col1 col-6">
				<img className="img" src="https://studycli.org/wp-content/uploads/2021/06/Chinese-Flashcards-01.jpg" />
			</div>
			<div className="col2 col-4">
				<form className="signIn">
					<label htmlFor="UserName">User</label>
					<input
						className="UserName p-2 m-3 w-80"
						type="text"
						id="UserName"
						name="UserName"
						placeholder="User"
					/>
					<label htmlFor="Password">Password</label>
					<input
						className="Password p-2 m-3 w-80"
						type="text"
						id="password"
						name="Password"
						placeholder="Password"
					/>
					<button className="bg-warning p-3 w-50 mx-auto">Join!</button>
				</form>
			</div>
		</div>
	);
};
