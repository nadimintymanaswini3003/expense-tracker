
document.addEventListener("DOMContentLoaded", function () {
    // Chart.js setup
    const ctx = document.getElementById('expenseChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: categoryLabels,
            datasets: [{
                data: categoryValues,
                backgroundColor: [
                    '#008080', '#20b2aa', '#40e0d0', '#66cdaa', '#5f9ea0', '#00ced1', '#2e8b57'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#004d4d',
                        font: { family: 'Poppins', size: 14 }
                    }
                },
                title: {
                    display: true,
                    text: 'Expenses by Category',
                    color: '#008080',
                    font: { family: 'Poppins', size: 18, weight: 'bold' }
                }
            }
        }
    });

    // Theme toggle
    const toggleBtn = document.getElementById('themeToggle');
    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark');
    });
});
