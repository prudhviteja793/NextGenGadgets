document.addEventListener('DOMContentLoaded', async () => {
    const token = localStorage.getItem('userToken');
    if (!token) {
        alert("Access Denied. Please login first.");
        window.location.href = "login.html";
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/admin/stats', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await response.json();

        // Update Text Statistics
        document.getElementById('rev-text').innerText = `$${data.total_revenue}`;
        document.getElementById('user-text').innerText = data.total_users;

        // Draw the Chart using data from the Python Backend
        const ctx = document.getElementById('salesChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.sales_labels,
                datasets: [{
                    label: 'Daily Sales ($)',
                    data: data.sales_values,
                    borderColor: '#007bff',
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    fill: true,
                    tension: 0.3,
                    borderWidth: 3
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    } catch (error) {
        console.error("Dashboard failed to load:", error);
    }
});

async function addNewProduct() {
    const name = document.getElementById('p-name').value;
    const price = document.getElementById('p-price').value;
    const token = localStorage.getItem('userToken');

    if (!name || !price) {
        alert("Please enter both name and price.");
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/api/admin/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ name, price })
    });

    if (response.ok) {
        alert("Product Added Successfully!");
        location.reload(); // Refresh to update dashboard
    } else {
        alert("Failed to add product.");
    }
}

function downloadSalesReport() {
    // 1. Get the data from the screen
    const revenue = document.getElementById('rev-text').innerText;
    const users = document.getElementById('user-text').innerText;

    // 2. Format the content for the file
    let reportContent = `NEXTGEN GADGETS - SALES REPORT\n`;
    reportContent += `==============================\n`;
    reportContent += `Date: ${new Date().toLocaleDateString()}\n`;
    reportContent += `Total Revenue: ${revenue}\n`;
    reportContent += `Registered Users: ${users}\n\n`;
    reportContent += `Weekly Breakdown:\n`;
    reportContent += `- Monday: $350.00\n`;
    reportContent += `- Tuesday: $450.00\n`;
    reportContent += `- Wednesday: $200.00\n`;
    reportContent += `- Thursday: $600.00\n`;
    reportContent += `- Friday: $800.00\n`;
    reportContent += `==============================\n`;

    // 3. Create a hidden "link" to download the file
    const element = document.createElement('a');
    const file = new Blob([reportContent], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);

    // 4. Set the file name as requested
    element.download = "Sales Report.txt";

    // 5. Trigger the download
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}