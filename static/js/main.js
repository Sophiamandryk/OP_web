// DOM Elements
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

// Navigation Functions
function navigateTo(page) {
    window.location.href = page;
}

function showLoginForm() {
    if (authContainer) {
        authContainer.classList.add('active');
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
    }
}

function showRegisterForm() {
    if (authContainer) {
        authContainer.classList.add('active');
        registerForm.classList.add('active');
        loginForm.classList.remove('active');
    }
}

function closeAuthContainer() {
    if (authContainer) {
        authContainer.classList.remove('active');
        loginForm.classList.remove('active');
        registerForm.classList.remove('active');
    }
}

function redirectToNeeds() {
    navigateTo('detailed_needs.html');
}

function goToProfile() {
    navigateTo('profile.html');
}

function goToHome() {
    navigateTo('indexs_new.html');
}

function logout() {
    // Clear any stored user data (cookies, localStorage, etc)
    localStorage.removeItem('user');
    sessionStorage.removeItem('user');
    
    // Redirect to home page with login prompt
    navigateTo('indexs_new.html?showLogin=true');
}

// Modal Functions
function openModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    }
}

function closeModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto'; // Enable scrolling
    }
}

// Profile Functions
function editProfile() {
    navigateTo('change_profile.html');
}

// Image Upload Functions
function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const container = event.target.parentElement;
            // If container is a div with class "photo-placeholder2"
            if (container.classList.contains('photo-placeholder2')) {
                container.innerHTML = `<img src="${e.target.result}" alt="Need Image" style="width:100%;height:100%;object-fit:cover;border-radius:20px;">`;
            } 
            // If container is the profile image container
            else if (container.classList.contains('profile-image')) {
                container.innerHTML = `<img src="${e.target.result}" alt="Profile Image" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">`;
            }
            
            // Show success message if exists
            const successMessage = document.getElementById('uploadSuccessMessage');
            if (successMessage) {
                successMessage.style.display = 'block';
                setTimeout(() => {
                    successMessage.style.display = 'none';
                }, 3000);
            }
        };
        
        reader.readAsDataURL(file);
        
        // Here you'd typically upload the file to server
        console.log('File would be uploaded to server:', file.name);
    }
}

// Form Validation Functions
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPassword(password) {
    return password.length >= 6;
}

