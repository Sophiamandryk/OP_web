const authContainer = document.getElementById('authContainer');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const loginBtn = document.querySelector('.login-btn');
const registerBtn = document.querySelector('.register-btn');
const switchToRegister = document.querySelector('.switch-to-register');
const switchToLogin = document.querySelector('.switch-to-login');


const loginFormElement = document.getElementById('loginFormElement');
const registerFormElement = document.getElementById('registerFormElement');
const loginLoading = document.getElementById('loginLoading');
const registerLoading = document.getElementById('registerLoading');
const logoutButton = document.getElementById('logoutButton');


function showLoginForm() {
    authContainer.classList.add('active');
    loginForm.classList.add('active');
    registerForm.classList.remove('active');
}

function showRegisterForm() {
    authContainer.classList.add('active');
    registerForm.classList.add('active');
    loginForm.classList.remove('active');
}


function closeAuthContainer() {
    authContainer.classList.remove('active');
    loginForm.classList.remove('active');
    registerForm.classList.remove('active');
}

function redirectToNeeds() {
    window.location.href = 'detailed_needs.html';
}


if (loginBtn) {
    loginBtn.addEventListener('click', function(e) {
        e.preventDefault();
        showLoginForm();
    });
}

if (registerBtn) {
    registerBtn.addEventListener('click', function(e) {
        e.preventDefault();
        showRegisterForm();
    });
}

if (switchToRegister) {
    switchToRegister.addEventListener('click', function(e) {
        e.preventDefault();
        showRegisterForm();
    });
}

if (switchToLogin) {
    switchToLogin.addEventListener('click', function(e) {
        e.preventDefault();
        showLoginForm();
    });
}


if (authContainer) {
    authContainer.addEventListener('click', function(e) {
        if (e.target === authContainer) {
            closeAuthContainer();
        }
    });
}


document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeAuthContainer();
    }
});


function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}


function isValidPassword(password) {
    return password.length >= 6;
}


if (loginFormElement) {
    loginFormElement.addEventListener('submit', function(e) {
        e.preventDefault();
        

        document.getElementById('emailError').style.display = 'none';
        document.getElementById('passwordError').style.display = 'none';
        document.getElementById('email').classList.remove('input-error');
        document.getElementById('password').classList.remove('input-error');
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        let isValid = true;
        

        if (!isValidEmail(email)) {
            document.getElementById('emailError').style.display = 'block';
            document.getElementById('email').classList.add('input-error');
            isValid = false;
        }
        

        if (!isValidPassword(password)) {
            document.getElementById('passwordError').style.display = 'block';
            document.getElementById('password').classList.add('input-error');
            isValid = false;
        }
        
        if (isValid) {

            loginLoading.style.display = 'block';
            

            loginLoading.style.display = 'block';
            
            fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
            })
            .then(response => response.json())
            .then(data => {

                loginLoading.style.display = 'none';
                
                if (data.success) {

                    redirectToNeeds();
                } else {

                    alert(data.message || 'Невірний email або пароль');
                }
            })
            .catch(error => {
                loginLoading.style.display = 'none';
                alert('Помилка при вході. Спробуйте ще раз.');
                console.error('Error:', error);
            });
        }
    });
}


if (registerFormElement) {
    registerFormElement.addEventListener('submit', function(e) {
        e.preventDefault();
        

        document.getElementById('nameError').style.display = 'none';
        document.getElementById('surnameError').style.display = 'none';
        document.getElementById('regEmailError').style.display = 'none';
        document.getElementById('usernameError').style.display = 'none';
        document.getElementById('regPasswordError').style.display = 'none';
        document.getElementById('password2Error').style.display = 'none';
        
        document.getElementById('reg-name').classList.remove('input-error');
        document.getElementById('reg-surname').classList.remove('input-error');
        document.getElementById('reg-email').classList.remove('input-error');
        document.getElementById('reg-username').classList.remove('input-error');
        document.getElementById('reg-password').classList.remove('input-error');
        document.getElementById('reg-password2').classList.remove('input-error');
        
        const name = document.getElementById('reg-name').value;
        const surname = document.getElementById('reg-surname').value;
        const email = document.getElementById('reg-email').value;
        const username = document.getElementById('reg-username').value;
        const password = document.getElementById('reg-password').value;
        const password2 = document.getElementById('reg-password2').value;
        
        let isValid = true;
        

        if (!name) {
            document.getElementById('nameError').style.display = 'block';
            document.getElementById('reg-name').classList.add('input-error');
            isValid = false;
        }
        

        if (!surname) {
            document.getElementById('surnameError').style.display = 'block';
            document.getElementById('reg-surname').classList.add('input-error');
            isValid = false;
        }
        

        if (!isValidEmail(email)) {
            document.getElementById('regEmailError').style.display = 'block';
            document.getElementById('reg-email').classList.add('input-error');
            isValid = false;
        }
        

        if (!username) {
            document.getElementById('usernameError').style.display = 'block';
            document.getElementById('reg-username').classList.add('input-error');
            isValid = false;
        }
        

        if (!isValidPassword(password)) {
            document.getElementById('regPasswordError').style.display = 'block';
            document.getElementById('reg-password').classList.add('input-error');
            isValid = false;
        }
        

        if (password !== password2) {
            document.getElementById('password2Error').style.display = 'block';
            document.getElementById('reg-password2').classList.add('input-error');
            isValid = false;
        }
        
        if (isValid) {

            registerLoading.style.display = 'block';
            

            setTimeout(function() {

                registerLoading.style.display = 'none';
                

                redirectToNeeds();
            }, 1500);
        }
    });
}


function openModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.add('active');
    }
}

function closeModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.remove('active');
    }
}


function goToProfile() {

    console.log('Navigating to profile');
}

if (logoutButton) {
    logoutButton.addEventListener('click', function(e) {
        e.preventDefault();
       
        window.location.href = 'indexs_new.html?showLogin=true';
    });
}


document.addEventListener('DOMContentLoaded', function() {

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('showLogin') === 'true') {

        showLoginForm();
    }
});

function previewImage(event) {
    const output = event.target.parentElement;
    if (event.target.files && event.target.files[0]) {
        const reader = new FileReader();
        reader.onload = function() {
            const img = document.createElement('img');
            img.src = reader.result;
            output.innerHTML = '';
            output.appendChild(img);
        };
        reader.readAsDataURL(event.target.files[0]);
    }
}

const homeLink = document.getElementById('homeLink');
if (homeLink) {
    homeLink.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = 'indexs_new.html';
    });
}