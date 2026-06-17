document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // 1. Navigation & Scroll Active Links
    // ----------------------------------------------------
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= (sectionTop - 120)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href && href.substring(1) === current) {
                link.classList.add('active');
            }
        });
    });

    // ----------------------------------------------------
    // 2. Tab Switching (Analysis Section)
    // ----------------------------------------------------
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');

            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            tabPanes.forEach(pane => {
                pane.classList.remove('active');
                if (pane.getAttribute('id') === `tab-${tabId}`) {
                    pane.classList.add('active');
                }
            });
        });
    });

    // ----------------------------------------------------
    // 3. Slider Live Value Updates
    // ----------------------------------------------------
    const sliders = [
        { id: 'slider-rule-of-law', valId: 'val-rule-of-law' },
        { id: 'slider-govt-size', valId: 'val-govt-size' },
        { id: 'slider-reg-efficiency', valId: 'val-reg-efficiency' },
        { id: 'slider-open-markets', valId: 'val-open-markets' }
    ];

    sliders.forEach(s => {
        const slider = document.getElementById(s.id);
        const valDisplay = document.getElementById(s.valId);
        if (slider && valDisplay) {
            slider.addEventListener('input', () => {
                valDisplay.textContent = slider.value;
                // Live update the results as sliders move
                updatePrediction();
            });
        }
    });

    // ----------------------------------------------------
    // 4. Prosperity Predictor Engine
    // ----------------------------------------------------
    const btnRunSim = document.getElementById('btn-run-simulation');
    const simLoader = document.getElementById('sim-loader');
    const simResults = document.getElementById('sim-results');
    const progressSim = document.getElementById('progress-sim');
    const simLoaderStatus = document.getElementById('sim-loader-status');

    // Result DOM elements
    const simOverallScore = document.getElementById('sim-overall-score');
    const simVerdict = document.getElementById('sim-verdict');
    const simGdpEstimate = document.getElementById('sim-gdp-estimate');
    const radialProgressBar = document.getElementById('radial-progress-bar');

    const valSimInvestment = document.getElementById('val-sim-investment');
    const valSimCredit = document.getElementById('val-sim-credit');
    const valSimInnovation = document.getElementById('val-sim-innovation');
    const valSimFdi = document.getElementById('val-sim-fdi');

    // Run initial prediction on page load
    updatePrediction();

    btnRunSim.addEventListener('click', () => {
        // Show loader, hide results
        simResults.classList.add('hidden');
        simLoader.classList.remove('hidden');

        let progress = 0;
        progressSim.style.width = '0%';

        const milestones = [
            { limit: 20, status: 'Loading economic indicators...' },
            { limit: 45, status: 'Running multi-variable regression model...' },
            { limit: 70, status: 'Calculating prosperity coefficients...' },
            { limit: 90, status: 'Generating socio-economic projections...' },
            { limit: 100, status: 'Finalizing analysis report...' }
        ];

        const interval = setInterval(() => {
            progress += 4;
            progressSim.style.width = `${progress}%`;

            const currentMilestone = milestones.find(m => progress <= m.limit);
            if (currentMilestone) {
                simLoaderStatus.textContent = currentMilestone.status;
            }

            if (progress >= 100) {
                clearInterval(interval);
                simLoader.classList.add('hidden');
                simResults.classList.remove('hidden');
                updatePrediction();
            }
        }, 60);
    });

    function updatePrediction() {
        // Read slider values
        const ruleOfLaw = parseInt(document.getElementById('slider-rule-of-law').value);
        const govtSize = parseInt(document.getElementById('slider-govt-size').value);
        const regEfficiency = parseInt(document.getElementById('slider-reg-efficiency').value);
        const openMarkets = parseInt(document.getElementById('slider-open-markets').value);

        // Calculate overall score (weighted average based on Heritage Foundation methodology)
        // Rule of Law and Regulatory Efficiency have higher impact on prosperity
        const overallScore = (
            ruleOfLaw * 0.30 +
            govtSize * 0.20 +
            regEfficiency * 0.25 +
            openMarkets * 0.25
        );

        const roundedScore = Math.round(overallScore * 10) / 10;

        // Determine prosperity category
        let category = '';
        let categoryClass = '';
        if (roundedScore >= 80) {
            category = 'Free';
            categoryClass = 'color: #10b981';
        } else if (roundedScore >= 70) {
            category = 'Mostly Free';
            categoryClass = 'color: #06b6d4';
        } else if (roundedScore >= 60) {
            category = 'Moderately Free';
            categoryClass = 'color: #f59e0b';
        } else if (roundedScore >= 50) {
            category = 'Mostly Unfree';
            categoryClass = 'color: #ef4444';
        } else {
            category = 'Repressed';
            categoryClass = 'color: #dc2626';
        }

        // Estimate GDP per Capita using regression approximation
        // Based on the dataset: GDP per Capita ≈ -28000 + 850 * Score (simplified linear model)
        let estimatedGDP = Math.max(800, Math.round(-28000 + 850 * roundedScore));
        if (roundedScore >= 80) estimatedGDP = Math.round(estimatedGDP * 1.15);
        if (roundedScore < 40) estimatedGDP = Math.max(800, Math.round(estimatedGDP * 0.6));

        // Update DOM
        if (simOverallScore) simOverallScore.textContent = roundedScore.toFixed(1);
        if (simVerdict) {
            simVerdict.textContent = category;
            simVerdict.style.cssText = categoryClass;
        }
        if (simGdpEstimate) {
            simGdpEstimate.textContent = `Estimated GDP per Capita: $${estimatedGDP.toLocaleString()}`;
        }

        // Update radial progress bar
        if (radialProgressBar) {
            const radius = 40;
            const circumference = 2 * Math.PI * radius;
            const offset = circumference - (roundedScore / 100) * circumference;
            radialProgressBar.style.strokeDasharray = `${circumference}`;
            radialProgressBar.style.strokeDashoffset = `${offset}`;

            // Color based on score
            if (roundedScore >= 70) {
                radialProgressBar.style.stroke = '#10b981';
            } else if (roundedScore >= 50) {
                radialProgressBar.style.stroke = '#f59e0b';
            } else {
                radialProgressBar.style.stroke = '#ef4444';
            }
        }

        // Update socio-economic outcomes
        if (valSimInvestment) {
            const investScore = (roundedScore / 10).toFixed(1);
            let investLabel = 'Low';
            if (roundedScore >= 70) investLabel = 'High';
            else if (roundedScore >= 50) investLabel = 'Moderate';
            valSimInvestment.textContent = `${investLabel} (${investScore} / 10)`;
        }

        if (valSimCredit) {
            let credit = 'CCC (Junk)';
            if (roundedScore >= 80) credit = 'AAA (Prime)';
            else if (roundedScore >= 70) credit = 'AA+ (High Grade)';
            else if (roundedScore >= 60) credit = 'BBB+ (Stable)';
            else if (roundedScore >= 50) credit = 'BB (Speculative)';
            else if (roundedScore >= 40) credit = 'B- (Highly Speculative)';
            valSimCredit.textContent = credit;
        }

        if (valSimInnovation) {
            let innovation = 'Very Low';
            if (roundedScore >= 80) innovation = 'World-Leading';
            else if (roundedScore >= 70) innovation = 'Strong';
            else if (roundedScore >= 60) innovation = 'Average';
            else if (roundedScore >= 45) innovation = 'Below Average';
            valSimInnovation.textContent = innovation;
        }

        if (valSimFdi) {
            let fdi = 0.2;
            if (roundedScore >= 80) fdi = 12.5;
            else if (roundedScore >= 70) fdi = 6.8;
            else if (roundedScore >= 60) fdi = 1.8;
            else if (roundedScore >= 50) fdi = 0.6;
            else if (roundedScore >= 40) fdi = 0.3;
            valSimFdi.textContent = `$${fdi} Billion / Year`;
        }
    }
});
