<<<<<<< HEAD
/* -----------------------------------------------------
# Assignment: Final Project - Software Testing Tools
# Written by: Prudhvi Teja Reddy Kandula (Student ID: 5805128)
# Short Description:
# This script manages all dynamic behavior for the NextGenGadgets site,
# including product filtering, cart persistence, drag-and-drop,
# sortable tables, and security validation for the registration process.
# ----------------------------------------------------- */

// --- 1. Product Data Definition ---
const products = [
    // Laptops (4 Total)
    { id: 'L001', name: 'Apple Macbook M4 Chip', category: 'laptops', price: 1500.00, image: 'images/laptops/AppleMacbookM4Chip.jpg', specs: 'M4 Chip, 16GB RAM, 512GB SSD. Perfect for high-performance tasks.' },
    { id: 'L002', name: 'Apple Macbook Pro', category: 'laptops', price: 1800.00, image: 'images/laptops/AppleMacbookPro.jpg', specs: 'M3 Pro, 18GB RAM, 1TB SSD. Studio-grade performance.' },
    { id: 'L003', name: 'Lenovo Thinkpad', category: 'laptops', price: 1100.00, image: 'images/laptops/LenovoThinkpad.jpg', specs: 'Intel i7, 32GB RAM, 1TB SSD. Business-class durability.' },
    { id: 'L004', name: 'Microsoft Surface Laptop', category: 'laptops', price: 1350.00, image: 'images/laptops/MicrosoftSurfaceLaptop.jpg', specs: 'PixelSense display, 16GB RAM, 512GB SSD. Premium design and touch support.' },

    // Smartphones (10 Total)
    { id: 'S001', name: 'Apple iPhone 15', category: 'smartphones', price: 799.00, image: 'images/smartphones/AppleiPhone15.jpg', specs: 'A16 Bionic, 6.1" display. Great camera system.' },
    { id: 'S002', name: 'Apple iPhone 15 Plus', category: 'smartphones', price: 899.00, image: 'images/smartphones/AppleiPhone15Plus.jpg', specs: 'A16 Bionic, 6.7" display. Longer battery life.' },
    { id: 'S003', name: 'Apple iPhone 16', category: 'smartphones', price: 999.00, image: 'images/smartphones/AppleiPhone16.jpg', specs: 'Next-Gen A-series, 6.1" display. Enhanced features.' },
    { id: 'S004', name: 'Apple iPhone 16e', category: 'smartphones', price: 699.00, image: 'images/smartphones/AppleiPhone16e.jpg', specs: 'Compact and efficient model.' },
    { id: 'S005', name: 'Apple iPhone 16 Plus', category: 'smartphones', price: 1099.00, image: 'images/smartphones/AppleiPhone16Plus.jpg', specs: 'Next-Gen A-series, 6.7" display. Large screen experience.' },
    { id: 'S006', name: 'Apple iPhone 16 Pro', category: 'smartphones', price: 1299.00, image: 'images/smartphones/AppleiPhone16Pro.jpg', specs: 'Pro features, 120Hz display, superior camera.' },
    { id: 'S007', name: 'Apple iPhone 16 Pro Max', category: 'smartphones', price: 1499.00, image: 'images/smartphones/AppleiPhone16ProMax.jpg', specs: 'The ultimate flagship, best camera and battery.' },
    { id: 'S008', name: 'Google Pixel 9', category: 'smartphones', price: 699.00, image: 'images/smartphones/GooglePixel9.jpg', specs: 'Tensor G4, advanced AI features. Best in class computational photography.' },
    { id: 'S009', name: 'Samsung S24', category: 'smartphones', price: 799.00, image: 'images/smartphones/SamsungS24.jpg', specs: 'Compact flagship, stunning dynamic AMOLED display.' },
    { id: 'S010', name: 'Samsung S24 Ultra', category: 'smartphones', price: 1299.00, image: 'images/smartphones/SamsungS24Ultra.jpg', specs: 'Snapdragon, S Pen integrated. Stunning dynamic AMOLED display.' },

    // Watches (6 Total)
    { id: 'W001', name: 'Apple Watch Hermès Series 10', category: 'watches', price: 1399.00, image: 'images/watches/AppleWatchHermèsSeries10.jpg', specs: 'Premium Hermès band, exclusive watch faces.' },
    { id: 'W002', name: 'Apple Watch Hermès Ultra 2', category: 'watches', price: 1799.00, image: 'images/watches/AppleWatchHermèsUltra2.jpg', specs: 'Rugged titanium case with premium Hermès band.' },
    { id: 'W003', name: 'Apple Watch SE', category: 'watches', price: 249.00, image: 'images/watches/AppleWatchSE.jpg', specs: 'Essential features for fitness and connectivity.' },
    { id: 'W004', name: 'Apple Watch Series 10', category: 'watches', price: 450.00, image: 'images/watches/AppleWatchSeries10.jpg', specs: 'S10 Chip, new health sensors. Our most advanced watch yet.' },
    { id: 'W005', name: 'Apple Watch Ultra 2', category: 'watches', price: 799.00, image: 'images/watches/AppleWatchUltra2.jpg', specs: 'Rugged titanium case, extreme battery life. For the adventurers.' },
    { id: 'W006', name: 'OnePlus Watch 2', category: 'watches', price: 299.00, image: 'images/watches/OnePlusWatch2.jpg', specs: 'Long-lasting battery, comprehensive fitness tracking.' }
];

// --- 2. Cart Data & Persistence Functions ---

const INITIAL_MOCK_CART = [
    // Mock data used if localStorage is empty to ensure drag-and-drop/remove features can be tested immediately.
    { id: 'L002', name: 'Apple Macbook Pro', price: 1800.00, quantity: 1 },
    { id: 'S007', name: 'Apple iPhone 16 Pro Max', price: 1499.00, quantity: 1 },
    { id: 'W005', name: 'Apple Watch Ultra 2', price: 799.00, quantity: 2 },
];

let cartItems = []; // Will be populated by loadCartFromLocal()

function saveCartToLocal() {
    // Saves the current state of cartItems to the browser's local storage
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
}

function loadCartFromLocal() {
    const localData = localStorage.getItem('cartItems');
    if (localData) {
        // Load existing data from storage
        cartItems = JSON.parse(localData);
    } else {
        // If nothing is stored, use the mock data for the first time and save it.
        cartItems = INITIAL_MOCK_CART;
        saveCartToLocal();
    }
}

function updateDateTime() {
    const dateTimeElement = document.getElementById('current-date-time');
    if (dateTimeElement) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' };
        dateTimeElement.textContent = now.toLocaleDateString('en-US', options);
    }
}

