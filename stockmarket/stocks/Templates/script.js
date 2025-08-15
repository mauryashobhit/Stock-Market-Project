 function animateCards() {
      const cards = document.querySelectorAll('.card');
      const windowBottom = window.innerHeight + window.scrollY;

      cards.forEach(card => {
        if (card.offsetTop < windowBottom - 100) {
          card.classList.add('visible');
        }
      });
    }
    window.addEventListener('scroll', animateCards);
    window.addEventListener('load', animateCards);

    const ctxMarket = document.getElementById('marketChart').getContext('2d');
    let marketData = [4000, 4200, 4150, 4300, 4450];
    const marketLabels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];

    const marketChart = new Chart(ctxMarket, {
      type: 'bar',
      data: {
        labels: marketLabels,
        datasets: [{
          label: 'Market Index',
          data: marketData,
          backgroundColor: ['#10b981', '#22c55e', '#34d399', '#4ade80', '#6ee7b7'],
          borderRadius: 10,
        }],
      },
      options: {
        animation: {
          duration: 1000,
          easing: 'easeOutQuart'
        },
        responsive: true,
        plugins: {
          tooltip: { mode: 'index', intersect: false },
          legend: { display: false },
        },
        scales: {
          y: {
            beginAtZero: false,
            ticks: { color: '#c9d1d9', font: { weight: 'bold' } },
            grid: { color: '#30363d' },
          },
          x: {
            ticks: { color: '#c9d1d9', font: { weight: 'bold' } },
            grid: { color: '#30363d' },
          },
        },
      },
    });

    const ctxTrend = document.getElementById('priceTrendChart').getContext('2d');
    let priceTrendLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'];
    let priceTrendData = [1400, 1425, 1450, 1470, 1460, 1480, 1495];

    const priceTrendChart = new Chart(ctxTrend, {
      type: 'line',
      data: {
        labels: priceTrendLabels,
        datasets: [{
          label: 'INFY Price (₹)',
          data: priceTrendData,
          borderColor: '#58a6ff',
          backgroundColor: 'rgba(88, 166, 255, 0.3)',
          fill: true,
          tension: 0.3,
          pointRadius: 4,
          pointHoverRadius: 6,
          pointBackgroundColor: '#58a6ff',
          borderWidth: 3,
        }],
      },
      options: {
        animation: {
          duration: 1500,
          easing: 'easeOutQuart'
        },
        responsive: true,
        plugins: {
          tooltip: { mode: 'nearest', intersect: false },
          legend: { labels: { color: '#c9d1d9' } },
        },
        scales: {
          y: {
            ticks: { color: '#c9d1d9', font: { weight: 'bold' } },
            grid: { color: '#30363d' },
          },
          x: {
            ticks: { color: '#c9d1d9', font: { weight: 'bold' } },
            grid: { color: '#30363d' },
          },
        },
      },
    });

    const ctxPortfolio = document.getElementById('portfolioChart').getContext('2d');
    const portfolioChart = new Chart(ctxPortfolio, {
      type: 'doughnut',
      data: {
        labels: ['INFY', 'TCS', 'RELIANCE', 'HDFCLIFE', 'SBIN'],
        datasets: [{
          data: [30, 25, 20, 15, 10],
          backgroundColor: [
            '#58a6ff',
            '#2ea043',
            '#f59e0b',
            '#ef4444',
            '#6366f1',
          ],
          borderWidth: 2,
          borderColor: '#0e1117',
        }],
      },
      options: {
        animation: {
          animateRotate: true,
          duration: 1500,
          easing: 'easeOutQuart'
        },
        responsive: true,
        plugins: {
          legend: { labels: { color: '#c9d1d9', font: { weight: 'bold' } } },
          tooltip: { enabled: true },
        },
      },
    });

    // Function to simulate live updates
    function updateCharts() {
      // Update market indices randomly (small fluctuations)
      for(let i=0; i<marketData.length; i++) {
        const change = (Math.random() - 0.5) * 40; // ±20 approx
        marketData[i] = Math.max(3800, Math.min(4600, marketData[i] + change));
      }
      marketChart.data.datasets[0].data = marketData;
      marketChart.update();

      // Update market index % display (relative to base values)
      const sp500Change = ((marketData[marketData.length-1] - 4000) / 4000) * 100;
      const nasdaqChange = ((marketData[marketData.length-2] - 4200) / 4200) * 100;
      const niftyChange = -0.14 + ((Math.random() - 0.5) * 0.3); // fluctuate near -0.14%

      document.getElementById('sp500').textContent =
        `${sp500Change >= 0 ? '+' : ''}${sp500Change.toFixed(2)}%`;
      document.getElementById('nasdaq').textContent =
        `${nasdaqChange >= 0 ? '+' : ''}${nasdaqChange.toFixed(2)}%`;
      document.getElementById('nifty').textContent =
        `${niftyChange >= 0 ? '+' : ''}${niftyChange.toFixed(2)}%`;

      // Update stock price trend with a new random price close to last one
      const lastPrice = priceTrendData[priceTrendData.length - 1];
      let newPrice = lastPrice + (Math.random() - 0.5) * 15;
      newPrice = Math.max(1350, Math.min(1550, newPrice));
      priceTrendData.push(newPrice);
      priceTrendData.shift(); // keep length constant

      priceTrendChart.data.datasets[0].data = priceTrendData;
      priceTrendChart.update();
    }

    setInterval(updateCharts, 3000);

    const form = document.getElementById('subscribeForm');
    form.addEventListener('submit', e => {
      e.preventDefault();
      const email = document.getElementById('emailInput').value;
      alert(`Thanks for subscribing, ${email}!`);
      form.reset();
    });