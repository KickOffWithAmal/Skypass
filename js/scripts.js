// Sticky Header Logic
const header = document.querySelector('header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Intersection Observer for Scroll Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('section, .service-card, .country-card, .faq-item').forEach(el => {
    observer.observe(el);
});

// FAQ Accordion Logic
document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const item = question.parentElement;
        item.classList.toggle('active');

        // Close other items
        document.querySelectorAll('.faq-item').forEach(otherItem => {
            if (otherItem !== item) {
                otherItem.classList.remove('active');
            }
        });
    });
});

// Mobile Menu Toggle
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const nav = document.querySelector('nav');
const navLinks = document.querySelectorAll('nav a');

// Toggle menu when hamburger is clicked
mobileMenuToggle.addEventListener('click', () => {
    mobileMenuToggle.classList.toggle('active');
    nav.classList.toggle('active');
    document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
});

// Close menu when a navigation link is clicked
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenuToggle.classList.remove('active');
        nav.classList.remove('active');
        document.body.style.overflow = '';
    });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (nav.classList.contains('active') &&
        !nav.contains(e.target) &&
        !mobileMenuToggle.contains(e.target)) {
        mobileMenuToggle.classList.remove('active');
        nav.classList.remove('active');
        document.body.style.overflow = '';
    }
});

// Smooth Scrolling without '#' in URL
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');

        if (targetId === '#') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            return;
        }

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            // Offset for fixed header
            const headerOffset = 80;
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// --- Lead Capture Form Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('lead-capture-form');
    const submitBtn = document.getElementById('submit-btn');
    const formStatus = document.getElementById('form-status');
    const phoneInput = document.getElementById('phone');

    if (form) {
        // Enforce numeric characters dynamically as the user types
        phoneInput.addEventListener('input', function(e) {
            this.value = this.value.replace(/[^0-9+]/g, '');
        });

        form.addEventListener('submit', async (e) => {
            // Prevent page reload on submit
            e.preventDefault();

            // Clear previous statuses
            formStatus.style.display = 'none';
            formStatus.className = 'form-status';
            
            // Extract and map form values
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            // 1. Basic validation for required fields
            if (!data.name || !data.email || !data.phone || !data.country) {
                showStatus('Please fill in all required fields.', 'error');
                return;
            }

            // 2. Validate email format
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(data.email)) {
                showStatus('Please enter a valid email address.', 'error');
                return;
            }

            // 3. Validate phone length (minimum 10 digits)
            const numericPhone = data.phone.replace(/[^0-9]/g, '');
            if (numericPhone.length < 10) {
                showStatus('Please enter a valid phone number with at least 10 digits.', 'error');
                return;
            }

            // Set loading state UI
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Submitting... <i class="fas fa-spinner fa-spin"></i>';
            submitBtn.style.opacity = '0.7';

            try {
                // Correct AWS API Gateway Endpoint
                const API_ENDPOINT = 'https://7udivkueg1.execute-api.ap-southeast-2.amazonaws.com/lead';
                
                const response = await fetch(API_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: data.name,
                        phone: data.phone,
                        email: data.email,
                        country: data.country,
                        travelDate: data.travelDate,
                        message: data.message || ""
                    })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                // Success response handling
                showStatus('Thank you! Your request has been submitted successfully.', 'success');
                form.reset(); // Clear the form
                
            } catch (error) {
                console.error('Lead Submission Error:', error);
                showStatus('Something went wrong. Please check your connection and try again.', 'error');
            } finally {
                // Restore button state
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
                submitBtn.style.opacity = '1';
            }
        });
    }

    // Helper function to render status banner
    function showStatus(message, type) {
        formStatus.textContent = message;
        formStatus.className = `form-status status-${type}`;
        formStatus.style.display = 'block';
    }
});
