// Get DOM elements
const authContainer = document.getElementById('authContainer');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const loginBtn = document.querySelector('.login-btn');
const registerBtn = document.querySelector('.register-btn');
const switchToRegister = document.querySelector('.switch-to-register');
const switchToLogin = document.querySelector('.switch-to-login');

// Get form elements
const loginFormElement = document.getElementById('loginFormElement');
const registerFormElement = document.getElementById('registerFormElement');
const loginLoading = document.getElementById('loginLoading');
const registerLoading = document.getElementById('registerLoading');

// Function to show login form
function showLoginForm() {
    authContainer.classList.add('active');
    loginForm.classList.add('active');
    registerForm.classList.remove('active');
}

// Function to show register form
function showRegisterForm() {
    authContainer.classList.add('active');
    registerForm.classList.add('active');
    loginForm.classList.remove('active');
}

// Function to close auth container
function closeAuthContainer() {
    authContainer.classList.remove('active');
    loginForm.classList.remove('active');
    registerForm.classList.remove('active');
}

// Function to redirect to needs page
function redirectToNeeds() {
    window.location.href = 'needs.html';
}

// Event listeners for showing/hiding forms
loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    showLoginForm();
});

registerBtn.addEventListener('click', function(e) {
    e.preventDefault();
    showRegisterForm();
});

switchToRegister.addEventListener('click', function(e) {
    e.preventDefault();
    showRegisterForm();
});

switchToLogin.addEventListener('click', function(e) {
    e.preventDefault();
    showLoginForm();
});

// Close when clicking outside the form
authContainer.addEventListener('click', function(e) {
    if (e.target === authContainer) {
        closeAuthContainer();
    }
});

// Close with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeAuthContainer();
    }
});

// Function to validate email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Function to validate password
function isValidPassword(password) {
    return password.length >= 6;
}

// Login form submission
loginFormElement.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Reset errors
    document.getElementById('emailError').style.display = 'none';
    document.getElementById('passwordError').style.display = 'none';
    document.getElementById('email').classList.remove('input-error');
    document.getElementById('password').classList.remove('input-error');
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    let isValid = true;
    
    // Validate email
    if (!isValidEmail(email)) {
        document.getElementById('emailError').style.display = 'block';
        document.getElementById('email').classList.add('input-error');
        isValid = false;
    }
    
    // Validate password
    if (!isValidPassword(password)) {
        document.getElementById('passwordError').style.display = 'block';
        document.getElementById('password').classList.add('input-error');
        isValid = false;
    }
    
    if (isValid) {
        // Show loading indicator
        loginLoading.style.display = 'block';
        
        // Simulate authentication delay
        setTimeout(function() {
            // Hide loading indicator
            loginLoading.style.display = 'none';
            
            // Redirect to needs page
            redirectToNeeds();
        }, 1500);
    }
});

// Register form submission
registerFormElement.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Reset errors
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
    
    // Validate name
    if (!name) {
        document.getElementById('nameError').style.display = 'block';
        document.getElementById('reg-name').classList.add('input-error');
        isValid = false;
    }
    
    // Validate surname
    if (!surname) {
        document.getElementById('surnameError').style.display = 'block';
        document.getElementById('reg-surname').classList.add('input-error');
        isValid = false;
    }
    
    // Validate email
    if (!isValidEmail(email)) {
        document.getElementById('regEmailError').style.display = 'block';
        document.getElementById('reg-email').classList.add('input-error');
        isValid = false;
    }
    
    // Validate username
    if (!username) {
        document.getElementById('usernameError').style.display = 'block';
        document.getElementById('reg-username').classList.add('input-error');
        isValid = false;
    }
    
    // Validate password
    if (!isValidPassword(password)) {
        document.getElementById('regPasswordError').style.display = 'block';
        document.getElementById('reg-password').classList.add('input-error');
        isValid = false;
    }
    
    // Validate password confirmation
    if (password !== password2) {
        document.getElementById('password2Error').style.display = 'block';
        document.getElementById('reg-password2').classList.add('input-error');
        isValid = false;
    }
    
    if (isValid) {
        // Show loading indicator
        registerLoading.style.display = 'block';
        
        // Simulate registration delay
        setTimeout(function() {
            // Hide loading indicator
            registerLoading.style.display = 'none';
            
            // Redirect to needs page
            redirectToNeeds();
        }, 1500);
    }
});