function updateCartTotal(action) {
    const cartBadge = document.getElementById('cart-total-items');
    if (!cartBadge) return;

    // Recalculate based on current cartItems for accuracy
    const totalCount = cartItems.reduce((acc, item) => acc + item.quantity, 0);
    cartBadge.textContent = totalCount;

    // Since the cart changed, save the new state
    saveCartToLocal();
}

// --- 3. Product Display and Filtering ---

function renderProducts(filterCategory = 'all', searchTerm = '') {
    const grid = document.getElementById('product-grid');
    if (!grid) return;

    grid.innerHTML = '';
    const lowerCaseSearchTerm = searchTerm.toLowerCase();

    let filteredProducts = products.filter(p => {
        const categoryMatch = filterCategory === 'all' || p.category.toLowerCase() === filterCategory.toLowerCase();

        const searchMatch = !searchTerm ||
            p.name.toLowerCase().includes(lowerCaseSearchTerm) ||
            p.category.toLowerCase().includes(lowerCaseSearchTerm);

        return categoryMatch && searchMatch;
    });

    if (filteredProducts.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1 / -1; text-align: center;">No products found matching your filter criteria.</p>';
        return;
    }

    grid.style.opacity = 0;
    setTimeout(() => {
        filteredProducts.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.setAttribute('data-id', product.id);
            const price = product.price.toFixed(2);

            card.innerHTML = `
                <img src="${product.image}" alt="${product.name}">
                <h4 class="product-name-link" data-product-id="${product.id}">${product.name}</h4>
                <p><strong>$${price}</strong></p>
                <button class="add-to-cart-btn" data-product-id="${product.id}">Add to Cart</button>
                <button class="view-details-btn product-name-link" data-product-id="${product.id}">View Details</button>
            `;

            grid.appendChild(card);
        });

        grid.style.opacity = 1;
    }, 500);
}

// --- 4. Modal Interaction ---

function openProductModal(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    const modal = document.getElementById('product-modal');
    if (!modal) return;

    document.getElementById('modal-product-name').textContent = product.name;
    document.getElementById('modal-product-specs').innerHTML = `
        <p><strong>Price:</strong> $${product.price.toFixed(2)}</p>
        <p><strong>Category:</strong> ${product.category}</p>
        <p><strong>Specifications:</strong> ${product.specs}</p>
        <hr>
        <h5>What's in the Box:</h5>
        <ul>
            <li>The device itself</li>
            <li>Charging Cable</li>
            <li>User Manual</li>
        </ul>
    `;
    modal.style.display = 'block';

    modal.querySelector('.modal-add-to-cart-btn').onclick = () => {
        // Find if item exists, if so increment quantity, otherwise add new item
        let cartItem = cartItems.find(item => item.id === productId);
        if (cartItem) {
            cartItem.quantity++;
        } else {
            cartItems.push({ id: product.id, name: product.name, price: product.price, quantity: 1 });
        }

        updateCartTotal('add'); // Calls saveCartToLocal
        alert(`${product.name} added to cart!`);
        modal.style.display = 'none';
    };
}

function closeProductModal() {
    const modal = document.getElementById('product-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// --- 5. FAQ Accordion Functionality ---

function setupFaqAccordion() {
    const headers = document.querySelectorAll('.accordion-header');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;
            const content = item.querySelector('.accordion-content');

            document.querySelectorAll('.accordion-item.active').forEach(activeItem => {
                if (activeItem !== item) {
                    activeItem.classList.remove('active');
                    activeItem.querySelector('.accordion-content').style.maxHeight = 0;
                }
            });

            item.classList.toggle('active');
            if (item.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = 0;
            }
        });
    });
}

// --- 6. Sortable Table Functionality (For orders.html) ---

function setupSortableTable() {
    const table = document.getElementById('order-history-table');
    if (!table) return;

    const headers = table.querySelectorAll('th[data-sort-key]');
    const tbody = table.querySelector('tbody');
    let sortDirection = {};

    function getColIndex(key, table) {
        const headerRow = table.querySelector('thead tr');
        const headers = Array.from(headerRow.querySelectorAll('th'));
        for (let i = 0; i < headers.length; i++) {
            if (headers[i].getAttribute('data-sort-key') === key) {
                return i;
            }
        }
        return -1;
    }

    function sortData(key, direction, tbody) {
        const colIndex = getColIndex(key, table);
        if (colIndex === -1) return;

        let rows = Array.from(tbody.querySelectorAll('tr'));

        rows.sort((a, b) => {
            let aValue = a.cells[colIndex].getAttribute('data-sort-value') || a.cells[colIndex].textContent.trim();
            let bValue = b.cells[colIndex].getAttribute('data-sort-value') || b.cells[colIndex].textContent.trim();

            if (!isNaN(aValue) && !isNaN(bValue)) {
                aValue = parseFloat(aValue.toString().replace('$', '').replace(',', ''));
                bValue = parseFloat(bValue.toString().replace('$', '').replace(',', ''));
            }

            let comparison = 0;
            if (aValue > bValue) {
                comparison = 1;
            } else if (aValue < bValue) {
                comparison = -1;
            }

            return direction === 'asc' ? comparison : comparison * -1;
        });

        rows.forEach(row => tbody.appendChild(row));
    }

    headers.forEach(header => {
        const key = header.getAttribute('data-sort-key');
        header.addEventListener('click', () => {
            const isAsc = sortDirection[key] === 'asc';
            const direction = isAsc ? 'desc' : 'asc';
            sortDirection[key] = direction;

            sortData(key, direction, tbody);

            headers.forEach(h => {
                const icon = h.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-sort-up', 'fa-sort-down');
                    icon.classList.add('fa-sort');
                }
            });
            const clickedIcon = header.querySelector('i');
            if (clickedIcon) {
                clickedIcon.classList.remove('fa-sort');
                clickedIcon.classList.add(direction === 'asc' ? 'fa-sort-up' : 'fa-sort-down');
            }
        });
    });
}


// --- 7. Cart Page Functionality ---

const cartTableBody = document.getElementById('draggable-cart-list');

