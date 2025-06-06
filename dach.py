import gradio as gr
import modelscope_studio.components.antd as antd
import modelscope_studio.components.base as ms
import modelscope_studio.components.pro as pro

with gr.Blocks() as demo, ms.Application(), antd.ConfigProvider():
    pro.WebSandbox(
        value={
            "./index.html":
            """ 
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Requests & Services Statistics Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        .status-dot {
            height: 10px;
            width: 10px;
            border-radius: 50%;
            display: inline-block;
        }
        
        /* Custom animation for KPIs */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .pulse {
            animation: pulse 2s infinite;
        }
        
        /* Sankey diagram placeholder */
        .sankey-container {
            height: 300px;
            background-image: 
                linear-gradient(90deg, #f0f0f0 1px, transparent 1px),
                linear-gradient(#f0f0f0 1px, transparent 1px);
            background-size: 20px 20px;
        }
    </style>
</head>
<body class="bg-gray-50">
    <div class="container mx-auto px-4 py-8">
        <!-- Header -->
        <header class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">Requests & Services Statistics</h1>
            <p class="text-gray-600">Dashboard showing historical data and performance metrics</p>
            <div class="flex items-center mt-2">
                <span class="status-dot bg-green-500 mr-1"></span>
                <span class="text-xs text-gray-500">Live data updating every 5 minutes</span>
            </div>
        </header>

        <!-- KPIs Section -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-6 mb-6">
            <!-- Total Users KPI -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Users</p>
                        <h2 class="text-2xl font-bold text-blue-600 my-1">15,284</h2>
                    </div>
                    <div class="bg-blue-100 p-2 rounded-lg">
                        <i class="fas fa-users text-blue-600"></i>
                    </div>
                </div>
            </div>

            <!-- Total Subscriptions -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Subscriptions</p>
                        <h2 class="text-2xl font-bold text-indigo-600 my-1">8,760</h2>
                    </div>
                    <div class="bg-indigo-100 p-2 rounded-lg">
                        <i class="fas fa-id-card text-indigo-600"></i>
                    </div>
                </div>
            </div>

            <!-- Total Requests -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Requests</p>
                        <h2 class="text-2xl font-bold text-purple-600 my-1">384M</h2>
                    </div>
                    <div class="bg-purple-100 p-2 rounded-lg">
                        <i class="fas fa-exchange-alt text-purple-600"></i>
                    </div>
                </div>
            </div>

            <!-- Total Revenue -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Revenue</p>
                        <h2 class="text-2xl font-bold text-green-600 my-1">$3.1M</h2>
                    </div>
                    <div class="bg-green-100 p-2 rounded-lg">
                        <i class="fas fa-dollar-sign text-green-600"></i>
                    </div>
                </div>
            </div>

            <!-- Total AI Models -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">AI Models</p>
                        <h2 class="text-2xl font-bold text-pink-600 my-1">127</h2>
                    </div>
                    <div class="bg-pink-100 p-2 rounded-lg">
                        <i class="fas fa-brain text-pink-600"></i>
                    </div>
                </div>
            </div>

            <!-- Total Spaces -->
            <div class="bg-white rounded-lg shadow p-4 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Spaces</p>
                        <h2 class="text-2xl font-bold text-orange-600 my-1">2,843</h2>
                    </div>
                    <div class="bg-orange-100 p-2 rounded-lg">
                        <i class="fas fa-cubes text-orange-600"></i>
                    </div>
                </div>
            </div>
        </div>

        <!-- Date Filter -->
        <div class="bg-white rounded-lg shadow p-4 mb-6 flex flex-wrap items-center justify-between">
            <div class="flex items-center space-x-2 mb-2 sm:mb-0">
                <i class="fas fa-calendar text-blue-500"></i>
                <span class="text-sm font-medium text-gray-700">Time Period:</span>
            </div>
            <div class="flex flex-wrap gap-2">
                <button class="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200">Today</button>
                <button class="px-3 py-1 text-xs bg-blue-600 text-white rounded-full">Last 7 days</button>
                <button class="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200">This month</button>
                <button class="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200">Custom range</button>
            </div>
        </div>

        <!-- KPIs Row -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <!-- Total Requests KPI -->
            <div class="bg-white rounded-lg shadow p-6 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Requests</p>
                        <h2 class="text-3xl font-bold text-blue-600 my-2">24,789</h2>
                        <p class="text-xs text-green-500 flex items-center">
                            <i class="fas fa-arrow-up mr-1"></i> 12.5% from last period
                        </p>
                    </div>
                    <div class="bg-blue-100 p-2 rounded-lg">
                        <i class="fas fa-exchange-alt text-blue-600 text-xl"></i>
                    </div>
                </div>
            </div>
            
            <!-- Avg Processing Time -->
            <div class="bg-white rounded-lg shadow p-6 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Avg Processing Time</p>
                        <h2 class="text-3xl font-bold text-indigo-600 my-2">1.24 <span class="text-sm">seconds</span></h2>
                        <p class="text-xs text-green-500 flex items-center">
                            <i class="fas fa-arrow-down mr-1"></i> 23% faster
                        </p>
                    </div>
                    <div class="bg-indigo-100 p-2 rounded-lg">
                        <i class="fas fa-stopwatch text-indigo-600 text-xl"></i>
                    </div>
                </div>
            </div>
            
            <!-- Success Rate -->
            <div class="bg-white rounded-lg shadow p-6 hover:shadow-lg transition-shadow">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Success Rate</p>
                        <h2 class="text-3xl font-bold text-green-600 my-2">98.7%</h2>
                        <p class="text-xs text-red-500 flex items-center">
                            <i class="fas fa-exclamation-triangle mr-1"></i> 34 failed requests
                        </p>
                    </div>
                    <div class="bg-green-100 p-2 rounded-lg pulse">
                        <i class="fas fa-check-circle text-green-600 text-xl"></i>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- Request Status Distribution -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Request Status Distribution</h3>
                    <div class="flex space-x-2">
                        <button class="p-1 text-blue-500 hover:bg-blue-50 rounded">
                            <i class="fas fa-expand"></i>
                        </button>
                    </div>
                </div>
                <div class="h-64">
                    <canvas id="statusChart" class="w-full h-full"></canvas>
                </div>
            </div>
            
            <!-- Requests by Service -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Requests per Service</h3>
                    <div class="flex space-x-2">
                        <span class="text-xs bg-gray-100 px-2 py-1 rounded-full">Last 7 days</span>
                        <button class="p-1 text-blue-500 hover:bg-blue-50 rounded">
                            <i class="fas fa-expand"></i>
                        </button>
                    </div>
                </div>
                <div class="h-64">
                    <canvas id="serviceChart" class="w-full h-full"></canvas>
                </div>
            </div>
        </div>

        <!-- Secondary Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- Requests by AI Model -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Requests by AI Model</h3>
                    <div class="flex items-center space-x-2">
                        <span class="text-xs bg-gray-100 px-2 py-1 rounded-full">Top 5</span>
                        <button class="p-1 text-blue-500 hover:bg-blue-50 rounded">
                            <i class="fas fa-expand"></i>
                        </button>
                    </div>
                </div>
                <div class="h-64">
                    <canvas id="modelChart" class="w-full h-full"></canvas>
                </div>
            </div>
            
            <!-- Requests Trend Over Time -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Requests Trend Over Time</h3>
                    <div class="flex items-center space-x-2">
                        <span class="text-xs bg-gray-100 px-2 py-1 rounded-full">Hourly</span>
                        <button class="p-1 text-blue-500 hover:bg-blue-50 rounded">
                            <i class="fas fa-expand"></i>
                        </button>
                    </div>
                </div>
                <div class="h-64">
                    <canvas id="trendChart" class="w-full h-full"></canvas>
                </div>
            </div>
        </div>

        <!-- Additional Data Section -->
        <div class="grid grid-cols-1 gap-6">
            <!-- Error Summary -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Error & Failure Summary</h3>
                    <button class="text-sm text-blue-500 hover:bg-blue-50 px-3 py-1 rounded">
                        View Details
                    </button>
                </div>
                <div class="h-64">
                    <canvas id="errorChart" class="w-full h-full"></canvas>
                </div>
            </div>
            
            <!-- Request Events -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-semibold text-gray-800">Request Flow Distribution</h3>
                    <button class="text-sm text-blue-500 hover:bg-blue-50 px-3 py-1 rounded">
                        Export Data
                    </button>
                </div>
                <div class="sankey-container rounded-lg border border-gray-200 flex items-center justify-center">
                    <div class="text-center p-6">
                        <i class="fas fa-project-diagram text-4xl text-gray-300 mb-3"></i>
                        <p class="text-gray-500">Sankey diagram visualization would appear here</p>
                        <p class="text-xs text-gray-400 mt-2">(Requires specialized library or custom implementation)</p>
                    </div>
                </div>
            </div>
            
            <!-- Recent Requests Table -->
            <div class="bg-white rounded-lg shadow overflow-hidden">
                <div class="flex items-center justify-between p-6 pb-0">
                    <h3 class="font-semibold text-gray-800">Recent Requests (Last 50)</h3>
                    <button class="text-sm text-blue-500 hover:bg-blue-50 px-3 py-1 rounded">
                        View All
                    </button>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-sm">
                        <thead class="bg-gray-50 text-gray-500">
                            <tr>
                                <th class="p-3 text-left">ID</th>
                                <th class="p-3 text-left">Service</th>
                                <th class="p-3 text-left">Model</th>
                                <th class="p-3 text-left">Status</th>
                                <th class="p-3 text-left">Duration</th>
                                <th class="p-3 text-left">Timestamp</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-200">
                            <tr>
                                <td class="p-3 font-mono text-xs">#REQ-78901</td>
                                <td class="p-3">Chat API</td>
                                <td class="p-3">GPT-4</td>
                                <td class="p-3"><span class="px-2 py-0.5 bg-green-100 text-green-800 text-xs rounded-full">Completed</span></td>
                                <td class="p-3">1.2s</td>
                                <td class="p-3 text-gray-500">2 mins ago</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-mono text-xs">#REQ-78900</td>
                                <td class="p-3">Image Gen</td>
                                <td class="p-3">DALL·E 3</td>
                                <td class="p-3"><span class="px-2 py-0.5 bg-yellow-100 text-yellow-800 text-xs rounded-full">Processing</span></td>
                                <td class="p-3">-</td>
                                <td class="p-3 text-gray-500">5 mins ago</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-mono text-xs">#REQ-78899</td>
                                <td class="p-3">Embeddings</td>
                                <td class="p-3">Ada v2</td>
                                <td class="p-3"><span class="px-2 py-0.5 bg-red-100 text-red-800 text-xs rounded-full">Failed</span></td>
                                <td class="p-3">0.4s</td>
                                <td class="p-3 text-gray-500">12 mins ago</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-mono text-xs">#REQ-78898</td>
                                <td class="p-3">Code Analysis</td>
                                <td class="p-3">Codex</td>
                                <td class="p-3"><span class="px-2 py-0.5 bg-green-100 text-green-800 text-xs rounded-full">Completed</span></td>
                                <td class="p-3">1.8s</td>
                                <td class="p-3 text-gray-500">18 mins ago</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="bg-gray-50 px-6 py-3 text-right">
                    <button class="text-sm text-blue-500 hover:underline">View more records →</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Initialize charts after DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Request Status Distribution - Doughnut Chart
            const statusCtx = document.getElementById('statusChart').getContext('2d');
            const statusChart = new Chart(statusCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Completed', 'Failed', 'Processing'],
                    datasets: [{
                        data: [18543, 267, 5980],
                        backgroundColor: [
                            '#10B981', // green
                            '#EF4444', // red
                            '#F59E0B'  // amber
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.raw || 0;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = Math.round((value / total) * 100);
                                    return `${label}: ${value.toLocaleString()} (${percentage}%)`;
                                }
                            }
                        }
                    },
                    cutout: '70%'
                }
            });

            // Requests per Service - Bar Chart
            const serviceCtx = document.getElementById('serviceChart').getContext('2d');
            const serviceChart = new Chart(serviceCtx, {
                type: 'bar',
                data: {
                    labels: ['Chat API', 'Image Generation', 'Text Embedding', 'Audio Processing', 'Code Analysis', 'Moderation'],
                    datasets: [{
                        label: 'Requests',
                        data: [8560, 4320, 3780, 2150, 2870, 3100],
                        backgroundColor: [
                            '#3B82F6', '#6366F1', '#8B5CF6', '#EC4899', '#F97316', '#10B981'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                display: false
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });

            // Requests by AI Model - Horizontal Bar Chart
            const modelCtx = document.getElementById('modelChart').getContext('2d');
            const modelChart = new Chart(modelCtx, {
                type: 'bar',
                data: {
                    labels: ['GPT-4', 'DALL·E 3', 'Claude 2', 'Llama 2', 'PaLM 2'],
                    datasets: [{
                        label: 'Requests',
                        data: [12000, 6400, 2800, 1500, 1100],
                        backgroundColor: '#6366F1',
                        borderWidth: 0
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            beginAtZero: true,
                            grid: {
                                display: false
                            }
                        },
                        y: {
                            grid: {
                                display: false
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });

            // Requests Trend Over Time - Line Chart
            const trendCtx = document.getElementById('trendChart').getContext('2d');
            const trendChart = new Chart(trendCtx, {
                type: 'line',
                data: {
                    labels: Array.from({length: 24}, (_, i) => `${i}:00`),
                    datasets: [{
                        label: 'Requests',
                        data: [120, 80, 60, 50, 70, 90, 150, 300, 420, 560, 720, 850, 920, 880, 820, 780, 860, 930, 1020, 1150, 1080, 920, 730, 450],
                        fill: false,
                        borderColor: '#10B981',
                        backgroundColor: '#10B981',
                        tension: 0.4,
                        borderWidth: 3,
                        pointRadius: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                display: false
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });

            // Error Summary - Stacked Bar Chart
            const errorCtx = document.getElementById('errorChart').getContext('2d');
            const errorChart = new Chart(errorCtx, {
                type: 'bar',
                data: {
                    labels: ['Chat API', 'Image Gen', 'Embeddings', 'Audio', 'Code', 'Moderation'],
                    datasets: [
                        {
                            label: 'Timeout Errors',
                            data: [12, 5, 3, 8, 2, 1],
                            backgroundColor: '#F97316'
                        },
                        {
                            label: 'Rate Limits',
                            data: [8, 2, 1, 4, 3, 0],
                            backgroundColor: '#F59E0B'
                        },
                        {
                            label: 'Content Policy',
                            data: [3, 15, 1, 2, 1, 7],
                            backgroundColor: '#F43F5E'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            stacked: true,
                            grid: {
                                display: false
                            }
                        },
                        y: {
                            stacked: true,
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        });
    </script>

    <!-- Users & Subscriptions Section -->
    <div id="users-stats" class="container mx-auto px-4 py-8">
        <!-- Header -->
        <header class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">Users & Subscriptions Statistics</h1>
            <p class="text-gray-600">Dashboard showing user activity and subscription metrics</p>
        </header>

        <!-- Active Users KPI -->
        <div class="bg-white rounded-lg shadow p-6 mb-8">
            <h3 class="font-semibold text-gray-800 mb-4">Active Users</h3>
            <div class="flex items-center justify-between">
                <div>
                    <h2 class="text-4xl font-bold text-blue-600">8,421</h2>
                    <p class="text-xs text-green-500 flex items-center">
                        <i class="fas fa-arrow-up mr-1"></i> 7.5% from last month
                    </p>
                </div>
                <div class="text-gray-500 text-sm">
                    Out of 15,284 total registered users
                </div>
            </div>
        </div>

        <!-- Top Charts Row -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- User Status Distribution -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">User Status Distribution</h3>
                <div class="h-64">
                    <canvas id="userStatusChart"></canvas>
                </div>
            </div>

            <!-- Subscriptions by Plan -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">Subscriptions by Plan</h3>
                <div class="h-64">
                    <canvas id="subscriptionPlanChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Bottom Charts Row -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- New Users Trend -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">New User Registrations</h3>
                <div class="h-64">
                    <canvas id="newUsersChart"></canvas>
                </div>
            </div>

            <!-- Last Login Activity -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">User Login Activity</h3>
                <div class="h-64">
                    <canvas id="loginActivityChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Request Per User -->
        <div class="bg-white rounded-lg shadow p-6">
            <h3 class="font-semibold text-gray-800 mb-4">Average Requests per Active User</h3>
            <div class="h-64">
                <canvas id="requestsPerUserChart"></canvas>
            </div>
        </div>
    </div>

    <!-- AI Models Statistics Section -->
    <div id="ai-models-stats" class="container mx-auto px-4 py-8">
        <!-- Header -->
        <header class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">AI Models Statistics</h1>
            <p class="text-gray-600">Dashboard showing model distribution and usage metrics</p>
        </header>

        <!-- Models KPIs Row -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <!-- Total Models KPI -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total AI Models</p>
                        <h2 class="text-3xl font-bold text-blue-600 my-2">127</h2>
                        <p class="text-xs text-green-500 flex items-center">
                            <i class="fas fa-arrow-up mr-1"></i> 8% growth
                        </p>
                    </div>
                    <div class="bg-blue-100 p-2 rounded-lg">
                        <i class="fas fa-brain text-blue-600 text-xl"></i>
                    </div>
                </div>
            </div>

            <!-- Categories Distribution Chart -->
            <div class="bg-white rounded-lg shadow p-6 md:col-span-2">
                <h3 class="font-semibold text-gray-800 mb-4">Models by Category</h3>
                <div class="h-64">
                    <canvas id="categoryChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Charts Row -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- Language Support Chart -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">Models by Supported Language</h3>
                <div class="h-64">
                    <canvas id="languageChart"></canvas>
                </div>
            </div>

            <!-- Custom vs Standard Chart -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">Custom vs Standard Models</h3>
                <div class="h-64">
                    <canvas id="modelTypeChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Most Used Models -->
        <div class="bg-white rounded-lg shadow p-6">
            <h3 class="font-semibold text-gray-800 mb-4">Most Used Models (Last 30 Days)</h3>
            <div class="h-64">
                <canvas id="popularModelsChart"></canvas>
            </div>
        </div>
    </div>

    <!-- Spaces Statistics Section -->
    <div id="spaces-stats" class="container mx-auto px-4 py-8">
        <!-- Header -->
        <header class="mb-8">
            <h1 class="text-3xl font-bold text-gray-800">Spaces Statistics</h1>
            <p class="text-gray-600">Dashboard showing spaces deployment and resource utilization</p>
        </header>

        <!-- Spaces KPIs -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <!-- Total Spaces KPI -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Spaces</p>
                        <h2 class="text-3xl font-bold text-blue-600 my-2">2,843</h2>
                        <p class="text-xs text-green-500 flex items-center">
                            <i class="fas fa-arrow-up mr-1"></i> 15 new today
                        </p>
                    </div>
                    <div class="bg-blue-100 p-2 rounded-lg">
                        <i class="fas fa-cubes text-blue-600 text-xl"></i>
                    </div>
                </div>
            </div>

            <!-- GPU vs Non-GPU Chart -->
            <div class="bg-white rounded-lg shadow p-6 md:col-span-2">
                <h3 class="font-semibold text-gray-800 mb-4">GPU vs Non-GPU Spaces</h3>
                <div class="h-64">
                    <canvas id="gpuChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Resource Usage -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <!-- RAM Usage KPI -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total RAM Usage</p>
                        <h2 class="text-3xl font-bold text-indigo-600 my-2">42.7 <span class="text-sm">TB</span></h2>
                        <p class="text-xs text-gray-500">Across all spaces</p>
                    </div>
                    <div class="bg-indigo-100 p-2 rounded-lg">
                        <i class="fas fa-memory text-indigo-600 text-xl"></i>
                    </div>
                </div>
            </div>

            <!-- CPU Usage KPI -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total CPU Cores</p>
                        <h2 class="text-3xl font-bold text-purple-600 my-2">5,284</h2>
                        <p class="text-xs text-gray-500">Allocated to spaces</p>
                    </div>
                    <div class="bg-purple-100 p-2 rounded-lg">
                        <i class="fas fa-microchip text-purple-600 text-xl"></i>
                    </div>
                </div>
            </div>

            <!-- Disk Usage KPI -->
            <div class="bg-white rounded-lg shadow p-6">
                <div class="flex items-start justify-between">
                    <div>
                        <p class="text-gray-500 text-sm font-medium">Total Disk Usage</p>
                        <h2 class="text-3xl font-bold text-pink-600 my-2">387 <span class="text-sm">TB</span></h2>
                        <p class="text-xs text-gray-500">Across all spaces</p>
                    </div>
                    <div class="bg-pink-100 p-2 rounded-lg">
                        <i class="fas fa-hdd text-pink-600 text-xl"></i>
                    </div>
                </div>
            </div>
        </div>

        <!-- Additional Spaces Stats -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- Public vs Private Chart -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-4">Public vs Private Spaces</h3>
                <div class="h-64">
                    <canvas id="visibilityChart"></canvas>
                </div>
            </div>

            <!-- Avg Resources Per Space -->
            <div class="bg-white rounded-lg shadow p-6">
                <h3 class="font-semibold text-gray-800 mb-6">Average Resources per Space</h3>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow transition-shadow">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-gray-500 text-xs font-medium uppercase tracking-wider">RAM</p>
                                <p class="text-2xl font-bold text-indigo-600 my-1">15.2 <span class="text-sm">GB</span></p>
                                <p class="text-xs text-green-500 flex items-center">
                                    <i class="fas fa-arrow-up mr-1"></i> 5% from last month
                                </p>
                            </div>
                            <div class="bg-indigo-100 p-2 rounded-lg">
                                <i class="fas fa-memory text-indigo-600"></i>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow transition-shadow">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-gray-500 text-xs font-medium uppercase tracking-wider">CPU Cores</p>
                                <p class="text-2xl font-bold text-purple-600 my-1">2.1</p>
                                <p class="text-xs text-gray-500">Avg per space</p>
                            </div>
                            <div class="bg-purple-100 p-2 rounded-lg">
                                <i class="fas fa-microchip text-purple-600"></i>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow transition-shadow">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-gray-500 text-xs font-medium uppercase tracking-wider">Storage</p>
                                <p class="text-2xl font-bold text-pink-600 my-1">142 <span class="text-sm">GB</span></p>
                                <p class="text-xs text-gray-500 flex items-center">
                                    <span class="w-2 h-2 bg-yellow-400 rounded-full mr-1"></span>
                                    Modest growth
                                </p>
                            </div>
                            <div class="bg-pink-100 p-2 rounded-lg">
                                <i class="fas fa-hdd text-pink-600"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Initialize charts for Users & Subscriptions page
        function initUsersCharts() {
            // User Status Distribution (Pie)
            new Chart(document.getElementById('userStatusChart'), {
                type: 'pie',
                data: {
                    labels: ['Active', 'Archived', 'New (7d)'],
                    datasets: [{
                        data: [8421, 4360, 1250],
                        backgroundColor: ['#10B981', '#6366F1', '#3B82F6']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Subscription Plans (Bar)
            new Chart(document.getElementById('subscriptionPlanChart'), {
                type: 'bar',
                data: {
                    labels: ['Free', 'Pro', 'Business', 'Enterprise'],
                    datasets: [{
                        label: 'Subscriptions',
                        data: [3250, 4270, 950, 290],
                        backgroundColor: '#8B5CF6'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // New Users Trend (Line)
            new Chart(document.getElementById('newUsersChart'), {
                type: 'line',
                data: {
                    labels: Array.from({length: 12}, (_, i) => `${i+1} months ago`).reverse(),
                    datasets: [{
                        label: 'New Users',
                        data: [150, 180, 210, 240, 290, 320, 380, 420, 450, 480, 510, 540],
                        fill: false,
                        borderColor: '#3B82F6',
                        tension: 0.3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Login Activity (Bar)
            new Chart(document.getElementById('loginActivityChart'), {
                type: 'bar',
                data: {
                    labels: ['Last 24h', 'Last week', 'Last month', 'Over month ago'],
                    datasets: [{
                        label: 'Users',
                        data: [2850, 3720, 5120, 3685],
                        backgroundColor: '#EC4899'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Requests Per User (Line)
            new Chart(document.getElementById('requestsPerUserChart'), {
                type: 'line',
                data: {
                    labels: Array.from({length: 7}, (_, i) => `Day ${i+1}`),
                    datasets: [{
                        label: 'Average Requests',
                        data: [45, 52, 38, 41, 56, 42, 48],
                        fill: false,
                        borderColor: '#10B981',
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        }

        // Initialize charts for AI Models page
        function initModelsCharts() {
            // Category Distribution (Pie)
            new Chart(document.getElementById('categoryChart'), {
                type: 'pie',
                data: {
                    labels: ['LLM', 'Image', 'Audio', 'Video', 'Multimodal', 'Other'],
                    datasets: [{
                        data: [65, 22, 18, 8, 12, 2],
                        backgroundColor: [
                            '#3B82F6', '#6366F1', '#8B5CF6', '#EC4899', '#F97316', '#10B981'
                        ]
                    }],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Language Support (Horizontal Bar)
            new Chart(document.getElementById('languageChart'), {
                type: 'bar',
                data: {
                    labels: ['English', 'Multilingual', 'Chinese', 'Spanish', 'French'],
                    datasets: [{
                        label: 'Models',
                        data: [87, 45, 32, 28, 19],
                        backgroundColor: '#6366F1'
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Custom vs Standard (Doughnut)
            new Chart(document.getElementById('modelTypeChart'), {
                type: 'doughnut',
                data: {
                    labels: ['Standard', 'Custom'],
                    datasets: [{
                        data: [85, 42],
                        backgroundColor: ['#10B981', '#3B82F6']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '70%'
                }
            });

            // Popular Models (Bar)
            new Chart(document.getElementById('popularModelsChart'), {
                type: 'bar',
                data: {
                    labels: ['GPT-4', 'Llama 2 70B', 'Claude 2', 'DALL·E 3', 'Whisper'],
                    datasets: [{
                        label: 'Requests (thousands)',
                        data: [1870, 1230, 980, 840, 550],
                        backgroundColor: '#EC4899'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        }

        // Initialize charts for Spaces page
        function initSpacesCharts() {
            // GPU Distribution (Pie)
            new Chart(document.getElementById('gpuChart'), {
                type: 'pie',
                data: {
                    labels: ['GPU Enabled', 'CPU Only'],
                    datasets: [{
                        data: [1430, 1413],
                        backgroundColor: ['#F97316', '#3B82F6']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Visibility (Doughnut)
            new Chart(document.getElementById('visibilityChart'), {
                type: 'doughnut',
                data: {
                    labels: ['Public', 'Private'],
                    datasets: [{
                        data: [1985, 858],
                        backgroundColor: ['#10B981', '#6366F1']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '70%'
                }
            });
        }

        // Initialize all charts when DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {
            initUsersCharts();
            initModelsCharts();
            initSpacesCharts();
        });
    </script>
</body>
</html>
 
                        
                    """
        },
        template="html",
        height=600,
    )


