// MathEngine Main JavaScript

// Global variables
const mathEngineApp = {
  currentTheme: "dark",
  sessionData: {
    startTime: Date.now(),
    exercisesCompleted: 0,
    correctAnswers: 0,
  },
}

// Declare bootstrap and MathJax variables
const bootstrap = window.bootstrap
const MathJax = window.MathJax

// Initialize application
document.addEventListener("DOMContentLoaded", () => {
  initializeApp()
  setupEventListeners()
  updateSessionInfo()
})

function initializeApp() {
  // Initialize tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))

  // Initialize popovers
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  var popoverList = popoverTriggerList.map((popoverTriggerEl) => new bootstrap.Popover(popoverTriggerEl))

  // Setup MathJax configuration
  if (MathJax) {
    MathJax.startup.defaultReady()
  }

  console.log("MathEngine initialized successfully")
}

function setupEventListeners() {
  // Sidebar collapse for mobile
  const sidebarToggle = document.getElementById("sidebarToggle")
  if (sidebarToggle) {
    sidebarToggle.addEventListener("click", () => {
      document.querySelector(".sidebar").classList.toggle("show")
    })
  }

  // Form validation
  const forms = document.querySelectorAll(".needs-validation")
  forms.forEach((form) => {
    form.addEventListener("submit", (event) => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }
      form.classList.add("was-validated")
    })
  })

  // Auto-resize textareas
  const textareas = document.querySelectorAll("textarea[data-auto-resize]")
  textareas.forEach((textarea) => {
    textarea.addEventListener("input", function () {
      this.style.height = "auto"
      this.style.height = this.scrollHeight + "px"
    })
  })
}

function updateSessionInfo() {
  // Update session timer every minute
  setInterval(() => {
    const elapsed = Math.floor((Date.now() - mathEngineApp.sessionData.startTime) / 60000)
    const sessionElement = document.getElementById("sessionTime")
    if (sessionElement) {
      sessionElement.textContent = elapsed + " min"
    }
  }, 60000)
}

// Utility Functions
function showNotification(message, type = "info", duration = 5000) {
  const notification = document.createElement("div")
  notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`
  notification.style.cssText = "top: 20px; right: 20px; z-index: 9999; min-width: 300px;"

  notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `

  document.body.appendChild(notification)

  // Auto-remove after duration
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove()
    }
  }, duration)
}

function formatMathExpression(expression) {
  // Basic formatting for mathematical expressions
  return expression.replace(/\*\*/g, "^").replace(/\*/g, "×").replace(/\//g, "÷")
}

function copyToClipboard(text) {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text).then(() => {
      showNotification("Copiado al portapapeles", "success", 2000)
    })
  } else {
    // Fallback for older browsers
    const textArea = document.createElement("textarea")
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand("copy")
    document.body.removeChild(textArea)
    showNotification("Copiado al portapapeles", "success", 2000)
  }
}

function validateMathInput(input) {
  // Basic validation for mathematical expressions
  const validChars = /^[0-9+\-*/().\s^√πe]+$/
  return validChars.test(input)
}

function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  const secs = seconds % 60

  if (hours > 0) {
    return `${hours}:${minutes.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`
  } else {
    return `${minutes}:${secs.toString().padStart(2, "0")}`
  }
}

function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Local Storage Utilities
function saveToLocalStorage(key, data) {
  try {
    localStorage.setItem(key, JSON.stringify(data))
    return true
  } catch (error) {
    console.error("Error saving to localStorage:", error)
    return false
  }
}

function loadFromLocalStorage(key, defaultValue = null) {
  try {
    const item = localStorage.getItem(key)
    return item ? JSON.parse(item) : defaultValue
  } catch (error) {
    console.error("Error loading from localStorage:", error)
    return defaultValue
  }
}

// Math-specific utilities
function simplifyFraction(numerator, denominator) {
  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b)
  }

  const divisor = gcd(Math.abs(numerator), Math.abs(denominator))
  return {
    numerator: numerator / divisor,
    denominator: denominator / divisor,
  }
}

function parseUserFraction(input) {
  // Parse various fraction formats: "3/4", "1 1/2", "0.75"
  input = input.trim()

  // Mixed number format: "1 1/2"
  const mixedMatch = input.match(/^(\d+)\s+(\d+)\/(\d+)$/)
  if (mixedMatch) {
    const whole = Number.parseInt(mixedMatch[1])
    const num = Number.parseInt(mixedMatch[2])
    const den = Number.parseInt(mixedMatch[3])
    return {
      numerator: whole * den + num,
      denominator: den,
    }
  }

  // Simple fraction format: "3/4"
  const fractionMatch = input.match(/^(\d+)\/(\d+)$/)
  if (fractionMatch) {
    return {
      numerator: Number.parseInt(fractionMatch[1]),
      denominator: Number.parseInt(fractionMatch[2]),
    }
  }

  // Decimal format: "0.75"
  const decimalMatch = input.match(/^(\d*\.?\d+)$/)
  if (decimalMatch) {
    const decimal = Number.parseFloat(decimalMatch[1])
    // Convert to fraction (simplified approach)
    const denominator = Math.pow(10, (decimal.toString().split(".")[1] || "").length)
    const numerator = decimal * denominator
    return simplifyFraction(numerator, denominator)
  }

  // Whole number
  const wholeMatch = input.match(/^(\d+)$/)
  if (wholeMatch) {
    return {
      numerator: Number.parseInt(wholeMatch[1]),
      denominator: 1,
    }
  }

  return null
}

// Export for use in other modules
window.MathEngineUtils = {
  showNotification,
  formatMathExpression,
  copyToClipboard,
  validateMathInput,
  formatTime,
  debounce,
  saveToLocalStorage,
  loadFromLocalStorage,
  simplifyFraction,
  parseUserFraction,
}

// Theme management
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-bs-theme")
  const newTheme = currentTheme === "dark" ? "light" : "dark"

  document.documentElement.setAttribute("data-bs-theme", newTheme)
  mathEngineApp.currentTheme = newTheme

  // Save preference
  saveToLocalStorage("mathengine_theme", newTheme)

  showNotification(`Tema cambiado a ${newTheme === "dark" ? "oscuro" : "claro"}`, "info", 2000)
}

// Load saved theme on startup
document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = loadFromLocalStorage("mathengine_theme", "dark")
  document.documentElement.setAttribute("data-bs-theme", savedTheme)
  mathEngineApp.currentTheme = savedTheme
})

// Keyboard shortcuts
document.addEventListener("keydown", (e) => {
  // Ctrl/Cmd + K for search (if implemented)
  if ((e.ctrlKey || e.metaKey) && e.key === "k") {
    e.preventDefault()
    const searchInput = document.querySelector('input[type="search"]')
    if (searchInput) {
      searchInput.focus()
    }
  }

  // Ctrl/Cmd + Enter for quick submit in forms
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    const activeElement = document.activeElement
    if (activeElement && (activeElement.tagName === "INPUT" || activeElement.tagName === "TEXTAREA")) {
      const form = activeElement.closest("form")
      if (form) {
        const submitBtn = form.querySelector('button[type="submit"]')
        if (submitBtn) {
          submitBtn.click()
        }
      }
    }
  }
})

console.log("MathEngine main.js loaded successfully")