function renderCartItems() {
    if (!cartTableBody) return;

    // Clear existing content
    cartTableBody.innerHTML = '';
    let subtotal = 0;

    if (cartItems.length === 0) {
        cartTableBody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 30px;">Your cart is empty.</td></tr>';
    } else {
        cartItems.forEach((item, index) => {
            const row = document.createElement('tr');
            const total = item.price * item.quantity;
            subtotal += total;

            row.setAttribute('draggable', 'true'); // For drag-and-drop
            row.setAttribute('data-cart-id', item.id);
            row.setAttribute('data-index', index);
            row.className = 'cart-item-row';

            row.innerHTML = `
                <td>${item.name}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td><input type="number" value="${item.quantity}" min="1" style="width: 50px;" data-item-index="${index}" class="quantity-input"></td>
                <td>$${total.toFixed(2)}</td>
                <td><button class="remove-item-btn" data-item-index="${index}">Remove</button></td>
            `;
            cartTableBody.appendChild(row);
        });
    }

    // Update summary section
    const totalItems = cartItems.reduce((acc, item) => acc + item.quantity, 0);
    if (document.getElementById('summary-item-count')) {
        document.getElementById('summary-item-count').textContent = totalItems;
        document.getElementById('summary-subtotal').textContent = `$${subtotal.toFixed(2)}`;
        document.getElementById('summary-total').textContent = `$${subtotal.toFixed(2)}`;
    }
    if (document.getElementById('review-item-count')) {
        document.getElementById('review-item-count').textContent = totalItems;
        document.getElementById('review-total-amount').textContent = `$${subtotal.toFixed(2)}`;
    }
}

function removeItemFromCart(index) {
    if (index >= 0 && index < cartItems.length) {
        cartItems.splice(index, 1); // Remove 1 item at the given index
        renderCartItems(); // Re-render the cart table
        updateCartTotal(); // Update the header badge and saves to local storage
    }
}

function handleCartInteractions() {
    if (!cartTableBody) return;

    // Remove Item Listener (Delegation)
    cartTableBody.addEventListener('click', (e) => {
        if (e.target.classList.contains('remove-item-btn')) {
            const index = parseInt(e.target.getAttribute('data-item-index'));
            removeItemFromCart(index);
        }
    });

    // Quantity Change Listener (Simulated for testing input change)
    cartTableBody.addEventListener('change', (e) => {
        if (e.target.classList.contains('quantity-input')) {
            const index = parseInt(e.target.getAttribute('data-item-index'));
            const newQuantity = parseInt(e.target.value);

            if (newQuantity < 1) {
                removeItemFromCart(index);
            } else {
                cartItems[index].quantity = newQuantity;
                renderCartItems();
                updateCartTotal(); // Update total and save
            }
        }
    });
}

// Drag-and-Drop Implementation
let draggedItem = null;

function setupDragAndDrop() {
    if (!cartTableBody) return;

    cartTableBody.addEventListener('dragstart', (e) => {
        const targetRow = e.target.closest('tr');
        if (targetRow && targetRow.classList.contains('cart-item-row')) {
            draggedItem = targetRow;
            setTimeout(() => targetRow.classList.add('dragging'), 0);
            e.dataTransfer.setData('text/plain', targetRow.getAttribute('data-index')); // Pass index, but we use the global draggedItem too
        }
    });

    cartTableBody.addEventListener('dragover', (e) => {
        e.preventDefault(); // Necessary to allow a drop
        const targetRow = e.target.closest('tr');
        if (targetRow && targetRow !== draggedItem && targetRow.classList.contains('cart-item-row')) {
            const rect = targetRow.getBoundingClientRect();
            const mouseY = e.clientY;
            const middle = rect.top + rect.height / 2;

            // Simple visual feedback (no placeholder for simplicity, just reorder on drop)
            targetRow.style.borderTop = (mouseY < middle) ? '2px solid var(--secondary-color)' : '';
            targetRow.style.borderBottom = (mouseY >= middle) ? '2px solid var(--secondary-color)' : '';
        }
    });

    cartTableBody.addEventListener('dragleave', (e) => {
        const rows = cartTableBody.querySelectorAll('tr');
        rows.forEach(row => {
            row.style.borderTop = '';
            row.style.borderBottom = '';
        });
    });

    cartTableBody.addEventListener('drop', (e) => {
        e.preventDefault();
        const targetRow = e.target.closest('tr');

        if (draggedItem && targetRow && targetRow !== draggedItem && targetRow.classList.contains('cart-item-row')) {
            const originalIndex = parseInt(draggedItem.getAttribute('data-index'));
            const newIndex = parseInt(targetRow.getAttribute('data-index'));

            // Use the cartItems array to manage actual order
            const itemToMove = cartItems.splice(originalIndex, 1)[0]; // Remove and get the item

            // Re-insert based on drop position relative to the middle
            const rect = targetRow.getBoundingClientRect();
            const mouseY = e.clientY;
            const middle = rect.top + rect.height / 2;

            if (mouseY < middle) {
                // Drop above target (insert at newIndex)
                cartItems.splice(newIndex, 0, itemToMove);
            } else {
                // Drop below target (insert after newIndex)
                cartItems.splice(newIndex + 1, 0, itemToMove);
            }

            renderCartItems(); // Re-render the whole list to update data-index attributes
            saveCartToLocal(); // Save the new order
        }

        // Cleanup styles
        const rows = cartTableBody.querySelectorAll('tr');
        rows.forEach(row => {
            row.style.borderTop = '';
            row.style.borderBottom = '';
        });
    });

    cartTableBody.addEventListener('dragend', (e) => {
        draggedItem.classList.remove('dragging');
        draggedItem = null;
    });
}

function setupCartPagination() {
    const paginationControls = document.getElementById('cart-pagination');
    if (!paginationControls) return;

    // This is a simple mock-up for testing pagination click/state
    paginationControls.addEventListener('click', (e) => {
        if (e.target.classList.contains('page-link')) {
            e.preventDefault();
            const targetPage = e.target.getAttribute('data-page');

            // Remove 'active' from all links
            paginationControls.querySelectorAll('.page-link').forEach(link => {
                link.classList.remove('active');
            });

            // Add 'active' to the target page number (or the surrounding controls)
            paginationControls.querySelector(`[data-page="${targetPage}"]`)?.classList.add('active');

            alert(`Simulating navigation to Cart Page ${targetPage}. This fulfills the Pagination testing requirement.`);
        }
    });
}

// --- 8. Multi-Step Form Functionality (For checkout.html) ---

const dynamicDropdownData = {
    USA: ['New York', 'California', 'Texas', 'Florida'],
    CAN: ['Ontario', 'Quebec', 'British Columbia', 'Alberta'],
    UK: ['England', 'Scotland', 'Wales', 'Northern Ireland']
};

