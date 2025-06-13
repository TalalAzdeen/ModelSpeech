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
    <title>RoadGuard - Intelligent Road Monitoring System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .gradient-bg {
            background: linear-gradient(135deg, #1e3a8a 0%, #0ea5e9 100%);
        }
        .road-pattern {
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 10h100v1H0z' fill='%23ffffff' fill-opacity='0.1'/%3E%3C/svg%3E");
        }
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        .map-container {
            height: 400px;
            background-image: url('https://maps.googleapis.com/maps/api/staticmap?center=24.7136,46.6753&zoom=11&size=800x400&maptype=roadmap&key=YOUR_API_KEY');
            background-size: cover;
            background-position: center;
        }
        .animate-pulse-slow {
            animation: pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
    </style>
</head>
<body class="bg-gray-50 font-sans antialiased">
    <!-- Navigation -->
    <nav class="gradient-bg text-white shadow-lg">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <i class="fas fa-road text-2xl"></i>
                <span class="text-xl font-bold">RoadGuard</span>
            </div>
            <div class="hidden md:flex space-x-8">
                <a href="#features" class="hover:text-blue-200 transition">Features</a>
                <a href="#dashboard" class="hover:text-blue-200 transition">Dashboard</a>
                <a href="#technology" class="hover:text-blue-200 transition">Technology</a>
                <a href="#contact" class="hover:text-blue-200 transition">Contact</a>
            </div>
            <button class="md:hidden text-white focus:outline-none">
                <i class="fas fa-bars text-2xl"></i>
            </button>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="gradient-bg road-pattern text-white py-20">
        <div class="container mx-auto px-4 flex flex-col md:flex-row items-center">
            <div class="md:w-1/2 mb-10 md:mb-0">
                <h1 class="text-4xl md:text-5xl font-bold mb-6">Intelligent Road Monitoring System</h1>
                <p class="text-xl mb-8 text-blue-100">Proactively detect and repair road damage to improve safety and reduce maintenance costs.</p>
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                    <button class="bg-white text-blue-900 px-6 py-3 rounded-lg font-semibold hover:bg-blue-100 transition">Request Demo</button>
                    <button class="border border-white text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition">Learn More</button>
                </div>
            </div>
            <div class="md:w-1/2 flex justify-center">
                <div class="relative w-full max-w-md">
                    <div class="bg-white bg-opacity-20 backdrop-blur-lg rounded-xl p-6 shadow-xl">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="font-bold text-lg">Live Alerts</h3>
                            <span class="bg-red-500 text-white text-xs px-2 py-1 rounded-full animate-pulse-slow">3 New</span>
                        </div>
                        <div class="space-y-4">
                            <div class="bg-white bg-opacity-10 p-3 rounded-lg">
                                <div class="flex items-start">
                                    <div class="bg-red-500 p-2 rounded-full mr-3">
                                        <i class="fas fa-exclamation text-white"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold">Pothole Detected</h4>
                                        <p class="text-sm text-blue-100">King Fahd Rd, Near Exit 15</p>
                                        <p class="text-xs text-blue-200">10 minutes ago</p>
                                    </div>
                                </div>
                            </div>
                            <div class="bg-white bg-opacity-10 p-3 rounded-lg">
                                <div class="flex items-start">
                                    <div class="bg-yellow-500 p-2 rounded-full mr-3">
                                        <i class="fas fa-road text-white"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold">Crack Formation</h4>
                                        <p class="text-sm text-blue-100">Olaya St, Section 3</p>
                                        <p class="text-xs text-blue-200">45 minutes ago</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Features Section -->
    <section id="features" class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-800 mb-4">Key Features</h2>
                <p class="text-gray-600 max-w-2xl mx-auto">Our comprehensive solution combines advanced technology with practical monitoring to keep roads safe and well-maintained.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-blue-100 text-blue-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-eye text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">Real-time Monitoring</h3>
                    <p class="text-gray-600">Continuous surveillance of road conditions using vehicle-mounted cameras and drones for comprehensive coverage.</p>
                </div>
                
                <!-- Feature 2 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-green-100 text-green-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-brain text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">AI-Powered Detection</h3>
                    <p class="text-gray-600">Advanced computer vision algorithms accurately identify potholes, cracks, and other road surface anomalies.</p>
                </div>
                
                <!-- Feature 3 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-purple-100 text-purple-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-map-marked-alt text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">Precision Mapping</h3>
                    <p class="text-gray-600">GPS-tagged damage locations with severity ratings for efficient maintenance prioritization.</p>
                </div>
                
                <!-- Feature 4 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-yellow-100 text-yellow-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-chart-line text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">Predictive Analytics</h3>
                    <p class="text-gray-600">Machine learning models predict potential problem areas before they become critical issues.</p>
                </div>
                
                <!-- Feature 5 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-red-100 text-red-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-bell text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">Automated Alerts</h3>
                    <p class="text-gray-600">Instant notifications to maintenance teams when critical road damage is detected.</p>
                </div>
                
                <!-- Feature 6 -->
                <div class="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition card-hover">
                    <div class="bg-indigo-100 text-indigo-800 w-12 h-12 rounded-full flex items-center justify-center mb-4">
                        <i class="fas fa-file-alt text-xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3 text-gray-800">Comprehensive Reporting</h3>
                    <p class="text-gray-600">Detailed reports on road conditions, maintenance history, and repair progress.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Dashboard Preview -->
    <section id="dashboard" class="py-16 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800 mb-4">Interactive Dashboard</h2>
                <p class="text-gray-600 max-w-2xl mx-auto">Monitor road conditions in real-time with our intuitive dashboard interface.</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg overflow-hidden">
                <div class="flex border-b border-gray-200">
                    <div class="px-4 py-3 bg-gray-100 text-gray-700 font-medium">Map View</div>
                    <div class="px-4 py-3 text-gray-500">Damage Reports</div>
                    <div class="px-4 py-3 text-gray-500">Maintenance Log</div>
                    <div class="px-4 py-3 text-gray-500">Analytics</div>
                </div>
                
                <div class="p-4">
                    <div class="map-container rounded-lg overflow-hidden relative">
                        <div class="absolute top-4 left-4 bg-white p-2 rounded-lg shadow-md z-10">
                            <div class="flex items-center space-x-2">
                                <span class="w-3 h-3 rounded-full bg-red-500"></span>
                                <span class="text-sm">Critical</span>
                            </div>
                            <div class="flex items-center space-x-2 mt-1">
                                <span class="w-3 h-3 rounded-full bg-yellow-500"></span>
                                <span class="text-sm">Moderate</span>
                            </div>
                            <div class="flex items-center space-x-2 mt-1">
                                <span class="w-3 h-3 rounded-full bg-green-500"></span>
                                <span class="text-sm">Minor</span>
                            </div>
                        </div>
                        
                        <!-- Map markers would be placed here in a real implementation -->
                        <div class="absolute top-1/3 left-1/4">
                            <div class="w-4 h-4 bg-red-500 rounded-full animate-ping"></div>
                            <div class="w-4 h-4 bg-red-500 rounded-full -mt-4"></div>
                        </div>
                        <div class="absolute top-2/5 left-3/5">
                            <div class="w-4 h-4 bg-yellow-500 rounded-full animate-ping"></div>
                            <div class="w-4 h-4 bg-yellow-500 rounded-full -mt-4"></div>
                        </div>
                        <div class="absolute top-1/2 left-1/3">
                            <div class="w-4 h-4 bg-green-500 rounded-full animate-ping"></div>
                            <div class="w-4 h-4 bg-green-500 rounded-full -mt-4"></div>
                        </div>
                    </div>
                    
                    <div class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="bg-blue-50 p-4 rounded-lg">
                            <div class="flex justify-between items-start">
                                <div>
                                    <p class="text-sm text-blue-600">Total Issues Detected</p>
                                    <h3 class="text-2xl font-bold text-gray-800">1,248</h3>
                                </div>
                                <div class="bg-blue-100 text-blue-800 p-2 rounded-full">
                                    <i class="fas fa-road"></i>
                                </div>
                            </div>
                            <div class="mt-2">
                                <span class="text-green-600 text-sm">+12% from last week</span>
                            </div>
                        </div>
                        
                        <div class="bg-yellow-50 p-4 rounded-lg">
                            <div class="flex justify-between items-start">
                                <div>
                                    <p class="text-sm text-yellow-600">Pending Repairs</p>
                                    <h3 class="text-2xl font-bold text-gray-800">87</h3>
                                </div>
                                <div class="bg-yellow-100 text-yellow-800 p-2 rounded-full">
                                    <i class="fas fa-tools"></i>
                                </div>
                            </div>
                            <div class="mt-2">
                                <span class="text-red-600 text-sm">-5% from last week</span>
                            </div>
                        </div>
                        
                        <div class="bg-green-50 p-4 rounded-lg">
                            <div class="flex justify-between items-start">
                                <div>
                                    <p class="text-sm text-green-600">Repairs Completed</p>
                                    <h3 class="text-2xl font-bold text-gray-800">1,161</h3>
                                </div>
                                <div class="bg-green-100 text-green-800 p-2 rounded-full">
                                    <i class="fas fa-check-circle"></i>
                                </div>
                            </div>
                            <div class="mt-2">
                                <span class="text-green-600 text-sm">+18% from last week</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Technology Stack -->
    <section id="technology" class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800 mb-4">Advanced Technology Stack</h2>
                <p class="text-gray-600 max-w-2xl mx-auto">Combining cutting-edge technologies to deliver accurate road monitoring solutions</p>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div class="bg-gray-50 p-6 rounded-xl text-center">
                    <div class="bg-blue-100 text-blue-800 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-robot text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Computer Vision</h3>
                    <p class="text-gray-600 text-sm">Advanced image analysis for precise damage detection</p>
                </div>
                
                <div class="bg-gray-50 p-6 rounded-xl text-center">
                    <div class="bg-purple-100 text-purple-800 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-brain text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Machine Learning</h3>
                    <p class="text-gray-600 text-sm">Self-improving algorithms for better accuracy</p>
                </div>
                
                <div class="bg-gray-50 p-6 rounded-xl text-center">
                    <div class="bg-green-100 text-green-800 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-map-marked-alt text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Geospatial Analysis</h3>
                    <p class="text-gray-600 text-sm">Precise location mapping of road issues</p>
                </div>
                
                <div class="bg-gray-50 p-6 rounded-xl text-center">
                    <div class="bg-yellow-100 text-yellow-800 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-cloud text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Cloud Computing</h3>
                    <p class="text-gray-600 text-sm">Scalable processing of large datasets</p>
                </div>
            </div>
            
            <div class="mt-12 bg-gray-50 rounded-xl p-8">
                <div class="flex flex-col md:flex-row items-center">
                    <div class="md:w-1/2 mb-8 md:mb-0">
                        <h3 class="text-2xl font-bold text-gray-800 mb-4">How It Works</h3>
                        <div class="space-y-4">
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-2 rounded-full mr-4">
                                    <span class="font-bold">1</span>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">Data Collection</h4>
                                    <p class="text-gray-600 text-sm">Cameras and sensors mounted on vehicles capture road surface images and vibration data.</p>
                                </div>
                            </div>
                            
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-2 rounded-full mr-4">
                                    <span class="font-bold">2</span>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">AI Analysis</h4>
                                    <p class="text-gray-600 text-sm">Computer vision algorithms process images to detect and classify road damage.</p>
                                </div>
                            </div>
                            
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-2 rounded-full mr-4">
                                    <span class="font-bold">3</span>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">Reporting</h4>
                                    <p class="text-gray-600 text-sm">Identified issues are geotagged and prioritized in the maintenance dashboard.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="md:w-1/2 flex justify-center">
                        <div class="relative w-full max-w-md">
                            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
                                <div class="flex items-center mb-4">
                                    <div class="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
                                    <div class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></div>
                                    <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
                                </div>
                                <div class="bg-gray-100 rounded-lg p-4 mb-4">
                                    <div class="flex items-center mb-2">
                                        <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                                            <i class="fas fa-car text-blue-800"></i>
                                        </div>
                                        <div>
                                            <h4 class="font-semibold">Vehicle #4521</h4>
                                            <p class="text-xs text-gray-500">Last scan: 5 minutes ago</p>
                                        </div>
                                    </div>
                                    <div class="pl-11">
                                        <div class="flex justify-between text-sm mb-1">
                                            <span>Images processed:</span>
                                            <span class="font-semibold">1,248</span>
                                        </div>
                                        <div class="flex justify-between text-sm mb-1">
                                            <span>Issues detected:</span>
                                            <span class="font-semibold">18</span>
                                        </div>
                                        <div class="flex justify-between text-sm">
                                            <span>Current location:</span>
                                            <span class="font-semibold">King Fahd Rd</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-blue-50 rounded-lg p-3 text-center">
                                    <p class="text-sm text-blue-800 font-medium">3 new critical issues require attention</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section class="py-16 gradient-bg text-white">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold mb-4">Transformative Benefits</h2>
                <p class="max-w-2xl mx-auto text-blue-100">Discover how RoadGuard revolutionizes road maintenance and safety</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white bg-opacity-10 p-6 rounded-xl backdrop-blur-sm">
                    <div class="text-blue-200 mb-4">
                        <i class="fas fa-shield-alt text-3xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3">Enhanced Safety</h3>
                    <p class="text-blue-100">Reduce accidents by up to 40% through early detection of hazardous road conditions.</p>
                </div>
                
                <div class="bg-white bg-opacity-10 p-6 rounded-xl backdrop-blur-sm">
                    <div class="text-blue-200 mb-4">
                        <i class="fas fa-money-bill-wave text-3xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3">Cost Savings</h3>
                    <p class="text-blue-100">Preventive maintenance reduces repair costs by 60% compared to emergency fixes.</p>
                </div>
                
                <div class="bg-white bg-opacity-10 p-6 rounded-xl backdrop-blur-sm">
                    <div class="text-blue-200 mb-4">
                        <i class="fas fa-chart-line text-3xl"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-3">Data-Driven Decisions</h3>
                    <p class="text-blue-100">Comprehensive analytics enable optimized resource allocation and planning.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-16 bg-white">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800 mb-4">Get In Touch</h2>
                <p class="text-gray-600 max-w-2xl mx-auto">Ready to revolutionize your road maintenance strategy? Contact us today.</p>
            </div>
            
            <div class="flex flex-col md:flex-row">
                <div class="md:w-1/2 mb-10 md:mb-0 md:pr-10">
                    <div class="bg-gray-50 p-8 rounded-xl">
                        <h3 class="text-xl font-semibold mb-6 text-gray-800">Contact Information</h3>
                        
                        <div class="space-y-6">
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-3 rounded-full mr-4">
                                    <i class="fas fa-map-marker-alt"></i>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">Office Location</h4>
                                    <p class="text-gray-600">123 Innovation Drive, Tech City, TC 12345</p>
                                </div>
                            </div>
                            
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-3 rounded-full mr-4">
                                    <i class="fas fa-envelope"></i>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">Email Us</h4>
                                    <p class="text-gray-600">info@roadguard.com</p>
                                    <p class="text-gray-600">support@roadguard.com</p>
                                </div>
                            </div>
                            
                            <div class="flex items-start">
                                <div class="bg-blue-100 text-blue-800 p-3 rounded-full mr-4">
                                    <i class="fas fa-phone-alt"></i>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-gray-800">Call Us</h4>
                                    <p class="text-gray-600">+1 (555) 123-4567</p>
                                    <p class="text-gray-600">+1 (555) 765-4321</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="md:w-1/2">
                    <form class="bg-gray-50 p-8 rounded-xl">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                                <input type="text" id="name" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                            </div>
                            <div>
                                <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                                <input type="email" id="email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                            </div>
                        </div>
                        
                        <div class="mb-6">
                            <label for="subject" class="block text-sm font-medium text-gray-700 mb-1">Subject</label>
                            <input type="text" id="subject" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                        </div>
                        
                        <div class="mb-6">
                            <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message</label>
                            <textarea id="message" rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></textarea>
                        </div>
                        
                        <button type="submit" class="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div>
                    <div class="flex items-center space-x-2 mb-4">
                        <i class="fas fa-road text-2xl text-blue-400"></i>
                        <span class="text-xl font-bold">RoadGuard</span>
                    </div>
                    <p class="text-gray-400">Intelligent road monitoring solutions for safer, better-maintained infrastructure.</p>
                    <div class="flex space-x-4 mt-4">
                        <a href="#" class="text-gray-400 hover:text-white transition">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white transition">
                            <i class="fab fa-linkedin-in"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white transition">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white transition">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white transition">Home</a></li>
                        <li><a href="#features" class="text-gray-400 hover:text-white transition">Features</a></li>
                        <li><a href="#dashboard" class="text-gray-400 hover:text-white transition">Dashboard</a></li>
                        <li><a href="#technology" class="text-gray-400 hover:text-white transition">Technology</a></li>
                        <li><a href="#contact" class="text-gray-400 hover:text-white transition">Contact</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-4">Services</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white transition">Road Monitoring</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition">Predictive Maintenance</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition">Damage Analysis</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition">Reporting Tools</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition">API Integration</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-4">Newsletter</h4>
                    <p class="text-gray-400 mb-4">Subscribe to our newsletter for the latest updates.</p>
                    <form class="flex">
                        <input type="email" placeholder="Your email" class="px-4 py-2 rounded-l-lg focus:outline-none text-gray-800 w-full">
                        <button type="submit" class="bg-blue-600 px-4 py-2 rounded-r-lg hover:bg-blue-700 transition">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </form>
                </div>
            </div>
            
            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
                <p class="text-gray-400 mb-4 md:mb-0">© 2023 RoadGuard. All rights reserved.</p>
                <div class="flex space-x-6">
                    <a href="#" class="text-gray-400 hover:text-white transition">Privacy Policy</a>
                    <a href="#" class="text-gray-400 hover:text-white transition">Terms of Service</a>
                    <a href="#" class="text-gray-400 hover:text-white transition">Cookies</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // Simple JavaScript for demonstration purposes
        document.addEventListener('DOMContentLoaded', function() {
            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
            
            // Mobile menu toggle would be implemented here
            const mobileMenuButton = document.querySelector('.md\\:hidden');
            // Implementation would require adding a mobile menu element
        });
    </script>
</body>
</html>
                      
 
                        
                    """
        },
        template="html",
        height=600,
    )
