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

// User Management Functions
function saveUserData(userData) {
    localStorage.setItem('userData', JSON.stringify(userData));
}

function getCurrentUser() {
    const userData = localStorage.getItem('userData');
    return userData ? JSON.parse(userData) : null;
}

function displayUsername() {
    const userNameElements = document.querySelectorAll('.user-name');
    const user = getCurrentUser();
    
    if (user && userNameElements.length > 0) {
        userNameElements.forEach(element => {
            element.textContent = `@${user.username}`;
        });
    }
}

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
    const user = getCurrentUser();
    if (user) {
        navigateTo('needs.html');
    } else {
        navigateTo('indexs_new.html');
    }
}

function logout() {
    localStorage.removeItem('userData');
    sessionStorage.removeItem('user');
    navigateTo('indexs_new.html?showLogin=true');
}

// Modal Functions
function openModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    const modal = document.getElementById('needModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

// Profile Functions
function editProfile() {
    navigateTo('change_profile.html');
}

// Image Upload Functions
function previewImage(event) {
    if (!event || !event.target || !event.target.files || event.target.files.length === 0) {
        console.error('Invalid file input event');
        return;
    }
    
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            // Find the target container using more reliable methods
            let container;
            if (event.target.id === 'imageUpload') {
                container = document.querySelector('.photo-placeholder2');
            } else {
                // For profile images
                container = document.getElementById('profileImageContainer');
            }
            
            if (!container) {
                console.error('Could not find container for image');
                return;
            }
            
            // Clear existing content and add the image
            if (container.classList.contains('photo-placeholder2')) {
                container.innerHTML = `<img src="${e.target.result}" alt="Need Image" style="width:100%;height:100%;object-fit:cover;border-radius:20px;">
                <input type="file" id="imageUpload" accept="image/*" style="display:none">`;
            } else {
                container.innerHTML = `<img src="${e.target.result}" class="avatar-image" alt="Profile Picture">`;
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
    }
}

// Re-attach event listeners for profile images
function setupProfileImageUploaders() {
    document.querySelectorAll('.profile-image').forEach(img => {
        if (!img.hasAttribute('data-listener-attached')) {
            img.setAttribute('data-listener-attached', 'true');
            img.addEventListener('click', function() {
                // Create a direct file input for this specific image
                const fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = 'image/*';
                fileInput.style.display = 'none';
                
                // Handle the file selection directly
                fileInput.addEventListener('change', function() {
                    if (this.files && this.files[0]) {
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            img.innerHTML = `<img src="${e.target.result}" class="avatar-image" alt="Profile Picture">`;
                            // Show success message if it exists
                            const successMsg = document.getElementById('uploadSuccessMessage');
                            if (successMsg) {
                                successMsg.style.display = 'block';
                                setTimeout(() => {
                                    successMsg.style.display = 'none';
                                }, 3000);
                            }
                        };
                        reader.readAsDataURL(this.files[0]);
                    }
                });
                
                // Trigger file selection
                document.body.appendChild(fileInput);
                fileInput.click();
                document.body.removeChild(fileInput);
            });
        }
    });
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
    if (loginBtn) loginBtn.addEventListener('click', (e) => { e.preventDefault(); showLoginForm(); });
    if (registerBtn) registerBtn.addEventListener('click', (e) => { e.preventDefault(); showRegisterForm(); });
    if (switchToRegister) switchToRegister.addEventListener('click', (e) => { e.preventDefault(); showRegisterForm(); });
    if (switchToLogin) switchToLogin.addEventListener('click', (e) => { e.preventDefault(); showLoginForm(); });
    
    if (authContainer) {
        authContainer.addEventListener('click', (e) => {
            if (e.target === authContainer) closeAuthContainer();
        });
    }
    
    const modalCloseButton = document.querySelector('.modal-overlay .back-button');
    if (modalCloseButton) {
        modalCloseButton.addEventListener('click', closeModal);
    }
    
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
                console.log('Navigating to About page'); 
            });
        }
    });
    
    const userProfile = document.querySelector('.user-profile');
    if (userProfile) {
        userProfile.addEventListener('click', goToProfile);
    }
    
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', (e) => {
            e.preventDefault();
            logout();
        });
    }
    
    const cardButtons = document.querySelectorAll('.card-button');
    cardButtons.forEach(button => {
        if (button.textContent === 'Перейти') {
            button.removeAttribute('onclick');
            button.addEventListener('click', openModal);
        }
    });
    
    const profileImages = document.querySelectorAll('.profile-image');
    profileImages.forEach(profileImage => {
        if (!profileImage.hasAttribute('data-listener-attached')) {
            profileImage.setAttribute('data-listener-attached', 'true');
            profileImage.addEventListener('click', function() {
                const fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = 'image/*';
                fileInput.style.display = 'none';
                fileInput.addEventListener('change', function(e) {
                    if (e.target.files && e.target.files.length > 0) {
                        const file = e.target.files[0];
                        if (file) {
                            const reader = new FileReader();
                            reader.onload = function(e) {
                                profileImage.innerHTML = `<img src="${e.target.result}" class="avatar-image" alt="Profile Picture">`;
                                const uploadMsg = document.getElementById('uploadSuccessMessage');
                                if (uploadMsg) {
                                    uploadMsg.style.display = 'block';
                                    setTimeout(() => {
                                        uploadMsg.style.display = 'none';
                                    }, 3000);
                                }
                            };
                            reader.readAsDataURL(file);
                        }
                    }
                });
                document.body.appendChild(fileInput);
                fileInput.click();
            });
        }
    });
    
    setupFormListeners();
    
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
            console.log('Profile form submitted');
            alert('Профіль успішно оновлено!');
            goToProfile();
        });
        
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
                
                setTimeout(function() {
                    const mockUser = {
                        id: 1,
                        username: email.split('@')[0],
                        email: email,
                        firstName: 'Користувач',
                        lastName: 'Системи'
                    };
                    
                    saveUserData(mockUser);
                    
                    loginLoading.style.display = 'none';
                    redirectToNeeds();
                }, 1000);
            }
        });
    }
    
    if (registerFormElement) {
        registerFormElement.addEventListener('submit', function(e) {
            e.preventDefault();
            
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
                    const mockUser = {
                        id: 1,
                        username: username,
                        email: email,
                        firstName: name,
                        lastName: surname
                    };
                    
                    saveUserData(mockUser);
                    
                    registerLoading.style.display = 'none';
                    redirectToNeeds();
                }, 1000);
            }
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    displayUsername();
    setupProfileImageUploaders(); // Add this line
    
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            setupEventListeners();
            displayUsername();
        }
    });
});

// Make functions available globally
window.navigateTo = navigateTo;
window.openModal = openModal;
window.closeModal = closeModal;
window.goToProfile = goToProfile;
window.editProfile = editProfile;
window.previewImage = previewImage;
window.logout = logout;
window.goToHome = goToHome;