function setupDynamicDropdowns() {
    const countryDropdown = document.getElementById('country');
    const stateProvinceDropdown = document.getElementById('stateProvince');

    if (!countryDropdown || !stateProvinceDropdown) return;

    countryDropdown.addEventListener('change', (e) => {
        const selectedCountry = e.target.value;

        // Clear previous options
        stateProvinceDropdown.innerHTML = '<option value="">Select State/Province...</option>';
        stateProvinceDropdown.disabled = true;

        if (selectedCountry && dynamicDropdownData[selectedCountry]) {
            dynamicDropdownData[selectedCountry].forEach(state => {
                const option = document.createElement('option');
                option.value = state;
                option.textContent = state;
                stateProvinceDropdown.appendChild(option);
            });
            stateProvinceDropdown.disabled = false;
        }
    });
}

function setupMultiStepForm() {
    const container = document.querySelector('.checkout-steps');
    if (!container) return;

    function navigateStep(targetStep) {
        const currentStep = container.querySelector('.step.active');
        const nextStep = container.querySelector(`[data-step="${targetStep}"]`);

        // When moving to step 3 (Review), populate the summary data
        if (parseInt(targetStep) === 3) {
            const fullName = document.getElementById('fullName')?.value || 'N/A';
            const address = document.getElementById('address')?.value || 'N/A';
            const city = document.getElementById('city')?.value || 'N/A';
            const zip = document.getElementById('zip')?.value || 'N/A';
            const country = document.getElementById('country')?.value || 'N/A';
            const state = document.getElementById('stateProvince')?.value || 'N/A';

            document.getElementById('review-address').textContent = `${fullName}, ${address}, ${city}, ${state} ${zip}, ${country}`;
        }

        if (currentStep) {
            currentStep.classList.remove('active');
        }
        if (nextStep) {
            nextStep.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    container.addEventListener('click', (e) => {
        if (e.target.classList.contains('next-step-btn')) {
            const currentForm = e.target.closest('form');
            // Check form validity before proceeding
            if (currentForm && !currentForm.checkValidity()) {
                currentForm.reportValidity();
                return;
            }
            const targetStep = e.target.getAttribute('data-target-step');
            navigateStep(targetStep);
        } else if (e.target.classList.contains('prev-step-btn')) {
            const targetStep = e.target.getAttribute('data-target-step');
            navigateStep(targetStep);
        } else if (e.target.id === 'place-order-btn') {
            alert('Order Placed Successfully! Redirecting to confirmation...');
            // Clear cart items for next test and save the empty state
            cartItems = [];
            updateCartTotal();
            saveCartToLocal();
            window.location.href = 'index.html';
        }
    });

    // Initial step setup
    navigateStep(1);
    setupDynamicDropdowns(); // Initialize dropdown logic
}


// --- 9. Event Listeners and Initialization ---

document.addEventListener('DOMContentLoaded', () => {

    // IMPORTANT: Load cart data before anything else
    loadCartFromLocal();

    // Global initial setup:
    updateDateTime();
    setInterval(updateDateTime, 1000);
    updateCartTotal(); // Initialize the cart badge count based on loaded data

    // --- Index Page Specific Logic ---
    if (document.getElementById('product-grid')) {
        renderProducts('all');

        // Search functionality
        const searchInput = document.querySelector('.search-input');
        const filterDropdown = document.getElementById('category-filter');

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                const searchTerm = e.target.value.trim();
                if (filterDropdown) {
                    filterDropdown.value = 'all';
                }
                renderProducts('all', searchTerm);
                document.querySelector('.filter-controls')?.scrollIntoView({ behavior: 'smooth' });
            });
        }

        // Category Filtering (Handles dropdown and category links)
        if (filterDropdown) {
            filterDropdown.addEventListener('change', (e) => {
                if (searchInput) searchInput.value = '';
                renderProducts(e.target.value);
            });
        }

        document.querySelectorAll('.category-link').forEach(link => {
            link.addEventListener('click', (e) => {
                const category = e.target.getAttribute('data-category');
                if (category) {
                    if (e.target.getAttribute('href') === '#') {
                        e.preventDefault();
                    }

                    if (searchInput) searchInput.value = '';
                    if (filterDropdown) {
                        filterDropdown.value = category;
                    }

                    renderProducts(category);
                    document.querySelector('.filter-controls')?.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Set up click listeners on the main grid (delegation)
        document.getElementById('product-grid')?.addEventListener('click', (e) => {
            // Add to Cart
            if (e.target.classList.contains('add-to-cart-btn')) {
                const productId = e.target.getAttribute('data-product-id');
                const product = products.find(p => p.id === productId);

                let cartItem = cartItems.find(item => item.id === productId);
                if (cartItem) {
                    cartItem.quantity++;
                } else if (product) {
                    cartItems.push({ id: product.id, name: product.name, price: product.price, quantity: 1 });
                }

                updateCartTotal(); // Updates total and saves to local storage
                alert(`${product.name} added to cart!`);
            }
            // Product Name Click or View Details button
            else if (e.target.classList.contains('product-name-link')) {
                const productId = e.target.getAttribute('data-product-id');
                openProductModal(productId);
            }
        });


        // Modal Close listeners
        document.querySelector('.close-button')?.addEventListener('click', closeProductModal);
        window.addEventListener('click', (event) => {
            const modal = document.getElementById('product-modal');
            if (event.target === modal) {
                closeProductModal();
            }
        });

        // Setup FAQ Accordion (only on index)
        setupFaqAccordion();
    }


    // --- Page-Specific Logic ---

    // Orders Page
    if(document.body.classList.contains('orders-page')) {
        setupSortableTable();
    }

    // Cart Page (UPDATED)
    if(document.body.classList.contains('cart-page')) {
        renderCartItems();
        handleCartInteractions();
        setupDragAndDrop();
        setupCartPagination();
    }

    // Checkout Page (UPDATED)
    if(document.body.classList.contains('checkout-page')) {
        setupMultiStepForm();
    }
});

// --- 10. Authentication & Security Logic ---

function handleRegistration(event) {
    event.preventDefault();

    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirmPassword').value;

    // Check if passwords match
    if (password !== confirmPassword) {
        alert("Registration Error: Passwords do not match!");
        return false;
    }

    alert("Registration Successful! Redirecting to Login...");
    window.location.href = 'login.html';
    return true;
}

function simulateForgotPassword() {
    const email = prompt("Enter your email to reset password:");
    if (email && email.includes("@")) {
        alert("Reset link sent to: " + email);
    } else if (email) {
        alert("Invalid email format.");
    }
}

// Bind Forgot Password link if on Login page
document.addEventListener('DOMContentLoaded', () => {
    const forgotLink = document.getElementById('forgot-password-link');
    if (forgotLink) {
        forgotLink.addEventListener('click', (e) => {
            e.preventDefault();
            simulateForgotPassword();
        });
    }
=======
/* -----------------------------------------------------
# Assignment: Final Project - Software Testing Tools
# Written by: Prudhvi Teja Reddy Kandula (Student ID: 5805128)
# Short Description:
# This script manages all dynamic behavior for the NextGenGadgets site,
# including product filtering, cart persistence, drag-and-drop,
# sortable tables, and security validation for the registration process.
# ----------------------------------------------------- */

// --- 1. Product Data Definition ---
const products = [
    // Laptops (4 Total)
    { id: 'L001', name: 'Apple Macbook M4 Chip', category: 'laptops', price: 1500.00, image: 'images/laptops/AppleMacbookM4Chip.jpg', specs: 'M4 Chip, 16GB RAM, 512GB SSD. Perfect for high-performance tasks.' },
    { id: 'L002', name: 'Apple Macbook Pro', category: 'laptops', price: 1800.00, image: 'images/laptops/AppleMacbookPro.jpg', specs: 'M3 Pro, 18GB RAM, 1TB SSD. Studio-grade performance.' },
    { id: 'L003', name: 'Lenovo Thinkpad', category: 'laptops', price: 1100.00, image: 'images/laptops/LenovoThinkpad.jpg', specs: 'Intel i7, 32GB RAM, 1TB SSD. Business-class durability.' },
    { id: 'L004', name: 'Microsoft Surface Laptop', category: 'laptops', price: 1350.00, image: 'images/laptops/MicrosoftSurfaceLaptop.jpg', specs: 'PixelSense display, 16GB RAM, 512GB SSD. Premium design and touch support.' },

    // Smartphones (10 Total)
    { id: 'S001', name: 'Apple iPhone 15', category: 'smartphones', price: 799.00, image: 'images/smartphones/AppleiPhone15.jpg', specs: 'A16 Bionic, 6.1" display. Great camera system.' },
    { id: 'S002', name: 'Apple iPhone 15 Plus', category: 'smartphones', price: 899.00, image: 'images/smartphones/AppleiPhone15Plus.jpg', specs: 'A16 Bionic, 6.7" display. Longer battery life.' },
    { id: 'S003', name: 'Apple iPhone 16', category: 'smartphones', price: 999.00, image: 'images/smartphones/AppleiPhone16.jpg', specs: 'Next-Gen A-series, 6.1" display. Enhanced features.' },
    { id: 'S004', name: 'Apple iPhone 16e', category: 'smartphones', price: 699.00, image: 'images/smartphones/AppleiPhone16e.jpg', specs: 'Compact and efficient model.' },
    { id: 'S005', name: 'Apple iPhone 16 Plus', category: 'smartphones', price: 1099.00, image: 'images/smartphones/AppleiPhone16Plus.jpg', specs: 'Next-Gen A-series, 6.7" display. Large screen experience.' },
    { id: 'S006', name: 'Apple iPhone 16 Pro', category: 'smartphones', price: 1299.00, image: 'images/smartphones/AppleiPhone16Pro.jpg', specs: 'Pro features, 120Hz display, superior camera.' },
    { id: 'S007', name: 'Apple iPhone 16 Pro Max', category: 'smartphones', price: 1499.00, image: 'images/smartphones/AppleiPhone16ProMax.jpg', specs: 'The ultimate flagship, best camera and battery.' },
    { id: 'S008', name: 'Google Pixel 9', category: 'smartphones', price: 699.00, image: 'images/smartphones/GooglePixel9.jpg', specs: 'Tensor G4, advanced AI features. Best in class computational photography.' },
    { id: 'S009', name: 'Samsung S24', category: 'smartphones', price: 799.00, image: 'images/smartphones/SamsungS24.jpg', specs: 'Compact flagship, stunning dynamic AMOLED display.' },
    { id: 'S010', name: 'Samsung S24 Ultra', category: 'smartphones', price: 1299.00, image: 'images/smartphones/SamsungS24Ultra.jpg', specs: 'Snapdragon, S Pen integrated. Stunning dynamic AMOLED display.' },

    // Watches (6 Total)
    { id: 'W001', name: 'Apple Watch Hermès Series 10', category: 'watches', price: 1399.00, image: 'images/watches/AppleWatchHermèsSeries10.jpg', specs: 'Premium Hermès band, exclusive watch faces.' },
    { id: 'W002', name: 'Apple Watch Hermès Ultra 2', category: 'watches', price: 1799.00, image: 'images/watches/AppleWatchHermèsUltra2.jpg', specs: 'Rugged titanium case with premium Hermès band.' },
    { id: 'W003', name: 'Apple Watch SE', category: 'watches', price: 249.00, image: 'images/watches/AppleWatchSE.jpg', specs: 'Essential features for fitness and connectivity.' },
    { id: 'W004', name: 'Apple Watch Series 10', category: 'watches', price: 450.00, image: 'images/watches/AppleWatchSeries10.jpg', specs: 'S10 Chip, new health sensors. Our most advanced watch yet.' },
    { id: 'W005', name: 'Apple Watch Ultra 2', category: 'watches', price: 799.00, image: 'images/watches/AppleWatchUltra2.jpg', specs: 'Rugged titanium case, extreme battery life. For the adventurers.' },
    { id: 'W006', name: 'OnePlus Watch 2', category: 'watches', price: 299.00, image: 'images/watches/OnePlusWatch2.jpg', specs: 'Long-lasting battery, comprehensive fitness tracking.' }
];

// --- 2. Cart Data & Persistence Functions ---

const INITIAL_MOCK_CART = [
    // Mock data used if localStorage is empty to ensure drag-and-drop/remove features can be tested immediately.
    { id: 'L002', name: 'Apple Macbook Pro', price: 1800.00, quantity: 1 },
    { id: 'S007', name: 'Apple iPhone 16 Pro Max', price: 1499.00, quantity: 1 },
    { id: 'W005', name: 'Apple Watch Ultra 2', price: 799.00, quantity: 2 },
];

let cartItems = []; // Will be populated by loadCartFromLocal()

function saveCartToLocal() {
    // Saves the current state of cartItems to the browser's local storage
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
}

function loadCartFromLocal() {
    const localData = localStorage.getItem('cartItems');
    if (localData) {
        // Load existing data from storage
        cartItems = JSON.parse(localData);
    } else {
        // If nothing is stored, use the mock data for the first time and save it.
        cartItems = INITIAL_MOCK_CART;
        saveCartToLocal();
    }
}

function updateDateTime() {
    const dateTimeElement = document.getElementById('current-date-time');
    if (dateTimeElement) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' };
        dateTimeElement.textContent = now.toLocaleDateString('en-US', options);
    }
}

function updateCartTotal(action) {
    const cartBadge = document.getElementById('cart-total-items');
    if (!cartBadge) return;

    // Recalculate based on current cartItems for accuracy
    const totalCount = cartItems.reduce((acc, item) => acc + item.quantity, 0);
    cartBadge.textContent = totalCount;

    // Since the cart changed, save the new state
    saveCartToLocal();
}

// --- 3. Product Display and Filtering ---

function renderProducts(filterCategory = 'all', searchTerm = '') {
    const grid = document.getElementById('product-grid');
    if (!grid) return;

    grid.innerHTML = '';
    const lowerCaseSearchTerm = searchTerm.toLowerCase();

    let filteredProducts = products.filter(p => {
        const categoryMatch = filterCategory === 'all' || p.category.toLowerCase() === filterCategory.toLowerCase();

        const searchMatch = !searchTerm ||
            p.name.toLowerCase().includes(lowerCaseSearchTerm) ||
            p.category.toLowerCase().includes(lowerCaseSearchTerm);

        return categoryMatch && searchMatch;
    });

    if (filteredProducts.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1 / -1; text-align: center;">No products found matching your filter criteria.</p>';
        return;
    }

    grid.style.opacity = 0;
    setTimeout(() => {
        filteredProducts.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.setAttribute('data-id', product.id);
            const price = product.price.toFixed(2);

            card.innerHTML = `
                <img src="${product.image}" alt="${product.name}">
                <h4 class="product-name-link" data-product-id="${product.id}">${product.name}</h4>
                <p><strong>$${price}</strong></p>
                <button class="add-to-cart-btn" data-product-id="${product.id}">Add to Cart</button>
                <button class="view-details-btn product-name-link" data-product-id="${product.id}">View Details</button>
            `;

            grid.appendChild(card);
        });

        grid.style.opacity = 1;
    }, 500);
}

// --- 4. Modal Interaction ---

function openProductModal(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;

    const modal = document.getElementById('product-modal');
    if (!modal) return;

    document.getElementById('modal-product-name').textContent = product.name;
    document.getElementById('modal-product-specs').innerHTML = `
        <p><strong>Price:</strong> $${product.price.toFixed(2)}</p>
        <p><strong>Category:</strong> ${product.category}</p>
        <p><strong>Specifications:</strong> ${product.specs}</p>
        <hr>
        <h5>What's in the Box:</h5>
        <ul>
            <li>The device itself</li>
            <li>Charging Cable</li>
            <li>User Manual</li>
        </ul>
    `;
    modal.style.display = 'block';

    modal.querySelector('.modal-add-to-cart-btn').onclick = () => {
        // Find if item exists, if so increment quantity, otherwise add new item
        let cartItem = cartItems.find(item => item.id === productId);
        if (cartItem) {
            cartItem.quantity++;
        } else {
            cartItems.push({ id: product.id, name: product.name, price: product.price, quantity: 1 });
        }

        updateCartTotal('add'); // Calls saveCartToLocal
        alert(`${product.name} added to cart!`);
        modal.style.display = 'none';
    };
}

function closeProductModal() {
    const modal = document.getElementById('product-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// --- 5. FAQ Accordion Functionality ---

function setupFaqAccordion() {
    const headers = document.querySelectorAll('.accordion-header');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;
            const content = item.querySelector('.accordion-content');

            document.querySelectorAll('.accordion-item.active').forEach(activeItem => {
                if (activeItem !== item) {
                    activeItem.classList.remove('active');
                    activeItem.querySelector('.accordion-content').style.maxHeight = 0;
                }
            });

            item.classList.toggle('active');
            if (item.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = 0;
            }
        });
    });
}

// --- 6. Sortable Table Functionality (For orders.html) ---

function setupSortableTable() {
    const table = document.getElementById('order-history-table');
    if (!table) return;

    const headers = table.querySelectorAll('th[data-sort-key]');
    const tbody = table.querySelector('tbody');
    let sortDirection = {};

    function getColIndex(key, table) {
        const headerRow = table.querySelector('thead tr');
        const headers = Array.from(headerRow.querySelectorAll('th'));
        for (let i = 0; i < headers.length; i++) {
            if (headers[i].getAttribute('data-sort-key') === key) {
                return i;
            }
        }
        return -1;
    }

    function sortData(key, direction, tbody) {
        const colIndex = getColIndex(key, table);
        if (colIndex === -1) return;

        let rows = Array.from(tbody.querySelectorAll('tr'));

        rows.sort((a, b) => {
            let aValue = a.cells[colIndex].getAttribute('data-sort-value') || a.cells[colIndex].textContent.trim();
            let bValue = b.cells[colIndex].getAttribute('data-sort-value') || b.cells[colIndex].textContent.trim();

            if (!isNaN(aValue) && !isNaN(bValue)) {
                aValue = parseFloat(aValue.toString().replace('$', '').replace(',', ''));
                bValue = parseFloat(bValue.toString().replace('$', '').replace(',', ''));
            }

            let comparison = 0;
            if (aValue > bValue) {
                comparison = 1;
            } else if (aValue < bValue) {
                comparison = -1;
            }

            return direction === 'asc' ? comparison : comparison * -1;
        });

        rows.forEach(row => tbody.appendChild(row));
    }

    headers.forEach(header => {
        const key = header.getAttribute('data-sort-key');
        header.addEventListener('click', () => {
            const isAsc = sortDirection[key] === 'asc';
            const direction = isAsc ? 'desc' : 'asc';
            sortDirection[key] = direction;

            sortData(key, direction, tbody);

            headers.forEach(h => {
                const icon = h.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-sort-up', 'fa-sort-down');
                    icon.classList.add('fa-sort');
                }
            });
            const clickedIcon = header.querySelector('i');
            if (clickedIcon) {
                clickedIcon.classList.remove('fa-sort');
                clickedIcon.classList.add(direction === 'asc' ? 'fa-sort-up' : 'fa-sort-down');
            }
        });
    });
}


