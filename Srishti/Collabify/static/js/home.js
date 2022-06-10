function display(element) {
    document.querySelector(element).style.display = "block";
}

function hide(element) {
    document.querySelector(element).style.display = "none";
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#login").addEventListener('click', () => {
        display(".login");
    });
    document.querySelector("#register").addEventListener('click', () => {
        display(".register");
    });
    document.querySelector("#exitlogin").addEventListener('click', () => {
        hide(".login");
    });
    document.querySelector("#exitregister").addEventListener('click', () => {
        hide(".register");
    });

    document.querySelector("#registerform").addEventListener('click', () => {
        let password = document.querySelector("#pass").value;
        let confirmpassword = document.querySelector("#cpass").value;

        console.log(password);
        console.log(confirmpassword);

        if (password != confirmpassword) {
            alert("Passwords don't match");
            return false;
        }
    })
})