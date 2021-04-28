import Axios from "axios";

async function login(email, password) {
    const res = await Axios.post("/api/login", {email, password});
    const {data} = await res;
    if (data.error) {
        return data.error
    } else {
        localStorage.setItem("access_token", data.access_token);
        return true
    }
}

function check() {
    if (localStorage.getItem("access_token")) {
        return true;
    } else {
        return false;
    }
}

function logout() {
    if (localStorage.getItem("access_token")) {
        const token = localStorage.getItem("access_token")
        Axios.post("/api/logout/access", {}, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }).then(res => {
            if (res.data.error) {
                console.error(res.data.error)
            } else {
                localStorage.removeItem("access_token")
            }
        })
    }
}

export {login, check, logout};