// --- 7. Cart Page Functionality ---

const cartTableBody = document.getElementById('draggable-cart-list');

function renderCartItems() {
    if (!cartTableBody) return;

    // Clear existing content
    cartTableBody.innerHTML = '';
    let subtotal = 0;

    if (cartItems.length === 0) {
        cartTableBody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 30px;">Your cart is empty.</td></tr>';
    } else {
        cartItems.forEach((item, index) => {
            const row = document.createElement('tr');
            const total = item.price * item.quantity;
            subtotal += total;

            row.setAttribute('draggable', 'true'); // For drag-and-drop
            row.setAttribute('data-cart-id', item.id);
            row.setAttribute('data-index', index);
            row.className = 'cart-item-row';

            row.innerHTML = `
                <td>${item.name}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td><input type="number" value="${item.quantity}" min="1" style="width: 50px;" data-item-index="${index}" class="quantity-input"></td>
                <td>$${total.toFixed(2)}</td>
                <td><button class="remove-item-btn" data-item-index="${index}">Remove</button></td>
            `;
            cartTableBody.appendChild(row);
        });
    }

    // Update summary section
    const totalItems = cartItems.reduce((acc, item) => acc + item.quantity, 0);
    if (document.getElementById('summary-item-count')) {
        document.getElementById('summary-item-count').textContent = totalItems;
        document.getElementById('summary-subtotal').textContent = `$${subtotal.toFixed(2)}`;
        document.getElementById('summary-total').textContent = `$${subtotal.toFixed(2)}`;
    }
    if (document.getElementById('review-item-count')) {
        document.getElementById('review-item-count').textContent = totalItems;
        document.getElementById('review-total-amount').textContent = `$${subtotal.toFixed(2)}`;
    }
}