// Event Listeners Setup - Called when DOM is loaded
function setupEventListeners() {
    // Auth buttons
    if (loginBtn) loginBtn.addEventListener('click', (e) => { e.preventDefault(); showLoginForm(); });
    if (registerBtn) registerBtn.addEventListener('click', (e) => { e.preventDefault(); showRegisterForm(); });
    if (switchToRegister) switchToRegister.addEventListener('click', (e) => { e.preventDefault(); showRegisterForm(); });
    if (switchToLogin) switchToLogin.addEventListener('click', (e) => { e.preventDefault(); showLoginForm(); });
    
    // Close modal when clicking outside
    if (authContainer) {
        authContainer.addEventListener('click', (e) => {
            if (e.target === authContainer) closeAuthContainer();
        });
    }
    
    // Modal close button
    const modalCloseButton = document.querySelector('.modal-overlay .back-button');
    if (modalCloseButton) {
        modalCloseButton.addEventListener('click', closeModal);
    }
    
    // Navigation links
    const homeLinks = document.querySelectorAll('.nav-link[href="#"]');
    homeLinks.forEach(link => {
        if (link.textContent === 'Головна') {
            link.addEventListener('click', (e) => { 
                e.preventDefault();
                goToHome(); 
            });
        } else if (link.textContent === 'Про нас') {
            link.addEventListener('click', (e) => { 
                e.preventDefault(); 
                // In a real app, you'd navigate to about page
                console.log('Navigating to About page'); 
            });
        }
    });
    
    // User profile area
    const userProfile = document.querySelector('.user-profile');
    if (userProfile) {
        userProfile.addEventListener('click', goToProfile);
    }
    
    // Logout button
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', (e) => {
            e.preventDefault();
            logout();
        });
    }
    
    // "Перейти" buttons on needs cards
    const cardButtons = document.querySelectorAll('.card-button');
    cardButtons.forEach(button => {
        if (button.textContent === 'Перейти') {
            button.addEventListener('click', openModal);
        }
    });
    
    // Edit profile button
    const editProfileButton = document.getElementById('editProfileButton');
    if (editProfileButton) {
        editProfileButton.addEventListener('click', editProfile);
    }
    
    // Profile image upload
    const profileImage = document.querySelector('.profile-image');
    if (profileImage && !profileImage.querySelector('input')) {
        profileImage.addEventListener('click', () => {
            // Create file input if it doesn't exist
            let fileInput = document.getElementById('profilePictureInput');
            if (!fileInput) {
                fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.id = 'profilePictureInput';
                fileInput.accept = 'image/*';
                fileInput.style.display = 'none';
                fileInput.addEventListener('change', previewImage);
                document.body.appendChild(fileInput);
            }
            fileInput.click();
        });
    }
    
    // Form submissions
    setupFormListeners();
    
    // Profile form in change_profile.html
    const profileForm = document.querySelector('.container form');
    if (profileForm) {
        const cancelBtn = profileForm.querySelector('.btn-cancel');
        if (cancelBtn) {
            cancelBtn.addEventListener('click', (e) => {
                e.preventDefault();
                goToProfile();
            });
        }
        
        profileForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // In a real app, you'd send form data to server
            console.log('Profile form submitted');
            
            // Show success message
            alert('Профіль успішно оновлено!');
            
            // Redirect back to profile
            goToProfile();
        });
        
        // Photo placeholder upload
        const photoPlaceholder = document.querySelector('.photo-placeholder .profile-image');
        if (photoPlaceholder) {
            photoPlaceholder.addEventListener('click', () => {
                const fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = 'image/*';
                fileInput.style.display = 'none';
                fileInput.addEventListener('change', previewImage);
                document.body.appendChild(fileInput);
                fileInput.click();
            });
        }
    }
    
    // Check URL params for showing login
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('showLogin') === 'true') {
        showLoginForm();
    }
}

// Setup form submission listeners
function setupFormListeners() {
    if (loginFormElement) {
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
                
                // In a real app, you'd send a fetch request
                // Simulate successful login
                setTimeout(function() {
                    loginLoading.style.display = 'none';
                    redirectToNeeds();
                }, 1000);
            }
        });
    }
    
    if (registerFormElement) {
        registerFormElement.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset errors
            const errorElements = ['nameError', 'surnameError', 'regEmailError', 'usernameError', 'regPasswordError', 'password2Error'];
            const inputElements = ['reg-name', 'reg-surname', 'reg-email', 'reg-username', 'reg-password', 'reg-password2'];
            
            errorElements.forEach(id => {
                const element = document.getElementById(id);
                if (element) element.style.display = 'none';
            });
            
            inputElements.forEach(id => {
                const element = document.getElementById(id);
                if (element) element.classList.remove('input-error');
            });
            
            // Get form values
            const name = document.getElementById('reg-name').value;
            const surname = document.getElementById('reg-surname').value;
            const email = document.getElementById('reg-email').value;
            const username = document.getElementById('reg-username').value;
            const password = document.getElementById('reg-password').value;
            const password2 = document.getElementById('reg-password2').value;
            
            let isValid = true;
            
            // Validate fields
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
                // Show loading indicator
                registerLoading.style.display = 'block';
                
                // In a real app, you'd send a fetch request
                // Simulate successful registration
                setTimeout(function() {
                    registerLoading.style.display = 'none';
                    redirectToNeeds();
                }, 1000);
            }
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', setupEventListeners);

// Make functions available globally
window.navigateTo = navigateTo;
window.openModal = openModal;
window.closeModal = closeModal;
window.goToProfile = goToProfile;
window.editProfile = editProfile;
window.previewImage = previewImage;
window.logout = logout;
window.goToHome = goToHome;