import React from 'react';
import { motion } from 'framer-motion'
function Dashboard() {
  // Sample data for the dashboard
  const healthMetrics = [
    { label: 'Blood Pressure', value: 120, color: 'bg-blue-500' },
    { label: 'Cholesterol', value: 200, color: 'bg-purple-500' },
    { label: 'RBC Count', value: 5.2, color: 'bg-teal-500' },
    { label: 'WBC Count', value: 7000, color: 'bg-orange-500' },
  ];

  // Find the maximum value for scaling
  const maxValue = Math.max(...healthMetrics.map((metric) => metric.value));

  return (
    <div className="min-h-screen pt-28 bg-gradient-to-r from-blue-500 to-purple-600 text-white p-8">
      <h1 className="text-4xl text-center font-bold mb-8">Health Dashboard</h1>
      <motion.div 
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 0.2 }}
      className="bg-white/90 p-6 rounded-lg shadow-lg max-w-3xl mx-auto">
        {healthMetrics.map((metric) => (
          <div key={metric.label} className="mb-4">
            <div className="text-gray-700 font-semibold mb-1">{metric.label}</div>
            <div className="relative w-full h-8 bg-gray-300 rounded-full overflow-hidden">
              <div
                className={`h-full ${metric.color}`}
                style={{ width: `${(metric.value / maxValue) * 100}%` }}
              ></div>
            </div>
            <div className="text-gray-700 text-sm mt-1">{metric.value}</div>
          </div>
        ))}
      </motion.div>
    </div>
  );
}

export default Dashboard;