function removeItemFromCart(index) {
    if (index >= 0 && index < cartItems.length) {
        cartItems.splice(index, 1); // Remove 1 item at the given index
        renderCartItems(); // Re-render the cart table
        updateCartTotal(); // Update the header badge and saves to local storage
    }
}

function handleCartInteractions() {
    if (!cartTableBody) return;

    // Remove Item Listener (Delegation)
    cartTableBody.addEventListener('click', (e) => {
        if (e.target.classList.contains('remove-item-btn')) {
            const index = parseInt(e.target.getAttribute('data-item-index'));
            removeItemFromCart(index);
        }
    });

    // Quantity Change Listener (Simulated for testing input change)
    cartTableBody.addEventListener('change', (e) => {
        if (e.target.classList.contains('quantity-input')) {
            const index = parseInt(e.target.getAttribute('data-item-index'));
            const newQuantity = parseInt(e.target.value);

            if (newQuantity < 1) {
                removeItemFromCart(index);
            } else {
                cartItems[index].quantity = newQuantity;
                renderCartItems();
                updateCartTotal(); // Update total and save
            }
        }
    });
}

// Drag-and-Drop Implementation
let draggedItem = null;

function setupDragAndDrop() {
    if (!cartTableBody) return;

    cartTableBody.addEventListener('dragstart', (e) => {
        const targetRow = e.target.closest('tr');
        if (targetRow && targetRow.classList.contains('cart-item-row')) {
            draggedItem = targetRow;
            setTimeout(() => targetRow.classList.add('dragging'), 0);
            e.dataTransfer.setData('text/plain', targetRow.getAttribute('data-index')); // Pass index, but we use the global draggedItem too
        }
    });

    cartTableBody.addEventListener('dragover', (e) => {
        e.preventDefault(); // Necessary to allow a drop
        const targetRow = e.target.closest('tr');
        if (targetRow && targetRow !== draggedItem && targetRow.classList.contains('cart-item-row')) {
            const rect = targetRow.getBoundingClientRect();
            const mouseY = e.clientY;
            const middle = rect.top + rect.height / 2;

            // Simple visual feedback (no placeholder for simplicity, just reorder on drop)
            targetRow.style.borderTop = (mouseY < middle) ? '2px solid var(--secondary-color)' : '';
            targetRow.style.borderBottom = (mouseY >= middle) ? '2px solid var(--secondary-color)' : '';
        }
    });

    cartTableBody.addEventListener('dragleave', (e) => {
        const rows = cartTableBody.querySelectorAll('tr');
        rows.forEach(row => {
            row.style.borderTop = '';
            row.style.borderBottom = '';
        });
    });

    cartTableBody.addEventListener('drop', (e) => {
        e.preventDefault();
        const targetRow = e.target.closest('tr');

        if (draggedItem && targetRow && targetRow !== draggedItem && targetRow.classList.contains('cart-item-row')) {
            const originalIndex = parseInt(draggedItem.getAttribute('data-index'));
            const newIndex = parseInt(targetRow.getAttribute('data-index'));

            // Use the cartItems array to manage actual order
            const itemToMove = cartItems.splice(originalIndex, 1)[0]; // Remove and get the item

            // Re-insert based on drop position relative to the middle
            const rect = targetRow.getBoundingClientRect();
            const mouseY = e.clientY;
            const middle = rect.top + rect.height / 2;

            if (mouseY < middle) {
                // Drop above target (insert at newIndex)
                cartItems.splice(newIndex, 0, itemToMove);
            } else {
                // Drop below target (insert after newIndex)
                cartItems.splice(newIndex + 1, 0, itemToMove);
            }

            renderCartItems(); // Re-render the whole list to update data-index attributes
            saveCartToLocal(); // Save the new order
        }

        // Cleanup styles
        const rows = cartTableBody.querySelectorAll('tr');
        rows.forEach(row => {
            row.style.borderTop = '';
            row.style.borderBottom = '';
        });
    });

    cartTableBody.addEventListener('dragend', (e) => {
        draggedItem.classList.remove('dragging');
        draggedItem = null;
    });
}

