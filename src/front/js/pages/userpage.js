import React from "react";
import "../../styles/home.scss";
import { Context } from "../store/appContext";

export const userpage = () => {
return (
    <div className="content mx-auto">
        <div className="col1 ">
            <section>
                <h1>Welcome</h1>
                <h3>name</h3>
                <h3>first</h3>
                <h3>Last</h3>
            </section>
        </div>
        <div className="col2">
            <section>
            <h1>Cards</h1>
                <h3>cards</h3>
                <h3>decks</h3>
                <h3>authors</h3>
            </section>
        </div>
    </div>
)
}