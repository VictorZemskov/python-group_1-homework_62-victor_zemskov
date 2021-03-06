import React, {Component, Fragment} from 'react'
import MenuItem from "./MenuItem/MenuItem";
import {connect} from "react-redux";



class Menu extends Component {
    state = {
        collapse: true
    };

    toggle = () => {
        this.setState({collapse: !this.state.collapse});
    };

    render() {
        // const username = localStorage.getItem('username');
        // является строкой, поэтому сравниваем с "true"
        // const isAdmin = localStorage.getItem('is_admin');
        const {username, is_admin, user_id} = this.props.auth;
        return <Fragment>
            <button onClick={this.toggle}
                    className="navbar-toggler"
                    type="button"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"/>
            </button>
            <div className={(this.state.collapse ? "collapse" : "") + " navbar-collapse"}
                 id="navbarNav">
                <ul className="navbar-nav mr-auto">
                    <MenuItem to="/">Фильмы</MenuItem>
                    <MenuItem to="/halls">Залы</MenuItem>
                    {is_admin === "true" ? [ <MenuItem to="/movies/add">Добавить фильм</MenuItem>,
                                            <MenuItem to="/halls/add">Добавить зал</MenuItem> ]: null}
                </ul>

                <ul className="navbar-nav ml-auto">
                    {user_id ? [
                        <MenuItem to={"/users/" + user_id}>{username}</MenuItem>,
                        <MenuItem to="/logout" key="logout">Выйти</MenuItem>
                    ] : [
                        <MenuItem to="/login" key="login">Войти</MenuItem>,
                        <MenuItem to="/register" key="register">Зарегистрироваться</MenuItem>
                    ]}
                </ul>
            </div>
        </Fragment>
    }
}

const mapStateToProps = state => ({auth: state.auth});
const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps) (Menu);