function setupCartPagination() {
    const paginationControls = document.getElementById('cart-pagination');
    if (!paginationControls) return;

    // This is a simple mock-up for testing pagination click/state
    paginationControls.addEventListener('click', (e) => {
        if (e.target.classList.contains('page-link')) {
            e.preventDefault();
            const targetPage = e.target.getAttribute('data-page');

            // Remove 'active' from all links
            paginationControls.querySelectorAll('.page-link').forEach(link => {
                link.classList.remove('active');
            });

            // Add 'active' to the target page number (or the surrounding controls)
            paginationControls.querySelector(`[data-page="${targetPage}"]`)?.classList.add('active');

            alert(`Simulating navigation to Cart Page ${targetPage}. This fulfills the Pagination testing requirement.`);
        }
    });
}

// --- 8. Multi-Step Form Functionality (For checkout.html) ---

const dynamicDropdownData = {
    USA: ['New York', 'California', 'Texas', 'Florida'],
    CAN: ['Ontario', 'Quebec', 'British Columbia', 'Alberta'],
    UK: ['England', 'Scotland', 'Wales', 'Northern Ireland']
};

function setupDynamicDropdowns() {
    const countryDropdown = document.getElementById('country');
    const stateProvinceDropdown = document.getElementById('stateProvince');

    if (!countryDropdown || !stateProvinceDropdown) return;

    countryDropdown.addEventListener('change', (e) => {
        const selectedCountry = e.target.value;

        // Clear previous options
        stateProvinceDropdown.innerHTML = '<option value="">Select State/Province...</option>';
        stateProvinceDropdown.disabled = true;

        if (selectedCountry && dynamicDropdownData[selectedCountry]) {
            dynamicDropdownData[selectedCountry].forEach(state => {
                const option = document.createElement('option');
                option.value = state;
                option.textContent = state;
                stateProvinceDropdown.appendChild(option);
            });
            stateProvinceDropdown.disabled = false;
        }
    });
}

