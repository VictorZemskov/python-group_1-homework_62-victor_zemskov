import React, {Component} from 'react'


class UserForm extends Component {
    // в props передаются начальные данные для user
    // в дальнейшем они копируются в state и извне компонента UserForm больше не меняются
    // (всё остальное управление значением user и его полей лежит на UserForm).
    constructor(props) {
        super(props);

        // пустой объект фильма для формы создания
        const newUser = {
            username: "",
            first_name: "",
            last_name: "",
            password: "",
            passwordConfirm: "",
            email: "",
        };

        this.state = {
            // category_name: [],
            submitEnabled: true,
            // изначально user пустой (для формы добавления)
            user: newUser,
            // posterFileName: ""
            errors: {}
        };

        // если movie передан через props
        if(this.props.user) {
            // браузер запрещает программно записывать в value полей типа "file"
            // что-либо, кроме пустой строки
            // поэтому ссылку на текущий постер храним в другом свойстве и отображаем рядом
            // this.state.posterUrl = this.props.movie.poster;

            // записываем в state существующий movie
            this.state.user = this.props.user;

            // но удаляем у него значение poster
            // чтобы при сабмите формы не отправлять существующий url или пустую строку
            // (чтобы API не ругался, т.к. url и строка не являются файлами).
            // если ничего не отправлять, постер не поменяется.
            // this.state.movie.poster = null;
        }
    }



    // блокировка отправки формы на время выполнения запроса
    disableSubmit = () => {
        this.setState(prevState => {
            let newState = {...prevState};
            newState.submitEnabled = false;
            return newState;
        });
    };


     passwordsMatch = () => {
        const {password, passwordConfirm} = this.state.user;
        return password === passwordConfirm
    };
    // отправка формы
    // внутри вызывает onSubmit - переданное действие - со своим фильмом в качестве аргумента.
     submitForm = (event) => {
        if(this.state.submitEnabled) {
            event.preventDefault();
            // блокировка ???
            this.disableSubmit();

            if (this.passwordsMatch()) {
            // распаковываем данные всех полей, кроме подтверждения пароля
            // const {passwordConfirm, ...restData} = this.state.user;
            // const {password} = this.state.user;
            this.props.onSubmit(this.state.user)

            }
        }
    };

    inputChanged = (event) => {
        this.setState({
            ...this.state,
            user: {
                ...this.state.user,
                [event.target.name]: event.target.value
            }
        })
    };

    passwordConfirmChange = (event) => {
        this.inputChanged(event);
        const password = this.state.user.password;
        const passwordConfirm = event.target.value;
        const errors = (password === passwordConfirm) ? [] : ['Пароли не совпадают'];
        this.setState({
            errors: {
                ...this.state.errors,
                passwordConfirm: errors
            }
        });
    };

    showErrors = (name) => {
        if(this.state.errors && this.state.errors[name]) {
            return this.state.errors[name].map((error, index) => <p className="text-danger" key={index}>{error}</p>);
        }
        return null;
    };

    render() {
        if (this.state.user) {
            // распаковка данных фильма, чтобы было удобнее к ним обращаться
            const {username, first_name, last_name, password, passwordConfirm, email} = this.state.user;
            // распаковка переменных из state.
            const {posterFileName, submitEnabled} = this.state;



            return <div>
                <h3>Имя пользователя: {username}</h3>
                <form onSubmit={this.submitForm}>
                    <div className="form-group">
                        <label>Имя</label>
                        <input type="text" className="form-control" name="first_name" value={first_name}
                               onChange={this.inputChanged}/>
                    </div>
                    <div className="form-group">
                        <label>Фамилия</label>
                        <input type="text" className="form-control" name="last_name" value={last_name}
                               onChange={this.inputChanged}/>
                    </div>
                     <div className="form-group">
                        <label>Пароль</label>
                        <input type="text" className="form-control" name="password" value={password}
                               onChange={this.inputChanged}/>
                    </div>
                    <div className="form-group">
                        <label>Еще раз пароль</label>
                        <input type="text" className="form-control" name="passwordConfirm" value={passwordConfirm}
                               onChange={this.passwordConfirmChange}/>
                        {this.showErrors('passwordConfirm')}
                    </div>
                    <div className="form-group">
                        <label>email</label>
                        <input type="text" className="form-control" name="email" value={email}
                               onChange={this.inputChanged}/>
                    </div>
                    <button disabled={!submitEnabled} type="submit"
                            className="btn btn-primary">Сохранить
                    </button>
                </form>
            </div>;
        }
    }
}


export default UserForm;