function setupMultiStepForm() {
    const container = document.querySelector('.checkout-steps');
    if (!container) return;

    function navigateStep(targetStep) {
        const currentStep = container.querySelector('.step.active');
        const nextStep = container.querySelector(`[data-step="${targetStep}"]`);

        // When moving to step 3 (Review), populate the summary data
        if (parseInt(targetStep) === 3) {
            const fullName = document.getElementById('fullName')?.value || 'N/A';
            const address = document.getElementById('address')?.value || 'N/A';
            const city = document.getElementById('city')?.value || 'N/A';
            const zip = document.getElementById('zip')?.value || 'N/A';
            const country = document.getElementById('country')?.value || 'N/A';
            const state = document.getElementById('stateProvince')?.value || 'N/A';

            document.getElementById('review-address').textContent = `${fullName}, ${address}, ${city}, ${state} ${zip}, ${country}`;
        }

        if (currentStep) {
            currentStep.classList.remove('active');
        }
        if (nextStep) {
            nextStep.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    container.addEventListener('click', (e) => {
        if (e.target.classList.contains('next-step-btn')) {
            const currentForm = e.target.closest('form');
            // Check form validity before proceeding
            if (currentForm && !currentForm.checkValidity()) {
                currentForm.reportValidity();
                return;
            }
            const targetStep = e.target.getAttribute('data-target-step');
            navigateStep(targetStep);
        } else if (e.target.classList.contains('prev-step-btn')) {
            const targetStep = e.target.getAttribute('data-target-step');
            navigateStep(targetStep);
        } else if (e.target.id === 'place-order-btn') {
            alert('Order Placed Successfully! Redirecting to confirmation...');
            // Clear cart items for next test and save the empty state
            cartItems = [];
            updateCartTotal();
            saveCartToLocal();
            window.location.href = 'index.html';
        }
    });

    // Initial step setup
    navigateStep(1);
    setupDynamicDropdowns(); // Initialize dropdown logic
}


// --- 9. Event Listeners and Initialization ---

document.addEventListener('DOMContentLoaded', () => {

    // IMPORTANT: Load cart data before anything else
    loadCartFromLocal();

    // Global initial setup:
    updateDateTime();
    setInterval(updateDateTime, 1000);
    updateCartTotal(); // Initialize the cart badge count based on loaded data

    // --- Index Page Specific Logic ---
    if (document.getElementById('product-grid')) {
        renderProducts('all');

        // Search functionality
        const searchInput = document.querySelector('.search-input');
        const filterDropdown = document.getElementById('category-filter');

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                const searchTerm = e.target.value.trim();
                if (filterDropdown) {
                    filterDropdown.value = 'all';
                }
                renderProducts('all', searchTerm);
                document.querySelector('.filter-controls')?.scrollIntoView({ behavior: 'smooth' });
            });
        }

        // Category Filtering (Handles dropdown and category links)
        if (filterDropdown) {
            filterDropdown.addEventListener('change', (e) => {
                if (searchInput) searchInput.value = '';
                renderProducts(e.target.value);
            });
        }

        document.querySelectorAll('.category-link').forEach(link => {
            link.addEventListener('click', (e) => {
                const category = e.target.getAttribute('data-category');
                if (category) {
                    if (e.target.getAttribute('href') === '#') {
                        e.preventDefault();
                    }

                    if (searchInput) searchInput.value = '';
                    if (filterDropdown) {
                        filterDropdown.value = category;
                    }

                    renderProducts(category);
                    document.querySelector('.filter-controls')?.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Set up click listeners on the main grid (delegation)
        document.getElementById('product-grid')?.addEventListener('click', (e) => {
            // Add to Cart
            if (e.target.classList.contains('add-to-cart-btn')) {
                const productId = e.target.getAttribute('data-product-id');
                const product = products.find(p => p.id === productId);

                let cartItem = cartItems.find(item => item.id === productId);
                if (cartItem) {
                    cartItem.quantity++;
                } else if (product) {
                    cartItems.push({ id: product.id, name: product.name, price: product.price, quantity: 1 });
                }

                updateCartTotal(); // Updates total and saves to local storage
                alert(`${product.name} added to cart!`);
            }
            // Product Name Click or View Details button
            else if (e.target.classList.contains('product-name-link')) {
                const productId = e.target.getAttribute('data-product-id');
                openProductModal(productId);
            }
        });


        // Modal Close listeners
        document.querySelector('.close-button')?.addEventListener('click', closeProductModal);
        window.addEventListener('click', (event) => {
            const modal = document.getElementById('product-modal');
            if (event.target === modal) {
                closeProductModal();
            }
        });

        // Setup FAQ Accordion (only on index)
        setupFaqAccordion();
    }


    // --- Page-Specific Logic ---

    // Orders Page
    if(document.body.classList.contains('orders-page')) {
        setupSortableTable();
    }

    // Cart Page (UPDATED)
    if(document.body.classList.contains('cart-page')) {
        renderCartItems();
        handleCartInteractions();
        setupDragAndDrop();
        setupCartPagination();
    }

    // Checkout Page (UPDATED)
    if(document.body.classList.contains('checkout-page')) {
        setupMultiStepForm();
    }
});

// --- 10. Authentication & Security Logic ---

function handleRegistration(event) {
    event.preventDefault();

    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirmPassword').value;

    // Check if passwords match
    if (password !== confirmPassword) {
        alert("Registration Error: Passwords do not match!");
        return false;
    }

    alert("Registration Successful! Redirecting to Login...");
    window.location.href = 'login.html';
    return true;
}

function simulateForgotPassword() {
    const email = prompt("Enter your email to reset password:");
    if (email && email.includes("@")) {
        alert("Reset link sent to: " + email);
    } else if (email) {
        alert("Invalid email format.");
    }
}

// Bind Forgot Password link if on Login page
document.addEventListener('DOMContentLoaded', () => {
    const forgotLink = document.getElementById('forgot-password-link');
    if (forgotLink) {
        forgotLink.addEventListener('click', (e) => {
            e.preventDefault();
            simulateForgotPassword();
        });
    }
>>>>>>> 6c46170 (Syncing local files with repository)
});